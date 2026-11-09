from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class ContactPage(BasePage):
    URL = 'https://practicesoftwaretesting.com/contact'
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    EMAIL = (By.ID, "email")
    SUBJECT = (By.ID, "subject")
    COUNTRY = (By.ID, "country")
    MESSAGE = (By.ID, "message")
    # ATTACHMENT = (By.CSS_SELECTOR, "[data-test='attachment']")
    SEND_BUTTON = (By.CSS_SELECTOR, "[data-test='contact-submit']")
    SEND_OK = (By.XPATH, '/html/body/app-root/div[2]/app-contact/div/div/div/div')
    MESSAGE_ALERT = (By.XPATH,'//*[@id="message_alert"]/div')
    HELP_BLOCK = (By.XPATH, '/html/body/app-root/div[2]/app-contact/div/div/div/form/div/div[2]/div[5]/div/div')

    def input_first_name(self, text):
        self.type(self.FIRST_NAME, text)

    def input_last_name(self, text):
        self.type(self.LAST_NAME, text)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def select_subject(self, subject):
        if subject is not None:
            dropdown = Select(self.find(self.SUBJECT))
            dropdown.select_by_visible_text(subject)

    def input_message(self, message):
        self.type(self.MESSAGE, message)

    def click_send(self):
        self.wait_clickable(self.SEND_BUTTON)
        self.click(self.SEND_BUTTON)

    def fill_all_data(self, user):
        self.input_first_name(user["first_name"])
        self.input_last_name(user["last_name"])
        self.enter_email(user["email"])
        self.select_subject(user["subject"])
        self.input_message(user["message"])
