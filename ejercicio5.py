'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''

#Función para determinar los números pares del 0 al 100:
def list_pair(n):
  return [i for i in range(n+1) if i % 2 == 0]

#Función para sumar los números pares del 0 al 100:
def sum_list(numbers):
  sum = 0
  for number in numbers:
    sum += number
  return sum

print(sum_list(list_pair(100)))