saldo = 0

while True:
    print("\n=== SISTEMA BANCÁRIO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        try:
            valor = float(input("Valor para depositar: "))
            if valor > 0:
                saldo += valor
                print("Depósito realizado!")
            else:
                print("Valor inválido.")
        except:
            print("Erro: digite um número válido.")

    elif opcao == "3":
        try:
            valor = float(input("Valor para sacar: "))
            if valor > saldo:
                print("Saldo insuficiente.")
            elif valor <= 0:
                print("Valor inválido.")
            else:
                saldo -= valor
                print("Saque realizado!")
        except:
            print("Erro: digite um número válido.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")