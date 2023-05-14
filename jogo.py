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
chutes = []
#       ANOTACOES
# -read() le o arquivo inteiro
# -readline() le linha por linha, depende da linha atual
# -readlines() le todas as linhas (incluindo os \n) e coloca elas numa lista
# -splitlines() transforma o texto em lista linha por linha, sem incluir os \n
# -len() no caso de uma lista retorna o numero de elementos, no caso de string retorna o numero de caracteres
# -isinstance() parece o type() mas retorna um valor booleano, ex: isinstance(5,int) retorna true 
# -try: testa um bloco por erros
# -except no caso de erros: cuida do erro como se fosse um if(substituir por try).. else(substituir por except)..
# -append() adiciona um item no final da lista
# -isalpha() retorna verdadeiro apenas se todos os caracteres sao letras do alfabeto aA-zZ (sem numeros)
# -decimal() retorna verdadeiro apenas se todos os caracteres sao numeros decimais 0-9 (sem ² nem ½)

def escolhaletra():
    checkletras()
    chute = (input('\nescolha uma letra\n:'))
    if chute.isalpha() and len(chute) == 1:
        if chute in chutes:
          print('\n\n-------------------------------------\nvc ja tentou essa letra, tente novamente ;)\n')
          escolhaletra()
        else:
          chutes.append(chute)
          escolhaletra()
    else:
          invalido()
          escolhaletra()

#separa as letras e as divide no caso de hifen, tambem revela letras caso ja tenho sido 'chutadas'
def checkletras():
    print('\n-------------------------------------\n')
    for letra in palavra:
        if letra == '-':
            print(' ', end=' ')
        elif letra in chutes:
            print(letra, end = ' ')
        else:
            print('_',end = ' ')
    print('')

#chamado no caso de algum valor invalido
def invalido():
        print('\n\n-------------------------------------\nvoce inseriu um valor invalido tente novamente!\n')


#define o jogo (ou pelo menos a escolha de palavras ate agora)
def start():
    global palavra
    modo = input('\nescolha um modo\n\n1 = facil\n2 = medio\n3 = dificil\n:')
    if modo.isdecimal():
        if int(modo) == 1:
            palavra = facil[random.randint(0,maxfacil)]
            escolhaletra()
        elif int(modo) == 2:
            palavra = medio[random.randint(0,maxmedio)]
            escolhaletra()
        elif int(modo) == 3:
            palavra = dificil[random.randint(0,maxdificil)]
            escolhaletra()
        else:
            invalido()
            start()
    else:
        invalido()
        start()
start()

