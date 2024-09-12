idadeDigitada = int(input(print("Digite uma idade: ")))

if idadeDigitada >= 18:
    if idadeDigitada == 18:
        print("Você tem exatamente 18 anos, parabéns")
    else:
        print("Você tem mais de 18 anos de vida...")

else:
    print("Infelizmente você não é maior de idade")



if idadeDigitada < 5 and idadeDigitada > 0:
    print("vc é um bebe")
elif idadeDigitada <= 5 and idadeDigitade <=10:
    print("Vc é uma criança")
else:
    print("vc n é nem criança nem bb")