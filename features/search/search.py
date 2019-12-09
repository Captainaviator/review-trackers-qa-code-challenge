from terrain.universal import basic
from lettuce import *
import time
from selenium.webdriver.common.keys import Keys


@step('the site search drop-down should appear')
def verify_site_search_dropdown_appears(step):
    dropdown_xpath = "//*[@class='findify-layouts--autocomplete--dropdown']"
    dropdown = basic.get_element_once_it_appears('XPATH', dropdown_xpath)
    assert dropdown.is_displayed()


@step('the site search drop-down should have "(.*)"')
def site_search_dropdown_has(step, thing):
    if thing == "trending searches":
        thing_class = 'findify-layouts--autocomplete--dropdown__suggestions-container'
        target_text = "TRENDING SEARCHES"
    elif thing == "trending products":
        thing_class = 'findify-layouts--autocomplete--dropdown__product-matches-container'
        target_text = "TRENDING PRODUCTS"
    else:
        assert False, 'Thing to search for not recognized'
    xpath = "//*[@class='{}']".format(thing_class)
    displayed_text = world.browser.find_element_by_xpath(xpath).text
    assert displayed_text[:17] == target_text
    assert len(displayed_text) > 30


@step('I click on item "(.*)" in trending "(.*)"')
def click_on_item_in_trending(step, number, search_type):
    time.sleep(2)
    if search_type == "searches":
        search_class = 'findify-components-autocomplete--search-suggestions__list'
        list_xpath = "//*[@class='{}']/li".format(search_class)
    elif search_type == "products":
        search_class = 'findify-components-autocomplete--product-matches'
        list_xpath = "//*[@class='{}']/div/div".format(search_class)
    else:
        assert False, 'search type not recognized'
    item_list = world.browser.find_elements_by_xpath(list_xpath)
    target_list_item = item_list[int(number)-1]
    world.searched_item = target_list_item.text
    print '      Clicking on "{}"\n'.format(world.searched_item)
    target_list_item.click()


@step('the search results should match what I searched for')
def search_results_should_match(step):
    search_results_name_class = 'findify-query-wrapper'
    results_name_xpath = "//*[@class='{}']/span/span/strong".format(search_results_name_class)
    query_results_text = basic.get_element_once_it_appears('XPATH', results_name_xpath).text
    assert query_results_text == world.searched_item, \
        'Search results ({}) do not match what was searched for ({})'\
            .format(query_results_text, world.searched_item)


@step('I should be on the correct product page')
def assert_on_correct_product_page(step):
    product_name_xpath = "//*[@class='product-info__title']"
    product_name = world.browser.find_element_by_xpath(product_name_xpath).text
    print '      Now on the page for {}\n'.format(product_name)
    assert product_name in world.searched_item, \
        'Search results ({}) do not match what was searched for ({})'.format(product_name, world.searched_item)


@step('I search for "(.*)"')
def search_for(step, query):
    search_field = world.browser.find_element_by_id('Search')
    search_field.send_keys(query)
    search_field.send_keys(Keys.ENTER)
    world.searched_item = query
