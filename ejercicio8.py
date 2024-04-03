'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

weigth = float(input('Introduzca su peso: '))
heigth = float(input('Introduzca su altura (en este formato: 1.65): '))
result = weigth / (heigth**2)

if result < 18.5:
  print('Su nivel de peso es bajo')

elif result >= 18.5: #únicamente me muestra la opción del if y de este elif, no sé por qué
  print('Su nivel de peso es normal')

elif result >= 25:
  print('Su nivel de peso es sobrepeso')

elif result > 30:
  print('Su nivel de peso es obesidad')

print(f'Su índice de IMC es de: {result}')