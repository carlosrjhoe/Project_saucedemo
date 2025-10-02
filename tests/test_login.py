from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    result = login_page.title_login_page()
    expected = 'Swag Labs'
    assert result == expected