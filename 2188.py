contador = 0
terrenos = int(input())
while True:
        c = 0
        coordenadasTerrenos = {}
        nenhum = False

        if terrenos == 0:
            break

        for i in range(1, terrenos +1):
            coordenadaTerreno = input().split()
            coordenadasTerrenos[i] = coordenadaTerreno

        while c < len(coordenadasTerrenos):
            cont = 1
            for i in coordenadasTerrenos:
                if cont == 1:
                    x11 = coordenadasTerrenos[i][0]
                    y11 = coordenadasTerrenos[i][1]
                    x21 = coordenadasTerrenos[i][2]
                    y21 = coordenadasTerrenos[i][3]
                    key1 = i 
                if cont == 2:
                    x12 = coordenadasTerrenos[i][0]
                    y12 = coordenadasTerrenos[i][1]
                    x22 = coordenadasTerrenos[i][2]
                    y22 = coordenadasTerrenos[i][3]
                    key2 = i 
                cont += 1
            
            if x12 >= x21 or y22 >= y12:
                nenhum = True
                break
            
            if x12 >= x11:
                x1 = x12
            else:
                x1 = x11

            if x22 <= x21:
                x2 = x22
            else:
                x2 = x21

            if y12 <= y11:
                y1 = y12
            else:
                y1 = y11

            if y22 >= y21:
                y2 = y22
            else:
                y2 = y21

            coord =  x1, y1, x2, y2
            del(coordenadasTerrenos[key1])
            del(coordenadasTerrenos[key2])

            coordenadasTerrenos['terreno1'] = coord
            c += 1

        contador += 1
        print(f"Teste {contador}")
        if nenhum: 
            print('nenhum')
        else: 
            print(coordenadasTerrenos['terreno1'])
        
        terrenos = int(input())
        if terrenos != 0:
            print('')
        else:
            break