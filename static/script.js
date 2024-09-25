// Exemplo de script para interações futuras
console.log('Biblioteca ativa!');
function removerLivro(livroId) {
    fetch(`/remover_livro/${livroId}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();  // Recarregar a página para atualizar a lista de livros
    })
    .catch(error => console.error('Erro:', error));
}
document.getElementById('form-usuario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitar o reload da página ao enviar o formulário

    const formData = new FormData(this);

    // Faz a requisição POST para cadastrar o usuário
    fetch('/cadastrar_usuario', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (response.ok) {
            location.reload();  // Recarregar a página para mostrar o novo usuário
        }
    })
    .catch(error => console.error('Erro ao cadastrar usuário:', error));
});
