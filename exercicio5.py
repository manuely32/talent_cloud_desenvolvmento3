#Função que receberá os parametros e efetura o calculo conforme informações do usuário
def calculadora(valor1, valor2, operacao):

    if(operacao == 1):
        calculo = valor1 + valor2
        sinalOperacao = " + "
    elif(operacao == 2):
        calculo = valor1 - valor2
        sinalOperacao = " - "
    elif(operacao == 3):
        calculo = valor1 * valor2
        sinalOperacao = " * "
    elif(operacao == 4):
        calculo = valor1 / valor2
        sinalOperacao = " / "
    
    resultado = f"Resultado: {valor1} {sinalOperacao} {valor2} = {calculo}"
    
    return resultado

#Utilizando o while para manter o programa rodando até que seja informada a opção sair.
while True:
    print("Informe a operação que deseja realizar:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    operacao = int(input())
    
    #Se opções forem válidas será solicitado os valores e repassados para a função calculadora e retornado o valor.
    if(operacao > 0  and operacao <= 4):
        print("Informa o primeiro numero:")
        valor1 = int(input())
        print("Informa o segundo numero:")
        valor2 = int(input())

        #Chamada da função calculadora repassando as variáveis
        resposta = calculadora(valor1, valor2, operacao)

        print(resposta)

    #Se opções não forem válidas, mostra mensagem ao usuário e mostra as opções novamente.
    elif(operacao < 0 or operacao > 4):
        print("Essa opção não existe!")

    #Condição para parar o código utilizando o break
    elif(operacao == 0):
        print("Fim do programa!")
        break



 