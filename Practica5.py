#escribir una solucion que pregunte al usuario
#su nombre y apellido, desplegar el texto en 
#pantalla invertido con un espacio entre ellos
nombre_completo = input("Escribe tu primer nombre y primer apellido: ")
nombre_completo = nombre_completo.split(" ")
nombre_completo = nombre_completo[::-1]
nombre_completo = " ".join(nombre_completo)
print(nombre_completo)


#Crear una solucion que le pregunte al usuario 
#su nombre y edad. Entonces escribir un mensaje
#que le diga el año en el que puede llegar a tener
#100 años de edad