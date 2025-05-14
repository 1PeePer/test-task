from typing import List, Dict
import os


def read_employee_data(filepath: str) -> List[Dict[str, str]]:
    """Read employee data from CSV file.
    
    Args:
        filepath: Path to CSV file containing employee data. Expected columns:
                 - id (str)
                 - email (str)
                 - name (str)
                 - department (str)
                 - hours_worked (str)
                 - One of: hourly_rate/rate/salary (str)
    
    Returns:
        List of dictionaries where each dictionary represents an employee.
        All rate-related columns are normalized to 'rate' key.
        Empty lines are skipped.
    
    Raises:
        FileNotFoundError: If specified file doesn't exist.
        ValueError: If file is empty or has inconsistent columns.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Employee data file not found: {filepath}")

    employees = []
    normalized_headers = []
    rate_column_found = False
    
    with open(filepath, 'r', encoding='utf-8') as file:
        # Read and process headers
        first_line = file.readline().strip()
        if not first_line:
            raise ValueError("Empty CSV file provided")
            
        original_headers = first_line.split(',')
        
        # Normalize headers and identify rate column
        for header in original_headers:
            header = header.strip()
            if header.lower() in {'hourly_rate', 'rate', 'salary'}:
                normalized_header = 'rate'
                rate_column_found = True
            else:
                normalized_header = header
            normalized_headers.append(normalized_header)
        
        if not rate_column_found:
            raise ValueError("No rate column (hourly_rate/rate/salary) found in CSV")
        
        # Process employee data
        for line_number, line in enumerate(file, start=2):
            line = line.strip()
            if not line:
                continue  # Skip empty lines
                
            values = line.split(',')
            if len(values) != len(normalized_headers):
                raise ValueError(
                    f"Line {line_number}: expected {len(normalized_headers)} columns, "
                    f"got {len(values)}"
                )
            
            # Create employee dictionary with normalized headers
            employee = {
                header: value.strip()
                for header, value in zip(normalized_headers, values)
            }
            employees.append(employee)
    
    return employees