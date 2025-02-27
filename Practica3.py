#Zonas Horarias
#Definir 5 ciudades del mundo y checar su diferencia en la zona horaria
#Calcular la hora de las 5 ciudades a base de la hora especificada por el usuario
#Cabe considerar que la hora sera representada en un sistema de 12 horas

ciudades_mundo=["dublin","londres","tokio","los_angeles","nueva_york","nueva_deli"]
horas_mundo=[+6,+7,+15,-2,+2,+11.3]
formato="AM"
hora_mexico = int(input("Ingresa el valor de la hora que quieres consultar: "))
if 0 <= hora_mexico <=24 :
    print("La hora en las siguientes ciudades seria: ")
    for hora in horas_mundo:
        if 0 < hora_mexico < 12:
            formato = "AM"
            hora_final = hora_mexico + hora
        elif hora_mexico in [0, 24]:
            formato = "AM"
            hora_final = 0 + hora
            if(hora_final > 12):
                hora_final = hora_final - 12
                formato = "PM"
        elif 12 < hora_mexico < 24:
            hora_final = (hora_mexico - 12)+hora
            formato = "PM"
        indice = horas_mundo.index(hora)
        print(ciudades_mundo[indice], abs(hora_final), formato)
else:
    print("La hora ingresada no es valida")

# #-------------------------------------------------------------------------#


