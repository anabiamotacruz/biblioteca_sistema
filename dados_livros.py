import json

# Inicialização das listas
livros = []
usuarios = []
livros_alugados = []

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

# Funções para carregar e salvar livros alugados
def carregar_livros_alugados():
    global livros_alugados
    try:
        with open('livros_alugados.json', 'r') as f:
            livros_alugados = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        livros_alugados = []

def salvar_livros_alugados():
    with open('livros_alugados.json', 'w') as f:
        json.dump(livros_alugados, f)

# Função para cadastrar livros
def cadastrar_livro(titulo, autor):
    livro = {'Título': titulo, 'Autor': autor}
    livros.append(livro)
    salvar_livros()
    print('Livro cadastrado com sucesso!')

# Função para listar livros
def listar_livros():
    if not livros:
        print('Nenhum livro cadastrado.')
    else:
        print('Lista de livros:')
        for i, livro in enumerate(livros):
            print(f'{i + 1}. {livro["Título"]} por {livro["Autor"]}')

# Função para listar livros alugados
def listar_livros_alugados():
    if not livros_alugados:
        print('Não há livros alugados.')
    else:
        print('Lista de livros alugados:')
        for i, livro in enumerate(livros_alugados):
            print(f'{i + 1}. {livro["Título"]} por {livro["Autor"]}')

# Remover livro do cadastro
def remover_livro():
    listar_livros()
    if livros:
        try:
            indice = int(input("Digite o número do livro que deseja remover: ")) - 1
            if 0 <= indice < len(livros):
                livro_removido = livros.pop(indice)
                salvar_livros()
                print(f'Livro "{livro_removido["Título"]}" removido com sucesso!')
            else:
                print('Número inválido.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

# Verificar se o usuário está cadastrado
def usuario_cadastrado(nome):
    for usuario in usuarios:
        if usuario["Nome"].lower() == nome.lower():
            return True
    return False

# Alugar livro
def alugar_livro(indice, usuario_index):
    if 0 <= indice < len(livros):
        livro = livros[indice]
        if livro.get('status') == 'disponível':
            livro['status'] = 'alugado'
            livro['alugado_por'] = usuarios[usuario_index]['Nome']
            livros_alugados.append(livro)
            salvar_livros()
            salvar_livros_alugados()
            print(f'Livro "{livro["Título"]}" alugado com sucesso!')
        else:
            print('Livro já está alugado.')

# Devolver livro
def devolver_livro(indice):
    if 0 <= indice < len(livros_alugados):
        livro = livros_alugados.pop(indice)
        livro['status'] = 'disponível'
        livro['alugado_por'] = None
        livros.append(livro)
        salvar_livros()
        salvar_livros_alugados()
        print(f'Livro "{livro["Título"]}" devolvido com sucesso!')

# Cadastrar novo usuário
def novo_cadastro():
    pessoa = input('Digite o nome: ')
    while True:
        try:
            idade = int(input('Digite a idade: '))
            if idade <= 0:
                raise ValueError
            break
        except ValueError:
            print('Idade inválida. Por favor, digite um número positivo.')

    cpf = input('Digite o CPF (somente números): ')
    celular = input('Digite o número de celular (somente números): ')

    usuario = {
        "Nome": pessoa,
        "Idade": idade,
        "CPF": cpf,
        "Celular": celular
    }

    usuarios.append(usuario)
    salvar_usuarios()  # Salvar usuários
    print(f'Leitor cadastrado(a) com sucesso!')

# Listar usuários
def listar_usuarios():
    if not usuarios:
        print('Nenhum usuário cadastrado.')
    else:
        print('Lista de usuários:')
        for i, usuario in enumerate(usuarios):
            print(f'{i + 1}. {usuario["Nome"]}, Idade: {usuario["Idade"]}, CPF: {usuario["CPF"]}, Celular: {usuario["Celular"]}')

# Remover usuário
def remover_usuario():
    listar_usuarios()
    if usuarios:
        try:
            indice = int(input("Digite o número do usuário que deseja remover: ")) - 1
            if 0 <= indice < len(usuarios):
                usuario_removido = usuarios.pop(indice)
                salvar_usuarios()  # Salvar usuários
                print(f'Usuário "{usuario_removido["Nome"]}" removido com sucesso!')
            else:
                print('Número inválido.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

# Menu principal
def main():
    carregar_livros()
    carregar_usuarios()
    carregar_livros_alugados()
    
    while True:
        print('Bem-vindo(a) de volta')
        senha = 'ecobio123'
        digitesenha = input('Por favor, digite a senha: ')
        if senha == digitesenha:
            print('Bem-vindo(a)')
            break
        else:
            print('Senha incorreta, tente novamente')

    while True:
        print('\nMenu')
        print('1. Cadastrar livros')
        print('2. Listar livros')
        print('3. Remover livro')
        print('4. Alugar livro')
        print('5. Devolver livro')
        print('6. Cadastro de pessoa')
        print('7. Listar pessoas')
        print('8. Remover pessoa')
        print('9. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            alugar_livro()
        elif opcao == '5':
            devolver_livro()
        elif opcao == '6':
            novo_cadastro()
        elif opcao == '7':
            listar_usuarios()
        elif opcao == '8':
            remover_usuario()
        elif opcao == '9':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()