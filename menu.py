import pendencias
import os
import pandas as pd
import mensageria


def menu():
    print('Digite I para incluir uma pendência')
    print('Digite S para selecionar todos os registro')
    print('Digite G para selecionar um registro pelo numero de documento')
    print('Digite D para deletar documento')
    print('Digite E para editar um documento')
    print()

    opcao = input('Digite o que deseja fazer! ')

    if opcao == 'I' or  opcao == 'i':
        os.system('cls')
        print('============================================') 
        documento = input('Digite o número do documento: ')
        observacao = input('Escreva a observação que deseja incluir: ')
        status = input('Coloque o status da pendência: ')
        if documento == '' or observacao == '' or status == '':
            print('É necessário que preencha todos os campos...')
            menu()
        else:
            pendencias.insereRegistro(documento, observacao, status) 
            print('============================================')
            menu()
            
    elif opcao == 'S' or  opcao == 's':
       os.system('cls')
       listapendencias = pendencias.selecionaTodosRegistros()
       df = pd.DataFrame(listapendencias, columns=['ID','Documento', 'Observação', 'Status'])
       print(df)
       print('============================================') 
       menu()

    elif opcao == 'G' or opcao == 'g':
        os.system('cls')
        print('============================================') 
        documento = input('Digite o número de documento que deseja buscar: ')
        registro_por_documento = pendencias.selecionaRegistroPorDocumento(documento)

        if registro_por_documento == None or documento == '':
            print(f'Nenhum regintro encontrado pelo número de {documento} ou está com o campo de busca vazio...')
            menu()
        else:    
            columns=['ID','Documento', 'Observação', 'Status']
            contador = 0
            for reg in registro_por_documento:
                print(f"{columns[contador]} : {reg}")
                contador = contador + 1
            
            print('============================================') 
            menu()

    elif opcao == 'D' or opcao == 'd':
         os.system('cls')
         print('============================================') 
         documento = input('Digite o número de documento que deseja deletar: ')
         pendencias.deletaRegistro(documento)
         print('============================================') 
         menu()

    elif opcao == 'E' or opcao == 'e':
        os.system('cls')
        documento = input('Digite o número do documento que deseja alterar a Observação e ou Status: ')
        verificaDocumento = pendencias.selecionaRegistroPorDocumento(documento)
        if verificaDocumento == None:
            print('Nenhum documento foi identificado para ser editado...')
            menu()
        else:
            observacao = input('Digite a nova observação: ')
            status = input('Digite o novo status: ') 
            pendencias.atualizaRegistro(observacao, status, documento)
            print(f'Documento {documento} alterado com sucesso!')
            print('============================================') 
            menu()
    else:
        mensageria.sairSimOuNaoMenu()