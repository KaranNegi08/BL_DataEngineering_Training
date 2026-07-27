from crewai import Agent
from config.llm_config import llm

writer = Agent(
    role="Business Report Writer",
    goal="Create executive reports",
    backstory="""
    Creates investor-grade reports.
    """,
    llm=llm,
    verbose=True
)