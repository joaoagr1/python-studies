dicionarioPessoa = {
    "nome": "João",
    "idade": 20
}

def modificar_dicionario(dicionario,chave,novoValor):
    print(dicionarioPessoa)

    def alterar_chave(chave,novoValor):

        dicionario[chave] = novoValor
        print(dicionarioPessoa)
    
    alterar_chave(chave, novoValor)


modificar_dicionario(dicionarioPessoa,"idade","10")
print(dicionarioPessoa)