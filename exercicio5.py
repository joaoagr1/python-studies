# Solicita ao usuário um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializa o valor do fatorial como 1
fatorial = 1

# Verifica se o número é positivo
if n < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Calcula o fatorial usando um loop for
    for i in range(1, n + 1):
        fatorial *= i
    
    # Exibe o resultado
    print(f"O fatorial de {n} é {fatorial}.")
