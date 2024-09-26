def soma(a,b):
    return a+b

def divisao(a,b):
    return a/b

def subtracao(a,b):
    return a-b


operacoes = {

"soma":soma,
"divisao":divisao,
"subtracao":subtracao

}

def calculadora(operacao,a,b):
    return operacoes[operacao](a,b)


operacao = input(print("Digite a operação que gostaria de realizar: "))
a = input(print("Digite o primeiro número: "))
b = input(print("Digite o segundo número: "))

resultado = calculadora(operacao,int(a),int(b))

print(resultado)
