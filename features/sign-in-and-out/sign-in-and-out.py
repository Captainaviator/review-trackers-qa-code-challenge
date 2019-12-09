from terrain.universal import basic
from lettuce import *
import time


@step('I should be on the "(.*)" page')
def assert_on_page(step, target_page):
    if target_page == 'Login':
        target_url = 'https://www.gouletpens.com/account/login'
    elif target_page == 'main':
        target_url = 'https://www.gouletpens.com/'
    elif target_page == 'My Account':
        target_url = 'https://www.gouletpens.com/account'
    else:
        assert False, 'target_page not recognized'
    url = world.browser.current_url
    print '      Now on {}\n'.format(url)
    assert url == target_url


@step('I am on the login page')
def go_to_the_login_page(step):
    world.browser.get('https://www.gouletpens.com/account/login')
    time.sleep(1)


@step('I enter "(.*)" in the "(.*)" field')
def enter_text_into_login_field(step, text, field):
    if field == 'email':
        text_field = world.browser.find_element_by_id('CustomerEmail')
    elif field == 'password':
        text_field = world.browser.find_element_by_id('CustomerPassword')
    else:
        assert False, 'field not recognized'
    text_field.click()
    text_field.send_keys(text)


@step('I click the sign in button')
def click_sign_in_button(step):
    button = world.browser.find_element_by_xpath('//*[@id="customer_login"]/ul/li[3]/button')
    button.click()


@step('the account link in the header should say "(.*)"')
def assert_account_link_text(step, target_text):
    account_link = world.browser.find_element_by_xpath("//*[@class='header__account-nav-link--account']")
    print '      Link text: {}\n'.format(account_link.text)
    assert account_link.text == target_text, 'Link text ({}) != target text ({})'


@step('I click the sign out link')
def click_sign_out_link(step):
    link = world.browser.find_element_by_link_text('SIGN OUT')
    link.click()


@step('I should see the incorrect email or password error message')
def assert_wrong_email_or_password_msg(step):
    error = basic.get_element_once_it_appears('CLASS_NAME', 'errors', max_wait=5)
    print '      Error text: {}\n'.format(error.text)
    assert error.text == 'Incorrect email or password.'
