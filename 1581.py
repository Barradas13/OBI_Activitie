n = int(input())
i = 1


while i <= n:
    pessoas = int(input())
    contador = 1
    linguasFaladas = []

    while contador <= pessoas:
        linguaFalada = input()
        if linguaFalada not in linguasFaladas:
            linguasFaladas.append(linguaFalada)
        contador += 1

    if len(linguasFaladas) == 1:
        for lingua in linguasFaladas:
            print(lingua)
    else:
        print('ingles')

    i += 1