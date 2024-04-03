'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

minutes = int(input('Ingrese los minutos: '))
hour = minutes // 60 # // división a la baja
final_minutes = minutes % 60  # % resto de la división

print(f'{hour} hora(s) y {final_minutes} minuto(s)')