from data.users import REGISTER_USER
from pages.register_page import RegisterPage


def test_successful_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[0])
    page.click_register()
    page.wait_page_changed(driver.current_url)
    assert "login" in driver.current_url


def test_register_empty_first_name(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[1])
    page.click_register()
    page.wait_visible(page.FAIL_FIRST_NAME)
    assert page.get_text(page.FAIL_FIRST_NAME) == "First name is required"


def test_register_empty_last_name(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[2])
    page.click_register()
    page.wait_visible(page.FAIL_LAST_NAME)
    assert page.get_text(page.FAIL_LAST_NAME) == "Last name is required"


def test_birthday_format_validation(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[3])
    page.click_register()
    page.wait_visible(page.FAIL_DOB)
    assert page.get_text(page.FAIL_DOB) == "Please enter a valid date in YYYY-MM-DD format."


def test_register_empty_country(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[4])
    page.click_register()
    page.wait_visible(page.FAIL_COUNTRY)
    assert page.get_text(page.FAIL_COUNTRY) == "Country is required"


def test_register_empty_email(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[5])
    page.click_register()
    page.wait_visible(page.FAIL_EMAIL)
    assert page.get_text(page.FAIL_EMAIL) == "Email is required"


def test_register_invalid_email(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[6])
    page.click_register()
    page.wait_visible(page.FAIL_EMAIL)
    assert page.get_text(page.FAIL_EMAIL) == "Email format is invalid"


def test_register_not_domain_email(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[7])
    page.click_register()
    page.wait_visible(page.FAIL_EMAIL)
    assert page.get_text(page.FAIL_EMAIL) == "Email format is invalid"


def test_register_domain_email(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[8])
    page.click_register()
    page.wait_visible(page.FAIL_EMAIL)
    assert page.get_text(page.FAIL_EMAIL) == "Email format is invalid"


def test_register_required_password(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[9])
    page.click_register()
    page.wait_visible(page.FAIL_PASSWORD)
    assert page.get_text(page.FAIL_PASSWORD) == """Password is required
Password must be minimal 6 characters long.
Password can not include invalid characters."""


def test_register_short_password(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[10])
    page.click_register()
    page.wait_visible(page.FAIL_PASSWORD)
    assert page.get_text(page.FAIL_PASSWORD) == """Password must be minimal 6 characters long.
Password can not include invalid characters."""


def test_register_password_invalid(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER[11])
    page.click_register()
    page.wait_visible(page.FAIL_PASSWORD)
    assert page.get_text(page.FAIL_PASSWORD) == "Password can not include invalid characters."
