import argparse
from typing import List
from scripts.file_reader import read_employee_data
from scripts.reports.payout import generate_payout_report


def parse_arguments() -> argparse.Namespace:
    """Parse and validate command line arguments.
    
    Returns:
        Namespace object with parsed arguments:
        - files: List of input CSV file paths
        - report: Report type to generate
        
    Raises:
        SystemExit: If invalid arguments are provided
    """
    parser = argparse.ArgumentParser(
        description='Generate salary reports from employee CSV data.',
        epilog='Example: python main.py data1.csv data2.csv --report payout'
    )
    
    parser.add_argument(
        'files',
        nargs='+',
        help='Paths to CSV files containing employee data.'
    )
    
    parser.add_argument(
        '--report',
        choices=['payout'],
        default='payout',
        help='Type of report to generate (currently only "payout" supported)'
    )
    
    return parser.parse_args()


def load_employee_data(file_paths: List[str]) -> List[dict]:
    """Load and combine employee data from multiple CSV files.
    
    Args:
        file_paths: List of paths to CSV files
        
    Returns:
        Combined list of all employee records
        
    Raises:
        SystemExit: If any file cannot be read or contains invalid data
    """
    all_employees = []
    
    for file_path in file_paths:
        try:
            employees = read_employee_data(file_path)
            all_employees.extend(employees)
        except (FileNotFoundError, ValueError) as e:
            raise SystemExit(f"Error processing {file_path}: {str(e)}")
    
    if not all_employees:
        raise SystemExit("No valid employee data found in input files")
        
    return all_employees


def generate_report(report_type: str, employees: List[dict]) -> str:
    """Generate the requested report from employee data.
    
    Args:
        report_type: Type of report to generate
        employees: List of employee records
        
    Returns:
        Formatted report as a "table" (string)
        
    Raises:
        ValueError: If unsupported report type is requested
    """
    if report_type == 'payout':
        return generate_payout_report(employees)
    else:
        raise ValueError(f"Unsupported report type: {report_type}")


def main() -> None:
    """The main entry point for the reporting script."""
    try:
        args = parse_arguments()
        employees = load_employee_data(args.files)
        report = generate_report(args.report, employees)
        print(report)
    except Exception as e:
        raise SystemExit(f"Error: {str(e)}")


if __name__ == '__main__':
    main()