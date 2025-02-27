#Conversor de divisas

#calcular en base a un valor dado por el usuario
#su equivalencia en las diferentes divisas definidas

#china
yuan=2.81
#japon
yen=0.14
#Estados Unidos
dolar=20.49
#union europea
euro=21.28
#Reino Unido
libra=25.5

pesos = int(input("Ingresa la cantidad de pesos a convertir: "))

print("Los pesos equivalen a {:.2f} yuanes".format(pesos*yuan))
print("Los pesos equivalen a {:.2f} yenes".format(pesos*yen))
print("Los pesos equivalen a {:.2f} dolares".format(pesos*dolar))
print("Los pesos equivalen a {:.2f} euros".format(pesos*euro))
print("Los pesos equivalen a {:.2f} libras".format(pesos*libra))
# #-------------------------------------------------------------------------#
 
