from scripts.reports.base import AbstractReport
from typing import List, Dict

class AVGRateReport(AbstractReport):

    @classmethod
    def generate(cls, employees: List[Dict]) -> str:
        """Generate a formatted avg rate report grouped by departments.
        
        Processes employee data to calculate average hourly rates by department,
        then formats the output as a table.
        
        Args:
            employees: List of dictionaries containing employee data with keys:
                    - 'department' (str)
                    - 'name' (str)
                    - 'rate' (str/int)
                    - 'hours_worked' (str/int)
        
        Returns:
            Formatted report string ready for printing
        """
        departments = {}
        
        # Process each employee and group by department
        for emp in employees:
            dept = emp['department']
            
            # Initialize department structure if not exists
            if dept not in departments:
                departments[dept] = {
                    'employees': [],
                    'avg_rate': 0
                }
            
            # Convert string values to integers for calculations
            try:
                rate = int(emp['rate'])
            except (ValueError, KeyError) as e:
                raise ValueError(f"Invalid employee data format: {e}") from e
            
            # Store employee data
            departments[dept]['employees'].append({
                'name': emp['name'],
                'rate': rate
            })

        # Update department totals
            departments[dept]['avg_rate'] += rate
        
        # Generate report lines
        report_lines = []
        
        for dept, data in departments.items():
            # Department header
            report_lines.append(f"  {dept.upper().ljust(12)} name {17 * ' '} rate")
            report_lines.append(f"{44 * '='}")
            
            # Employee rows
            max_line_length = 0
            tmp_count = 0
            for emp in data['employees']:
                tmp_count += 1

                # Format each column with proper alignment
                name_column = emp['name'].ljust(20)
                rate_column = str(emp['rate']).ljust(4)
                
                # Build employee row string
                emp_str = f"| {10 * '-'} | {name_column} | {rate_column} |"
                report_lines.append(emp_str)
                
                # Track maximum line length for separator alignment
                max_line_length = max(max_line_length, len(emp_str))
            
            # Department separator
            report_lines.append(f"{max_line_length * '='}")
            
            # Department totals row
            total_column = "avg_rate :".ljust(10)
            avg_rate_column = str(round(data['avg_rate'] / tmp_count, 1)).ljust(4)
            report_lines.append(
                f"| {total_column} | {len(name_column) * '-'} | {avg_rate_column} |"
            )
            
            # Section end marker
            report_lines.append(f"{max_line_length * '^'}")
            report_lines.append("\n")  # Empty line between departments
        
        return "\n".join(report_lines)

    @classmethod
    def get_name(cls) -> str:
        return "avg_rate"