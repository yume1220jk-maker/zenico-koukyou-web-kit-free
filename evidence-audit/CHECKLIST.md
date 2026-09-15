# 公開前Evidence Checklist

「動いた」ではなく「何を確認できたか」を残すためのチェックリストです。確認できない項目は **UNKNOWN**、対象外は **N_A** とします。

- 対象を所有している、または検査権限があるか
- public / unauthenticated / non-destructive scopeか
- 主要URL・routeは意図どおりか
- index / noindex / robotsは公開段階と整合するか
- Privacy説明と観測できる計測実装に重大な矛盾がないか
- 公開HTML/JS/configに明白なpassword/token/private key等が露出していないか
- build/runtimeの主張に実行evidenceがあるか（資料提供時）
- rollback可能な既知良好状態を識別できるか（資料提供時）
- UNKNOWNを推測でPASSにしていないか

## 判定

適用されるblocking checkに **FAIL** または **UNKNOWN** が1件でもあればREADYとは判定しません。N_Aは適用条件を満たさない場合に限り、理由を残します。

このチェックリストはpenetration test、法令遵守証明、security certificationではありません。

サービス詳細:
https://zenico-evidence-audit.vercel.app/?utm_source=github&utm_medium=organic&utm_campaign=evidence_audit_pilot_v1
