class InventoryPage:
    """
    Page Object страницы списка товаров (inventory.html).

    Здесь мы собираем ВСЕ действия, которые можно выполнить на странице:
    - проверка загрузки
    - сортировка
    - получение списка товаров
    - открытие карточки товара
    и др.

    Благодаря этому тесты остаются чистыми и читаемыми.
    """

    # ====== ЛОКАТОРЫ ======
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_TITLE = ".inventory_details_name"
    SORT_DROPDOWN = "[data-test='product_sort_container']"

    def __init__(self, page):
        """Сохраняем ссылку на страницу Playwright."""
        self.page = page

    # ----------------------------
    #     Проверки загрузки
    # ----------------------------
    def is_loaded(self):
        """Проверяем, что список товаров отображается."""
        return self.page.is_visible(self.INVENTORY_LIST)

    # ----------------------------
    #     Сортировка товаров
    # ----------------------------
    def sort_items_by(self, option_text: str):
        """
        Выполняет сортировку товаров.

        option_text — текст опции сортировки:
        - 'Name (A to Z)'
        - 'Name (Z to A)'
        - 'Price (low to high)'
        - 'Price (high to low)'
        """
        self.page.select_option(self.SORT_DROPDOWN, label=option_text)

    # ----------------------------
    #     Чтение списка товаров
    # ----------------------------
    def get_item_titles(self):
        """
        Возвращает список ИМЕН товаров в текущем порядке.
        Используется в тестах сортировки.
        """
        return self.page.locator(self.INVENTORY_ITEM_NAME).all_text_contents()

    def get_items_count(self):
        """
        Возвращает количество товаров на странице.
        Полезно для smoke-тестов.
        """
        return self.page.locator(self.INVENTORY_ITEM).count()

    # ----------------------------
    #     Работа с товаром
    # ----------------------------
    def get_first_item_name(self):
        """Получаем название первого товара."""
        return self.page.text_content(self.INVENTORY_ITEM_NAME)

    def open_first_item(self):
        """Открываем карточку первого товара."""
        self.page.click(self.INVENTORY_ITEM_NAME)

    def is_product_page_open(self, expected_name):
        """
        Проверяем что в карточке товара открыт тот,
        на который кликнули.
        """
        title = self.page.text_content(self.INVENTORY_ITEM_TITLE)
        return expected_name.strip() in title.strip()
