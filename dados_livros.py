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
        print('Nenhum livro cadastrado.')
    else:
        print('Lista de livros:')
        for i, livro in enumerate(livros):
            print(f'{i + 1}. {livro['titulo']} por {livro['autor']}')

# Menu para o usuário escolher entre cadastrar ou listar livros ou sair
def main():
 while True:
    print('\nMenu')
    print('1. Cadastrar livros')
    print('2. Listar livros')
    print('3. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente')

if __name__ == "__main__":
    main()