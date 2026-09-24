import importlib.util
from datetime import date
from pathlib import Path
spec = importlib.util.spec_from_file_location("recent", Path(__file__).with_name("zenico_recent_notices.py"))
recent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recent)

now = date(2026, 9, 24)
good = b"""<Results><SearchResults><SearchResult><ProjectName>CMS website renewal</ProjectName><OrganizationName>Demo Authority</OrganizationName><ExternalDocumentURI>https://example.jp/tender/123</ExternalDocumentURI><CftIssueDate>2026-09-23</CftIssueDate><TenderSubmissionDeadline>2026-09-30</TenderSubmissionDeadline></SearchResult></SearchResults></Results>"""
results = recent.parse(good, now)
assert len(results) == 1
assert "https://example.jp/tender/123" in recent.render(results, now)
expired = good.replace(b"2026-09-30", b"2026-09-20")
assert recent.parse(expired, now) == []
unknown_deadline = good.replace(b"<TenderSubmissionDeadline>2026-09-30</TenderSubmissionDeadline>", b"")
assert recent.parse(unknown_deadline, now) == []
assert "0件" in recent.render([], now)
bad_url = good.replace(b"https://example.jp/tender/123", b"javascript:alert(1)")
assert recent.parse(bad_url, now) == []
assert recent.parse(b"<Results><SearchResults/></Results>", now) == []
print("All candidate-safety parser tests passed.")
