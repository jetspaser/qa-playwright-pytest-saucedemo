import pytest
import time
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_open_product_from_inventory(page, base_url):
    """
    Проверка перехода с главной страницы (inventory)
    на страницу товара.
    Шаги:
    1. Логинимся под стандартным пользователем
    2. Проверяем, что список товаров отображается
    3. Кликаем по первому товару
    4. Проверяем, что открылась страница товара
    """

    # Инициализация объектов страниц
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1️⃣ Заходим на страницу логина
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    # 2️⃣ Проверяем, что страница inventory загрузилась
    assert inventory_page.is_loaded(), "Inventory page did not load!"

    # 3️⃣ Получаем название первого товара
    first_item_name = inventory_page.get_first_item_name()
    assert first_item_name, "No items found on inventory page!"

    # 4️⃣ Кликаем по первому товару
    inventory_page.open_first_item()

    # 5️⃣ Проверяем, что открылся экран товара
    assert inventory_page.is_product_page_open(first_item_name), "Product page not opened!"

    time.sleep(1)
