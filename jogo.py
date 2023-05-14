import random
#abre os arquivos
facil = open('dificuldades/facil.txt')
medio = open('dificuldades/medio.txt')
dificil = open('dificuldades/dificil.txt')
#transforma os txt em lista
facil = facil.read().splitlines()
medio = medio.read().splitlines()
dificil = dificil.read().splitlines()
#define o maximo que o numero aleatorio vai escolher depois (o -1 esta la pq a contagem assim como no js comeca no 0)
maxfacil = len(facil)-1
maxmedio = len(medio)-1
maxdificil = len(dificil)-1

#       ANOTACOES
# -read() le o arquivo inteiro
# -readline() le linha por linha, depende da linha atual
# -readlines() le todas as linhas (incluindo os \n) e coloca elas numa lista
# -splitlines() transforma o texto em lista linha por linha, sem incluir os \n
# -len() no caso de uma array retorna o numero de elementos, no caso de string retorna o numero de caracteres
# -isinstance() parece o type() mas retorna um valor booleano, ex: isinstance(5,int) retorna true 
# -try: testa um bloco por erros
# -except no caso de erros: cuida do erro como se fosse um if(substituir por try).. else(substituir por except)..


#chamado no caso de algum valor invalido
def invalido():
        print('-------------------------------------\nvoce inseriu um valor invalido tente novamente!\n')
        start()


#define o jogo (ou pelo menos a escolha de palavras ate agora)
def start():
    modo = input('escolha um modo\n\n1 = facil\n2 = medio\n3 = dificil\n:')
    try:
        if int(modo) == 1:
            print(facil[random.randint(0,maxfacil)])
        elif int(modo) == 2:
            print(medio[random.randint(0,maxmedio)])
        elif int(modo) == 3:
            print(dificil[random.randint(0,maxdificil)])
        else:
            invalido()
    except:
        invalido()

start()

