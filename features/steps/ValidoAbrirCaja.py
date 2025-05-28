from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from utils.elements import *
import time

@given("al ingresar a la seccion de caja")
def step_impl(context):
    botonCaja(context).click()


@when("hago click en inicar caja")
def step_impl(context):
  botonIniciarCaja(context).click()


@step('ingreso monto inicial "{monto}"')
def step_impl(context, monto):
    formMonto(context).click()
    formMonto(context).send_keys(monto)
    time.sleep(3)




@step('ingreso numero de caja "{valor}"')
def step_impl(context, valor):
    formNumeroCaja(context).send_keys(valor)
    time.sleep(3)


@step("hago click en agregar")
def step_impl(context):
   wait = WebDriverWait(context.browser, 10)
   xpathbotonAgregar = '//span[text()=" Agregar "]/parent::*'
   elemento = wait.until(element_to_be_clickable((By.XPATH, xpathbotonAgregar)))
   elemento.click()



@then('Deberia aperturar una caja con el siguiente mensaje "{texto}"')
def step_impl(context, texto):
    assert mensajevalidacion(context).text == texto, "NO PASO"


@given("hago click en cerrar caja")
def step_impl(context):
   cerrarCaja(context).click()
   time.sleep(2)


@when("ingreso el valor de la caja {valor}")
def step_impl(context, valor):
   valorefectivo(context).click()
   time.sleep(2)
   valorefectivo(context).send_keys(valor)
   time.sleep(2)


@step("el boton aceptar se deberia habilitar")
def step_impl(context):
   wait = WebDriverWait(context.browser, 10)
   context.botonAceptar = '//span[contains(text()," Aceptar ")]/parent::*'
   context.elementobotonAceptar = wait.until(element_to_be_clickable((By.XPATH, context.botonAceptar)))



@step("Hago click en aceptar")
def step_impl(context):
    assert context.elementobotonAceptar.is_displayed(), "NO SE MUESTRA"
    context.elementobotonAceptar.click()


@then("Deberia cerrar una caja correctamente con el mensaje {mensajecierre}")
def step_impl(context, mensajecierre):
    assert MensajeCierreCaja(context,mensajecierre).is_displayed(), "NO SE MUESTRA"
