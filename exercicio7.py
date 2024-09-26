

produtos = (

("computador",1500.00,10),
("celular",800.00,25),
("fone",600.00,15)

)

produto_mais_caro = produtos[0]

for produto in produtos :
    if produto[1] > produto_mais_caro[1]:
        produto_mais_caro = produto


print(f"O produto mais caro é {produto_mais_caro[0]}")

print(produtos[0][2])