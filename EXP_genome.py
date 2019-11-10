#----------------------------------------------------#
# Alg.: R3PTZ ----------------------- Disciplina: PAA#
# Aluno: Vinícius Morais dos Santos ----- RA: 0002864#
#----------------------------------------------------#
#from validador import imprimeSaida;
import random;
from random import randint;
# Funcao responsavel por montar o genoma 1 a 1. Verifica nela as possibilidades uma a uma:
def r3ptzElemento(verified_input, step, genome):
    life_base = ['X','P','E'];
    if (step > verified_input):
        return genome;
    # Pega a base de vida "X,E,P", e sorteia sempre uma ordem para os candidados em cada iteração(montagem do genoma).
    # Isso para nao fixar os valores de ordem, pois com valores fixados (seguindo a ordem da base), sempre estava encontrando 
    # erros ou ficava em loop até pra genomas pequenos. Ai testando de forma aleatoria deu certo:
    order = [];
    # Crio uma auxiliar para manter a base padrao intacta:
    base_auxiliar = life_base;
    while(base_auxiliar !=[]):
        chosen = random.choice(base_auxiliar);
        base_auxiliar.remove(chosen);
        order.append(chosen);
    # Loop de acordo com as possibilidades de escolha possiveis (X,E,P):
    opt_Gene = 0;
    while(opt_Gene < 3):
        # Com o genoma que ja tenho construido ate o momento, entre as minhas opcoes (X,E,P), gero um novo genoma
        # encaixando apenas mais um gene de acordo com a ordem aleatoriamente gerada, 
        # e faco as verificacoes de validação:
        genarated_genome = genome;
        if (opt_Gene == 0):
            # Caso o ultimo gene do genoma for igual ao novo gene que será testado para completar o genoma, ja cancela essa opcao e tenta outro aleatorio.
            # Assim evitará execusoes em falso, tentativas que serao verificadas e darao errado:
            if str(order[0] != genome[-1:]):                
                genarated_genome += str(order[0]);
            else:
                # Aleatoriza um numero, 0 ou 1
                a = randint(0,1);
                if (a == 0):
                    genarated_genome += str(order[1]);
                else:
                    genarated_genome += str(order[2]);
        elif (opt_Gene == 1):
            # Caso o ultimo gene do genoma for igual ao novo gene que será testado para compor o genoma, ja cancela essa opcao e tenta outro aleatorio:
            if str(order[1] != genome[-1:]):  
                genarated_genome += str(order[1]);
            else:
                # Aleatoriza um numero, 0 ou 1
                a = randint(0,1);
                if (a == 0):
                    genarated_genome += str(order[0]);
                else:
                    genarated_genome += str(order[2]);
        else:
            # Caso o ultimo gene do genoma for igual ao novo gene que será testado para compor o genoma, ja cancela essa opcao e tenta outro aleatorio:
            if str(order[2] != genome[-1:]):  
                genarated_genome += str(order[2]);
            else:
                # Aleatoriza um numero, 0 ou 1
                a = randint(0,1);
                if (a == 0):
                    genarated_genome += str(order[0]);
                else:
                    genarated_genome += str(order[1]);
        position = 1;
        # Uso "posição" para efetuar o controle do genoma ja construido.
        # Para percorrer na string. Para assim analisar se a opçao de gene escolhido (x,e,p), deixa o genoma
        # validado de acordo com as regras passadas:
        while(position <= len(genome)):
            end = 0;
            while(position != end):
                # Particionamento de strings:
                p1 = genome[len(genome)-(position+end):len(genome)-end];
                p2 = genarated_genome[len(genarated_genome)-position:len(genarated_genome)];
                # Percorro o genoma para verificar se de alguma forma possui algum gene igual. Exemplo:
                # XEP EX(E PXP) (EPX P)EP XEP XPE XPX EPX EPX PEP XEP XEP EXP EXE PEX PEP XEP EXP XEX
                # no qual os genes destacados entre paranteses sao "vizinhos". Caso aconteça essa situação, muda a opcao de 
                # gene para se testar:
                if(p1 == p2):
                    # Set no novo genoma o VAZIO, para q ele saia do loop de posicao logo apos, e com vazio vá para o loop
                    # de options, e tentar outra opcao de gene:
                    genarated_genome = '';
                    break;
                end += 1;
            # Verifico para sair do loop, para entrar em outra opcao quando da errado a escolhida anteriormente:
            if(genarated_genome != ''):
                position += 1;
            else:
                break;
        # Se novo genoma diferente de vazio, adiciono outra chamada no procedimento gerado de genoma, criando a 
        # "pilha de recursao" para montagem do genoma:
        if(genarated_genome != ''):
            step += 1;
            genome = r3ptzElemento(verified_input, step, genarated_genome);
            return genome;
        # Controle das opcoes de gene:
        opt_Gene +=1;
    return genome;
# Verifica entrada do elemento que representa o tamanho do genoma:
def lerEntradaElemento():
    while (True): 
        # Uso o "eval" para validar o input(runCodes Pedi):    
        entry = eval(input());
        # Entradad de ser entre 1 e 5000:
        if ((entry >= 1) and (entry <= 5000)):
            break;
        else:
            # Enquanto a entrada nao atender os requisitos necessario, passa mensagem de erro e pedi nova entrada:
            print("\nA entrada deve ser entre 1 e 5000.");
            entry = eval(input());
    return entry;
# Funcao principal do algoritmo:
def principal():
    # Uso a variavel step, para controle de posicao, por exemplo, se for 5 a entrada essa variavel será responsavel por 
    # ajudar no controle do genoma desse tamanho, pois cada passo, representa um gene que irá forma o genoma completo:
    step = 1;
    # Chama a funcao de validação de entrada:
    verified_input = lerEntradaElemento();
    output = '';
    # Monta o genoma:
    while (True):
        if (len(output) == verified_input):
            break;
        else:    
            output = '';
            output = r3ptzElemento(verified_input, step, output);  
    #imprimeSaida(output);
    print(output);
principal();