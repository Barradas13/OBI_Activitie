n = input()
palavras = input()
eduardo = 1
listaPalavras = palavras.split()
listaResultados = []

for i in listaPalavras:
    verificou = False
    if len(i) > 3:
        listaResultados.append(i)
        verificou = True
    if len(i) > 1 and verificou ==False:
        if i[0] == 'O' and i[1] == 'B':
            listaResultados.append('OBI')
            verificou = True
        if i[0] == 'U' and i[1] == 'R':
            listaResultados.append('URI')
            verificou = True
        
    if verificou == False:
        listaResultados.append(i)


for res in listaResultados:
    if eduardo != len(listaResultados):
        print(res, end=' ')
        eduardo += 1
    else:
        print(res)