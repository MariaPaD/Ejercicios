'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''

#Me falta crear un input de lista

def sum_list(numbers): #Función para sumar todos los números de la lista
  sum = 0
  for number in numbers:
    sum += number
  return sum
