import random


def jogar() :
    imprime_cabecalho()

    palavraSecreta = busca_palavra_secreta()

    letrasAcertadas = inicializa_forca(palavraSecreta)

    letrasJaInformadas = []

    print(letrasAcertadas)

    tentativas = 0
    while True:
        chute = recebe_chute()

        if (chute in letrasJaInformadas):
            print("Voce já informou essa letra, tente outra ")
            continue

        letrasJaInformadas = chute
        if (chute in palavraSecreta):
            letrasAcertadas = atualiza_letras_acertadas(chute, palavraSecreta, letrasAcertadas)

            if ('_' not in letrasAcertadas): # esse if vai procurar o caracter _ dentro da lista
                mensagem_vencedor()
                break
        else :
            desenha_forca(tentativas)
            if (tentativas >= 7):
                mensagem_perdedor(palavraSecreta)
                break
            tentativas += 1
        print(letrasAcertadas)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def atualiza_letras_acertadas(chute, palavraSecreta, letrasAcertadas):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):  # upper vai transformar a letra em maiusculo
            letrasAcertadas[index] = chute  # upper vai transformar a letra em minusculo
        index += 1

    return letrasAcertadas

def recebe_chute():
    return input("Qual a letra? ").strip().upper()  # strip vai tirar os espacos do inicio e fim da letra


def imprime_cabecalho():
    print("*****************************************")
    print("     Bem vindo ao jogo de forca          ")
    print("*****************************************")

def busca_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo :
        palavras.append(linha.strip())

    arquivo.close()

    rnd = random.randrange(1, len(palavras))
    palavraSecreta = palavras[rnd].upper()
    return palavraSecreta

def inicializa_forca(palavraSecreta):
    return ['_' for letra in palavraSecreta] # um laco dentro da inicializacao da lista. Vai incluir o _ para cada letrad a palavra


# esse if vai identificar se o arquivo foi importado em algum outro arquivo ou se está sendo executado diretamente no console
if (__name__ == "__main__") :
    jogar()    
