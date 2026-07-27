from crewai import Task

def create_research_task(company, researcher):
    return Task(
        description=f"""
    Research {company}.

        Find:
        - Products
        - Business Model
        - Competitors
        - Market Position
        - Recent News
    """,
    expected_output="Detailed research report",
    agent= researcher
    )