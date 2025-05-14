from typing import List, Dict

def read_employee_data(filepath: str) -> List[Dict]:
    """Чтение CSV файла с данными сотрудников."""
    employees = []
    with open(filepath, 'r') as f:
        headers = f.readline().strip().split(',')
        for i in range(len(headers)):
            if headers[i] in {'hourly_rate', 'rate', 'salary'}:
                headers[i] = 'rate'
        
        # Нормализация названий колонок
        headers = [h.strip() for h in headers]
        
        for line in f:
            if not line.strip():
                continue
                
            values = line.strip().split(',')
            employee = dict(zip(headers, values))
            employees.append(employee)
    
    return employees
