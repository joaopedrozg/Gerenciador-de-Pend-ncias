import msvcrt
import login_acesso
import os
import menu
import mensageria



def getpass(prompt):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        char = msvcrt.getch()
        if char == b'\r':
            print('')
            return password
        elif char == b'\x08': 
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char.decode('utf-8')
            print('*', end='', flush=True)

def login():
    opcao = input('Digite N para cadastrar ou E para entrar: ')
    if opcao == 'n' or opcao == 'N':
        usuario = input('Digite seu Login: ')
        senha = getpass('Digite a senha: ')
        verificacaoUser = login_acesso.verificaUsuario(usuario, senha)
       
        if verificacaoUser ==  None:
            login_acesso.insereUsuario(usuario, senha)
            login()
        elif usuario == verificacaoUser[0]:
            print('Usuário ou senha indisponíveis...')
            login()
       
        

    elif opcao == 'e' or opcao == 'E':
        usuario = input('Digite seu Login: ')
        senha = getpass('Digite a senha: ')
        verificacao = login_acesso.verificaUsuario(usuario, senha)
        if verificacao == None:
            os.system('cls')
            print('Usuário não cadastrado')
            print('ACESSO NEGADO')
            print('Cadastre-se primeiro para usar o Gerenciador')
            login()
            
        elif verificacao[0] == usuario and verificacao[1] == senha:
            os.system('cls')
            menu.menu()
    else: 
        mensageria.sairSimOuNao()

