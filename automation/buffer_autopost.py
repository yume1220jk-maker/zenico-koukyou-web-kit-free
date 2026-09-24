"""At-most-once Buffer scheduler for ZENICO's public procurement guide channel.

This intentionally will NOT publish until the user's X account is connected to
Buffer and GitHub secrets ZENICO_BUFFER_API_KEY / ZENICO_BUFFER_CHANNEL_ID are set.
Each run claims at most one hand-reviewed original post, commits its claim,
then schedules it. Ambiguous API failures fail closed (no automatic retry).
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE_FILE = ROOT / "automation" / "buffer_posts.json"
STATE_FILE = ROOT / "automation" / "buffer_post_state.json"
API = "https://api.buffer.com"


def graphql(key, query):
    request = urllib.request.Request(
        API, data=json.dumps({"query": query}).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + key},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        result = json.load(response)
    if result.get("errors") or not result.get("data"):
        raise RuntimeError("Buffer API rejected request; see Buffer logs")
    return result["data"]


def validate_channel(key, channel_id):
    organizations = graphql(key, "query { account { organizations { id } } }")["account"]["organizations"]
    for org in organizations:
        org_id = json.dumps(org["id"])
        q = "query { channels(input: { organizationId: " + org_id + " }) { id name service } }"
        result = graphql(key, q)
        for channel in result.get("channels", []):
            if channel.get("id") == channel_id and channel.get("service", "").lower() in ("twitter", "x"):
                expected = os.getenv("ZENICO_BUFFER_EXPECTED_ACCOUNT", "").strip().lstrip("@").lower()
                actual = channel.get("name", "").strip().lstrip("@").lower()
                if expected and expected != actual:
                    raise RuntimeError("Connected X channel name differs from expected account")
                if not expected:
                    raise RuntimeError("Set ZENICO_BUFFER_EXPECTED_ACCOUNT to the dedicated X channel name")
                return
    raise RuntimeError("Configured Buffer channel is not a connected X account")


def load_state():
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def save_state(s):
    STATE_FILE.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(stage):
    key = os.getenv("ZENICO_BUFFER_API_KEY")
    channel_id = os.getenv("ZENICO_BUFFER_CHANNEL_ID")
    if not key or not channel_id:
        print("SETUP_REQUIRED: no verified Buffer/X connection; no publication attempted")
        return 0
    validate_channel(key, channel_id)
    queue = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    state = load_state()
    existing_claims = [k for k, v in state.items() if v.get("status") == "claimed"]
    if stage == "claim":
        if existing_claims:
            print("BLOCKED: previous claim requires verification: " + existing_claims[0])
            return 0
        candidate = next((x for x in queue if x["id"] not in state), None)
        if candidate is None:
            print("NO_OP: all current original posts already processed")
            return 0
        state[candidate["id"]] = {"status": "claimed"}
        save_state(state)
        print("CLAIMED: " + candidate["id"])
        return 0
    if stage == "publish":
        if len(existing_claims) != 1:
            print("NO_OP: no uniquely claimed post")
            return 0
        item = next(x for x in queue if x["id"] == existing_claims[0])
        q = ("mutation { createPost(input: { text: " + json.dumps(item["text"], ensure_ascii=False) +
             ", channelId: " + json.dumps(channel_id) +
             ", schedulingType: automatic, mode: addToQueue }) { "
             "... on PostActionSuccess { post { id } } ... on MutationError { message } } }")
        try:
            outcome = graphql(key, q)["createPost"]
            if not outcome.get("post", {}).get("id"):
                raise RuntimeError("Buffer did not confirm queued post")
            state[item["id"]] = {"status": "queued", "buffer_post_id": outcome["post"]["id"]}
            print("QUEUED: " + item["id"])
        except Exception:
            # Response may have been lost after posting. Never blindly retry.
            state[item["id"]] = {"status": "manual_check_required"}
            print("NEEDS_REVIEW: API outcome uncertain; do not automatically resend")
        save_state(state)
        return 0
    raise ValueError("expected claim or publish")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: buffer_autopost.py claim|publish")
    sys.exit(main(sys.argv[1]))
