while True:

    texto = input()
    maiuscula = True
    executar = False
    textoRes = ''

    try:
        for i in texto:
            if maiuscula and i != ' ':
                textoRes += i.upper()
                maiuscula = False
            elif i != ' ':
                textoRes += i.lower()
                maiuscula = True
            else:
                textoRes += i
                
        print(textoRes)

    except EOFError:
        break