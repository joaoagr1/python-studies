def outer():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador

    return incrementar

# Cria uma instância da função incrementar
incrementar = outer()

# Chama a função incrementar várias vezes e exibe o valor de contador
print(incrementar())  # Saída: 1
print(incrementar())  # Saída: 2
print(incrementar())  # Saída: 3
print(incrementar())  # Saída: 4