#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ["README.md", "README.pdf", "brief.yaml", "prompt.md", "data/mock-data.csv", "data/mock-context.json", "solution/expected-output.json", "evidence/checklist.md"]
missing = [p for p in required if not (root / p).exists()]
result = {"activity": root.name, "status": "FAIL" if missing else "PASS", "missing": missing}
expected = root / "solution/expected-output.json"
if expected.exists():
    data = json.loads(expected.read_text())
    for key in ["decision", "evidence", "human_owner", "acceptance"]:
        if key not in data:
            result["status"] = "FAIL"
            result.setdefault("missing_fields", []).append(key)
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
