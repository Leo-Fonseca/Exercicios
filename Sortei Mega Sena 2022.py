# Definindo o input para o usuário
# Criando um laço a partir do número digitado pelo usuário
# Criando uma lista de números inteiros (de 1 até 60) com laço de 6 repetições
# Printando a lista
# Definindo um intervalo de 1 segundo entre cada print
# Msg para o usuário


import random
import time

njogos = int(input('Quantos jogos você deseja fazer?'))
for d in range(njogos):
    lista = [random.randint(1,60) for c in range(6)]
    print(lista)
    time.sleep(1)
print('Boa sorte com seus {} jogos'.format(njogos))