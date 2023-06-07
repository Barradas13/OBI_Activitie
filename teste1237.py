while True:
    try:
        frase1 = input()
        frase2 = input()
        substring = ''
        resultado = ''
        i = 0

        while i < len(frase1):
            tentativa = substring + frase1[i]
            print(tentativa)
            if tentativa in frase2 and tentativa in frase1:
                substring += frase1[i]
                if len(substring) >= len(resultado):
                    resultado = substring
            else:
                substring = ""
                if len(tentativa) > 1:
                    i -= 1

            i += 1
            
        print(len(resultado))

    except EOFError:
        break