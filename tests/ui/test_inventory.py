import pytest
from playwright.sync_api import Page

from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_open_product_from_inventory(page: Page, base_url: str) -> None:
    """
    Проверка перехода с inventory-страницы
    в карточку товара.

    Шаги:
    1. Логинимся под стандартным пользователем
    2. Проверяем, что inventory страница открыта
    3. Открываем карточку первого товара
    4. Проверяем, что открылась корректная карточка
    """

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1️⃣ Логин
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    # 2️⃣ Проверка загрузки inventory
    assert inventory_page.is_opened(), "Inventory page did not open!"

    # 3️⃣ Открываем первый товар и сохраняем его имя
    first_item_name = inventory_page.open_first_item()
    assert first_item_name, "Failed to get first item name!"

    # 4️⃣ Проверяем, что открылась нужная карточка товара
    assert inventory_page.is_product_page_open(first_item_name), "Product page not opened!"


@pytest.mark.ui
def test_sort_by_name_atoz(page: Page, base_url: str) -> None:
    """
    Проверка сортировки товаров по имени (A → Z).
    """

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Логин
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_opened(), "Inventory page did not open!"

    # Сортировка
    inventory_page.sort_items_by("Name (A to Z)")

    # Получаем список имён товаров
    names = inventory_page.get_item_titles()

    # Проверка сортировки
    assert names == sorted(names), "Items are not sorted A to Z!"
