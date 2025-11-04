import pandas as pd
from db.db_logger import fetch_recent_logs


def generate_report(path="reports/report_samples/report.xlsx"):
    logs = fetch_recent_logs(1000)
    df = pd.DataFrame(logs)
    summary = df.groupby("path").agg(
        avg_latency=("time","mean"),
        success_rate=("status", lambda s: (s==200).mean())
    ).reset_index()
    summary.to_excel(path, index=False)