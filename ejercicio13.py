'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
number = int(input('Introduzca un número entero: '))
i = 2
while number % i != 0:  
    i += 1
if i == number:
    print(f'El número {number} es primo')
else:
   print(f'El númerno {number} no es primo')
   
#No me queda muy claro 