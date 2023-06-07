while True:
    try:
        frase = input()
        fraseLista = frase.split()
        resultado = 0
        letra = fraseLista[0][0].upper()
        letraRepetida= ''
        primeiraVez = True

        for palavra in fraseLista:
            letraAnterior = letra
            letra = palavra[0].upper()


            if letraAnterior == letra and letraAnterior != letraRepetida and not primeiraVez:
                    resultado += 1
                    letraRepetida = letra

            if letra != letraAnterior:
                 letraRepetida = ''

            primeiraVez = False

        print(resultado)

    except EOFError:
        break