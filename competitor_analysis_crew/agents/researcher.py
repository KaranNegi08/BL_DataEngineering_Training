from crewai import Agent

from config.llm_config import llm
from tools.search_tool import search_tool

researcher = Agent(
    role="Market Research Analyst",
    goal="Gather accurate information about companies",
    backstory="""
    Expert market researcher specializing in
    competitor intelligence and industry trends.
    """,
    tools=[search_tool],
    llm=llm,
    verbose=True
)