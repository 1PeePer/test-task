from unittest.mock import patch
from main import main
import pytest


reports = ["payout", "avg_rate"]  #add new report title here

for report in reports:
    def test_main(sample_csv, capsys, tmp_report = report):
        """Test reading a valid CSV file"""
        test_args = ["main.py", sample_csv, "--report", tmp_report]
        with patch('sys.argv', test_args):
            json_result = main()
            txt_result = capsys.readouterr().out
            str_report_type = f'"report_type": "{tmp_report}"'

            assert f"{type(json_result)}" == "<class 'str'>"
            assert str_report_type in json_result
            assert '"department": "Marketing"' in json_result
            assert '"name": "Alice Johnson"' in json_result
            assert "marketing" in txt_result.lower()
            assert "alice johnson" in txt_result.lower()

    def test_main_invalid_report(sample_csv, capsys):
        """Test reading a valid CSV file with invalid report name"""
        test_args = ["main.py", sample_csv, "--report", "invalid"]
        
        with patch('sys.argv', test_args):
            with patch('main.read_employee_data', return_value=[]):
                with pytest.raises(SystemExit):
                    main()
                
                captured = capsys.readouterr()
                assert "invalid choice" in captured.err

    def test_main_missing_file(tmp_report = report):
        """Test reading missing CSV file"""
        test_args = ["main.py", "nonexistent.csv", "--report", tmp_report]
        
        with patch('sys.argv', test_args):
            with pytest.raises(FileNotFoundError, match="Employee data file not found"):
                main()

    def test_main_empty_file(sample_empty_csv, tmp_report = report):
        """Test reading empty CSV file"""
        test_args = ["main.py", sample_empty_csv, "--report", tmp_report]
        
        with patch('sys.argv', test_args):
            with pytest.raises(ValueError, match="Empty CSV file provided"):
                main()