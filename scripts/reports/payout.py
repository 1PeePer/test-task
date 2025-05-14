from typing import List, Dict


def generate_payout_report(employees: List[Dict]) -> str:
    """Generate a formatted payout report grouped by departments.
    
    Processes employee data to calculate total hours and payout per department,
    then formats the output as table.
    
    Args:
        employees: List of dictionaries containing employee data with keys:
                  - 'department' (str)
                  - 'name' (str)
                  - 'hours_worked' (str/int)
                  - 'rate' (str/int)
    
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
        try:
            hours = int(emp['hours_worked'])
            rate = int(emp['rate'])
            payout = hours * rate
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid employee data format: {e}") from e
        
        # Store employee data
        departments[dept]['employees'].append({
            'name': emp['name'],
            'rate': rate,
            'hours': hours,
            'payout': payout
        })
        
        # Update department totals
        departments[dept]['total_hours'] += hours
        departments[dept]['total_payout'] += payout
    
    # Generate report lines
    report_lines = []
    
    for dept, data in departments.items():
        # Department header
        report_lines.append(f"  {dept.upper().ljust(11)} name {17 * ' '} rate   hours {3 * ' '} payout")
        report_lines.append(f"{65 * '_'}")
        
        # Employee rows
        max_line_length = 0
        for emp in data['employees']:
            # Format each column with proper alignment
            name_column = emp['name'].ljust(20)
            rate_column = str(emp['rate']).ljust(4)
            hours_column = (str(emp['hours']) + ' h').ljust(7)
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
    
    return "\n".join(report_lines)