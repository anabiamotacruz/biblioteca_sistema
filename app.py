<<<<<<< Updated upstream
from flask import Flask, render_template, request, redirect, url_for
import json
import dados_livros 

app = Flask(__name__)

# Inicializar dados
dados_livros.carregar_livros()
dados_livros.carregar_usuarios()
dados_livros.carregar_livros_alugados()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        dados_livros.cadastrar_livro(request.form['titulo'], request.form['autor'])
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/listar_livros')
def listar_livros():
    return render_template('listar.html', livros=dados_livros.livros)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect, jsonify, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar flash

# Inicialização das listas
livros = []
usuarios = []

# Funções para carregar e salvar livros
def carregar_livros():
    global livros
    try:
        with open('livros.json', 'r') as f:
            livros = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        livros = []

def salvar_livros():
    with open('livros.json', 'w') as f:
        json.dump(livros, f)

# Funções para carregar e salvar usuários
def carregar_usuarios():
    global usuarios
    try:
        with open('usuarios.json', 'r') as f:
            usuarios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []

def salvar_usuarios():
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

# Página inicial
@app.route('/')
def index():
    carregar_livros()
    carregar_usuarios()
    return render_template('index.html', livros=livros, usuarios=usuarios, enumerate=enumerate)

# Rota para cadastrar livro
@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    
    # Cada livro começa como disponível
    livro = {
        'Título': titulo,
        'Autor': autor,
        'status': 'disponível',  # Status do livro
        'alugado_por': None  # Inicialmente, ninguém alugou
    }
    livros.append(livro)
    salvar_livros()
    flash(f'Livro "{titulo}" cadastrado com sucesso!', 'success')
    return redirect('/')

# Rota para remover livro
@app.route('/remover_livro/<int:livro_id>', methods=['POST'])
def remover_livro(livro_id):
    carregar_livros()
    if 0 <= livro_id < len(livros):
        livro_removido = livros.pop(livro_id)
        salvar_livros()
        flash(f'Livro "{livro_removido["Título"]}" removido com sucesso!', 'success')
        return jsonify({'message': f'Livro "{livro_removido["Título"]}" removido com sucesso!'}), 200
    return jsonify({'message': 'Livro não encontrado.'}), 404

# Rota para cadastrar novo usuário
@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    idade = request.form['idade']
    cpf = request.form['cpf']
    celular = request.form['celular']

    # Verifica se a idade é um número positivo
    try:
        idade = int(idade)
        if idade <= 0:
            return jsonify({'message': 'Idade inválida. Por favor, insira um número positivo.'}), 400
    except ValueError:
        return jsonify({'message': 'Idade inválida. Por favor, insira um número válido.'}), 400

    # Verifica se o CPF é único
    carregar_usuarios()
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            return jsonify({'message': 'Usuário com esse CPF já cadastrado.'}), 400

    # Adiciona o novo usuário
    usuario = {
        "Nome": nome,
        "Idade": idade,
        "CPF": cpf,
        "Celular": celular
    }
    usuarios.append(usuario)
    salvar_usuarios()
    flash(f'Usuário {nome} cadastrado com sucesso!', 'success')
    return jsonify({'message': f'Usuário {nome} cadastrado com sucesso!'}), 200

# Rota para remover usuário
@app.route('/remover_usuario/<int:id>', methods=['POST'])
def remover_usuario(id):
    carregar_usuarios()
    try:
        usuario_removido = usuarios.pop(id)
        salvar_usuarios()
        flash(f'Usuário {usuario_removido["Nome"]} removido com sucesso!', 'success')
    except IndexError:
        flash("Usuário não encontrado.", "error")
    return redirect('/')

# Rota para alugar livro
@app.route('/alugar_livro/<int:indice>', methods=['POST'])
def alugar_livro(indice):
    carregar_livros()
    if indice < len(livros):
        # Verifica se o livro está disponível
        if livros[indice]['status'] == 'disponível':
            # Aluga o livro
            livros[indice]['status'] = 'alugado'
            # Obtém o índice do usuário a partir do formulário
            usuario_index = request.form.get('usuario')
            livros[indice]['alugado_por'] = int(usuario_index)
            salvar_livros()  # Salva as alterações nos livros
            flash(f'Livro "{livros[indice]["Título"]}" alugado com sucesso!', 'success')
            return redirect('/')
    flash("Livro não disponível ou índice inválido", "error")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> Stashed changes
