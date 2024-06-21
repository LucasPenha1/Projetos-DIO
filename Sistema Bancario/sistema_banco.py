menu = """ \nBEM VINDO
[d] depositar
[s] sacar
[e] extrato
[q] sair
=> """

saldo = 0
limite =500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = input("Informe o valor de depósito: ")
        try: 
            valor = float(valor)
        except: 
           print("Digite um valor válido! \n")  
           continue                   
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "s":
        valor = input("Informe o valor de saque: ")
        try: 
            valor = float(valor)
        except: 
           print("Digite um valor válido! \n")  
           continue                   
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Atenção! Você não tem saldo suficiente!")
                        
        elif excedeu_limite:
            print("Atenção! O valor do saque excede o limite!")
            
        elif excedeu_saques:
            print("Atenção! Número de saques excedido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques+=1
        else: 
            print("O valor informado é inválido!")
    
    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)    
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, selecione novamente a operação desejada.")
            
            
            
         
                
        