from lettuce import *
import time


@step('I am on a product page')
def go_to_product_page(step):
    world.browser.get('https://www.gouletpens.com/products/visconti-homo-sapiens-fountain-pen-dark-age')
    time.sleep(1)
    header = world.browser.find_element_by_xpath('//*[@id="shopify-section-header"]/div/header')
    world.browser.execute_script("return arguments[0].scrollIntoView(true);", header)
    time.sleep(1)


@step('I click reviews stars')
def click_on_review_stars(step):
    review_stars_class = 'stamped-product-reviews-badge stamped-main-badge'
    world.browser.find_element_by_xpath('//*[@class="{}"]'.format(review_stars_class)).click()
    time.sleep(4)


@step('the reviews section should be scrolled into view')
def assert_reviews_in_view(step):
    reviews_class = 'read-more__content read-more__content--reviews js-readMoreContent open'
    reviews_section = world.browser.find_element_by_xpath('//*[@class="{}"]'.format(reviews_class))
    assert reviews_section.is_displayed()


@step('I click on the keyword in position "(.*)"')
def click_review_keyword(step, position):
    keywords_list = world.browser.find_elements_by_xpath('//*[@class="stamped-summary-keywords-list"]/li')
    target_keyword = keywords_list[int(position)-1]
    world.clicked_keyword = target_keyword.text
    print '      Clicking on {}\n'.format(world.clicked_keyword)
    target_keyword.click()
    time.sleep(3)


@step('I select "(.*)" from the "(.*)" filter')
def select_review_filter_dropdown(step, target_selection, target_filter):
    filter_dropdowns = world.browser.find_elements_by_xpath('//*[@class="stamped-filter-selects"]/select')
    for dropdown in filter_dropdowns:
        if target_filter in dropdown.text:
            world.filtering_by = target_filter
            dropdown.click()
            dropdown_list = world.browser.find_elements_by_xpath('//*[@class="stamped-filter-select"]/option')
            for filter in dropdown_list:
                if filter.text == target_selection:
                    world.filter_level = filter.text
                    print '      found {}\n'.format(filter.text)
                    filter.click()
                    time.sleep(4)


@step('the reviews should filter correctly by "(.*)"')
def assert_reviews_filtered(step, filter):
    reviews_list = world.browser.find_elements_by_xpath('//*[@class="stamped-reviews"]/div')
    for review in reviews_list:
        print '      searching review #{}\n'.format(reviews_list.index(review)+1)
        scale_translation = {'Ideal For': {'Beginner': 1, 'Intermediate': 3, '4': 4, 'Experienced': 5},
                             'Value': {'Low': 1, 'Medium': 3, '4': 4, 'High': 5},
                             'Quality': {'Low': 1, 'Medium': 3, '4': 4, 'High': 5}}
        if filter == 'keyword':
            review_body = review.find_element_by_xpath('.//*[@class="stamped-review-body"]')
            highlighted_text = review_body.find_element_by_xpath('.//*[@class="stamped-keyword-highlight"]').text
            print '        Found highlighted "{}"\n'.format(highlighted_text)
            assert highlighted_text.lower() == world.clicked_keyword.lower()
        elif filter == 'filter':
            review_bars = review.find_elements_by_xpath('.//*[@class="stamped-review-options"]/ul/li')
            for bar in review_bars:
                bar_title = bar.find_element_by_xpath('.//strong').text
                scale = bar.find_element_by_xpath('.//*[@class="stamped-review-option-scale"]')
                scale_value = scale.get_attribute('data-value')
                print '        {}: {}\n'.format(bar_title, scale_value)
                if bar_title == world.filtering_by:
                    filtered_level = scale_translation[world.filtering_by][world.filter_level]
                    assert scale_value == str(filtered_level), \
                        'Scale value ({}) != filtered_level ({})'.format(scale_value, filtered_level)
                    break
        else:
            assert False, 'filter not recognized'
