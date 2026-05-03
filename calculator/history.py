import json
import os

class History:
    MAX_RECORDS = 1000

    def __init__(self, filename="history.json"):
        self.filename = filename
        self.records = []
        self.load()

    def add_record(self, expression, result):
        """Adds a new record to the history."""
        record = {
            "expression": expression,
            "result": result
        }
        self.records.append(record)
        if len(self.records) > self.MAX_RECORDS:
            self.records = self.records[-self.MAX_RECORDS:]
        self.save()

    def get_all(self):
        return self.records

    def get_last(self, n=5):
        return self.records[-n:]

    def clear(self):
        self.records = []
        self.save()

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.records = json.load(f)
        else:
            self.records = []