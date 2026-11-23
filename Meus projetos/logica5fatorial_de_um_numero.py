numero = int(input('Digite o fatorial que quer calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1,numero +1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
        print(f'o fatorial de {numero} e {fatorial}')
else:
    print('informe apenas numero positivos')