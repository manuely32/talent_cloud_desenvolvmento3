const titulo = document.getElementById('titulo')
const listaOrdenada = document.getElementById('lista-ordenada')
const listaNaoOrdenada = document.querySelector('ul')
const link = document.querySelector('a')

titulo.innerText = 'Titulo da página'
link.innerText = 'Site Proz Educação'
listaNaoOrdenada.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`
listaOrdenada.innerHTML = `
    <li><a href='https://www.youtube.com/'>YouTube</a></li>
    <li><a href='https://www.dio.me/'>Dio.</a></li>
    <li><a href='https://www.facebook.com/'>facebook</a></li>
`


