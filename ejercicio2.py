'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

def suma_restaurante(precios):
  suma = 0
  for precio in precios:
    suma += precio
  return suma
lista_de_precios = [10, 20, 30]
iva = 0.15
resultado = suma_restaurante(lista_de_precios) * iva + suma_restaurante(lista_de_precios)
print('La factura con IVA es: ' + str(resultado))

#No sé cómo realizar la lista manual lista_de_precios