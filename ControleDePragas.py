def vizinhos(matrix, i, j):
    return [(x,y)   for x in [i-1,i,i+1] 
                        for y in [j-1,j,j+1] 
                            if x in range(0,len(matrix)) and y in range(0,len(matrix[x])) and (x,y) != (i,j)]

def geraMatrix(matrix, linha, coluna):
    for i in range(linha):
        aux = [];
        valor = input().split();
        for j in range(coluna): 
            aux.append(int(valor[j]));
        matrix.append(aux);

def principal ():
    qntCasos = input();
    listaDias = [];
    # Loop da quantidade de casos, não uso varivel para percorer o loop porque nao a utilizo pra nada:
    for _ in range(int(qntCasos)): 
        dias = 0;
        matrix = [];
        tamMatrix = input().split();
        lin, col = int(tamMatrix[0]), int(tamMatrix[1]);
        geraMatrix(matrix, lin, col);
        X, Y = lin, col;
        remedioX, remedioY = input().split();
        remedioX, remedioY = int(remedioX)-1, int(remedioY)-1;
        # Aplica remedio:
        if matrix[remedioX][remedioY] == 1:
            matrix[remedioX][remedioY] = (0);
        espalhaRemedio = [(remedioX,remedioY)];
        auxEspalhaRemedio = espalhaRemedio;
        listaVizinhos = [];
        # Enquanto tiver valores 1 na matrix, faca:
        while len([valor for linha in matrix for valor in linha if valor == 1]) >= 1:
            for elemento in sorted(espalhaRemedio):
                valor = vizinhos(matrix, elemento[0],elemento[1]);
                for x in valor: 
                    if matrix[x[0]][x[1]] != 0:
                        listaVizinhos.append(x);
                espalhaRemedio.remove(elemento);
            if len(listaVizinhos) == 0:
                break;
            for coord in sorted(listaVizinhos):
                # Aplica remedio:
                if matrix[coord[0]][coord[1]] == 1:
                    matrix[coord[0]][coord[1]] = (0);
                if coord not in auxEspalhaRemedio:
                    espalhaRemedio.append(coord);
                    auxEspalhaRemedio.append(coord);
                listaVizinhos.remove(coord);
            if len(listaVizinhos) == 0 : 
                dias+=1;  
        listaDias.append(dias);
    for caso in listaDias:
        print (str(caso));

principal();