from crewai import Agent
from config.llm_config import llm

fact_checker= Agent(
    role="Fcat Checker",
    goal="Verify all findings",
    backstory="""
    Expert in validation and verification.
    """,
    llm=llm,
    verbose =True
)