import pytest
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_sort_by_name_ztoa(page, base_url):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1. Логинимся
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    # 2. Ждём перехода на inventory
    page.wait_for_url("**/inventory.html", timeout=5000)

    # 3. ЖДЁМ ПРАВИЛЬНЫЙ локатор сортировки
    sort_dd = page.locator("[data-test='product-sort-container']")
    sort_dd.wait_for(state="visible", timeout=5000)

    # 4. Применяем сортировку Z→A
    inventory_page.sort_items_by("Name (Z to A)")

    # 5. Ждём обновления списка
    page.wait_for_timeout(300)

    # 6. Получаем названия товаров
    names = inventory_page.get_item_titles()

    # 7. Проверяем сортировку
    assert names == sorted(names, reverse=True)
