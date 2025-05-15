from scripts.reports.base import AbstractReport
from typing import List, Dict

class AVGRateReport(AbstractReport):

    @classmethod
    def generate(cls, employees: List[Dict]) -> List:
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
            name = emp['name']
            rate = int(emp['rate'])
            hours = int(emp['hours_worked'])
            payout = hours * rate
            
            # Store employee data
            departments[dept]['employees'].append({
                'name': name,
                'rate': rate,
                'hours_worked': hours,
                'payout': payout
            })

        # Update department totals
            departments[dept]['avg_rate'] += rate
        #data['avg_rate'] / len(data['employees'])

        json_data = {
            "report_type": "avg_rate",
            "data": [
                {
                    "department": dept,
                    "employees": data['employees'],
                    "avg_rate": round(data['avg_rate'] / len(data['employees']), 1)
                }
                for dept, data in departments.items()
            ]
        }
        
        # Generate report lines
        report_lines = []
        
        for dept, data in departments.items():
            # Department header
            report_lines.append(f"  {dept.upper().ljust(12)} name {17 * ' '} rate")
            report_lines.append(f"{44 * '='}")
            
            # Employee rows
            max_line_length = 0
            for emp in data['employees']:

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
            avg_rate_column = str(round(data['avg_rate'] / len(data['employees']), 1)).ljust(4)
            report_lines.append(
                f"| {total_column} | {len(name_column) * '-'} | {avg_rate_column} |"
            )
            
            # Section end marker
            report_lines.append(f"{max_line_length * '^'}")
            report_lines.append("\n")  # Empty line between departments

            txt_data = "\n".join(report_lines)
        
        return [json_data, txt_data]

    @classmethod
    def get_name(cls) -> str:
        return "avg_rate"