def zoo():
    grupo = []

    while True:
        visitante = input("Digite a idade de um dos visitantes: ")
        if visitante == "":
            break

        grupo.append(int(visitante))

    preco = 0.00

    for idade in grupo:
        if idade <= 2:
            preco += 0
        elif 3 <= idade <= 12:
            preco += 14.00
        elif idade >= 65:
            preco += 18.00
        else:
            preco += 23.00

    print(f"O preço total foi: R$ {preco:.2f}")

zoo()
