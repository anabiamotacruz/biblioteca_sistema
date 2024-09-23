from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Exemplo de dados (poderia ser dados de um banco de dados)
livros = [
    {"id": 1, "titulo": "Livro A", "autor": "Autor A"},
    {"id": 2, "titulo": "Livro B", "autor": "Autor B"}
]

# Rota para pegar a lista de livros (GET)
@app.route('/api/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)

# Rota para adicionar um novo livro (POST)
@app.route('/api/livros', methods=['POST'])
def add_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

if __name__ == '__main__':
    app.run(debug=True)