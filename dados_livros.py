# Colocar todos os livros presentes na biblioteca:
livros = []

# Função para cadastro de livros:
def cadastrar_livro():
    titulo = input("Digite o título do livro: \f")
    autor = input('Digite o nome do autor do livro: \f')
    livro = {'Título': titulo, 'Autor': autor}
    livros.append(livro)
    print('Livro cadastrado com sucesso! \f')

# Função para listar os livros cadastrados
def listar_livros():
    if not livros:
        print('Nenhum livro cadastrado. \f')
    else:
        print('Lista de livros: \f')
        for i, livro in enumerate(livros):
            print(f'{i + 1}. {livro['titulo']} por {livro['autor']} \f')

# Função para cadastrar novo usuário da biblioteca
def novo_cadastro():
    pessoa = input('Digite o nome: \f')
    idade = int(input('Digite a idade: \f'))
    cpf = float(input('Digite o cpf: \f'))
    celular = float(input('Digite o número de celular: \f'))
    print(f'Confira as informações: \f Nome: {pessoa} \f Idade: {idade} \f CPF: {cpf} \f Celular: {celular} \f')
    print(f'Leitor cadastrado(a) com sucesso! \f')

# Menu para o usuário escolher entre cadastrar ou listar livros ou sair
def main():
 while True:
    print('\f Seja bem-vindo(a) de volta \f')
    senha = 'ecobio123'
    digitesenha = input('\f Por favor, digite a senha: ')
    if senha==digitesenha:
        print('\nMenu')
        print('\f 1. Cadastrar livros \f 2. Listar livros \f 3. Cadastro de pessoa \f 4. Sair \f')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            novo_cadastro()
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente')
    else:
        print('\f Senha incorreta, tente novamente \f')

if __name__ == "__main__":
    main()