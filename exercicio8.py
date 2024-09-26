dicionarioAlunos = {

    "joao":8.00,
    "pedro":3.00,
    "enzo":6.00

}

notaTotal = 0.00

nomeConsultarNota = input(print("Digite o nome de um aluno para consultar a nota: "))
print(f"A nota desse aluno foi: {dicionarioAlunos[nomeConsultarNota]} ")

for aluno in dicionarioAlunos:
    notaTotal = notaTotal + dicionarioAlunos[aluno]

print(notaTotal)


print(dicionarioAlunos["joao"])