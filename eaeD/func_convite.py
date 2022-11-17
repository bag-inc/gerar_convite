__autor__ = "bag inc"

import random

#? Função para gerar convites e receber-los com base no nome da sala




class Func_convite:
    def __init__(self):
        pass


    def gerar_convite(self):
        sal = input("Digite o nome da sala: ")
        ger = input("Deseja gerar convite?:")


        number_aleat = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        rand_idx = random.randrange(len(number_aleat))
        k = number_aleat[rand_idx]
            
        letter_aleat = ["a", "b","c","d","e","f","g","h","i","j","k", "l",
                        "m","n","o","p","q","r","s","t","u","v","w","x"
                        ,"y","z"]
        rand_idx2 = random.randrange(len(letter_aleat))
        k2 = letter_aleat[rand_idx2]

    
        con = sal.replace(" ",k+k2)
        print(con)

        '''
        codigos = {}

        for co in con:
            codigos[con] = sal
        print(codigos)
        '''
        
