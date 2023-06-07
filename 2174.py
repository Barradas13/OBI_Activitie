n = input()
i = 1
listaPomekon = []

while i <= int(n):

    i += 1
    pomekon = input()

    if pomekon not in listaPomekon:
        listaPomekon.append(pomekon)

faltantes = 151 - int(len(listaPomekon))

print(f'Falta(m) {faltantes} pomekon(s).')