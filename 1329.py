vezesJogadas = int(input('Digite quantas vezes o jogo foi jogado:'))
lista = input('Digite os valores da lista:')
lista = lista.split(' ')

i = 1

mariaWins = 0
joaoWins = 0

print(lista[1])

for i in lista:
    print(i)
    if i == 1:
        joaoWins += 1
    else:
        mariaWins += 1
        
print(joaoWins, mariaWins)