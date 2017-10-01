import sys, random

num = random.randint(1, 10)
maximoTentativas = 3
rodada = 1

#while (rodada <= maximoTentativas) :
for rodada in range(1, maximoTentativas + 1) :
    print("Tentativa {} de {}".format(rodada, maximoTentativas))
    chute = int(input("Adivinhe o valor: "))
    if (chute <=0 or chute > 10) :
        print("O valor deve ser entre 1 e 10")
        continue;

    if (chute == num) :
        print("Parabéns, você acertou!!")
        break
    elif (chute > num) :
        print("Errou!! Você digitou um valor maior! ")
    elif (chute < num) :
        print("Errou!! Você digitou um valor menor!  ")        
 #   rodada = rodada + 1    
print("Fim do jogo")