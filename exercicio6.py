
#Solicitando nome do usuário
print("Informe seu nome:")
nome = input()

#Utilização de while para manter a solicitação do ano de nascimento caso o usuário não informe de forma correta.
while True:
    #Usando try exception para capturar erros e informar ao usuário
    try:
        print("Informe o ano de nascimento entre 1922 e 2021:")
        anoNascimento = int(input())

        #Verificando se o ano digitado está entre o período permitido.
        if(anoNascimento >= 1922 and anoNascimento <= 2021):
            #Calculando idade e parando o while
            idade = 2022 - anoNascimento
            print(f"{nome} você tem {idade} anos!")
            break
        else:
            print("Ano está fora do período determinado!")
    except:
        print("Ano inválido!")

