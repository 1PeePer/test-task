from scripts.reports.avg_rate import AVGRateReport

def test_payout_report_format(sample_employees):
    """Test for generating reports in different formats (json, txt)"""
    report = AVGRateReport.generate(sample_employees)
    json_report, txt_report = report[0], report[-1]

    assert "Marketing" in json_report['data'][0]['department']
    assert "Alice" in json_report['data'][0]['employees'][0]['name']
    assert 160 == json_report['data'][0]['employees'][0]['hours_worked']
    assert "marketing" in txt_report.lower()
    assert "alice" in txt_report.lower()

def test_payout_calculations(sample_employees):
    """Test for correctness of calculations in the report"""
    report = AVGRateReport.generate(sample_employees)
    json_report, txt_report = report[0], report[-1]

    assert 50.0 == json_report['data'][1]['avg_rate']
    assert "50.0" in txt_report.lower()