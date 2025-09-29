def menu():
    modelo_menu = (""" -=- BANCO -=-
       [1] Depositar
       [2] Sacar
       [3] Visualizar Extrato
       [4] Novo Usuário
       [5] Nova Conta
       [6] Listar Contas
       [0] Sair
    """)
    return input(modelo_menu + "\nEscolha: ")

def realizar_deposito(saldo_disponivel, deposito, historico, /):
    if deposito > 0:
        saldo_disponivel += deposito
        historico += f"Depósito: R${deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Não foi possível concluir a operação! Tente novamente!")
    return saldo_disponivel, historico

def realizar_saque(*, saldo_disponivel, saque, historico, limite_de_valor, numero_saques, limite_saques):
    exceder_limite = saque > limite_de_valor
    exceder_saldo = saque > saldo_disponivel
    exceder_saques = numero_saques >= limite_saques

    if exceder_limite:
        print("O valor do saque excede o limite permitido! Tente novamente.")
    elif exceder_saldo:
        print("Você não tem saldo suficiente para terminar essa operação.")
    elif exceder_saques:
        print("Você atingiu seu limite de saques! Tente novamente amanhã.")
    elif saque > 0:
        saldo_disponivel -= saque
        historico += f"Saque: R${saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possível concluir a operação!")

    return saldo_disponivel, historico, numero_saques

def mostrar_extrato(saldo_disponivel, /, *, historico):
    print("=========== Extrato ===========")
    print("Não houve movimentações na conta" if not historico else historico, end="")
    print(f"Saldo: R${saldo_disponivel:.2f}")
    print("================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF [apenas números]: ")
    usuario = filtro_usuarios(cpf, usuarios)
    if usuario:
        print("Já existe um usuário cadastrado com esse CPF!")
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento [dd-mm-aaaa]: ")
    endereco = input("Informe seu endereço [logradouro, número - bairro - cidade/UF]: ")
    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [u for u in usuarios if u["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, num_conta, usuarios):
    cpf = input("Informe seu CPF [somente números]: ")
    usuario = filtro_usuarios(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"Agencia": agencia, "Numero da conta": num_conta, "Usuário": usuario}
    print("Usuário não encontrado! Encerrando operação")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
Agência: {conta['Agencia']}
C/C: {conta['Numero da conta']}
Titular: {conta['Usuário']['nome']}
"""
        print("=" * 40)
        print(linha.strip())
    if not contas:
        print("Nenhuma conta cadastrada.")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 2000.0
    limite_de_valor = 500.0
    historico = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao_menu = menu()

        if opcao_menu == "1":
            deposito = float(input("Informe o valor do depósito: "))
            saldo, historico = realizar_deposito(saldo, deposito, historico)

        elif opcao_menu == "2":
            saque = float(input("Informe o valor do saque: "))
            saldo, historico, numero_saques = realizar_saque(
                saldo_disponivel=saldo,
                saque=saque,
                historico=historico,
                limite_de_valor=limite_de_valor,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao_menu == "3":
            mostrar_extrato(saldo, historico=historico)

        elif opcao_menu == "4":
            criar_usuario(usuarios)

        elif opcao_menu == "5":
            num_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao_menu == "6":
            listar_contas(contas)

        elif opcao_menu == "0":
            print("Saindo...")
            break

        else:
            print("Operação inválida! Tente novamente.")

if __name__ == "__main__":
    main()
