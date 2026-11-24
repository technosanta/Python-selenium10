import logging

import pytest

from pages.test_registration_form import RegistrationForm

from fixtures.browser_setup import driver
@pytest.mark.parametrize("first_name,email,phone", [
    ("John", "john@example.com", "1234567890"),
    ("Mark", "mark@example.com", "0987654321")
])
def test_fill_registration_form(driver, first_name, email, phone):


    # Create an instance of the RegistrationForm page object
    registration_form = RegistrationForm(driver)

    logging.info(f"Filling the registration form with First Name: {first_name}, Email: {email}, Phone: {phone}")
    # Fill the registration form
    registration_form.fill_form(first_name, email, phone)