# Proyecto Urban Grocers 


---
## INDICE

- Descripción 
- Lista de comprobación
- Archivos de proyecto
- Paquetes de python
- Instrucciones para las pruebas


---
## Descripción
Proyecto para comprobar 9 pruebas automatizadas

---
## Lista de comprobación 
№	Description	ER:
- 1	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 2	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
- 3	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
- 4	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
- 5	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 6	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 7	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
- 9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400
---
## Archivo de proyecto
- .gitignore
- configuration.py
- create_kit_name_kit_test.py
- data.py
- README.md
- Sender_stand_request.py
---
## Paquetes de Python
- pip
- Pytest
- requests
---
## Instrucciones para las pruebas

Creación del Proyecto para Urban Grocers
Realización de:

- 1 Clona el repositorio de GitHub en tu máquina local:
 git clone https://github.com/tu_usuario/qa-project-Urban-Grocers-app-es.git
- 2 Crea y Navega a la carpeta del proyecto:
 cd qa-project-Urban-Grocers-app-es
- 3 Si usas un Sotfware como Pycham ve a los paquetes e instala 
pip, pythes, requests
- 4 Estas listos para correr los test desde pycham
 


