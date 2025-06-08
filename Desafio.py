menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha a opção: """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opção == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques).")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opção == "e":
        print("\n================= EXTRATO =================")
        if not extrato:
            print("Nenhuma transação realizada.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===========================================")

    elif opção == "q":
        print("Saindo do sistema. Até logo!")
        break
