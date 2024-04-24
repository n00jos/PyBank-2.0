import time

def depositar(saldo, valor, extrato,/):
    if valor > 0:   
        saldo += valor
        extrato.append([f"Deposito de R${valor:.2f}"])
        print(f'Seu saldo atual é de: R${saldo:.2f}')
        time.sleep(3)
    else:
        print('Valor não permitido, Tente novamente!')
        time.sleep(3)
    return saldo

def sacar(*, valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
        if valor > 0 and valor <= limite:
            saldo -= valor
            extrato.append([f"Saque de R${valor:.2f}"])
            numero_saques += 1
            print(f'Saque realizado com sucesso. Seu saldo atual é de: R${saldo:.2f}')
            time.sleep(2)
        
        elif valor > limite:
            print(f'Valor acima do limite de saque permitido por saque. Seu limite atual é de R${limite:.2f}.')
            time.sleep(2)

        else:
            print(f'Valor não permitido. Seu saldo atual é de: R${saldo:.2f}. Tente novamente')
            time.sleep(2)
    else:
        print(f'Limite de saques diários atingido. Você só pode sacar {LIMITE_SAQUES} vezes por dia.')
        time.sleep(2)        
    return saldo, numero_saques
    

def extrato_bancario(saldo, *,extrato):
    print('========= Extrato =========')
    for item in extrato:
            print(item)
    print('---------------------------')
    print(f'Saldo atual de R${saldo}')
    print('===========================')    
    time.sleep(5)

def cadastro_cliente():
    
    nome = input("Qual o seu nome? \n")
    dia = input("Qual seu dia nascimento? \n")
    mes = input("Mês de nacimento? \n")
    ano = input ("Ano de nascimento? \n")
    print("Endereço:")
    rua = input("Qual a sua Rua? \n")
    n = input("Numero? \n")
    bairro = input("Bairro? \n")
    cidade = input ("Cidade? \n")
    estado = input("Estado? (sigla) \n")
    cpf = input("Qual o seu Cadastro de Pessoa Fisica(CPF)(Apenas os numeros)? \n")
    data_n = {'dia':dia,'mes':mes, 'ano':ano}
    endereco = {'rua': rua,'n':n,'bairro':bairro,'cidade':cidade,'estado':estado}
    cliente = {'nome': nome, 'data_n': data_n, 'cpf':cpf,'endereco':endereco}
    return cliente, cpf

def cpf_cadastrado(cpf, lista_cpf):
    return cpf in lista_cpf
    
def criar_conta(cpf, cpf_cadastrados):
    cpf_cliente = input("Digite seu CPF para iniciarmos a abertura de sua conta PyBank! \n")
    if cpf_cliente in cpf_cadastrados:
        print("CPF já cadastrado!")
        return cpf_cliente    
    else:

        return None  

def contas(cliente, cpf, numero_conta, agencia):
    numero_conta += 1
    conta_a = {'numero': numero_conta, 'agencia': agencia, 'cliente': cliente['nome'], 'cpf': cpf}
    return conta_a
    

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    valor = 0
    cliente = {}
    clientes = []
    cpf_cadastrados = []
    conta_c = ""
    agencia = "0001"
    numero_conta = 0
    while True:
        print( '''
__________________________________
|################################|
|########### Py  Bank ###########|
|################################|
|================================|
| Qual operação deseja realizar? |
|================================|
|### [ D ] - Depositar        ###|
|### [ S ] - Sacar            ###|
|### [ E ] - Extrato          ###|
|### [ P ] - Cadastro Pessoa  ###|
|### [ C ] - Criar Conta      ###|
|### [ Q ] - Sair             ###|
|================================|
|################################|
==================================
''' )

        opc =  (input("Escolha uma das opções: "))
        
        if opc == "d":
            valor = float(input('Depositar, qual valor deseja depositar? R$'))
            saldo = depositar(saldo, valor, extrato)
        elif opc == "s":
            valor = float(input('Sacar, qual valor deseja sacar? R$'))
            saldo, numero_saques = sacar(valor=valor, saldo=saldo, extrato = extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)  
        elif opc == "e":
            extrato_bancario(saldo, extrato = extrato)     
        elif opc == "p":
            cliente, cpf = cadastro_cliente()
            cpf = cliente['cpf']
            if cpf_cadastrado(cpf, cpf_cadastrados):
                print("CPF já cadastrado!")
                time.sleep(2)
            else:
                cpf_cadastrados.append(cpf)
                clientes.append(cliente)
                print('Cadastro realizado com sucesso Sr(a) ', cliente['nome'] )
                time.sleep(2)
        elif opc == "c":
            cpf_cliente = criar_conta(cpf, cpf_cadastrados)
            if cpf_cliente:
                conta_c = input(f'Olá Sr(a) {cliente['nome']} com CPF:  {cliente['cpf']}. Deseja prosseguir com a abertura da sua conta PyBank?(s/n)')
                if conta_c == 's': 
                    numero_conta += 1 
                    nova_conta = contas(cliente, cpf, numero_conta, agencia)
                    print(f"Conta criada com sucesso para {cliente['nome']}! Detalhes da conta: {nova_conta}")
                else:
                    break
                     



            else:
                print('CPF não encontrado! Realize o cadastro de pessoa no menu anterior.')
             
            

        
        elif opc == "q":
            print('Obrigado por usar o Py Bank 24hrs. Volte sempre!')
            break 
        
        else:
            print('Operação invalida, tente novamente.')
            time.sleep(2)


if __name__ == "__main__":
    main()