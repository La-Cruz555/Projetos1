usuario = ''
senha = ''
tentativas = 0

while (usuario != 'NoobMaster69' or senha != 'trovao123') and  tentativas < 3:
    usuario = input('Digite seu nick: ')
    senha = input('Digite sua senha: ')
    tentativas += 1
    if usuario == 'NoobMaster69' and senha == 'trovao123':
     print('Login feito com sucesso')
    else:
       print('Tente novamento em 30 minutos')