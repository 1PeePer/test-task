import json
import argparse
from scripts.file_reader import read_employee_data
from scripts.reports import get_report, REPORTS

def main():
    # 1. Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='CSV files with data')
    parser.add_argument(
        '--report', 
        choices=REPORTS,
        default='payout',
        help=f'Report type: {', '.join(REPORTS.keys())}'
    )
    args = parser.parse_args()

    # 2. Loading data
    all_employees = []
    for file in args.files:
        all_employees.extend(read_employee_data(file))

    # 3. Generating a report
    report_class = get_report(args.report)
    if not report_class:
        print(f"Неизвестный тип отчёта: {args.report}")
        return
    report = report_class.generate(all_employees)
    print(report)
    
    return json.dumps(report, indent=2)

if __name__ == '__main__':
    main()