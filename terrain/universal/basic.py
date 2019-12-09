from lettuce import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

@step('I am on the main page')
def go_to_the_main_page(step):
    world.browser.get('https://www.gouletpens.com/')
    time.sleep(1)


@step('I click the "(.*)"')
def click_the_thing(step, thing):
    if thing == "search field":
        thing_xpath = "//*[@class='header__search-form-container header__search-form-container--desktop']"
    elif thing == "Sign In / Sign Up link":
        thing_xpath = "//*[@class='header__account-nav-link--account']"
    else:
        assert False, "Thing to click on is't recognized"
        # add more things
    world.browser.find_element_by_xpath(thing_xpath).click()


def get_element_once_it_appears(element_type, element_string, name='Target page element', max_wait=30):
    """
    This only returns a single element (not a list of elements)
    Does not take relative paths for things like XPATH

    :param element_type: strings: ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
    :param element_string: the element string itself
    :param name: name of the element
    :param max_wait: in seconds
    :return: element
    """
    browser = world.browser
    try:
        print '        Waiting for "{}" for up to {} seconds...'.format(name, max_wait)
        # print element_string, '\n'
        start_time = time.time()
        element_attribute = getattr(By, element_type)
        wait = WebDriverWait(browser, max_wait)
        element = wait.until(EC.presence_of_element_located((element_attribute, element_string)))
        end_time = time.time()
        elapsed_time = str(end_time - start_time)[:-10]
        print '          Found it after {} seconds\n'.format(elapsed_time)
        return element
    except TimeoutException:
        print '        {} took longer than {} seconds to appear\n'.format(name, max_wait)
