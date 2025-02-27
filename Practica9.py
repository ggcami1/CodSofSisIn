#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales
for i in range(1, 11):
    print(i)
#-------------------------------------------------------------------------#
#Escibir un programa que imprima los primeros 10 numeros impares
for i in range(1, 20, 2):
    print(i)
#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales en orden descendente
for i in range(10, 0, -1):
    print(i)
#-------------------------------------------------------------------------#
#Escribir un programa que escriba la tabla de multiplicar de un numero especificado por el usuario
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
#-------------------------------------------------------------------------#
#Escribir un programa que escriba el producto de los digitos de un numero especificado por el usuario
numero = int(input("Ingresa un número: "))
producto = 1

for digito in str(numero):
    producto *= int(digito)

print(f"El producto de los dígitos de {numero} es {producto}")
