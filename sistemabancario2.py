saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato

def sacar(valor, saldo, limite_saque, numero_saques, extrato):
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
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    if cpf in usuarios:
        print("Usuário já cadastrado.")
        return usuarios
    nome = input("Informe o nome do usuário: ")
    usuarios[cpf] = {"nome": nome}
    print(f"Usuário {nome} cadastrado com sucesso.")
    return usuarios

def cadastrar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    if cpf not in usuarios:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return contas
    numero_conta = len(contas) + 1
    contas[numero_conta] = {"cpf": cpf, "saldo": 0}
    print(f"Conta número {numero_conta} cadastrada para o usuário {usuarios[cpf]['nome']}.")
    return contas

usuarios = {}
contas = {}

menu = """
========= MENU =========
[u] Cadastrar usuário
[c] Cadastrar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
========================
=> """

while True:
    opcao = input(menu).lower()

    if opcao == 'u':
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == 'c':
        contas = cadastrar_conta(contas, usuarios)

    elif opcao == 'd':
        valor = float(input("Informe o valor do depósito: R$ "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$ "))
        saldo, extrato, numero_saques = sacar(valor, saldo, limite_saque, numero_saques, extrato)

    elif opcao == 'e':
        exibir_extrato(saldo, extrato)

    elif opcao == 'q':
        print("Encerrando o sistema. Obrigado por usar!")
        break

    else:
        print("Operação inválida.")
