'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''

no_discount = float(input('Introduce el precio inicial del artículo: '))
discount = no_discount * 20 / 100
print(f'El precio final con descuento es : {no_discount - discount}')