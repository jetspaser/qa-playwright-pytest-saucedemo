class InventoryPage:
    INVENTORY_LIST = ".inventory_list"

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.is_visible(self.INVENTORY_LIST)
