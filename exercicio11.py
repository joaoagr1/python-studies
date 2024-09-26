def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def divisao(a,b):
    return a/b


operacoes = {

    "soma":soma,
    "subtracao":subtracao,
    "divisao":divisao

}

print(operacoes["soma"])

def calculadora(operacao,a,b):
    return operacoes[operacao](a,b)


resultado = calculadora("soma",1,1)


