class ExplanationEngine:

    def __init__(self, steps):
        self.steps = steps

    def explain_tools(self):
        explanations = []

        step_map = {step["id"]: step for step in self.steps}

        for step in self.steps:
            if step["type"] == "tool_call":
                parent = step_map.get(step["parent"])

                if parent and parent["type"] == "thought":
                    explanation = {
                        "tool": step["content"],
                        "reason": parent["content"]
                    }

                    explanations.append(explanation)

        return explanations