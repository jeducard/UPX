import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para criar a tabela de usuários no banco de dados
def criar_tabela_usuarios():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        celular TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        foto_documento BLOB,
        foto_reconhecimento BLOB,
        biometria TEXT,
        modo TEXT DEFAULT 'light'
    )
    """)
    conexao.commit()
    conexao.close()

# Função para cadastrar um novo usuário
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    celular = dados['celular']
    senha = dados['senha']
    
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, celular, senha) VALUES (?, ?, ?, ?)",
                       (nome, email, celular, senha))
        conexao.commit()
        conexao.close()
        return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201
    except sqlite3.IntegrityError:
        conexao.close()
        return jsonify({'mensagem': 'Erro: E-mail ou celular já cadastrados.'}), 400

# Função para iniciar sessão com biometria
@app.route('/biometria', methods=['POST'])
def iniciar_sessao_biometria():
    dados = request.get_json()
    usuario_id = dados['id']
    biometria = dados['biometria']
    
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET biometria = ? WHERE id = ?", (biometria, usuario_id))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': 'Sessão iniciada com biometria.'}), 200

if __name__ == '__main__':
    criar_tabela_usuarios()
    app.run(debug=True)
