import os
import sys
import pytest
from datetime import datetime

# === 1. Абсолютный путь к src ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(BASE_DIR, "src")

# Проверяем что src существует
print("DEBUG SRC_PATH:", SRC_PATH)
print("DEBUG exists:", os.path.isdir(SRC_PATH))

# Добавляем src в PYTHONPATH
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

print("DEBUG sys.path:", sys.path)

# === 2. Теперь импортируем APIClient ===
from api.api_client import APIClient


# === 3. Создаём reports ===
os.makedirs("reports", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
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


@pytest.fixture
def api_client():
    return APIClient("https://jsonplaceholder.typicode.com")
