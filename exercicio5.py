valor = int(input("Digite o valor do saque: "))
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${nota}")
        valor %= nota