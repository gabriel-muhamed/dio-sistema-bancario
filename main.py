import time

menu = """
=============================

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

=============================

=> """

deposito = "Digite o valor do depósito: "

saque = "Digite o valor do saque: "

saldo = 0
extrato = ""
limite = 500
numero_saques = 0

while True:
    opcao = input(menu)
    
    # Depósito
    if opcao == "d": 
        valor_depositado = input(deposito)
        extrato += "\n" + "+ " + "R$" + valor_depositado
        saldo = saldo + int(valor_depositado)
        time.sleep(1)
    
    # Saque
    elif opcao == "s":
        valor_sacado = input(saque)
        if int(valor_sacado) <= limite and int(valor_sacado) <= saldo and numero_saques < 3:
            saldo = saldo - int(valor_sacado)
            extrato += "\n" + "- " + "R$" + valor_sacado
            numero_saques += 1
            print("Valor sacado!")
        elif int(valor_sacado) > limite:
            print("Valor solicitado acima do limite de saque!")
        elif int(valor_sacado) > saldo:
            print("Valor solicitado acima do saldo disponível!")
        else:
            print("Número de saque diário atingido!")
        time.sleep(1)

    # Extrato
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações hoje!")
            time.sleep(1)
        else:
            print(f"Seu extrato: {extrato}" + "\n")
            print(f"Saldo: {saldo}" + "\n")
            print(f"Número de saques hoje: {numero_saques}")
            time.sleep(1)

    # Sair
    elif opcao == "q":
        break

    else: 
        print("Opção inválida, escolha outra opção válida!")
        time.sleep(2)