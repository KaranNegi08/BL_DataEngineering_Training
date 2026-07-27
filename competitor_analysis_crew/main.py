from dotenv import load_dotenv

load_dotenv()

from crews.competitor_crew import create_competitor_crew
from utils.save_report import save_report


company = input(
    "Enter company name: "
)

crew = create_competitor_crew(
    company
)

result = crew.kickoff()

save_report(
    company,
    result
)

print(result)