'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''


age = int(input('Introduzca su edad, por favor: '))
if age >= 18:
  print('Eres mayor de edad')

elif age < 18: #también lo podría poner con else:
  print('No eres mayor de edad')