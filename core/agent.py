from core.task_analyzer import analyze_task
from core.planner import create_plan
from core.reasoning import generate_reasoning


class Agent:
    """
    Central controller of the AI Agent Framework.
    """

    def run(self, user_input: str) -> str:
        # Step 1: Analyze task
        analysis = analyze_task(user_input)

        # Step 2: Create execution plan
        plan = create_plan(analysis["task_type"], user_input)

        # Step 3: Generate reasoning
        reasoning = generate_reasoning(plan)

        # Step 4: Build structured response
        response = (
            "AI Agent Execution\n"
            "------------------\n"
            f"Task Type : {analysis['task_type']}\n\n"
            "Execution Plan & Reasoning:\n"
        )

        for index, (step, reason) in enumerate(zip(plan, reasoning), start=1):
            response += (
                f"{index}. {step}\n"
                f"   Reason: {reason}\n"
            )

        return response

