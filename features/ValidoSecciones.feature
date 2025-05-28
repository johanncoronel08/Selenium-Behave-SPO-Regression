Feature: Se realiza una validaccion de secciones


  Scenario: REALIZAR UN LOGIN VALIDO
  Given ingreso a la URL "https://spo-dev.btspo.co/auth"
  When valido que estoy en la url correcta
  And Ingreso usuario "btspo@yopmail.com" y contraseña valida "Coronel-1992"
  And hago click en iniciar sesion
  And selecciono la sucursal
  Then al hacer click en continuar deberia llevarme al dashboard principal "https://spo-dev.btspo.co/"

  Scenario Outline: valido cada una de las secciones del dashboard
    Given Hago click en el <modulo>
    Then valido cada una de las se <Secciones>
    Examples: 
    |modulo   |Secciones|
    |Productos |   https://spo-dev.btspo.co/products/dashboard      |
    |Cajas     |   https://spo-dev.btspo.co/cashiers/dashboard      |
    |Combos    |   https://spo-dev.btspo.co/combos      |
    |Gastos    |   https://spo-dev.btspo.co/gastos      |
    |Usuarios  |   https://spo-dev.btspo.co/usuarios    |

