'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
word = input('Inserte su palabra, por favor: ')
def is_palindrome(word):
  word = word.lower()
  return word == word[::-1]
print(is_palindrome(word))
