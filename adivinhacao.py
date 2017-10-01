import random

def jogar():
    print("*****************************************")
    print("     Bem vindo ao jogo de adivinhação    ")
    print("*****************************************")
    print("Escolha o nível de dificuldade")
    nivel = int(input("(1) Fácil, (2) Médio, (3) Difícil: "))
    totalTentativas = 5
    valor = random.randrange(1, 101)

    if (nivel == 1) :
        totalTentativas = 20
    elif (nivel == 2) :
        totalTentativas = 10
    elif(nivel == 3) :
        totalTentativas = 5

    for rodada in range(1, totalTentativas + 1) :
        print("Tentativa {} de {}".format(rodada, totalTentativas))
        chute = int(input("Digite um valor de 1 a 100 : "))
        if (chute <= 0 or chute > 100) :
            print("O numero deve ser maior que zero e menor que 100. Você desperdiçou uma tentativa.")
            continue

        if (chute == valor) :
            print("Parabéns, você acertou")
            break
        elif chute > valor:
            print("Errou! Seu chute foi muito alto ")
        elif chute < valor :
            print("Errou! Seu chute foi muito baixo")    
    print("Fim de Jogo")



# esse if vai identificar se o arquivo foi importado em algum outro arquivo ou se está sendo executado diretamente no console
if (__name__ == "__main__") :
    jogar()    
