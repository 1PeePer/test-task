import pytest
from scripts.file_reader import read_employee_data

def test_valid_file(sample_csv):
    """Test reading a valid CSV file"""
    employees = read_employee_data(sample_csv)
    assert len(employees) == 3
    assert "Alice" in employees[0]["name"]
    assert employees[1]["rate"] == "40"

def test_empty_file(sample_empty_csv):
    """Test reading empty CSV file"""
    with pytest.raises(ValueError, match="Empty CSV file provided"):
        read_employee_data(sample_empty_csv)

def test_missing_file():
    """Test reading missing CSV file"""
    with pytest.raises(FileNotFoundError):
        read_employee_data("nonexistent.csv")

def test_invalid_headers(tmp_path):
    """Test reading CSV file with invalid headers"""
    csv_data = "id,name\n1,Alice"
    file_path = tmp_path / "invalid.csv"
    file_path.write_text(csv_data)
    
    with pytest.raises(ValueError, match="No rate column in CSV"):
        read_employee_data(file_path)

def test_invalid_data(tmp_path):
    """Test reading CSV file with invalid data"""
    csv_data = "id,name,rate\n1,Alice"
    file_path = tmp_path / "invalid.csv"
    file_path.write_text(csv_data)
    
    with pytest.raises(ValueError, match="incorrect data file"):
        read_employee_data(file_path)
