from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_swag_page()
    result = login_page.title_access_page()
    expected = 'Swag Labs'
    assert result == expected

def test_login_with_valid_username(driver):
    login_page = LoginPage(driver)
    login_page.open_swag_page()
    login_page.set_username()
    login_page.set_password()
    login_page.click_buton_login()
    result = login_page.title_product_page()
    expected = 'Products'
    assert result == expected
