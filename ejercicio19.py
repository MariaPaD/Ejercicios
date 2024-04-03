'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''

year = int(input('Ingrese el año: '))
if year % 4 == 0:
  print(f'{year} es bisiesto')
else:
  print(f'{year} no es bisiesto')