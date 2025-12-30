from typing import Generator
import pytest
from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright

@pytest.fixture(scope="session")
def base_url() -> str:
    """
    Базовый URL приложения SauceDemo.
    """
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    """
    Fixture для запуска браузера на всю сессию тестирования.
    Возвращает объект Browser.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """
    Fixture для создания нового контекста браузера на каждый тест.
    Позволяет тестам быть изолированными.
    """
    ctx = browser.new_context()
    yield ctx
    ctx.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """
    Fixture для получения страницы (Page) Playwright.
    Каждый тест получает чистую страницу.
    """
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def login_page(page: Page) -> Page:
    """
    Fixture для перехода на страницу логина SauceDemo.
    Возвращает страницу, готовую к взаимодействию в тестах.
    """
    page.goto("https://www.saucedemo.com/")
    return page
