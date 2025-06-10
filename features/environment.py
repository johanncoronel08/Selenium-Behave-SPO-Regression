import os
import time
from dotenv import load_dotenv

from selenium import webdriver
import allure
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import  Options as SafariOptions

load_dotenv()
def before_feature(context,scenario):
    navegador=""
    print(scenario.tags)
    if "firefox" in scenario.tags:
        navegador=FirefoxOptions()
    elif "edge" in scenario.tags:
        navegador=EdgeOptions()
    elif "safari" in scenario.tags:
        navegador=SafariOptions()
    else:
        navegador=ChromeOptions()

    tipo_ejecucion=os.getenv("TIPO_EJECUCION")
    if tipo_ejecucion=="grid":
        grid_url=os.getenv("GRID_URL")
        context.browser= webdriver.Remote(command_executor=grid_url,options=navegador)
    else :
        if tipo_ejecucion=="jenkins":
            navegador.add_argument('--headless')
            navegador.add_argument('--no-sandbox')
            navegador.add_argument('--disable-dev-shm-usage')

        if "firefox" in scenario.tags:
            context.browser = webdriver.Firefox(options=navegador)
        elif "edge" in scenario.tags:
            context.browser = webdriver.Edge(options=navegador)
        elif "safari" in scenario.tags:
            context.browser = webdriver.Safari(options=navegador)
        else:
            context.browser = webdriver.Chrome(options=navegador)
    context.browser.implicitly_wait(5)
    context.browser.maximize_window()


#def before_feature(context, scenario):
    #if  "chrome" in scenario.tags:
       # chrome_options = webdriver.ChromeOptions()
     #   chrome_options.add_argument("--incognito")
    #    context.browser = webdriver.Chrome(options=chrome_options)
    #elif "firefox" in scenario.tags:
    #    firefox_options = webdriver.FirefoxOptions()
     #   firefox_options.add_argument("--incognito")
      #  context.browser = webdriver.Firefox(options=firefox_options)
    #elif "edge" in scenario.tags:
     #   edge_options = webdriver.EdgeOptions()
     #   edge_options.add_argument("--incognito")
     #   context.browser = webdriver.Edge(options=edge_options)
    #elif "safari" in scenario.tags:
    #    safari_options = webdriver.SafariOptions()
      #  safari_options.add_argument("--incognito")
      #  context.browser = webdriver.Safari(options=safari_options)
    #else:
       # context.browser = webdriver.Chrome()

   # context.browser.maximize_window()
  #  context.browser.implicitly_wait(10)



def after_feature(context, scenario):
    time.sleep(3)
    context.browser.quit()

def after_step(context, step):
    capturadepantalla = context.browser.get_screenshot_as_png()
    allure.attach(capturadepantalla, name=step.name, attachment_type=allure.attachment_type.PNG)