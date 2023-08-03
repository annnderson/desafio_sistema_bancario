Menu = """

[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - sair

"""

valor_saque_limite = 500
LIMITE_SAQUE = 3
extrato = ""
saldo = 0
numero_saque = 0

while True:
    opçao = input(Menu)
    
    if opçao == "d":
        valor = float(input("Insira o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! valor inválido") 
             
        
    elif opçao == "s":
        valor = float(input("Insira o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > valor_saque_limite
        
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! valor do saque excede o limite")
            
        elif excedeu_saque:
            print("Operação falhou! o número máximo de saques foi excedido")     
            
        elif valor > 0:
            saldo -= valor    
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saque = 1
            
        else:
            print("Operação falhou! valor informado inválido")    
            
    elif opçao == "e":
        print("\n=======Extrato========") 
        print("Não foram realizadas  movimentações." if not extrato else extrato)  
        print(f"Extrato: {saldo:.2f}")
        print("\n=======================")     
    
    elif input("q"):
        break
    
    else:
        print("Operação falhou! escolha a opção desejada novamente")
    
    


    



