#----------------------------------------------------#
# Alg.: PontosProximos--------------- Disciplina: PAA#
# Aluno: Vinícius Morais dos Santos ----- RA: 0002864#
#----------------------------------------------------#
import math
from math import sqrt
# Calcula a distancia entre dois pontos passado:
def calculaDistancia(x1, y1, x2, y2):
    resultado = sqrt((x2 - x1) **2 + (y2 - y1) **2);
    if float(resultado) < 10000:
        return float(("%.4f" %resultado));
    else:
        return 'INFINITY';
def principal():
    # Numeros de pontos a serem lidos de determinado caso:
    numPontos = input();
    resultadoFinal = [];
    # Ate que o numPontos seja 0, loop:
    while int(numPontos) != 0:
        # Lista de pontos do caso especifico:
        listaPontos = [];
        # Pega os pontos e adiciona as coordenadas na lista:
        for i in range(0,int(numPontos)):
            valores = input().split();
            coordXY = [float(valores[0]), float(valores[1])];
            listaPontos.append(eval('coordXY'));
        tamLista = len(listaPontos);
        menor = float('INFINITY');
        # Encontra a menor distancia entre os pontos:
        for i in range(0, tamLista-1):
            for x in range(i+1, len(listaPontos)):
                atual = float(calculaDistancia(listaPontos[i][0],
                listaPontos[i][1],listaPontos[x][0],listaPontos[x][1]));
                if (atual < menor):
                    menor = atual;
        # Armazena o resultado do determinado caso na lista de resultado:
        if menor != float('INFINITY'):
            resultadoFinal.append("%.4f" %float(menor));
        else: 
            resultadoFinal.append('INFINITY');
        # Numeros de pontos a serem lidos de determinado caso:      
        numPontos = input();
    # Imprime o resultado de cada caso:
    for caso in resultadoFinal:
        print (caso);

principal();