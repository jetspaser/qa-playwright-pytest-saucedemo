class InventoryPage:
    INVENTORY_LIST = ".inventory_list"

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.is_visible(self.INVENTORY_LIST)

class InventoryPage:
    # ====== Локаторы ======
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_TITLE = ".inventory_details_name"

    def __init__(self, page):
        """
        Класс для работы со страницей списка товаров (inventory).
        """
        self.page = page

    def is_loaded(self):
        """Проверяем, что страница загружена — виден список товаров."""
        return self.page.is_visible(self.INVENTORY_LIST)

    def get_first_item_name(self):
        """Получаем текст первого товара."""
        return self.page.text_content(self.INVENTORY_ITEM_NAME)

    def open_first_item(self):
        """Кликаем по первому товару в списке."""
        self.page.click(self.INVENTORY_ITEM_NAME)

    def is_product_page_open(self, expected_name):
        """Проверяем, что открылась страница именно этого товара."""
        title = self.page.text_content(self.INVENTORY_ITEM_TITLE)
        return expected_name.strip() in title.strip()
