import re


class ComplianceChecker:

    def __init__(self, rules_data):
        self.rules = rules_data.get("rules", [])

    def check(self, conversation):

        violations = []

        for msg in conversation["messages"]:

            if msg["role"] != "agent":
                continue

            text = msg["text"].lower()

            for rule in self.rules:

                for kw in rule.get("keywords", []):

                    pattern = re.escape(kw.lower())

                    if re.search(pattern, text):

                        violations.append({
                            "rule_id": rule["id"],
                            "category": rule["category"],
                            "severity": rule["severity"],
                            "matched_keyword": kw,
                            "message": msg["text"]
                        })

                        break

        return violations