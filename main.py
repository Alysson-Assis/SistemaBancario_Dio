menu = """
[d] Despositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            

    elif opcao == "s":
        
        if numeros_saques == LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários")
            
        else:
            numeros_saques += 1
    
            valor = float(input("Informe o valor de saque: R$"))
            if saldo == 0:
                print("Você não possue valor para saque.")
            elif valor > limite:
                print("Você exedeu o valor limite de saque.")
            
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}"
            

    elif opcao == "e":
        print(extrato)
        print(f"\nSaldo: R${saldo:.2f}")

    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente o operador desejado.")