# Created by Admin at 24/5/2025
Feature: validacion de de apertura de caja

Scenario: REALIZAR UN LOGIN VALIDO
  Given ingreso a la URL "https://spo-dev.btspo.co/auth"
  When valido que estoy en la url correcta
  And Ingreso usuario "btspo@yopmail.com" y contraseña valida "Coronel-1992"
  And hago click en iniciar sesion
  And selecciono la sucursal
  Then al hacer click en continuar deberia llevarme al dashboard principal "https://spo-dev.btspo.co/"

Scenario: validar apertura de caja
  Given al ingresar a la seccion de caja
  When hago click en inicar caja
  And ingreso monto inicial "100"
  And ingreso numero de caja "13"
  And hago click en agregar
  Then Deberia aperturar una caja con el siguiente mensaje "La caja fue creada exitosamente."

Scenario: Cerrar caja abierta
  Given hago click en cerrar caja
  When ingreso el valor de la caja "100"
  And el boton aceptar se deberia habilitar
  And Hago click en aceptar
  Then Deberia cerrar una caja correctamente con el mensaje "La caja fue cerrada exitosamente."


