import pytest
from playwright.sync_api import Page


# Если в будущем используем POM, импортируем здесь:
# from src.pages.login_page import LoginPage

def test_login_success(login_page: Page) -> None:
    """
    Успешная авторизация стандартным пользователем.

    Шаги:
    1. Вводим username и password.
    2. Нажимаем кнопку логина.
    3. Проверяем переход на страницу Inventory.
    """
    # Ввод логина и пароля
    login_page.fill("input[data-test='username']", "standard_user")
    login_page.fill("input[data-test='password']", "secret_sauce")

    # Нажатие кнопки Login
    login_page.click("input[data-test='login-button']")

    # Проверка URL и наличия элементов на странице Inventory
    assert "inventory.html" in login_page.url
    assert login_page.locator(".inventory_list").is_visible()


def test_login_fail_invalid_password(login_page: Page) -> None:
    """
    Попытка авторизации с неправильным паролем.

    Шаги:
    1. Вводим username.
    2. Вводим неверный password.
    3. Проверяем появление ошибки.
    """
    login_page.fill("input[data-test='username']", "standard_user")
    login_page.fill("input[data-test='password']", "wrong_password")
    login_page.click("input[data-test='login-button']")

    # Проверка сообщения об ошибке
    error_message = login_page.locator("h3[data-test='error']")
    assert error_message.is_visible()
    assert "Username and password do not match" in error_message.inner_text()
