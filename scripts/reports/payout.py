from scripts.reports.base import AbstractReport
from typing import List, Dict


class PayoutReport(AbstractReport):

    @classmethod
    def generate(cls, employees: List[Dict]) -> List:
        """Generate a formatted payout report grouped by departments.
        
        Processes employee data to calculate total hours and payout per department,
        then formats the output as table.
        
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
                    'total_hours': 0,
                    'total_payout': 0
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
            departments[dept]['total_hours'] += hours
            departments[dept]['total_payout'] += payout

        
        json_data = {
            "report_type": "payout",
            "data": [
                {
                    "department": dept,
                    "employees": data['employees'],
                    "total_hours": data['total_hours'],
                    "total_payout": data['total_payout']
                }
                for dept, data in departments.items()
            ]
        }
        
        # Generate report lines
        report_lines = []
        
        for dept, data in departments.items():
            # Department header
            report_lines.append(f"  {dept.upper().ljust(11)} name {17 * ' '} rate   hours {3 * ' '} payout")
            report_lines.append(f"{65 * '='}")
            
            # Employee rows
            max_line_length = 0
            for emp in data['employees']:
                # Format each column with proper alignment
                name_column = emp['name'].ljust(20)
                rate_column = str(emp['rate']).ljust(4)
                hours_column = (str(emp['hours_worked']) + ' h').ljust(7)
                payout_column = ('$' + str(emp['payout'])).ljust(9)
                
                # Build employee row string
                emp_str = f"| {9 * '-'} | {name_column} | {rate_column} | {hours_column} | {payout_column} |"
                report_lines.append(emp_str)
                
                # Track maximum line length for separator alignment
                max_line_length = max(max_line_length, len(emp_str))
            
            # Department separator
            report_lines.append(f"{max_line_length * '='}")
            
            # Department totals row
            total_column = "total :".ljust(9)
            total_hours_column = (str(data['total_hours']) + ' h').ljust(7)
            total_payout_column = ('$' + str(data['total_payout'])).ljust(9)
            report_lines.append(
                f"| {total_column} | {len(name_column) * '-'}---{len(rate_column) * '-'} | "
                f"{total_hours_column} | {total_payout_column} |"
            )
            
            # Section end marker
            report_lines.append(f"{max_line_length * '^'}")
            report_lines.append("\n")  # Empty line between departments

            txt_data = "\n".join(report_lines)
        
        return [json_data, txt_data]
    
    @classmethod
    def get_name(cls) -> str:
        return "payout"