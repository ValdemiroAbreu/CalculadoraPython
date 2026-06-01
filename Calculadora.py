def text_operacao(opcao,valorP = None ):
        operacao = definicao_operacao(opcao)

        print(f"==={operacao}===\n")
        
        if valorP is None:
            print("Digite o primeiro número: \n")
            valorP = float(input())
        else:
             print(f"Resultado da última operação: {valorP}\n")
        
        print(f"==={operacao}===\n" +
        f"Primeiro número: {valorP}\n" +
        "Digite o segundo valor\n")
        valorS = float(input())
        
        if operacao == "Soma":
            resultado = soma(valorP,valorS)
        elif operacao == "Subtração":
            resultado = subtracao(valorP,valorS)
        elif operacao == "Multiplicação":
            resultado = multiplicacao(valorP,valorS)
        elif operacao == "Divisão":                
            resultado = divisao(valorP,valorS)            
        
        print(f"==={operacao}===\n" +
        f"Primeiro número: {valorP}\n" +
        f"Segundo número: {valorS}\n" +
        f"Resultado da {operacao.lower()}: {resultado} \n")
        resultado_continuacao = text_operacao(opcao,0)
        
        texto_continuar_operacao(opcao,resultado_continuacao)
        return resultado_continuacao


def texto_continuar_operacao(opcao,resultado_continuacao):
    operacao = definicao_operacao(opcao)
    print(f"==={operacao}===\n" +
        f"1 - Continuar a {operacao.lower()}\n" +
        f"2 - Realizar uma nova {operacao.lower()}\n" +
        "3 - Realizar uma nova operação\n" +
        "0 - Encerrar operação\n")
    opcao_cont = int (input())
    if opcao_cont == 1:
        return text_operacao(opcao, resultado_continuacao)
    elif opcao_cont == 2:
        text_operacao(opcao)
    elif opcao_cont == 3:
        return
    elif opcao_cont == 0:
        exit()
             
def soma(valorP,valorS):
    return valorP + valorS
def subtracao(valorP,valorS):
    return valorP - valorS
def multiplicacao(valorP,valorS):
    return valorP * valorS
def divisao(valorP,valorS):
    return valorP / valorS
def definicao_operacao(opcao):
    if opcao == 1:
        return "Soma"
    elif opcao == 2:
        return "Subtração"
    elif opcao == 3:
        return "Multiplicação"
    elif opcao == 4:
        return "Divisão"

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
        resultado_continuacao = text_operacao(opcao)
        #while True:
           # texto_continuar_operacao(opcao, resultado_continuacao)
    elif opcao == 2:
                text_operacao(opcao)

    elif opcao == 3:
                text_operacao(opcao)

    elif opcao == 4:
                text_operacao(opcao)

    elif opcao == 0:
        break

    else:
        print("Opção inválida")
                