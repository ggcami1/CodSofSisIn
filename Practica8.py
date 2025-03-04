#-------------------------------------------------------------------------#
#Pregunta el nombre de una ciudad y muestra el monumento mas famoso de esa ciudad
# Ciudad		Monumento
#Delhi			Red Fort
#Paris			Torre Eifel
#Nueva York		Estatua de la Libertad
#Rio de Janeiro	Cristo Redentor

ciudades=["Delhi","Paris","Nueva York","Rio de Janeiro"]
monumentos=["Red Fort","Torre Eifel","Estatua de la libertad","Cristo Redentor"]

nombre_ciudad=input("Escribe el nombre de la ciudad del que quieres saber su monumento mas famoso: ")

if nombre_ciudad in ciudades:
    indice=ciudades.index(nombre_ciudad)
    print("El monumento mas famoso de la ciudad de",nombre_ciudad,"es",monumentos[indice])
else:
    print("No hay registro de el monumento de esa ciudad")
#-------------------------------------------------------------------------#
#Escriba un programa para verificar si una persona puede votar o no
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres elegible para votar.")
else:
    print("No eres elegible para votar.")

#-------------------------------------------------8------------------------#
#Escriba un programa que identifique entre dos numeros cual es el menor
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

if numero1 < numero2:
    print(f"El número menor es {numero1}")
elif numero2 < numero1:
    print(f"El número menor es {numero2}")
else:
    print("Ambos números son iguales")

#-------------------------------------------------------------------------#
#Escribir un programa que identifique si el numero ingresado por el usuario es par o impar
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")