menu = """
[d] Depósito
[s] sacar
[e] extrato
[q] sair

"""

saldo = 100
limite = 500
deposito = 0
saque = 0
extrato = ""
numero_saque = 0
Limite_saque = 0
extrato_deposito = ""
extrato_saque = ""

while True:
    opcao = input(menu)

    if opcao == "d":
        print("### Depósito ###")
        deposito = float(input("Digite o valor de deposito:  "))
        print(f"Depósito de R$ {deposito:.2f} efectuado com sucesso.")
        extrato_deposito += f"R$ {deposito:.2f}, " 
        saldo += deposito

    elif opcao == "s":
        if Limite_saque != 3:
            print("### saque ###")
            saque = float(input("Digite o valor do saque (inferior ou igual a 500 R$):  "))
            if saque <= limite:
                if saldo >= saque:    
                    print(f"Saque de R$ {saque:.2f} executado com sucesso.\n")
                    saldo -= saque
                    extrato_saque += f"R$ {saque:.2f}, "
                    Limite_saque += 1
                else:
                    print("Operação cancelada, Saldo insuficiente.\n")
            else:
                print("Impossível efectuar operação. saque superior a R$ 500")        

              
    elif opcao == "e":
        print("### Extrato ###")
        print(f"saques realizados hoje: {extrato_saque}\n")
        print(f"Depositos: {extrato_deposito}")
        print(f"Saldo actual: {saldo:.2f}")
        

        
    elif opcao == "q":
        break

    else:
        print("opação invalida. Selecione uma opçao valida\n")
           
    numero_saque += 1          
    