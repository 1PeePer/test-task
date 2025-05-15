import pytest
from typing import List, Dict
from scripts.file_reader import read_employee_data

@pytest.fixture
def sample_employees(tmp_path = 'data/data1.csv') -> List[Dict]:
    """Example of employee information"""
    employees_data = read_employee_data(tmp_path)
    return employees_data

@pytest.fixture
def sample_csv(tmp_path = 'data/data1.csv'):
    """Example path to a file with employee information"""
    return tmp_path

@pytest.fixture
def sample_empty_csv(tmp_path = 'data/data4.csv'):
    """Example of path to empty file"""
    return tmp_path