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