input=[5,1,3,6,2,4,2,1,3,5,1,2,3,4,5,6,7,8,9]
def python_snake(xs):
    #determinamos el numero de filas de la matriz
    serpiente_filas= len(xs)
    serpiente_columnas=0
    left=0
    right=0
    res=0
    contador=0
    for i in xs:
        if contador==0
            right=i
            if contador%2==0:
                if contador>0:
                    res=i-xs[contador-1]
                else:
                    res=right+res
            serpiente_columnas=serpiente_columnas+i
        else:
            serpiente_columnas=serpiente_columnas-i
        if(serpiente_columnas<0):
            if(abs(serpiente_columnas)>left):
            #left es la cantidad de espacios que hay en la primer fila desde el inicio de la matriz hasta la cabeza de la serpiente
                left=abs(serpiente_columnas)
        contador=contador+1
    #determinamos el numero de columnas de la matriz
    serpiente_columnas=left+right
    snake = []
    #llenamos la matriz de espacios vacios
    for i in range(serpiente_filas):
        fila = []
        for j in range(serpiente_columnas):
                fila.append(" ")
        snake.append(fila)
    fila_serpiente= 0
    suma= 0
    #la primera posicion de la serpiente es el valor absoluto de left
    pos= left
    cont3= 0
    for i in xs:
        body = i
        if cont3%2==0:
            suma=suma+body
            cont3+=1
        else:
            suma=suma-body
            if suma<0:
                pos=left-abs(suma)
            else:
                pos = suma+1
            cont3+=1
        for j in range(body): #este ciclo determina la cantidad de espacios que ocupa el cuerpo de la serpiente
            if fila_serpiente==0 and j==0:
                #solo al inicio imprmimos la cabeza de la serpiente
                snake[fila_serpiente][abs(left)]="H"
            else: #determinamos si la ultima fila va de izquierda a derecha o de derecha a izquierda para poner la cola
                  # en la posicion correcta
                print("pos is", pos)
                print("j is", j)
                print("i is", i)
                print("suma is", suma)
                print("body is", body)
                print("right is", right)
                print("fila_serpiente is", fila_serpiente)
                snake[fila_serpiente][pos + j] = "X"
                if cont3%2==0 and j==(body-1) and fila_serpiente==serpiente_filas-1:
                    snake[fila_serpiente][pos]="T"
                    print("entre1")
                elif cont3%2!=0 and j==(body-1) and fila_serpiente==serpiente_filas-1:
                    print("entre2")
                    snake[fila_serpiente][pos+j]="T"
        fila_serpiente+=1
    for row in snake:
        print(row)
python_snake(input)