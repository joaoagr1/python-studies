resultado_global = 0  # Inicializa a variável global

def soma(a, b):
    global resultado_global
    resultado_global = a + b
    return resultado_global

# Chama a função soma para definir o valor de resultado_global
soma(3, 4)

print(resultado_global)