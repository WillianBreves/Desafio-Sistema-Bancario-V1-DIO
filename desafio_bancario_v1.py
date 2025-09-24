menu = (""" -=- BANCO -=-
[1] Depósito
[2] Saque
[3] Extrato
[0] Encerrar Programa \n""")

saldo_disponivel = 2000
contador_saques = 0
LIMITE_SAQUES = 3
LIMITE_SALDO_SAQUES = 500
depositos_realizados = []
saques_realizados = []


while True:
    opcao_menu = int(input(menu))
    
    if opcao_menu == 1:
        deposito = float(input("Digite o quando deseja depositar em sua conta: R$ "))
        
        if deposito < 0:
            print("Você deve adicionar somente valores positivos!")
            deposito = float(input("Digite o quando deseja depositar em sua conta: R$ "))
            
        saldo_disponivel += deposito
        depositos_realizados.append(deposito)
        
        
    if opcao_menu == 2:
        contador_saques += 1
        
        if contador_saques > LIMITE_SAQUES:
            print("Você não pode realizar mais saques! O limite diário já foi atingido")
            break
            
        saque = float(input("Digite o valor que deseja sacar: R$ "))        
        
        if saque > LIMITE_SALDO_SAQUES:
            print("Você deve realizar saques com um limite de R$500")
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            
        if saque > saldo_disponivel:
            print("Você não tem saldo disponível em conta para realizar a operação!")
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            
        saldo_disponivel -= saque
        saques_realizados.append(saque)
    
    if opcao_menu == 3:
        print(f"-=- EXTRATO -=- \n Saldo Disponível: {saldo_disponivel :.2f}")
        if len(depositos_realizados) == 0:
            print("Não houve movimentações de depósito na conta!")
        else:
            print("Depósitos Realizados: R$"  + ", R$ ".join([str(v) for v in depositos_realizados]))
        if len(saques_realizados) == 0:
            print("Não houve movimentações de saque na conta!")
        else:
            print("Saques Realizados: R$" + ", R$" .join([str(v) for v in saques_realizados]))
            
    if opcao_menu == 0:
        break