'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

my_word = input('Por favor, ingrese la palabra: ')
def count_vowels(my_word):
  counter = 0
  for c in my_word:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
      counter += 1
  return counter

print(count_vowels(my_word))