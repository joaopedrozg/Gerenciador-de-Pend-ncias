import criadorDasBases
import login
from colorama import Fore


if __name__ == "__main__":
    print(Fore.GREEN)
    print('============================================') 
    print('== Bem Vindo ao Gerenciador de Pendências ==')
    print('============================================') 
    print()
    
    criadorDasBases.conectar()
    login.login()
    



