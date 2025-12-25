from typing import Dict


def analyze_task(user_input: str) -> Dict[str, str]:
    """
    Classifies the user task correctly.
    Priority: tool > planning > general
    """

    text = user_input.lower().strip()

    # Highest priority: tool
    if "calculate" in text:
        task_type = "tool"

    # Planning tasks
    elif any(word in text for word in ["plan", "study plan", "schedule", "roadmap"]):
        task_type = "planning"

    # Fallback: general
    else:
        task_type = "general"

    return {
        "task_type": task_type,
        "query": user_input
    }

