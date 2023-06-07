"""fibonat = []
fibonot = []

k = int(input())

i = 1
numero = 1 
numeroAnterior = 0

while True:
    res = numero + numeroAnterior

    fibonat.append(res)

    numeroAnterior = numero
    numero = res

    if i not in fibonat:
        fibonot.append(i)
    
    if len(fibonot) >= k:
        print(fibonot[k-1])

    i +=1"""

k = int(input())
numero = 1
numeroAnterior = 0
contadorFibonat = 0
pare = False

while not pare:
    res = numeroAnterior + numero
    resProximo = res + numero
    if res + 1 < resProximo:
        for i in range(numero + 1, res):
            contadorFibonat += 1
            if contadorFibonat == k:
                print(i)
                pare = True

    numeroAnterior = numero
    numero = res

