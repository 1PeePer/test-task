from scripts.reports.payout import PayoutReport

def test_avg_rate_report_format(sample_employees):
    """Test for generating reports in different formats (json, txt)"""
    report = PayoutReport.generate(sample_employees)
    json_report, txt_report = report[0], report[-1]

    assert "Marketing" in json_report['data'][0]['department']
    assert "Alice" in json_report['data'][0]['employees'][0]['name']
    assert 8000 == json_report['data'][0]['employees'][0]['payout']
    assert "marketing" in txt_report.lower()
    assert "alice" in txt_report.lower()
    assert "8000" in txt_report.lower()

def test_avg_rate_calculations(sample_employees):
    """Test for correctness of calculations in the report"""
    report = PayoutReport.generate(sample_employees)
    json_report, txt_report = report[0], report[-1]

    assert 320 == json_report['data'][1]['total_hours']
    assert 16200 == json_report['data'][1]['total_payout']
    assert "320 h" in txt_report.lower()
    assert "$16200" in txt_report.lower()