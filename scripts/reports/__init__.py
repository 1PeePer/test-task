from scripts.reports.payout import PayoutReport # Add a new report to imports
from scripts.reports.avg_rate import AVGRateReport 

# A list of all available reports
REPORTS = {
    report.get_name(): report
    for report in [PayoutReport, AVGRateReport]  # Add new reports to this list
}

def get_report(report_name: str):
    """Get report class by name."""
    return REPORTS.get(report_name)