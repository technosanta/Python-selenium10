from selenium.webdriver.common.by import By


class RegistrationForm:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        self.gender_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[id='gender']")
        self.email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        self.phone_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='mobile']")

    def fill_form(self, first_name, email, phone):
        self.first_name_field.send_keys(first_name)
        self.gender_checkbox.click()
        self.email_field.send_keys(email)
        self.phone_field.send_keys(phone)

    def validate_first_name(self, expected_first_name):
        actual_first_name = self.first_name_field.get_attribute("value")
        assert actual_first_name == expected_first_name, f"Expected first name: {expected_first_name}, but got: {actual_first_name}"

    def validate_gender(self, expected_gender):
        actual_gender = self.gender_checkbox.get_attribute("checked")
        assert actual_gender == expected_gender, f"Expected gender: {expected_gender}, but got: {actual_gender}"

    def validate_email(self, expected_email):
        actual_email = self.email_field.get_attribute("value")
        assert actual_email == expected_email, f"Expected email: {expected_email}, but got: {actual_email}"

    def validate_phone(self, expected_phone):
        actual_phone = self.phone_field.get_attribute("value")
        assert actual_phone == expected_phone, f"Expected phone: {expected_phone}, but got: {actual_phone}"
