from crewai import Task

def create_strategy_task(
    strategist,
    fact_check_task
):
    return Task(
        description="""
        Perform SWOT analysis.

        Provide:
        - Strengths
        - Weaknesses
        - Opportunities
        - Threats
        """,
        expected_output="Strategic analysis",
        context=[fact_check_task],
        agent=strategist
    )