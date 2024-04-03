'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
'''

celsius_degrees = 20
fahrenheit_degrees = ((celsius_degrees) * 9 / 5) + 32 

print(fahrenheit_degrees)

#Después de investigar como pedir un valor por pantalla lo realicé de otra manera:


celsius = input('Grados Celsisus: ')
fahrenheit_degrees = float(celsius) * 9 / 5 + 32

print(f'{celsius_degrees} grados Celsius son {fahrenheit_degrees} grados Fahrenheit')