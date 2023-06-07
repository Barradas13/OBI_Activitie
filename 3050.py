contador = 0
while True:
    try:
        coordenadas = input().split()
        meteoros = int(input())
        meteorosDentro = 0
        contador += 1

        x1 = int(coordenadas[0])
        y1 = int(coordenadas[1])
        x2 = int(coordenadas[2])
        y2 = int(coordenadas[3])

        for i in range(1, meteoros +1):
            coordenadasMeteoro = input().split()
            xMeteoro = int(coordenadasMeteoro[0])
            yMeteoro = int(coordenadasMeteoro[1])

            if xMeteoro >= x1 and yMeteoro <= y1 and xMeteoro <= x2 and yMeteoro >= y2:
                meteorosDentro +=1
            
        print(f"Teste {contador}")
        print(meteorosDentro)
    
    except EOFError:
        break