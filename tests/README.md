/|\ Test-Task-Workmate
    Руководство по тестированию скрипта


/|\ Общая информация

    Тесты для проекта написаны с использованием pytest и покрывают:

        - Чтение CSV-файлов
        - Генерацию всех типов отчётов
        - CLI-интерфейс


/|\ Запуск тестов:

    1. Базовый запуск (bash):

        - pytest tests/ -v

    2. С проверкой покрытия (bash):

        - pytest --cov=main --cov=scripts --cov=scripts/reports --cov-report=term-missing

    3. Генерация HTML-отчёта (bash):

        - pytest --cov=main --cov=scripts --cov=scripts/reports --cov-report=html
        - start htmlcov/index.html  #Для просмотра отчёта


/|\ Добавление тестов для новых отчётов:

    1. Создайте файл в tests/test_reports/ (например, test_new_report.py)

    2. Используйте шаблон:


        from scripts.reports.new_report import NewReport

        def test_new_report_format(sample_employees):
            """Тест форматирования отчёта"""
            report = NewReport.generate(sample_employees)
            assert "Ожидаемый результат" in report

        def test_new_report_calculations(sample_employees):
            """Тест корректности расчётов"""
            report = NewReport.generate(sample_employees)
            assert "123" in report  # Проверка конкретных вычислений


    3. Добавьте название нового репорта в test_main.py:


        from unittest.mock import patch
        from main import main
        import pytest


        reports = ["payout", "avg_rate", "new_report"]  #add new report title here
        #Остальной код остается без изменений 


/|\ Полезные команды

    Запуск конкретного теста:

        - pytest tests/test_reports/test_payout.py::test_payout_calculations -v

    Запуск с таймаутом:

        - pytest --timeout=10  # Прерывать долгие тесты

/|\ Структура тестов

    tests/
    |-- test_reports/          # Тесты отчётов
    |   |- __init__.py
    |   |- test_avg_rate.py    # Тесты отчёта по средней ставке
    |   |- test_payout.py      # Тесты отчёта по выплатам
    |-- __init__.py
    |-- conftest.py            # Общие фикстуры
    |-- README.md              # Этот файл
    |-- test_file_reader.py    # Тесты чтения файлов
    |-- test_main.py           # Тесты CLI