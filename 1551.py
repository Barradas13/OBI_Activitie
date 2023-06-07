n = int(input())
i=1

while i <= n:
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    total = 0
    frase = input()

    for letraFrase in frase:
        for letraAlfa in alfabeto:
            if letraFrase.upper() == letraAlfa:
                alfabeto.remove(letraAlfa)
                total +=1
    
    if total == 26:
        print('frase completa')
    elif total < 13:
        print('frase mal elaborada')
    else:
        print('frase quase completa')
    
    i+=1
