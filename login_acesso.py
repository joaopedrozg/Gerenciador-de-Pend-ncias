import sqlite3

conn = sqlite3.connect('login.db')

cursor = conn.cursor()


def insereUsuario(usuario, senha):
    cursor.execute('''INSERT INTO login
                      (usuario, senha) 
                      VALUES (?, ?)''',
                      (usuario, senha))
    
    conn.commit()
    return print('Usuário inserido com sucesso!')

def verificaUsuario(usuario, senha):
    cursor.execute('''SELECT usuario, senha 
                      FROM login 
                      WHERE usuario = ? 
                      AND senha = ?''',
                      (usuario, senha))
    
    verificacao = cursor.fetchone()
    return verificacao
