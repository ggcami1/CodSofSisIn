from dask.array import left_shift

input=[1,2,3]
def python_snake(xs):
    #determinamos el numero de filas de la matriz
    serpiente_filas= len(xs)
    serpiente_columnas=0
    left=0
    contador=0
    for i in xs:
        if contador%2==0:
            serpiente_columnas=serpiente_columnas+i
        else:
            serpiente_columnas=serpiente_columnas-i
        if(serpiente_columnas<0):
            #left es la cantidad de espacios que hay en la primer fila desde el inicio de la matriz hasta la cabeza de la serpiente
            left=serpiente_columnas
        contador=contador+1
    #determinamos el numero de columnas de la matriz
    serpiente_columnas=abs(left)+serpiente_columnas
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
    pos= abs(left)
    cont3= 0
    for i in xs:
        body = i
        if cont3%2==0:
            suma=suma+body
            cont3+=1
        else:
            suma=suma-body
            if suma<0:
                pos=0
            else:
                pos = suma
            cont3+=1
        for j in range(body): #este ciclo determina la cantidad de espacios que ocupa el cuerpo de la serpiente
            if fila_serpiente==0 and j==0:
                #solo al inicio imprmimos la cabeza de la serpiente
                snake[fila_serpiente][abs(left)]="H"
            else: #determinamos si la ultima fila va de izquierda a derecha o de derecha a izquierda para poner la cola
                  # en la posicion correcta
                if cont3%2==0 and j==(body-1) and fila_serpiente==serpiente_filas-1:
                    snake[fila_serpiente][pos]="T"
                elif cont3%2!=0 and j==(body-1) and fila_serpiente==serpiente_filas-1:
                    snake[fila_serpiente][pos+j]="T"
                else:
                    # lo demas es parte del cuerpo de la serpiente
                    snake[fila_serpiente][pos+j] = "X"
        fila_serpiente+=1
    print("Snake is :", snake)
python_snake(input)