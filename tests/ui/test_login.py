import pytest
import time
from src.pages.login_page import LoginPage

@pytest.mark.ui     # ← добавили маркер
def test_login_success(page):
    """
    простой smoke-тест: открываем saucedemo, логинимся стандартным пользователем
    и проверяем, что произошёл переход на страницу inventory.
    """
    base = "https://www.saucedemo.com/"
    page.goto(base)

    # вводим действенные тестовые данные (они известны для SauceDemo)
    page.fill("input#user-name", "standard_user")
    page.fill("input#password", "secret_sauce")
    page.click("input#login-button")

    # подождём коротко, пока страница загрузится (Playwright обычно авто-ожидает)
    page.wait_for_url("**/inventory.html", timeout=5000)

    # убеждаемся, что URL содержит inventory и что список товаров виден
    assert "inventory" in page.url
    assert page.is_visible(".inventory_list")

    # немного паузы визуально (если headless=False), чтобы виден был результат
    time.sleep(1)
