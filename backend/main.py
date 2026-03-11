from reason_logger import ReasonLogger
from agent import SimpleAgent
import json
from explanation_engine import ExplanationEngine
from graph_builder import GraphBuilder

logger = ReasonLogger()
agent = SimpleAgent(logger)

result = agent.run("What is the capital of France?")

print("\nAgent answer:\n")
print(result)

print("\nReasoning steps:\n")
logger.show()

print("\nRaw structure:\n")
print(json.dumps(logger.export(), indent=2))

trace_file = logger.save_trace()

print("\nTrace saved to:")
print(trace_file)
 
engine = ExplanationEngine(logger.export())

explanations = engine.explain_tools()

print("\nTool explanations:\n")

for e in explanations:
    print(f"Tool '{e['tool']}' was used because:")
    print(f"  {e['reason']}\n")

graph = GraphBuilder(logger.export()).build()

print("\nGraph structure:\n")
print(json.dumps(graph, indent=2))