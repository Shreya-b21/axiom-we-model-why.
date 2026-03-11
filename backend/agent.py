# backend/agent.py

from backend.reason_logger import ReasonLogger
from backend.tools import search_tool, calculator_tool


class Agent:

    def __init__(self):
        # keep logger attribute for structure
        self.logger = None


    def run(self, prompt):

        # create a fresh logger for each run
        self.logger = ReasonLogger()

        prompt_id = self.logger.add_step("prompt", prompt)

        # initial reasoning
        thought = "Analyzing the prompt to decide which tool to use."
        thought_id = self.logger.add_step("thought", thought, prompt_id)

        if any(char.isdigit() for char in prompt):

            # reasoning for choosing calculator
            decision = "Detected numbers in the prompt. Using calculator_tool."
            decision_id = self.logger.add_step("thought", decision, thought_id)

            tool_name = "calculator_tool"
            tool_id = self.logger.add_step("tool_call", tool_name, decision_id)

            result = calculator_tool(prompt)

        else:

            # reasoning for choosing search
            decision = "Prompt looks like a factual query. Using search_tool."
            decision_id = self.logger.add_step("thought", decision, thought_id)

            tool_name = "search_tool"
            tool_id = self.logger.add_step("tool_call", tool_name, decision_id)

            result = search_tool(prompt)

        result_id = self.logger.add_step("tool_result", result, tool_id)

        answer = result
        self.logger.add_step("answer", answer, result_id)

        return answer, self.logger.get_trace()