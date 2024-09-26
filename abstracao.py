def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def divisao(a,b):
    return a/b

def multiplicacao(a,b):
    return a*b


dicFuncEscolhida = {

    "soma":soma,
    "subtracao":subtracao,
    "divisao":divisao,
    "multiplicacao":multiplicacao

}

operacao = input("escolha sua operação: ")

a = float(input("Digite o primeiro número: "))

b = float(input("Digite o segundo número: "))

if operacao in dicFuncEscolhida:
    resultado = dicFuncEscolhida[operacao](a,b)
else:
    print("Operação inválida")

print(resultado)
