while True:
    try:
        frase1 = input()
        frase2 = input()
        substring = ''
        resultado = ''
        

        for i in frase1:
            tentativa = substring + i 
            if tentativa in frase2 and tentativa in frase1:
                for i in frase1:
                    tentativa = substring + i 
                    if tentativa in frase2 and tentativa in frase1:
                        substring += i 
                        if len(substring) >= len(resultado):
                            resultado = substring 
                    else:
                        substring = ''


        print(len(resultado))

    except EOFError:
        break