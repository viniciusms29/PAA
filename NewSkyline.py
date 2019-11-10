#----------------------------------------------------#
# Alg.: Skyline --------------------- Disciplina: PAA#
# Aluno: Vinícius Morais dos Santos ----- RA: 0002864#
#----------------------------------------------------#
# Posicao 0 = Esquerda
# Posicao 1 = Altura
# Posicao 2 = Direita
def skyline(buildings):
    #- Pegando o inicio do primeiro predio, e o fim do ultimo predio. Posso fazer um -#
    #- loop entre os predios para ir preenchendo os demais, com as devidas verifica. -#
    # Pega a menor esquerda. Ou seja, o inicio do primeiro prédio a ser construido:
    left = 9999;
    for build in buildings:
        if (build[0] < left):
            left = build[0];
    #---------------------------------------------------------#
    # Pega a maior direita. Ou seja, o final do ultimo prédio a ser construido:
    right = 0;
    for build in buildings:
        if (build[2] > right):
            right = build[2];
    #---------------------------------------------------------#
    # Variavel para controle das alturas dos predios:
    heigthAux = None; 
    # Lista para armazenamento da solucao:
    output = [];
    allHeigth = [];
    height = 0;
    for i in range(left, right + 1):
        # Pego as alturas de cada iteracao de i:
        for build in buildings:
            if ((build[0] <= i) and (build[2] > i)): 
                # Evitar duplicidade:
                if (build[1] in allHeigth):
                    pass
                else:
                    allHeigth.extend([build[1]]);
        # Pego a maior(best) altura das selecionadas no laço acima:
        if (allHeigth):
            for best in allHeigth:
                if (best > height):
                    height = best;
        # Caso nao tenha mais alturas na iterecao, ele seta como 0:            
        else:
            heigth = 0;
        # Monta a solução a cada iteração:
        if (height != heigthAux):
            output.extend([i,height]);
            heigthAux = height;
        # Reseta as variaveis a cada nova iteração:
        allHeigth = [];
        height = 0;    
    return output;

def lerEntrada():
    listTuples = [];
    while (1):
        # Valida a entrada:
        entrada = eval(input());
        # Se entrada for diferente da flag de parada, adiciona na lista de predios:
        if ((entrada != (0,0,0))  and (entrada != (0, 0, 0))):
            listTuples.extend([entrada]);
        else:
            break;
    return listTuples;

def principal ():
    # Pega todos os predios:
    buildings = lerEntrada();
    #buildings = [(0,8,5),(1,4,7),(2,10,9),(11,5,15),(14,3,28),(17,11,20),(19,17,22),(25,13,30)]
    # Pega as solucoes:
    solution = skyline(buildings);
    # Monta a saída:
    out = ""
    for i in range(0,len(solution)):
        if (i != len(solution) - 1 ):
            out = out + str(solution[i]) + ",";
        else:
            out = out + str(solution[i]);
    
    print("("+out+")");

principal();