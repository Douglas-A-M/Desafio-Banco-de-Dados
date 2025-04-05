menu = """ ===== Bem-Vindo ao Banco Python =====

Pressione
[1] Sacar\n[2] Depósito\n[3] Extrato\n[0] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if  opcao =="2":
        valor = float(input("Qual a quantia que deseja depositar: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Foi depositado o valor de R$: {valor:.2f}"
        else:
            print("O saldo tem que ser maior que 0 para ser válido!")

    elif opcao =="1":
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques excedido! Tente novamente Amanhã!")
        elif saldo <= 0:
            print("Sem saldo para saque!")

        else:
            valor = float(input("Qual a quantia que deseja sacar: "))
            if valor > saldo:
                print("Saldo insuficiente!")

            elif valor <= 0 or valor > limite:
                print("O valor digitado está incorreto!\n Corrigir e tentar novamente!")
                        

            else:
                saldo -= valor
                extrato += f"Saque de R${valor: .2f}"
                numero_saques += 1
                

    elif opcao =="3":
        print(""" ======EXTRATO====== """)
        print(f"Seu saldo é: R$ {saldo: .2f}")
        print(f"Seu Limite de Saques diário é: {LIMITE_SAQUES - numero_saques}")
        
    elif opcao == "0":
        break
    else:
        print("Opção inválida! Tente novamente com uma opção válida!")