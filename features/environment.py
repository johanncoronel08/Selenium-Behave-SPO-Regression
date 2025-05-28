import time

from selenium import webdriver
import allure






def before_feature(context, scenario):
    if  "chrome" in scenario.tags:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        context.browser = webdriver.Chrome(options=chrome_options)
    elif "firefox" in scenario.tags:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--incognito")
        context.browser = webdriver.Firefox(options=firefox_options)
    elif "edge" in scenario.tags:
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--incognito")
        context.browser = webdriver.Edge(options=edge_options)
    elif "safari" in scenario.tags:
        safari_options = webdriver.SafariOptions()
        safari_options.add_argument("--incognito")
        context.browser = webdriver.Safari(options=safari_options)
    else:
        context.browser = webdriver.Chrome()

    context.browser.maximize_window()
    context.browser.implicitly_wait(10)



def after_feature(context, scenario):
    time.sleep(3)
    context.browser.quit()

def after_step(context, step):
    capturadepantalla = context.browser.get_screenshot_as_png()
    allure.attach(capturadepantalla, name=step.name, attachment_type=allure.attachment_type.PNG)