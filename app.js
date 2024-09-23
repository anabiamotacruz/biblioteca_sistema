console.log('Arquivo app.js carregado');
// Função para buscar livros da API
fetch('http://127.0.0.1:5000/api/livros')
    .then(response => response.json()) // Converte a resposta em JSON
    .then(data => {
        const listaLivros = document.getElementById('lista-livros');
        data.forEach(livro => {
            const item = document.createElement('li');
            item.textContent = `${livro.titulo} - ${livro.autor}`;
            listaLivros.appendChild(item);
        });
    })
    .catch(error => console.error('Erro ao buscar livros:', error));