import os
import pytest
from datetime import datetime

# Создаём папку reports, если её нет
os.makedirs("reports", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук, который сохраняет артефакты только если тест УПАЛ.
    Защищён от ошибок: если браузер закрыт — ничего не делаем.
    """
    outcome = yield
    rep = outcome.get_result()

    # Скриншот только при падении на этапе выполнения теста
    if rep.when != "call" or not rep.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base = f"reports/{item.name}_{timestamp}"

    screenshot_path = f"{base}.png"
    html_path = f"{base}.html"

    # Пытаемся сохранить артефакты
    try:
        page.screenshot(path=screenshot_path)
    except Exception:
        return  # браузер закрыт → просто выходим

    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page.content())
    except Exception:
        pass

    print(f"\n[ARTIFACT] saved screenshot: {screenshot_path}")
    print(f"[ARTIFACT] saved html: {html_path}")
