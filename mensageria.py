import login
import menu

def sairSimOuNao():
                opcaon = input('Deseja sair? Y/N: ')
                if opcaon == 'N' or opcaon == 'n':
                    login.login()
                elif opcaon == 'Y' or opcaon == 'y':
                    quit()
                elif opcaon == '':
                     sairSimOuNao()

def sairSimOuNaoMenu():
                opcaon = input('Deseja sair? Y/N: ')
                if opcaon == 'N' or opcaon == 'n':
                    menu.menu()
                elif opcaon == 'Y' or opcaon == 'y':
                    quit()
                elif opcaon == '':
                     sairSimOuNaoMenu()

                     