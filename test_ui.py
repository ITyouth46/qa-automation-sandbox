import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_saucedemo_successful_login(page: Page):
    # 1. Создаем объект страницы
    login_page = LoginPage(page)
    
    # 2. Открываем сайт
    login_page.open()
    
    # 3. Вводим креды
    login_page.login("standard_user", "secret_sauce")
    
    # 4. Проверяем, что нас пустило (после логина URL меняется на инвентарь)
    assert "inventory.html" in page.url

@pytest.mark.parametrize("username, password", [
    ("admin", "1234"),
    ("standart_user", ""),
    ("", "secret_sauce"),
    ("locked_out_user", "secret_sauce")
])

def test_saucedemo_failed_login(page: Page, username, password):
    # 1. Создаем объект страницы
    login_page = LoginPage(page)
    
    # 2. Открываем сайт
    login_page.open()
    
    # 3. Вводим креды
    login_page.login(username, password)
    
   
    assert login_page.error_message.is_visible()

def test_add_item_to_cart(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack()

    assert inventory_page.count_shopping_cart.inner_text() == "1"

    inventory_page.go_to_cart()

    cart_page = CartPage(page)

    assert cart_page.item_name.inner_text() == "Sauce Labs Backpack"