#Algoritmo Imprimir numero de Andares de um prédio

#Declaração das variáveis
quantAndares = 10
naoImprimirAndar = 2

#Utilizando o for para imprimir os numeros dos andares
for i in range(1, quantAndares + 1):
  if(i == naoImprimirAndar):
    continue
  print(f"{i}º Andar" )

#Utilizando o while para imprimir os numeros dos andares
i = 1
while( i <= quantAndares):
  if(i != naoImprimirAndar):
    print(f"{i}º Andar" )
  i = i + 1

#Imprimindo os numeros em ordem decrescente com for 
for i in range(quantAndares, 0 ,-1):
  if(i == naoImprimirAndar):
    continue
  print(f"{i}º Andar" )

# Imprimindo os numeros em ordem decrescente com while
i = quantAndares
while( i > 0):
  if(i != naoImprimirAndar):
    print(f"{i}º Andar" )
  i = i - 1