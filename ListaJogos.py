import sys, adivinhacao, forca

def escolhe():

    print("************************************************************")
    print("*              || Bem vindo ao cassinopy ||                *")
    print("************************************************************")
    escolha = 0
    while escolha != 5 :

        print("")
        print("Escolha seu Jogo:")
        print("(1) Jogo de Adivinhação")
        print("(2) Jogo de Forca")
        print("(3) Jogo de Dados")
        print("(5) Sair")
        escolha = int(input("Qual é a sua opção: "))
        print("")

        if (escolha == 1) :
            adivinhacao.jogar()
        elif (escolha == 2) :
            forca.jogar()
        elif (escolha == 3) :
            print("Jogo ainda nao disponivel")
        elif (escolha == 5) :
            print("Volte sempre!")
            sys.exit()    


if (__name__ == "__main__") :
    escolhe()            