#Função que receberá os parametros e efetura o calculo conforme informações do usuário
def calculadora(valor1, valor2, operacao):
    if(operacao == 1):
        calculo = valor1 + valor2
        resultado = f"Resultado: {valor1} + {valor2} = {calculo}"
    elif(operacao == 2):
        calculo = valor1 - valor2
        resultado = f"Resultado: {valor1} - {valor2} = {calculo}"
    elif(operacao == 3):
        calculo = valor1 * valor2
        resultado = f"Resultado: {valor1} * {valor2} = {calculo}"
    elif(operacao == 4):
        calculo = valor1 / valor2
        resultado = f"Resultado: {valor1} / {valor2} = {calculo}"
    else:
        resultado = "Operação não encontrada!!"
    return resultado

#Solicitando valores das variáveis que serão repassadas para a função.
valor1 = input("Informa o primeiro numero:")
valor2 = input("Informa o segundo numero:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Informa a operacao que deseja resalizar:")

#Chamada da função calculadora repassando as variáveis
resposta = calculadora(int(valor1), int(valor2),int(operacao))

print(resposta)