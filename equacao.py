def modulando(valor):
    return valor + valor * -2

def diferencaEntreCordenadas(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]

    if a < 0:
        a = modulando(a)
    if b < 0:
        b = modulando(b)

    return (a + b) ** 1/2


p1 = (1, 3)
p2 = (2, 3)
p3 = (4, 3)
p4 = (5, 3)
p5 = (3.996, 1)
p6 = (1.98, 1)

c1 = diferencaEntreCordenadas(p2, p6)
c2 = diferencaEntreCordenadas(p3, p5)
c3 = diferencaEntreCordenadas(p1, p4)

pisca = (c1 + c2) / (2 * c3)

if pisca > 0.5:
    print('Nao piscou')
else:
    print('piscou')






"""BOCA ABERTA"""

def modulando(valor):
    return valor + valor * -2

def diferencaEntreCordenadas(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]

    if a < 0:
        a = modulando(a)
    if b < 0:
        b = modulando(b)

    return (a + b) ** 1/2


p1 = (1, 3)
p2 = (2, 3)
p3 = (4, 3)
p4 = (5, 3)
p5 = (3.996, 1)
p6 = (1.98, 1)

c1 = diferencaEntreCordenadas(p2, p6)
c2 = diferencaEntreCordenadas(p3, p5)
c3 = diferencaEntreCordenadas(p1, p4)

pisca = (c1 + c2) / (2 * c3)

if pisca < 0.5:
    print('BOCA FECHADA')
else:
    print('BOCA ABERTA')