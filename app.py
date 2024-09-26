from flask import Flask, render_template, request, redirect, url_for
from dados_livros import livros, usuarios
import dados_livros

app = Flask(__name__)

# Carregar os dados iniciais
dados_livros.carregar_livros()
dados_livros.carregar_usuarios()
dados_livros.carregar_livros_alugados()

@app.route('/')
def index():
    return render_template('index.html', livros=dados_livros.livros, usuarios=dados_livros.usuarios)

# Rota para cadastrar um novo livro
@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        dados_livros.cadastrar_livro(titulo, autor)
        return redirect(url_for('index'))
    return render_template('cadastrar_livro.html')

# Rota para alugar um livro
@app.route('/alugar_livro/<int:livro_id>', methods=['POST'])
def alugar_livro(livro_id):
    # Verifique se o livro_id está dentro do intervalo da lista de livros
    if livro_id < 0 or livro_id >= len(livros):
        return "Livro não encontrado", 404  # Retorna erro 404 se o livro não existir
    
    # Pegue o ID do usuário do formulário
    usuario_id = int(request.form['usuario'])  # Convertendo para int para garantir o índice correto
    
    # Acesse o livro a partir da lista de livros
    livro = livros[livro_id]
    
    # Verifique se o livro está disponível
    if livro['status'] == 'disponível':
        livro['status'] = 'alugado'
        livro['alugado_por'] = usuario_id  # Armazene o índice do usuário que alugou
    
    # Redirecione de volta para a página inicial
    return redirect(url_for('index'))

# Rota para devolver um livro
@app.route('/devolver_livro/<int:livro_id>', methods=['POST'])
def devolver_livro(livro_id):
    livro = livros[livro_id]
    
    if livro['status'] == 'alugado':
        livro['status'] = 'disponível'
        livro['alugado_por'] = None  # Redefine para None ao devolver
    
    return redirect(url_for('index'))


# Rota para cadastrar um novo usuário
@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        cpf = request.form['cpf']
        celular = request.form['celular']
        dados_livros.novo_cadastro(nome, idade, cpf, celular)
        return redirect(url_for('index'))
    return render_template('cadastrar_usuario.html')

if __name__ == "__main__":
    app.run(debug=True)
