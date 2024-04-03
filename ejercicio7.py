'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''

number_a = float(input('Introduca el primer número: '))
number_b = float(input('Introduca el segundo número: '))
arithmetic_operation = input('Introduzca la operación deseada (+ - * /): ')
suma = '+'
resta = '-'
multiplicación = '*'
división = '/'

if arithmetic_operation == suma:
  print(f'La suma es: {number_a + number_b}')
  
elif arithmetic_operation == resta:
  print(f'La resta es: {number_a - number_b}')

elif arithmetic_operation == multiplicación:
  print(f'La multiplicación es: {number_a * number_b}')
  
elif arithmetic_operation == división:
  print(f'La división es: {number_a / number_b}')