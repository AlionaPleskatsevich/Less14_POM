from pages.contact_page import ContactPage
from data.contact import CONTACT


def test_successful_send_no_file(driver):
    page = ContactPage(driver)
    page.open()
    page.fill_all_data(CONTACT[0])
    page.click_send()
    page.wait_visible(page.SEND_OK)
    assert page.get_text(page.SEND_OK) == """Thanks for your message! We will contact you shortly."""

def test_send_min_message(driver):
    page = ContactPage(driver)
    page.open()
    page.fill_all_data(CONTACT[1])
    page.click_send()
    page.wait_visible(page.MESSAGE_ALERT)
    assert page.get_text(page.MESSAGE_ALERT) == """Message must be minimal 50 characters"""


def test_send_max_message(driver):
    page = ContactPage(driver)
    page.open()
    page.fill_all_data(CONTACT[2])
    page.click_send()
    page.wait_visible(page.HELP_BLOCK)
    assert page.get_text(page.HELP_BLOCK) == """The message field must not be greater than 250 characters."""


def test_send_no_message(driver):
    page = ContactPage(driver)
    page.open()
    page.fill_all_data(CONTACT[3])
    page.click_send()
    page.wait_visible(page.MESSAGE_ALERT)
    assert page.get_text(page.MESSAGE_ALERT) == """Message is required"""
    