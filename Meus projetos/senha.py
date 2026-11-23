senhas = ["Abc", "Senha123", "Oi", "12345", "Python123"]
for senha in senhas:
    if len(senha) >=6:
        print(f'  A senha {senha} e valida')
    else:
        print(f'A senha {senha} e invalidade')