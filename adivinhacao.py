import random

def jogo_adivinhacao():
    numero_secreto = random.randrange(0, 101)
    total_de_tentativas = 0
    pontos = 1000

    #print(numero_secreto)

    print("Qual Nível de dificuldade?")
    print("1 - Fácil, 2 - Médio, 3 - Difícil")

    nivel = int(input("Defina seu nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! seu chute foi maior do que o número secreto")
                ponto_perdidos = abs(numero_secreto - chute) #função abs torna o número absoluto 40-60 = -20 abs(-20) = 20
                pontos = pontos - ponto_perdidos
            elif(menor):
                print("Você errou! seu chute foi menor do que o número secreto")
                ponto_perdidos = abs(numero_secreto - chute) #função abs torna o número absoluto 40-60 = -20 abs(-20) = 20
                pontos = pontos - ponto_perdidos
    print("Fim de Jogo")

if(__name__ == "__main__"): #para verificar se chamou o jogo de adivinhação por primeiro ai a variavel __name__ recebe o valor de __main__ ou se chamou através do arquivos jogos
    jogo_adivinhacao()