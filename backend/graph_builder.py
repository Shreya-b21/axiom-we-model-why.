class GraphBuilder:

    def __init__(self, steps):
        self.steps = steps

    def build(self):
        nodes = []
        edges = []

        for step in self.steps:
            nodes.append({
                "id": step["id"],
                "label": step["type"],
                "content": step["content"]
            })

            if step["parent"]:
                edges.append({
                    "source": step["parent"],
                    "target": step["id"]
                })

        return {
            "nodes": nodes,
            "edges": edges
        }