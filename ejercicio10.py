'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

number_day = int(input('¿Qué número de día de la semana es hoy (1, 2, 3, 4, 5, 6 o 7)?: '))
if number_day == 1 :
  print('Hoy es Lunes')
elif number_day == 2 :
  print('Hoy es Martes')
elif number_day == 3 :
  print('Hoy es Miércoles')
elif number_day == 4 :
  print('Hoy es Jueves')
elif number_day == 5 :
  print('Hoy es Viernes')
elif number_day == 6 :
  print('Hoy es Sábado')
elif number_day == 7 :
  print('Hoy es Domingo')
else:
  print('No has introducido un número del 1 al 7, inténtelo de nuevo por favor')