class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.add_product_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.count_shopping_cart = page.locator(".shopping_cart_badge")

    def add_backpack(self):
        self.add_product_backpack.click()

