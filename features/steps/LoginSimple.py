from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.elements import *
import time


@given('ingreso a la URL "{url}"')
def step_impl(context, url):
    context.browser.get(url)
    context.urlobtenida = url


@when("valido que estoy en la url correcta")
def step_impl(context):
    assert context.browser.current_url == context.urlobtenida, "FALLO EL TEST"


@step('Ingreso usuario "{user}" y contraseña valida "{clave}"')
def step_impl(context, user, clave):
    campouser(context).click()
    campouser(context).send_keys(user)
    campopasss(context).click()
    campopasss(context).send_keys(clave)




@step("hago click en iniciar sesion")
def step_impl(context):
    campoBotonLogin(context).click()


@step("selecciono la sucursal")
def step_impl(context):
    time.sleep(3)
    #WebDriverWait(context.browser,10).until(EC.visibility_of(campoSucursal1(context)))
    campoSucursal1(context).click()


@then('al hacer click en continuar deberia llevarme al dashboard principal "{variable}"')
def step_impl(context, variable):
    campoContinuar(context).click()
    time.sleep(2)
    assert context.browser.current_url == variable, "FALLO EL TEST"