while True:
    try:
        perna = input()
        linguagem = ''

        if perna == 'esquerda':
            linguagem = 'ingles'
        elif perna == 'direita':
            linguagem = 'frances'
        if perna == 'nenhuma':
            linguagem = 'portugues'
        if perna == 'as duas':
            linguagem = 'caiu'
        
        print(linguagem)
        

    except EOFError:
        break