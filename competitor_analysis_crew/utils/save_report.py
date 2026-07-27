from pathlib import Path

def save_report(company, report):
    Path("outputs/reports").mkdir(parents=True, exist_ok=True)

    file_name = company.replace(
        " ",
        "_"
    )

    path = f"outputs/reports/{file_name}.md"

    with open(path,"w", encoding="utf-8") as f:
        f.write(str(report))

    print(f"Report saved to {path}")