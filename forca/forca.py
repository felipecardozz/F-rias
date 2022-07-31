import random
from desenho import enforcamento
import string

lista = ["Amarelo", "Amor", "Amiga", "Mãe", "Meia", "Noite", "Oculos", "onibus", "Ovo", "Pai", "Patético", "Parque", "Passarinho", "Peixe", "Pijama", "Rato", "Umbigo", "Clube", "Copo", "Doce", "Elefante", "Escola", "Estojo", "Faca", "Foto", "Garfo", "Geleia", "Girafa", "Janela", "Limonada", "Esquerdo", "Filantropo", "Fugaz", "HIV", "Sigma", "Horrorizado", "Maluco", "Impacto", "Gênio", "vasco",
         "FLUFLUFLUFLU", "Modernidade", "Oftalmologista", "Bolsonaro", "Pororoca", "Quarentena", "Quimera", "Ardiloso", "Asterisco", "Basquete", "Caminho", "Champanhe", "Chiclete", "Chuveiro", "Coelho", "Contexto", "Acender", "Afilhado", "Branco", "Cama", "Caneca", "Celular", "Ceu", "Desalmado", "Esfirra", "Ave", "Avião", "Balao", "Bebe", "Bolo", "Reportagem", "Sino", "Taciturno", "Ufanismo", "Víscera"]

# Definimos nosso elemento ou variável como palavra


# palavraDecente serve para achar apenas palavras sem acentuação
def palavraDecente(lista):
    # choice atributo do random para escolher aleatoriamente
    palavra = random.choice(lista)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(lista)

    return palavra.upper()

# Defininfo a forma como a forca funciona pegando palavras decentes da lista e método de letras usadas


def forca():
    palavra = palavraDecente(lista)
    letrasDaPalavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letrasUsadas = set()

# Tentativas de acerto das letras
    vidas = 7

# Para saber a resposta do jogador
    while len(letrasDaPalavra) > 0 and vidas > 0:
        print("Você tem", vidas, " vidas e usou as letras: ",
              ' '.join(letrasUsadas))

# Qual a palavra selecionada
        listaDePalavras = [
            letra if letra in letrasUsadas else '-' for letra in palavra]
        print(enforcamento[vidas])
        print("Palavra:", ' '.join(listaDePalavras))

        letrasDoJogador = input("Digite uma letra: ").upper()
        if letrasDoJogador in alfabeto - letrasUsadas:
            letrasUsadas.add(letrasDoJogador)
            if letrasDoJogador in letrasDaPalavra:
                letrasDaPalavra.remove(letrasDoJogador)
                print('')

            else:
                vidas = vidas - 1  # takes away a life if wrong
                print("Errou,", letrasDoJogador, "tão erradas")

        # Para quando o jogador não digita letra
        elif letrasDoJogador in letrasUsadas:
            print("Tu já falou essa ai, bobão")

        else:
            print("Mané, isso nem letra é ")
            
    # Morreu 
    if vidas == 0:
        print(enforcamento[vidas])
        print("Era", palavra, ", deu pra tu não")
    else:
        print("Também fica fácil quando a resposta é ", palavra)


if __name__ == '__main__':
    forca()
