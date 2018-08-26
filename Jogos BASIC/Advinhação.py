import random

def jogar():

    # APRESENTAÇÃO
    print("**" * 20)
    print("Jogo de advinhação")
    print("**" * 20)

    # VARIAVEIS
    tentativas = 0
    contador = 0
    al = random.randrange(0, 26)
    pontos = 50

    # ENTRADAS
    nivel = int(input("(1) - facil (2) - medio (3) dificil: "))
    print("VC POSSUI INICIALMENTE %d" % (pontos))

    # CONDIÇÃO DO NIVEL
    if nivel == 1:
        tentativas = 15

    elif nivel == 2:
        tentativas = 10

    elif nivel == 3:
        tentativas = 5

    else:
        print("Nivel não existente")

    # JOGO
    while contador < tentativas:
        numero = int(input("Digite o numero entre (0 a 25): "))
        print("-=-=" * 20)
        while numero < 0 or numero > 25:
            numero = int(input("DIGITE NOVAMENTE!!!: "))

        print("Rodada {} de {}".format(contador + 1, tentativas))

        if numero == al:
            print("Parabens vc acertou! e fez %d pontos" % (pontos))
            break

        else:
            if numero < al:
                print("Voce errou para baixo""\n")

            if numero > al:
                print("Voce errou para cima""\n")

        pontos_perdidos = abs(numero - al)
        pontos = pontos - pontos_perdidos

        contador += 1

    print("FIM DO JOGO")

if __name__ == "__main__":
    jogar()



