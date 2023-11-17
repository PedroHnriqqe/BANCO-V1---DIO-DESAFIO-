menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
deposito = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

dinheiroConta = 0

opcao = input(menu)

while True:

    #Opção de Deposito
    if opcao == "d":
        print("Depósito - Por favor insira um valor maior que 0:")
        deposito = int(input())
        if deposito > 0:
            print(f"Você inseriu o valor de R${float(deposito)}, obrigado por utilizar nosso banco!")
            dinheiroConta = dinheiroConta + deposito
            extrato += f"Deposito de R${float(deposito)}\n"
            opcao = input(menu)
            
        elif deposito < 0 or deposito == 0:
            print("Valor incorreto! Por favor insira apenas números maiores que 0 e tente novamente:")
            opcao = input(menu)
            
    #Opção de Saque
    elif opcao == "s":
        print(f"Saque - Saldo em conta {float(dinheiroConta)}")
        print("Quanto deseja sacar? (Limite de saque R$500)")
        saque = int(input())
        
        #Realiza o saque se respeitar o limite de R$ 500
        if saque > 500:
            print(f"Saque de R${saque} INVÁLIDO, por favor respeite o limite de R${limite} por saque! ")
            opcao = input(menu)
            
        #Realiza o saque se respeitar o limite de saque diário de 3 vezes no mesmo dia!
        elif numero_saques >=3: 
            print(f"Limite de saques diário atingido!  Saques disponíveis:{LIMITE_SAQUES}, Números de saques realizados no dia: {numero_saques}")
            break
            
        #Verifica se existe o valor em conta!
        elif dinheiroConta <= 0 :
            print("Não foi possível realizar o saque, verifique se o valor desejado está disponível em sua conta!")
            print(f"Valor disponível: {float(dinheiroConta)}")
            
        #Saque realizado com sucesso!
        else:
            dinheiroConta = dinheiroConta - saque
            print(f"Você retirou R${saque}! saldo em conta: R${float(dinheiroConta)}, Obrigado por utilizar nosso banco!")
            LIMITE_SAQUES -=1
            numero_saques += 1
            extrato += f"Saque de R${float(saque)}\n"
            opcao = input(menu)
            
    #Opção de extrato
    elif opcao == "e":
        print("Extrato - Saídas e entradas da conta!")
        print(extrato)
        opcao = input(menu)
        print(f"Saldo em conta:{float(dinheiroConta)} ")
        
    elif opcao == "q":
        break
    
 