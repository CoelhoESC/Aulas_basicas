usuario_bd = 'everton'
senha_bd = '123456'

while True:
    usuario = str(input('Nome de usuário: ')).strip().lower()
    senha = input('Senha do usuário: ')
    if usuario == usuario_bd and senha == senha_bd:
        print('Login com sucesso!')
        break
    else:
        print('Usuário ou senha invalidos!')
        print('Tente de novo...')
        continue
