from crewai import Crew

from agents.researcher import researcher
from agents.fact_checker import fact_checker
from agents.strategist import strategist
from agents.writer import writer
from tasks.research_task import create_research_task
from tasks.fact_check_task import create_fact_check_task
from tasks.strategy_task import create_strategy_task
from tasks.report_task import create_report_task


def create_competitor_crew(company):

    research_task= create_research_task(company, researcher)

    fact_check_task = create_fact_check_task(
        fact_checker,
        research_task
    )

    strategy_task = create_strategy_task(
        strategist,
        fact_check_task
    )

    report_task = create_report_task(
        writer,
        strategy_task
    )

    return Crew(
        agents=[
            researcher,
            fact_checker,
            strategist,
            writer
        ],
        tasks=[
            research_task,
            fact_check_task,
            strategy_task,
            report_task
        ],
        verbose= True
    )