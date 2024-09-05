LIMITE_SAQUE = 3

saldo = 0
numero_saques = 0
limite = 500
extrato = []

print("SISTEMA BANCARIO".center(30, "="))
interface = """
    [1]. Sacar
    [2]. Depositar
    [3]. Consultar saldo
    [4]. Exibir extrato
    
    [0]. Sair
    
> """
while True:
    
    opcao = int(input(interface))
    
    if opcao == 1:
        saque = float(input("Saque\nR$ "))
        
        if saldo < saque:
            print("Saldo insuficiente")
            
        elif numero_saques >= LIMITE_SAQUE:
                print("Limite de saques atingido")
                
        else:
            saldo -= saque
            extrato.append({'saque': saque})
    
    elif opcao == 2:
        deposito = float(input("Depositar\nR$ "))
        
        if deposito < 0:
            print("Digite um valor positivo.")
        
        else:
            saldo += deposito
            extrato.append({'deposito': deposito})
    
    elif opcao == 3:
        print(f"Saldo: R${saldo:.2f}")
        
    elif opcao == 4:
        print("EXTRATO".center(15, "="))
        
        if extrato == None:
            print("\n\nNenhum depósito ou saque foi realizado.")
            
        else:
            print(extrato)
    
    elif opcao == 0:
        break
    
    else:
        print("Opção inválida.")