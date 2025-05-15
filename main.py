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
    report = get_report(args.report).generate(all_employees)
    print(report[-1])
    
    return json.dumps(report[0], indent=2)

if __name__ == '__main__':
    main()