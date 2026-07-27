from crewai import Agent
from config.llm_config import llm

strategist = Agent(
    role="Business Strategist",
    goal="Analyze strengths and weaknesses",
    backstory="""
    Former management consultant.
    """,
    llm=llm,
    verbose=True
)