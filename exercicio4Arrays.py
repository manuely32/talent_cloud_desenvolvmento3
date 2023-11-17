lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

#substituindo batons por rímel
lista_produtos[1] = "rimel"

#substituindo loções por cremes hidratantes
lista_produtos[4] = "cremes hidratantes"

#removendo delineadores da lista
lista_produtos.pop()

#adicione dois novos produtos da sua escolha à lista. 
lista_produtos.append("sombra")
lista_produtos.append("desodorantes")

for i in range(len(lista_produtos)):
    print(f"Temos {lista_produtos[i]} à venda!")

#lista após as alterações
print(lista_produtos)
