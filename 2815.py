texto = input()
texto = texto.split()
resultado = []

for palavra in texto:
    if len(palavra) > 3:
        primeiraSilaba = palavra[0] + palavra[1]
        segundaSilaba = palavra[2] + palavra[3]

        if primeiraSilaba == segundaSilaba:
             contador = 0
             palavraRes = ''

             for letra in palavra:
                 if contador > 1:
                     palavraRes += letra
                 else:
                     contador +=1

             resultado.append(palavraRes)
        else:
            resultado.append(palavra)
    else:
        resultado.append(palavra)

resultadoString = ''
i = 0

for word in resultado:
    if len(resultado) == i:
        resultadoString += word
    else:
        resultadoString += word +  ' '
        i += 1

print(resultadoString[:len(resultadoString)-1])

