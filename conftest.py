import os
import sys
import pytest
from datetime import datetime

# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Создаём папку reports, если её нет
os.makedirs("reports", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Сохраняем артефакты при падении теста."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call" or not rep.failed:
        return

    page = item.funcargs.get("page")
    if not page:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base = f"reports/{item.name}_{timestamp}"

    try:
        page.screenshot(path=f"{base}.png")
    except Exception:
        return

    try:
        with open(f"{base}.html", "w", encoding="utf-8") as f:
            f.write(page.content())
    except Exception:
        pass


# ==== API CLIENT FIXTURE ====

from src.api.api_client import APIClient


@pytest.fixture
def api_client():
    """Создаёт API-клиент для API-тестов."""
    return APIClient("https://jsonplaceholder.typicode.com")
