def contador(i, f, p):
    for n in range(i, f+1):
        print(n, end=' -> ')
    print('FIM')

    print('-=-'*10)

    i = 10
    f = 0
    p = -2

    for n in range(i, f-1, p):
        print(n, end=' -> ')
    print('FIM')

    print('-=-'*10)

    i = int(input('Digite o número de início: '))
    f = int(input('Digite o número de fim: '))
    p = int(input('Digite quantos números a contagem vai pular: '))

    if i > f:
        f -= 1
    else:
        f += 1
    if i > f and p >= -1:
        p *= -1
    if i < f and p <= -1:
        p *= -1
    if i > f and p == 0:
        p = -1
    elif i < f and p == 0:
        p = 1

    for n in range(i, f, p):
        print(n, end=' -> ')
    print('FIM')


contador(1, 10, 1)
