from playwright.sync_api import Page


class InventoryPage:
    """
    Page Object страницы списка товаров (inventory.html).

    Инкапсулирует все действия и проверки страницы:
    - проверка загрузки
    - сортировка
    - работа со списком товаров
    - переход в карточку товара
    """

    # ====== ЛОКАТОРЫ ======
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_TITLE = ".inventory_details_name"
    SORT_DROPDOWN = '[data-test="product-sort-container"]'
    ACTIVE_SORT_OPTION = "[data-test='active-option']"
    ITEM_PRICE = "[data-test='inventory-item-price']"

    def __init__(self, page: Page) -> None:
        """
        Конструктор InventoryPage.

        :param page: Объект Page Playwright
        """
        self.page = page

    # ----------------------------
    #     Проверки страницы
    # ----------------------------
    def is_opened(self) -> bool:
        """
        Проверяет, что страница inventory загружена.

        :return: True, если список товаров отображается
        """
        return self.page.locator(self.INVENTORY_LIST).is_visible()

    # ----------------------------
    #     Сортировка товаров
    # ----------------------------
    def sort_items_by(self, option_text: str) -> None:
        """
        Выполняет сортировку товаров по заданной опции.

        :param option_text: Текст опции сортировки, например:
                            - 'Name (A to Z)'
                            - 'Name (Z to A)'
                            - 'Price (low to high)'
                            - 'Price (high to low)'
        """
        self.page.select_option(self.SORT_DROPDOWN, label=option_text)

    def get_active_sort_option(self) -> str:
        """
        Возвращает текущую выбранную опцию сортировки.

        :return: Название активной сортировки
        """
        return self.page.locator(self.ACTIVE_SORT_OPTION).text_content()

    # ----------------------------
    #     Список товаров
    # ----------------------------
    def get_item_titles(self) -> list[str]:
        """
        Возвращает список названий товаров в текущем порядке.

        :return: Список названий товаров
        """
        return self.page.locator(self.INVENTORY_ITEM_NAME).all_text_contents()

    def get_items_count(self) -> int:
        """
        Возвращает количество товаров на странице.

        :return: Количество товаров
        """
        return self.page.locator(self.INVENTORY_ITEM).count()

    # ----------------------------
    #     Работа с товаром
    # ----------------------------
    def open_first_item(self) -> str:
        """
        Открывает карточку первого товара.

        :return: Название товара, по которому был клик
        """
        first_item = self.page.locator(self.INVENTORY_ITEM_NAME).first
        item_name = first_item.text_content()
        first_item.click()
        return item_name

    def is_product_page_open(self, expected_name: str) -> bool:
        """
        Проверяет, что открыта карточка ожидаемого товара.

        :param expected_name: Название товара
        :return: True, если заголовок совпадает
        """
        title = self.page.locator(self.INVENTORY_ITEM_TITLE).text_content()
        return expected_name.strip() in title.strip()

    # ----------------------------
    #     Цены товаров
    # ----------------------------
    def get_item_prices(self) -> list[float]:
        """
        Возвращает список цен товаров.

        :return: Список цен в формате float
        """
        prices_raw = self.page.locator(self.ITEM_PRICE).all_text_contents()
        return [float(price.replace("$", "")) for price in prices_raw]
