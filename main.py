import argparse
from scripts.file_reader import read_employee_data
from scripts.reports.payout import generate_payout_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='CSV файлы с данными сотрудников')
    parser.add_argument('--report', choices=['payout'], default='payout')
    args = parser.parse_args()

    all_employees = []
    for file in args.files:
        all_employees.extend(read_employee_data(file))

    if args.report == 'payout':
        report = generate_payout_report(all_employees)
        print(report)

if __name__ == '__main__':
    main()