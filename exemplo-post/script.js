const nomeProduto = document.getElementById('nome-produto');
const valorProduto = document.getElementById('valor-produto');
const descricaoProduto = document.getElementById('descricao-produto');
const btnEnviar = document.getElementById('btn-enviar');
const feedbackUsuario = document.getElementById('feedback-usuario')
const produtosCadastrados = document.getElementById('produtos-cadastrados')

function cadastrarProduto(e) {
    e.preventDefault()

    const dados = {
        produto: nomeProduto.value,
        valor: valorProduto.value,
        descricao: descricaoProduto.value
    }

    fetch('https://httpbin.org/post', {
        method: 'POST',
        body: JSON.stringify(dados)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.json.produto)
            const divProduto = document.createElement('div')
            divProduto.innerHTML = `
            <p>Produto: ${data.json.produto}</p>
            <p>Valor: ${data.json.valor}</p>
            <p>Descrição: ${data.json.descricao}</p>
           `
            divProduto.classList.add('produto-div')
            produtosCadastrados.appendChild(divProduto)

            feedbackUsuario.innerText = 'Produto cadastrado com sucesso!!!.'

            nomeProduto.value = ''
            valorProduto.value = ''
            descricaoProduto.value = ''
        })
        .catch(e => {
            feedbackUsuario.innerText = 'Erro ao cadastrar o produto.'
            console.log(e)
        })
}


btnEnviar.addEventListener('click', (e) => cadastrarProduto(e))