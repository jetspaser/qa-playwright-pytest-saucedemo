import pytest
from playwright.sync_api import Page

from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_sort_by_name_ztoa(page: Page, base_url: str) -> None:
    """
    Проверка сортировки товаров по имени (Z → A).
    """

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1️⃣ Логин
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    # 2️⃣ Проверка загрузки inventory
    assert inventory_page.is_opened(), "Inventory page did not open!"

    # 3️⃣ Сортировка товаров Z→A
    inventory_page.sort_items_by("Name (Z to A)")

    # 4️⃣ Получаем список имён товаров
    names = inventory_page.get_item_titles()

    # 5️⃣ Проверяем, что список отсортирован Z→A
    assert names == sorted(names, reverse=True), "Items are not sorted Z to A!"
