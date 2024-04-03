menu = '''

    [d] Depositar
    
    [s] Sacar
    
    [e] Extrato
    
    [q] Sair

    [c] Conta

=> '''

saldo = 0
limite = 500
retirado = 0
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3
conta = 0

while True:

    opcao = input(menu)


    if opcao == "d":
        print("============Depósito============")
        print("digite um valor:")
        deposito = int(input())
        numero_formatado = f"R$ {deposito:,.2f}"

        if deposito > 0:
            conta = conta + deposito
            print("depositado: " + str(numero_formatado))
            extrato.append("\ndepositado:" + str(deposito))
        elif deposito < 0:
            print("valor invalido")



    elif opcao == "s":
        print("Saque")
        print("============Sacar============")
        saque = int(input("valor a ser sacado: "))
        numero_formatado2 = f"R$ {saque:,.2f}"
        if saque > 500:
            print("valor invalido")
        elif saque > conta:
            print("valor invalido")
        elif numero_saque == LIMITE_SAQUE:
            print("valor invalido")
        else:
            conta = conta - saque
            print(f'retirado:'+ str(numero_formatado2))
            extrato.append("\nretirado:" + str(saque))



    elif opcao == "e":
        print("============Extrato============")
        extrato_string = "\n".join(extrato)
        numero_formatado2 = f"R$ {conta:,.2f}"
        print("sua conta possui: " + str(numero_formatado2))
        print(extrato_string)



    elif opcao == "c":
        print("==========Conta================")
        if conta == "":
            print("conta vazia")
        else:
            numero_formatado2 = f"R$ {conta:,.2f}"
            print("sua conta possui: " + str(numero_formatado2))

    elif opcao == "q":
        print("operação Finalizada")
        break




