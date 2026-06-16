num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("Por favor, informe apenas números positivos.")
else:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print(f"Fatorial = {fatorial}")