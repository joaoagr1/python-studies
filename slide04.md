Associações e Escopo em Python
Introdução às Associações
Definição
Associação é o processo de ligar um identificador a um valor em programação.

Importância
Entender associações é crucial para manipular dados eficientemente em Python.

Tipos
Existem associações estáticas e dinâmicas, cada uma com características únicas.

Associação Estática em Python
Definição
Associação estática ocorre quando o tipo da variável não muda após a atribuição.

Exemplo

python
Copiar código
x = 10  # x está estaticamente associado a um inteiro
Vantagem
Proporciona maior previsibilidade e segurança de tipos no código.

Associação Dinâmica em Python
Exemplo

python
Copiar código
x = 10        # x é inicialmente um inteiro
x = "Olá"     # x agora é uma string
print(x)      # Imprime "Olá"
Vantagens

Flexibilidade: Permite que variáveis mudem de tipo durante a execução do programa.
Produtividade: Facilita o desenvolvimento rápido e prototipagem de código.
Expressividade: Permite escrever código mais conciso e expressivo em certas situações.
Introdução ao Escopo
Definição
Escopo é a região do código onde uma variável é reconhecida e pode ser acessada.

Importância
O escopo determina a visibilidade e o tempo de vida das variáveis em um programa.

Tipos de Escopo em Python
Python possui escopos locais, globais e não locais (nonlocal).

Escopo Global em Python
Definição
Variáveis definidas no nível mais alto de um módulo têm escopo global.

Exemplo

python
Copiar código
x = 10  # Variável global
Acesso
Pode ser acessada de qualquer parte do código, incluindo funções.

Escopo Local em Python
Definição
Variáveis definidas dentro de uma função têm escopo local.

Exemplo

python
Copiar código
def funcao():
    y = 5  # Variável local
    print(y)
Escopo Não Local (Nonlocal) em Python
Definição
Usado em funções aninhadas para acessar variáveis do escopo externo.

Exemplo

python
Copiar código
def externa():
    x = 10
    def interna():
        nonlocal x
        x = 20
    interna()
    print(x)  # Imprime 20
Regra LEGB em Python
Local (L): Variáveis definidas dentro da função atual.
Enclosing (E): Variáveis em escopos de funções externas.
Global (G): Variáveis definidas no nível mais alto do módulo.
Built-in (B): Nomes predefinidos em Python, como print() ou len().
Exemplo de Resolução LEGB

python
Copiar código
x = 'global'
def func():
    x = 'local'
    print(x)

func()
print(x)
Resultado:

Imprime: local global
Palavra-chave 'global' em Python
Uso
Permite modificar uma variável global dentro de uma função.

Exemplo

python
Copiar código
x = 10
def mudar_global():
    global x
    x = 20

mudar_global()
print(x)  # Imprime 20
Palavra-chave 'nonlocal' em Python
Uso
Permite modificar uma variável de um escopo externo (mas não global) em funções aninhadas.

Exemplo

python
Copiar código
def externa():
    x = 10
    def interna():
        nonlocal x
        x = 20
    interna()
    print(x)  # Imprime 20

externa()
Escopo de Funções em Python
Definição
Cada chamada de função cria um novo escopo local.

Exemplo

python
Copiar código
def soma(a, b):
    resultado = a + b
    return resultado

print(soma(3, 4))  # 7
# print(resultado)  # Erro: 'resultado' não está definido
Escopo de Classes em Python
Atributos de Classe
Compartilhados por todas as instâncias da classe.

Atributos de Instância
Específicos para cada objeto criado a partir da classe.

Exemplo

python
Copiar código
class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, cor):
        self.cor = cor  # Atributo de instância
Escopo de Módulos em Python
Definição
Variáveis definidas no nível mais alto de um módulo têm escopo de módulo.

Exemplo

python
Copiar código
# Em modulo.py
x = 10

# Em outro_arquivo.py
import modulo
print(modulo.x)  # Imprime 10
Escopo de Compreensões em Python
Definição
Variáveis em compreensões de lista têm escopo próprio.

Exemplo

python
Copiar código
x = [i for i in range(5)]
print(x)  # [0, 1, 2, 3, 4]
# print(i)  # Erro: 'i' não está definido
Escopo em Estruturas de Controle
If, For, While
Não criam um novo escopo em Python.

Exemplo

python
Copiar código
for i in range(3):
    x = i
print(x)  # Imprime 2 (o último valor de i)
Escopo de Exceções em Python
Try-Except
Variáveis definidas no bloco try são acessíveis no bloco except.

Exemplo

python
Copiar código
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")
# x não está definido aqui
Escopo de Geradores em Python
Definição
Geradores mantêm seu estado entre chamadas.

Exemplo

python
Copiar código
def contador():
    i = 0
    while True:
        yield i
        i += 1

c = contador()
print(next(c))  # 0
print(next(c))  # 1
Closures em Python
Definição
Funções que "lembram" o ambiente onde foram criadas.

Exemplo

python
Copiar código
def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

dobro = multiplicador(2)
print(dobro(5))  # 10
Escopo de Decoradores em Python
Definição
Decoradores podem afetar o escopo das funções que decoram.

Exemplo

python
Copiar código
def meu_decorador(func):
    def wrapper():
        print("Antes")
        func()
        print("Depois")
    return wrapper

@meu_decorador
def dizer_oi():
    print("Olá!")

dizer_oi()
# Imprime:
# Antes
# Olá!
# Depois
Boas Práticas de Escopo
Minimize Variáveis Globais
Use variáveis globais com moderação para evitar efeitos colaterais.

Encapsulamento
Use funções e classes para encapsular variáveis e lógica.

Nomes Descritivos
Use nomes claros para evitar confusão entre escopos diferentes.

Conclusão: Associações e Escopo em Python
Associações:
Entender como Python associa nomes a valores é fundamental.

Escopo:
O escopo determina a visibilidade e o ciclo de vida das variáveis.

Prática:
Experimentar com diferentes escopos ajuda a evitar erros comuns.