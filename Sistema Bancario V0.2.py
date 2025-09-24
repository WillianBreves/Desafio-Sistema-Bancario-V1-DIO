import datetime

menu = (""" -=- BANCO -=-
[1] Depósito
[2] Saque
[3] Extrato
[0] Encerrar Programa \n""")

saldo_disponivel = 2000
contador_saques = 0
depositos_realizados = []
saques_realizados = []
contador_operacoes = 0 

LIMITE_SAQUES = 3
LIMITE_SALDO_SAQUES = 500
OPERACOES_DIARIAS_MAX = 10

hoje = datetime.datetime.now()
dia_anterior = None

while True:
    opcao_menu = int(input(menu))
    
    if dia_anterior != hoje:
        contador_operacoes = 0
        dia_anterior = hoje
    
    if opcao_menu == 1:
        contador_operacoes += 1
        if contador_operacoes > OPERACOES_DIARIAS_MAX:
            print("Você não pode fazer mais operações hoje! Limite atingido")
            
        deposito = float(input("Digite o quando deseja depositar em sua conta: R$ "))
        
        if deposito < 0:
            print("Você deve adicionar somente valores positivos!")
            deposito = float(input("Digite o quando deseja depositar em sua conta: R$ "))
            
        saldo_disponivel += deposito
        deposito_agora = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        depositos_realizados.append((deposito, deposito_agora))
        
        
    if opcao_menu == 2:
        contador_saques += 1
        contador_operacoes += 1
        if contador_operacoes > OPERACOES_DIARIAS_MAX:
            print("Você não pode fazer mais operações hoje! Limite atingido")
            
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
        saque_agora = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        saques_realizados.append((saque, saque_agora))
    
    if opcao_menu == 3:
        print(f"-=- EXTRATO -=- \n Saldo Disponível: {saldo_disponivel :.2f}")
        if len(depositos_realizados) == 0:
            print("Não houve movimentações de depósito na conta!")
        else:
            for valor, data in depositos_realizados:
                print(f"Depósitos realizados: R${valor:.2f} em {data}")
        if len(saques_realizados) == 0:
            print("Não houve movimentações de saque na conta!")
        else:
            for valor, data in saques_realizados:
                print(f"Saques realizados: R${valor:.2f} em {data}")
            
    if opcao_menu == 0:
        break