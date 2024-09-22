import json

# Colocar todos os livros e usuários presentes na biblioteca:
livros = []
usuarios = []

# Função para carregar livros de um arquivo
def carregar_livros():
    global livros
    try:
        with open('livros.json', 'r') as f:
            livros = json.load(f)
    except FileNotFoundError:
        livros = []

# Função para salvar livros em um arquivo
def salvar_livros():
    with open('livros.json', 'w') as f:
        json.dump(livros, f)

# Função para carregar usuários de um arquivo
def carregar_usuarios():
    global usuarios
    try:
        with open('usuarios.json', 'r') as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = []

# Função para salvar usuários em um arquivo
def salvar_usuarios():
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

# Função para cadastro de livros:
def cadastrar_livro():
    titulo = input("Digite o título do livro: \f")
    autor = input('Digite o nome do autor do livro: \f')
    livro = {'Título': titulo, 'Autor': autor}
    livros.append(livro)
    salvar_livros()
    print('Livro cadastrado com sucesso! \f')

# Função para listar os livros cadastrados
def listar_livros():
    if not livros:
        print('Nenhum livro cadastrado. \f')
    else:
        print('Lista de livros: \f')
        for i, livro in enumerate(livros):
            print(f'{i + 1}. {livro["Título"]} por {livro["Autor"]} \f')

# Remover livros do cadastro
def remover_livro():
    listar_livros()
    if livros:
        try:
            indice = int(input("Digite o número do livro que deseja remover: ")) - 1
            if 0 <= indice < len(livros):
                livro_removido = livros.pop(indice)
                salvar_livros()
                print(f'Livro "{livro_removido["Título"]}" removido com sucesso! \f')
            else:
                print('Número inválido. \f')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número. \f')

# Função para cadastrar novo usuário da biblioteca
def novo_cadastro():
    pessoa = input('Digite o nome: \f')
    while True:
        try:
            idade = int(input('Digite a idade: \f'))
            if idade <= 0:
                raise ValueError
            break
        except ValueError:
            print('Idade inválida. Por favor, digite um número positivo. \f')
    cpf = (input('Digite o cpf: \f'))
    celular = (input('Digite o número de celular: \f'))
    print(f'Confira as informações: \f Nome: {pessoa} \f Idade: {idade} \f CPF: {cpf} \f Celular: {celular} \f')
    usuarios.append(usuario)
    salvar_usuarios()
    print(f'Leitor cadastrado(a) com sucesso! \f')

# Função para listar os usuários cadastrados
def listar_usuarios():
    if not usuarios:
        print('Nenhum usuário cadastrado. \f')
    else:
        print('Lista de usuários: \f')
        for i, usuario in enumerate(usuarios):
            print(f'{i + 1}. {usuario["Nome"]}, Idade: {usuario["Idade"]}, CPF: {usuario["CPF"]}, Celular: {usuario["Celular"]} \f')

# Função para remover um usuário da lista
def remover_usuario():
    listar_usuarios()
    if usuarios:
        try:
            indice = int(input("Digite o número do usuário que deseja remover: ")) - 1
            if 0 <= indice < len(usuarios):
                usuario_removido = usuarios.pop(indice)
                salvar_usuarios()
                print(f'Usuário "{usuario_removido["Nome"]}" removido com sucesso! \f')
            else:
                print('Número inválido. \f')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número. \f')

# Menu para o usuário escolher entre cadastrar ou listar livros ou sair
def main():
 carregar_livros()
 carregar_usuarios()
 while True:
    print('\f Seja bem-vindo(a) de volta \f')
    senha = 'ecobio123'
    digitesenha = input('\f Por favor, digite a senha: ')
    if senha==digitesenha:
        print('\f Bem-vindo(a) \f')
        break
    else:
        print('\f Senha incorreta, tente novamente \f')

 while True:
        print('\nMenu')
        print('\f 1. Cadastrar livros \f 2. Listar livros \f 3. Remover livro \f 4. Cadastro de pessoa \f 5. Listar pessoas \f 6. Remover pessoa \f 7. Sair \f')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            novo_cadastro()
        elif opcao == '5':
            listar_usuarios()
        elif opcao == '6':
            remover_usuario()
        elif opcao == '7':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente')

if __name__ == "__main__":
    main()