import gc

# 1. Instanciação de 3 variáveis com valores diferentes
a = 10
b = 20
c = 30

# 2. Apresentando os endereços de memória das variáveis
print(f"Endereço de memória de a: {id(a)}")
print(f"Endereço de memória de b: {id(b)}")
print(f"Endereço de memória de c: {id(c)}")

# 3. Limpando os valores das variáveis (atribuir `None`)
a = None
b = None
c = None

# Forçando o garbage collector para limpar referências
gc.collect()

# 4. Apresentando os endereços de memória após limpeza
a = b = c = None  # Atribuindo None para que compartilhem o mesmo endereço

print(f"Endereço de memória de a: {id(a)}")
print(f"Endereço de memória de b: {id(b)}")
print(f"Endereço de memória de c: {id(c)}")
