import json
from collections import defaultdict
def generate_report(json_file_path):
    report = dict()

    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(fp=file)
        for row in data:
            if row["assignee"] not in report:
                report[row["assignee"]] = 0
            if row["status"] == "completed":
                report[row["assignee"]] += 1

    return report

print(generate_report("test.json"))
