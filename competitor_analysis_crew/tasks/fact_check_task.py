from crewai import Task

def create_fact_check_task(fact_checker,
    research_task):
    return Task(
        description="""
        Validate all research findings.
        Remove unsupported claims.
        """,
        expected_output="Verified report",
        context=[research_task],
        agent=fact_checker
    )