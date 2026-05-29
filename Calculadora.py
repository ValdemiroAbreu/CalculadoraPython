def soma(valorP,valorS):
    return valorP + valorS
def text_soma():
        print("===Somar===\n"+
        "Digite o primeiro número \n")
        valorP = float(input())
        print("===Somar===\n" +
        f"Primeiro número: {valorP}\n" +
        "Digite o segundo valor\n")
        valorS = float(input())
        resultado = soma(valorP,valorS)
        print("===Somar===\n" +
        f"Primeiro número: {valorP}\n" +
        f"Segundo número: {valorS}\n" +
        f"Resultado da soma: {resultado} \n")
def subtracao(valorP,valorS):
    return valorP - valorS
def multiplicacao(valorP,valorS):
    return valorP * valorS
def divisao(valorP,valorS):
    return valorP / valorS

i = 0
while i <= 0:
    print("===Calculadora===")
    print(
        "Digite o número da operação\n"
        "1 - Soma\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "0 - Encerrar operação\n"
    )
    opcao = int(input())
    print(" ")
    if opcao == 1:
        print("===Somar===\n"+
        "Digite o primeiro número \n")
        valorP = float(input())
        print("===Somar===\n" +
        f"Primeiro número: {valorP}\n" +
        "Digite o segundo valor\n")
        valorS = float(input())
        resultado = soma(valorP,valorS)
        print("===Somar===\n" +
        f"Primeiro número: {valorP}\n" +
        f"Segundo número: {valorS}\n" +
        f"Resultado da soma: {resultado} \n")
        
        """
        print("===Somar===\n" +
        "1 - Continuar a soma\n" +
        "2 - Realizar uma nova soma\n" +
        "3 - Realizar uma nova operação\n" +
        "0 - Encerrar operação\n")
        opcao = int ((input))
        if opcao == 1:
            text_soma()
        """
    elif opcao == 2:
        print("===Subtração===\n"+
        "Digite o primeiro número \n")
        valorP = float(input())
        print("===Subtração===\n" +
        f"Primeiro número: {valorP}\n" +
        "Digite o segundo valor\n")
        valorS = float(input())
        resultado = subtracao(valorP,valorS)
        print("===Subtração===\n" +
        f"Primeiro número: {valorP}\n" +
        f"Segundo número: {valorS}\n" +
        f"Resultado da subtração: {resultado} \n")

    elif opcao == 3:
        print("===Multiplicação===\n"+
        "Digite o primeiro número \n")
        valorP = float(input())
        print("===Multiplicação===\n" +
        f"Primeiro número: {valorP}\n" +
        "Digite o segundo valor\n")
        valorS = float(input())
        resultado = multiplicacao(valorP,valorS)
        print("===Multiplicação===\n" +
        f"Primeiro número: {valorP}\n" +
        f"Segundo número: {valorS}\n" +
        f"Resultado da multiplicação: {resultado} \n")

    elif opcao == 4:
        print("===Divisão===\n"+
        "Digite o primeiro número \n")
        valorP = float(input())
        print("===Divisão===\n" +
        f"Primeiro número: {valorP}\n" +
        "Digite o segundo valor\n")
        valorS = float(input())
        resultado = divisao(valorP,valorS)
        print("===Divisão===\n" +
        f"Primeiro número: {valorP}\n" +
        f"Segundo número: {valorS}\n" +
        f"Resultado da divisão: {resultado} \n")

    elif opcao == 0:
        break

    else:
        print("Opção inválida")
                