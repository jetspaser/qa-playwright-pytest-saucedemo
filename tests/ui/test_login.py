import pytest
import time
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_login_wrong_password(page, base_url):
    """
    Негативный тест: логин с неправильным паролем
    должен показывать пользователю сообщение об ошибке.
    """
    login_page = LoginPage(page)

    # Шаг 1: открыли страницу логина
    login_page.open(base_url)

    # Шаг 2: вводим неверный пароль
    login_page.login("standard_user", "wrong_pass")

    # Шаг 3: проверяем, что появилось сообщение об ошибке
    assert login_page.is_error_visible(), "Ошибка не отображается!"

    # Шаг 4: проверяем сам текст ошибки
    text = login_page.get_error_text()
    assert "do not match" in text, "Текст ошибки неверный!"

@pytest.mark.ui
def test_login_wrong_username(page, base_url):
    """
    Негативный тест: логин с неправильным username
    должен показывать ошибку на странице.
    """
    login_page = LoginPage(page)

    # Шаг 1: открыли страницу логина
    login_page.open(base_url)

    # Шаг 2: вводим неверный логин
    login_page.login("wrong_user", "secret_sauce")

    # Шаг 3: проверяем, что появилось сообщение об ошибке
    assert login_page.is_error_visible(), "Ошибка не отображается!"

    # Шаг 4: проверяем текст ошибки
    text = login_page.get_error_text()
    assert "do not match" in text or "Username and password" in text, "Текст ошибки неверный!"
