def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

operacoes = {

    "soma":soma,
    "subtracao":subtracao

}

def  aplicar_operacao(a,b,func):
    return func(a,b)

def gerar_operacao(operacao):
    return operacoes[operacao]


resultado = aplicar_operacao(1,2,gerar_operacao("soma"))


print(resultado)