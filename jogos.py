import forca
import adivinhacao

def escolhe_jogo():
    print("**********************************")
    print("*********Escolha se Jogo!*********")
    print("**********************************")

    print("1 - Forca, 2 - Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogo_forca()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogo_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()

