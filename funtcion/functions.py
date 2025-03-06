import random
from os import system, name 

#funcao apagar a tela
def clear_screen ():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')
        return "limpo"
    
#funcao conteudo do jogo
def game_corp():
    clear_screen()
    print("\nBem vindo ao jogo da forca")
    print("Vamos começar \n")
    print("Adivinhe a palavra abaixo: \n")
    
    #lista de palavras
    words =["banana", "abacate", "uva", "morango", "laranja",]
    word = random.choice(words) #escolhe uma palavra aleatoria
    word = word.lower() 
    
    words_list = ['_' for letra in word] 
    
    #numero de chances
    chances = 6
    while chances > 0:
        print(" ".join(words_list))
        print("\nChances Restante: ", chances)
        print("\nLetras erradas: ", " " .join(wrong_letters)) 
        
        #tentaivas
        tentativa = input("\nDigite uma letra: ").lower()
        if tentativa in word:
            index = 0
            for letra in word:
                if tentativa == letra:
                    words_list[index] = letra
                index += 1
        else:
            chances -= 1
            wrong_letters.append(tentativa)
    #lista de letras erradas
    wrong_letters = []