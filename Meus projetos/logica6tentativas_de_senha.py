senha = ''
tentativas = 0
while (senha !=  '123456') and tentativas < 3:
    senha = input('Digite a Senha: ')
    tentativas += 1
    if senha == '123456':
     print('acesso liberado! ')

    elif (senha != '123456') and tentativas < 3:
     print('senha incorreta')

    else:

      print('Exesso de tentativas! tente novamente em 15 minutos.')