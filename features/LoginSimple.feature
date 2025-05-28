# Created by Admin at 17/5/2025
Feature: Se realiza un login simple


  Scenario: REALIZAR UN LOGIN VALIDO
  Given ingreso a la URL "https://spo-dev.btspo.co/auth"
  When valido que estoy en la url correcta
  And Ingreso usuario "btspo@yopmail.com" y contraseña valida "Coronel-1992"
  And hago click en iniciar sesion
  And selecciono la sucursal
  Then al hacer click en continuar deberia llevarme al dashboard principal "https://spo-dev.btspo.co/"

