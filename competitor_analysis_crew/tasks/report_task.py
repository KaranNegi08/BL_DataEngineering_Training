from crewai import Task

def create_report_task(
    writer,
    strategy_task
):
    return Task(
        description="""
        Create final executive report.

        Sections:
        - Executive Summary
        - Company Overview
        - Competitor Analysis
        - SWOT Analysis
        - Recommendations
        """,
        expected_output="Professional markdown report",
        context=[strategy_task],
        agent=writer
    )