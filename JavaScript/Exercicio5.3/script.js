const titulo = document.createElement('h1')
titulo.id = "titulo"
titulo.innerText = 'Título da Página'

// Adicionando o primeiro produto (método complexo)
const produto = document.createElement('div')
const imagem_produto = document.createElement('img')
imagem_produto.src = "imagem.jpg"

const nome_produto = document.createElement('p')
nome_produto.innerText = "Mochila Cinza"

const preco_produto = document.createElement('p')
preco_produto.innerText = 'R$ 15,00'

produto.appendChild(imagem_produto)
produto.appendChild(nome_produto)
produto.appendChild(preco_produto)

const body = document.querySelector('body')

body.appendChild(titulo)
body.appendChild(produto)

// Adicionando o segundo produto (método simples)
const produto2 = document.createElement('div')
produto2.innerHTML = `
    <img src="imagem2.jpg" alt="">
    <p>Bolsa feminina</p>
    <p>R$ 35,00</p>
`
body.appendChild(produto2)