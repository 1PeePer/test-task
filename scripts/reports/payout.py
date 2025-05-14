from typing import List, Dict

def generate_payout_report(employees: List[Dict]) -> str:
    """Генерация текстового отчёта по зарплатам."""
    departments = {}
    
    # Группировка по отделам и расчёты
    for emp in employees:
        dept = emp['department']
        if dept not in departments:
            departments[dept] = {'employees': [], 'total_hours': 0, 'total_payout': 0}
        
        hours = int(emp['hours_worked'])
        rate = int(emp['rate'])
        payout = hours * rate
        
        departments[dept]['employees'].append({
            'name': emp['name'],
            'hours': hours,
            'rate': rate,
            'payout': payout
        })
        departments[dept]['total_hours'] += hours
        departments[dept]['total_payout'] += payout
    
    # Форматирование вывода
    report_lines = []
    for dept, data in departments.items():
        report_lines.append(f"  {dept.upper()}{' ' * (13 - len(dept))}name{19 * ' '}rate{3 * ' '}hours{4 * ' '}payout")
        report_lines.append(f"{65 * '='}")
        
        # Добавляем информацию о сотрудниках (учитывая максимальное кол-во символов в ячейках)
        for emp in data['employees']:
            name_column = f"{emp['name']}{' ' * (20 - len(str((emp['name']))))}"
            hours_column = f"{emp['hours']}{' ' * (6 - len(str(emp['hours'])))}"
            rate_column = f"{emp['rate']}{' ' * (4 - len(str(emp['rate'])))}"
            payout_column = f"{emp['payout']}{' ' * (8 - len(str(emp['payout'])))}"
            emp_str = f"| {10 * '-'} | {name_column} | {rate_column} | {hours_column} | ${payout_column} |"
            report_lines.append(emp_str)
        
        report_lines.append(f"{len(emp_str) * '='}")
        
        total_column = f"total :{2 * ' '}"
        total_hours_column = f"{data['total_hours']}{' ' * (6 - len(str(data['total_hours'])))}"
        total_payout_column = f"{data['total_payout']}{' ' * (8 - len(str(data['total_payout'])))}"
        report_lines.append(
            f"  {total_column}    {len(name_column) * ' '}    {len(rate_column) * ' '}   {total_hours_column}   ${total_payout_column}  "
        )
        report_lines.append("\n")  # Пустая строка между отделами
    
    return "\n".join(report_lines)