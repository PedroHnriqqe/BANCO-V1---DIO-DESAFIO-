#Método depositar
def depositar(saldo_atual, extrato_atual):
    print("Depósito - Por favor insira um valor maior que 0:")
    deposito = int (input())
    #Depósito com sucesso caso o valor seja maior do que 0
    if deposito > 0:
        print(f"Você inseriu o valor de R${float(deposito)}, obrigado por utilizar nosso banco!")
        #O parâmetro declarado na função é adicionado na variável global deposito
        saldo_atual += deposito
        extrato_atual += f"Deposito de R${float(deposito)}\n"
        #retorna os parâmetros "saldo_atual" e "extrato_atual"
        return saldo_atual,extrato_atual
    #Depósito incorreto caso seja menor ou igual a 0
    elif deposito <= 0:
        print("Valor incorreto! Por favor insira apenas números maiores que 0 e tente novamente!")
        #retorna os parâmetros "saldo_atual" e "extrato_atual"
        return saldo_atual,extrato_atual
    


#Método Sacar    
def sacar(saldo_atual,extrato_atual, limite_saques,numero_saques):
    print(f"Saque - Saldo em conta {float(saldo_atual)}")
    print("Quanto deseja sacar? (Limite de saque R$ 500)")
    saque = int(input())
    
    if saque > 500:
        print(f"Saque de R${saque} INVÁLIDO, por favor respeite o limite de R$ {limite_saques} por saque!")
        #Não realiza o saque se o usuário já tiver sacado mais do que 3 vezes
    elif numero_saques >= 3:
        print(f"Limte de saques diário atingido! Saques disponíveis: {LIMITE_SAQUES}, números de saques realizados no dia: {numero_saques}")
        #Não realiza o saque se não houver dinheiro na conta
    elif  saldo_atual <= 0:
        print("Não foi possível realizar o saque, verifique se o valor desejado está disponível em sua conta!")
        print(f"Valor disponíviel: {float(saldo_atual)}")
    else:
        #Com dinheiro em conta, o saque é feito normalmente!
        saldo_atual -= saque
        print(f"Você retirou R${saque}! saldo em conta: R${float(saldo_atual)}, obrigado por utilizar nosso banco!")
        limite_saques -= 1
        numero_saques += 1
        extrato_atual += f"Saque de R${float(saque)}\n"
    
    return saldo_atual,extrato_atual,limite_saques,numero_saques

#Método de exibir extrato
def exibir_extrato(extrato_atual,dinheiro_conta_atual):
    print(extrato_atual)
    print(f"Saldo em conta:{float(dinheiro_conta_atual)}")
    
    return extrato_atual,dinheiro_conta_atual
        
        
#Método de gerenciamento de usuários, registrar usuários caso não existente        
def gerenciamento_usuarios(lista_usuarios):
    
    usuario = input("Bem vindo! Insira seu usuário:")
    
    if usuario in lista_usuarios:
        print(f"Usuário já existente! Bem vindo {usuario}!")
    else:
        print(f"Usuário não existente! Realizando o cadastro de usuário:")
        
        cpf_usuario = input("Por favor insira seu CPF: ")
        
        if cpf_usuario in lista_usuarios:
            
            print("Usuário já existente! Por favor realize o login...")
        else:
            data_nascimento_usuario = input("Por favor insira sua data de nascimento: ")
            endereco_usuario = input("Por favor insira seu endereço no formato logradouro - bairro - cidade/sigla estado: ")
        
        lista_usuarios.extend([usuario, cpf_usuario,data_nascimento_usuario,endereco_usuario])
        
        print("Usuário adicionado com sucesso!")
        print("Informações do usuário:")
        for i in range(0, len(lista_usuarios),4):
            print(f"Usuário: {lista_usuarios[i]}, CPF: {lista_usuarios[i + 1]}, Data de Nascimento: {lista_usuarios[i + 2]}, Endereço: {lista_usuarios[i+3]}")
        
def gerenciamento_conta_corrente(usuario, verificar_contas):
    numero_conta = len(verificar_contas) + 1
    numero_agencia = "0001"
    
    detalhes_conta  = {
        "Número_conta":numero_conta,
        "Numero_agencia":numero_agencia,
        "usuario": usuario,
        "saldo": saldo
    }

    verificar_contas.append(detalhes_conta)
    
    print(f"Conta corrente criada com sucesso para o usuário {usuario}!")
    print(f"Informações da conta corrente:")
    print(f"Número da conta: {numero_conta}")
    print(f"Agência: {numero_agencia}")
    print(f"Saldo: R${saldo}\n")
    
    return verificar_contas


#Menu que serve de interface ao usuário
menu = """
[c] Criar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

#Declaração de variáveis
lista_usuarios = []
verificando_contas_corrente = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
dinheiro_conta = 0

#Chamando a função de gerenciamento de usuários com o parâmetro da lista_usuários declarada acima
gerenciamento_usuarios(lista_usuarios)


usuario = input("Insira seu usuário para realizar operações: ")

if usuario not in lista_usuarios:
    print("Usuário não encontrado.")
    print("Realizando o cadastro.")
    gerenciamento_usuarios(lista_usuarios)


opcao = input(menu)
while True:
    # Opção de Deposito
    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
        opcao = input(menu)
    elif opcao == "c":
        verificando_contas_corrente = gerenciamento_conta_corrente(usuario, verificando_contas_corrente)
        opcao = input(menu)
    # Opção de Saque
    elif opcao == "s":
        saldo, extrato, LIMITE_SAQUES, numero_saques = sacar(saldo, extrato, LIMITE_SAQUES, numero_saques)
        opcao = input(menu)
    # Opção de extrato
    elif opcao == "e":
        print("Extrato - Saídas e entradas da conta!")
        extrato, dinheiro_conta = exibir_extrato(extrato, saldo)
        opcao = input(menu)
    elif opcao == "q":
        break