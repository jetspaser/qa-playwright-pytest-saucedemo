# UI + API AutoTests (Playwright + Pytest)

Небольшой учебно-проект для демонстрации навыков автоматизации тестирования Web UI и API.  
Используется **Playwright** для UI-автотестов и **Requests** для API-тестов.
Структура проекта максимально приближена к промышленной (pytest + фикстуры + отчёты + Page Object Model).

Проект будет расширяться — смотреть Roadmap ниже.

-----------------------------

## Стек технологий

- Python 3.11
- Pytest
- Playwright
- Requests
- Pytest-HTML (отчёты)
- Page Object Model (POM)
- Git / GitHub

-----------------------------

## Структура проекта

- `src/pages` — Page Object классы (LoginPage, InventoryPage и др.)
- `tests/ui` — UI-тесты (Smoke, негативные сценарии и т.п.)
- `tests/api` — будущие API-тесты
- `utils` — вспомогательные функции и утилиты
- `tests_data` — тестовые данные (JSON / CSV и пр.)
- `conftest.py` — фикстуры для Pytest (инициализация браузера, base_url)
- `pytest.ini` — конфигурация Pytest и настройка маркеров
- `reports` — HTML-отчёты
- `README.md` — описание проекта

-----------------------------

## Прогресс проекта

✅ Smoke-тест успешного логина
✅ Негативные тесты (неверный пароль / логин)
✅ Проверка загрузки страницы инвентаря
🟡 Подготовка структуры для API-тестов
🟡 Планируется параметризация тестов и CI-интеграция

-----------------------------

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Установить зависимости
pip install -r requirements.txt

# Запустить все тесты
pytest

# Запустить только UI-тесты
pytest -m ui

# UI-тесты с открытием браузера
pytest -m ui --headed

# Запустить только API-тесты
pytest -m api

# Запустить конкретный тест
pytest tests/ui/test_inventory.py::test_sort_by_name_atoz

# Сгенерировать HTML-отчёт
pytest --html=reports/report.html --self-contained-html

# Запуск UI-тестов в выбранном браузере
pytest -m ui --browser chromium
pytest -m ui --browser firefox
pytest -m ui --browser webkit

# Параллельный запуск тестов (если установлен pytest-xdist)
pytest -n auto

#requirements - зависимости

pytest==7.4.0
playwright==1.40.0
pytest-playwright==0.4.3
requests==2.31.0


