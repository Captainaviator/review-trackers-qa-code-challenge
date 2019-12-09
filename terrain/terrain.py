from lettuce import before, after, world
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@before.all
def setup_browser():
    world.browser = webdriver.Chrome(executable_path="C:/Program Files/selenium/chromedriver.exe")
    world.wait = WebDriverWait(world.browser, 2)
    world.browser.set_window_size(1900, 1000)


@after.each_scenario
def reset_browser(scenario):
    world.browser.delete_all_cookies()


@after.outline
def reset_browser(o, t, th, f):
    world.browser.delete_all_cookies()


@after.all
def close_browser(close):
    world.browser.quit()
