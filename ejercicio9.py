'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''

cantidad = float(input('Introduzca la cantidad de dólares que desea cambiar: '))
operation = cantidad * 0.85

print(f'El cambio de {cantidad} dólares son {operation} euros')