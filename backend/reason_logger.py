import uuid
import json
from datetime import datetime


class ReasonLogger:

    def __init__(self):
        self.steps = []

    # original logging method
    def log(self, step_type, content, parent=None):

        step = {
            "id": str(uuid.uuid4()),
            "type": step_type,
            "content": content,
            "parent": parent
        }

        self.steps.append(step)
        return step["id"]

    # new method used by agent.py
    def add_step(self, step_type, content, parent=None):
        return self.log(step_type, content, parent)

    def show(self):

        for step in self.steps:
            parent = step["parent"] if step["parent"] else "None"
            print(f"[{step['type']}] {step['content']}  (parent: {parent})")

    def export(self):
        return self.steps

    def get_trace(self):
        return self.steps

    def save_trace(self):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"traces/trace_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(self.steps, f, indent=2)

        return filename