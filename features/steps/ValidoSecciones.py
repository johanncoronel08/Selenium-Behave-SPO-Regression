import time

from behave import *

from utils.elements import *


@given('Hago click en el {modulo}')
def step_impl(context, modulo):
    SeccionModulos(context, modulo).click()
    time.sleep(3)


@then('valido cada una de las se {variable}')
def step_impl(context, variable):
    Secciones(context, variable)
    time.sleep(3)