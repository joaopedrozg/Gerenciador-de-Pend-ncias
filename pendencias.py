import sqlite3

conn = sqlite3.connect('pendencias.db')

cursor = conn.cursor()


def insereRegistro(documento, observacao, status):
    cursor.execute('''INSERT INTO pendencias
                      (documento, observacao, status) 
                      VALUES (?, ?, ?)''', 
                     (documento, observacao, status))
    
    conn.commit()
    return print('Registro inserido com sucesso!')


def selecionaRegistroPorDocumento(documento):
    cursor.execute('''SELECT id, documento, observacao, status
                      FROM pendencias
                      WHERE documento = ?''',
                     (documento,))
    
    pendencia = cursor.fetchone()
    return pendencia

def selecionaTodosRegistros():
    cursor.execute('''SELECT id, documento, observacao, status 
                      FROM pendencias''')
    
    pendencias = cursor.fetchall()
    return pendencias

def deletaRegistro(documento):    
    verificaSeExisteRegistro = selecionaRegistroPorDocumento(documento)

    if verificaSeExisteRegistro != None:

        cursor.execute('DELETE FROM pendencias WHERE documento=?', (documento,))
        conn.commit()
        verificaSeFoiDeletado = selecionaRegistroPorDocumento(documento)

        if verificaSeFoiDeletado == None:

            return print(f'Deletado com sucesso o documento {documento}!')
    
    else:
        return print(f'Erro, documento {documento} não exite na base de dados...')
     

def atualizaRegistro(observacao, status, documento):    
    cursor.execute('''UPDATE pendencias
                      SET observacao = ?, status = ?
                      WHERE documento = ?''', 
                      (observacao, status, documento))
    conn.commit()
