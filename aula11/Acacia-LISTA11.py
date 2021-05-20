#ProvaFinal
#Acacia Calegari
#114153997

# importa a função sample do módulo random
from random import sample

posicoes_selecionadas = [] #lista que recebe as posicoes selecionadas
tela = [] #lista que recebe os numeros da tela, a tela eh aquele quadradinho 4x4(4 por 4)

# preenche tela com valores
def reset_tela():
    ''' essa funcao preenche a variavel tela com numeros aleatorios da
    lista de pares de 1 a 8'''
    possiveis_valores = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]  # lista com possiveis valores
    for y in range(4): #esse for eh pra cada linha preencher os numeros dos possiveis valores, o y eh a posicao vertical.
        linha = [] #isso aqui eh cada linha da tela que vou preenchendo, seja na horizontal ou vertical
        for x in range(4): #esse x eh da posicao horizontal
            valor = sample(possiveis_valores, 1)[0] #aqui eh uma funcao sample que fica dentro do modulo random , e serve pra pegar um valor aleatorio dentro da lista de valores possiveis
            possiveis_valores.remove(valor) #aqui removo o valor q foi pego
            linha.append(valor)#aqui adiciono o valor a linha
        tela.append(linha) #aqui adiciono a linha na tela

# função para imprimir tela
def imprimir_tela(mask = True):
    ''' essa funcao imprime os valores na tela '''
    for y in range(4): #aqui eh um loop que interage em cada posicao vertical, y da tela. o 4 eh pq vai de 0 a 3 
        saida = "" #aqui crio uma variavel vazia p saida, p futuramente ser adicionado os numeros na tela
        for x in range(4): #esse for eh pra pegar a posicao de cada posicao horizontal x, de 0 a 3 
            numero = tela[y][x] #aqui pego o valor da tela usando as posicoes x e y
            if mask and ([y, x] not in posicoes_selecionadas): #se quiser esconder os numeros com asterisco 
                numero = "*" #aqui deixa o numero escondido pelo asterisco
            saida = saida + str(numero) + " " #aqui concateno o numero na saida 
        print(saida) #aqui printa o numero na saida

# funcao que le a primeira posicao
def selecionar_primeira_posicao():
    '''essa funcao le a primeira posicao, e coloca um imput, para o usuário digitar '''
    print("Escolha a primeira posição [x,y]: ") #mensagem para o usuario poder escolher a primeira posicao
    while True: #loop que fica rodando ate o usuario digitar uma opcao valida
        entrada = input() #aqui aparece a opcao para o usuario digitar a posicao x e y (horizontal e vertical do jogo)
        primeira_posicao = entrada.split(",") #separa a entrada em x e y
        x = int(primeira_posicao[0]) #atribui a primeira posicao a x
        y = int(primeira_posicao[1]) #atribui a primeira posicao a y
        
        if x <0 or x > 3: #valida se x esta no intervalo de 0 a 3
            print("Posição inválida. Escolha a primeira posição [x,y]:") #interage com o usuario caso a posicao x seja invalida
            continue #reinicia o loop
        if y <0 or y > 3: #valida se y esta no intervalo de 0 a 3
            print("Posição inválida. Escolha a primeira posição [x,y]:") #interage com o usuario caso a posicao y seja invalida
            continue #reinicia o loop
        return [x,y] #retorna a posicao selecionada, se tudo estiver certo

# funcao que le a segunda posicao
def selecionar_segunda_posicao():
     '''essa funcao le a segunda posicao, e coloca um imput, para o usuário digitar '''
    print("Escolha a segunda posição [x,y]: ") #mensagem para o usuario poder escolher a segunda posicao
    while True: #loop que fica rodando ate o usuario digitar uma opcao valida
        entrada = input() #aqui aparece a opcao para o usuario digitar a posicao x e y (horizontal e vertical do jogo)
        segunda_posicao = entrada.split(",") #separa a entrada em x e y
        x = int(segunda_posicao[0]) #atribui a primeira posicao a x
        y = int(segunda_posicao[1]) #atribui a primeira posicao a y
        
        if x <0 or x > 3: #valida se x esta no intervalo de 0 a 3
            print("Posição inválida. Escolha a segunda posição [x,y]:") #interage com o usuario caso a posicao x seja invalida
            continue #reinicia o loop
        if y <0 or y > 3: #valida se y esta no intervalo de 0 a 3
            print("Posição inválida. Escolha a segunda posição [x,y]:") #interage com o usuario caso a posicao y seja invalida
            continue #reinicia o loop
        return [x,y] #retorna a posicao selecionada, se tudo estiver certo
 
# cria novo jogo
reset_tela()
# imprime tela mostrando os números
imprimir_tela(mask=False) #aqui mostra na tela os numeros aleatorios de tamanho 4x4(4 por 4)

# avisa que o jogo começou
print("INICIANDO JOGO") #mostra essa menssagem de iniciando jogo, para o usuario
cont_jogadas = 0 #aqui conta quantas vezes o usuario jogou ate vencer

# loop do jogo
while True:
    cont_jogadas = cont_jogadas + 1 #aqui aumenta a quantidade de jogadas em 1
    imprimir_tela() #Aqui imprime a tela inicial (aquele monte de asteriscos de tamanho 4 x 4(4 por 4)

    pos1 = selecionar_primeira_posicao() #atribui a primeira posicao selecionada pelo usuario
    posicoes_selecionadas.append(pos1) #adiciona a primeira posicao a lista de posicoes selecionadas
    imprimir_tela() #mostra na tela os asteriscos nao selecionados , e os valores das posicoes selecionadas
    
    pos2 = selecionar_segunda_posicao() #atribui a segunda posicao selecionada pelo usuario
    posicoes_selecionadas.append(pos2) #adiciona a primeira posicao a lista de posicoes selecionadas
    imprimir_tela() #mostra na tela os asteriscos nao selecionados , e os valores das posicoes selecionadas
    
    valor1 = tela[pos1[0]][pos1[1]] #aqui recebe os valores da primeira posicao
    valor2 = tela[pos2[0]][pos2[1]] #aqui recebe os valores da segunda posicao

    if valor1 != valor2: #aqui compara se os valores da primeira e segunda posicao sao diferentes
        print("Você errou... tente de novo.") #aqui interage com o usuario , avisando que houve um erro
        # remove da lista as posições desse turno
        posicoes_selecionadas.remove(pos1) #aqui remove da lista a posicao 1 selecionada na jogada
        posicoes_selecionadas.remove(pos2) #aqui remove da lista a posicao 2 selecionada na jogada
    else: #caso as comparacoes sejam iguais, ou seja ,acerte as posicoes
        print("Parabéns! Você acertou")    #interage com o usuario , avisando que acertou
        
    
    if len(posicoes_selecionadas) == 16: #verifica se o usuario conseguiu achar todas as 16 posicoes
        print("VOCÊ VENCEU EM " + cont_jogadas + " JOGADAS") #aqui informa que o usuario venceu, e a quantidade de jogadas.
        break
