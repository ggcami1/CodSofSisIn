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
encontrado = False
y = 0;
for x in ciudades:
    if(nombre_ciudad==x):
        print(monumentos[y])
        encontrado=True
        break
    else:
        y += 1
if encontrado is False:
    print("No hay registro de el monumento de esa ciudad")
#-------------------------------------------------------------------------#
#Escriba un programa para verificar si una persona puede votar o no

#-------------------------------------------------------------------------#
#Escriba un programa que identifique entre dos numeros cual es el menor
 
#-------------------------------------------------------------------------#
#Escribir un programa que identifique entre 4 personas cual es la de mnor edad

#-------------------------------------------------------------------------#
#Escribir un programa que identifique si una letra es Mayusula o Minuscula de una palabra escrita por el usuario