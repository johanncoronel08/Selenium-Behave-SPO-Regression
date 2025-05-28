from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

user = "//input[@placeholder='Introduce el correo aquí']"
passs = '//input[@placeholder="Introduce tu contraseña"]'
botoniniciar = '//button/span[@class="mdc-button__label" and contains(text(),"Iniciar sesión")]'
sucursal1 = '(//span[contains(text(),"Sucursal")]//parent::*)[1]'
continuar = '//span[contains(text()," Continuar ")]'


def campouser(context):
 elementoUser = context.browser.find_element(By.XPATH, user)
 return elementoUser

def campopasss(context):
    elementoPass = context.browser.find_element(By.XPATH, passs)
    return elementoPass

def campoBotonLogin(context):
    elementoLogin = context.browser.find_element(By.XPATH, botoniniciar)
    return elementoLogin

#def campoSucursal1(context):
   # elementoSucursal1 = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, sucursal1)))
   # return elementoSucursal1

def campoSucursal1(context):
    elemetoSucursal1 = context.browser.find_element(By.XPATH, sucursal1)
    return elemetoSucursal1

def campoContinuar(context):
    elementoContinuar = context.browser.find_element(By.XPATH, continuar)
    return elementoContinuar

def SeccionModulos(context, modulo):
    variabledinamica=f'(//span[contains(text(),"{modulo}")])[1]/parent::*'
    EleccionModulos = context.browser.find_element(By.XPATH, variabledinamica)
    return EleccionModulos

def Secciones(context, seccion):
    urlactual = context.browser.current_url
    print(urlactual)
    print(seccion)
    assert context.browser.current_url == seccion,"NO SE VALIDO"


def fun_buscar_por_xapth(context, xpath):
    return context.browser.find_element(by=By.XPATH, value=xpath)



def botonCaja(context):
    variablebotoncaja = fun_buscar_por_xapth(context, "(//a[@ng-reflect-router-link='/cashiers'])[2]")
    return variablebotoncaja

def botonIniciarCaja(context):
    variablebotoniniciarcaja = fun_buscar_por_xapth(context,xpath='//span[text()=" Iniciar caja "]/parent::*')
    return variablebotoniniciarcaja

def formMonto(context):
    variableformMonto = fun_buscar_por_xapth(context, xpath='//input[@data-input-name="initialAmount"]')
    return variableformMonto

def formNumeroCaja(context):
    variablenrcaja = fun_buscar_por_xapth(context,xpath='//input[@data-input-name="cashierNumber"]')
    return variablenrcaja

def funBotonAgregar(context):
    variablebotonagregar = fun_buscar_por_xapth(context, xpath='//span[text()=" Agregar "]/parent::*')
    return variablebotonagregar

def mensajevalidacion(context):
    variablemensaje = fun_buscar_por_xapth(context,xpath=f'//span[contains(text(),"La caja fue creada exitosamente.")]')
    return variablemensaje


def verventas(context):
    variableverventas = fun_buscar_por_xapth(context,xpath='(//button[contains(text()," Ver ventas ")])[1]')
    return variableverventas

def cerrarCaja(context):
    variablecerracaja = fun_buscar_por_xapth(context,xpath='//span[contains(text()," Cerrar Caja ")]')
    return variablecerracaja

def valorefectivo(context):
    variablevalorefectivo = fun_buscar_por_xapth(context, xpath='//input[@formcontrolname="customInput"]')
    return variablevalorefectivo

def MensajeCierreCaja(context, mensaje):
    variablemensajeCierre = fun_buscar_por_xapth(context, xpath=f'//span[contains(text(),{mensaje})]')
    return variablemensajeCierre


