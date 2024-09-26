listaDeNumeros = [1,2,3,4,5,6,7,8,9]
numeroProcurado = int(input(print("Digite um número para procurar na lista")))

for numero in listaDeNumeros:
    if numero == numeroProcurado:
        print("O número está presente na lista")
        break;

   