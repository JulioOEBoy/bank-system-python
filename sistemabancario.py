saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

menu = """
========= MENU =========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
========================
=> """

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$ "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIO

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Limite por saque excedido.")
        elif excedeu_saques:
            print("Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    -R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido.")

    elif opcao == 'e':
        print("\n========== EXTRATO ==========")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida.")
