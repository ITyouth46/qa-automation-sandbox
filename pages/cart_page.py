class CartPage:
    def __init__(self, page):
        self.page = page
        self.item_name = page.locator(".inventory_item_name")