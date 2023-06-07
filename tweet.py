num = int(input())
i = 1


while(i<= num):
    linha = input()
    linha = linha.split()
    
    comeco = 0
    maiorpalavra = linha[0]
    listaresultado = []
    indice = 0
    
    while len(linha) > 0:
        
        for palavra in linha:
            if len(maiorpalavra) < len(palavra):
                maiorpalavra = palavra
            else:
                comeco += 1
                    
        linha.remove(maiorpalavra)
        
        listaresultado.append(maiorpalavra)
        maiorpalavra = ''
        comeco = 0
        
   
    i += 1 

    eduardo = 1

    for res in listaresultado:

        if eduardo != len(listaresultado):
            print(res, end=' ')
            eduardo += 1
        else:
            print(res)