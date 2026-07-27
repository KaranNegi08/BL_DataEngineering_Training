import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
load_dotenv()

# Make sure your API key is set:
# PowerShell:
# $env:OPENAI_API_KEY="your_api_key"

llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

researcher = Agent(
    role="Research Specialist",
    goal="Find accurate information about AI in education",
    backstory="""
    You are an experienced researcher who specializes in gathering
    accurate and reliable information from multiple sources.
    """,
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Blog Writer",
    goal="Write engaging and informative content",
    backstory="""
    You are a professional content writer with expertise in creating
    informative and engaging blog articles.
    """,
    llm=llm,
    verbose=True
)

editor = Agent(
    role="Editor",
    goal="Improve quality and readability",
    backstory="""
    You are a senior editor who reviews content for clarity,
    grammar, and readability.
    """,
    llm=llm,
    verbose=True
)

research_task = Task(
    description="""
    Research the benefits of AI in education.

    Include:
    - Personalized learning
    - Automated grading
    - Student engagement
    - Challenges and limitations
    """,
    expected_output="""
    A detailed research report in markdown format.
    """,
    agent=researcher
)

writing_task = Task(
    description="""
    Write a 1500-word blog article using the research report.
    """,
    expected_output="""
    A well-structured blog article with:
    - Title
    - Introduction
    - Main sections
    - Conclusion
    """,
    context=[research_task],
    agent=writer
)

editing_task = Task(
    description="""
    Review the article and improve:
    - Grammar
    - Readability
    - Structure
    - Professional tone
    """,
    expected_output="""
    Final polished article ready for publication.
    """,
    context=[writing_task],
    agent=editor
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    verbose=True
)

result = crew.kickoff()

print("\n" + "=" * 80)
print(result)
print("=" * 80)