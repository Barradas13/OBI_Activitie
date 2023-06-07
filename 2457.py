letra = input()
frase = input()
frase = frase.split()
total = len(frase)
res = 0


for palavra in frase:
    if letra in palavra:
        res +=1

res = (res * 100) / total

print(f'{res:.1f}')