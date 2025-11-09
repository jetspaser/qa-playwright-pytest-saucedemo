import os
import pytest
from datetime import datetime

# Создаём папку reports, если её нет
os.makedirs("reports", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук, отлавливающий результат теста.
    Если тест упал — сохраняем артефакты: скриншот, HTML и видео (если включено).
    """
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        page = item.funcargs.get("page", None)
        if page:
            # timestamp
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            # пути файлов
            screenshot_path = f"reports/{test_name}_{now}.png"
            html_path = f"reports/{test_name}_{now}.html"

            # сохраняем скрин
            page.screenshot(path=screenshot_path)
            # сохраняем DOM
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(page.content())

            print(f"\n[ARTIFACT] saved screenshot: {screenshot_path}")
            print(f"[ARTIFACT] saved html dump: {html_path}")
