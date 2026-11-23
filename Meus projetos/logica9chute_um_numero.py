import random
valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input('Chute um numero: '))
    if chute > valor_aleatorio:
        print('Menos')
    elif chute < valor_aleatorio:
        print('Mais')
    else:
        print('acertou')
        acertou = True
