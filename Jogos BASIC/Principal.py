2
2
import Forca
import Advinhação

def escolha():
    # APRESENTAÇÃO
    print("BEM-VINDO escolha seu jogo")

    # ENTRADA
    tipo = int(input("(1) - Advinhação (2) - Forca: "))

    # ESCOLHA
    if tipo == 1:
        Advinhação.jogar()

    if tipo == 2:
        Forca.jogar()

if __name__ == "__main__":
    escolha()




