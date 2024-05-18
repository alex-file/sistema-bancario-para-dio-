
# telas

ms = '''
####### BANCO FREE 24 HORAS #########
    
    [1] PARA SALDO    
    [2] PARA SACAR
    [3] PARA DEPOSITAR
    [4] PARA EXTRATO
    [5] PARA SAIR

#####################################
'''
#volto

SACAR = '''
####### BANCO FREE 24 HORAS #########
         TELA DE SAQUE
QUANTO VOCÊ DESEJA SACAR?     
#####################################
'''
DEPOSITO = '''
####### BANCO FREE 24 HORAS #########
         TELA DE DEPOSITO
QUANTO VOCÊ DESEJA DEPOSITAR?     
#####################################
'''

SAIDA = '''
############ BANCO FREE 24 HORAS #################
## OBRIGADO POR ULTILIZAR O BANCO FREE 24 HORAS! # 
##################################################
'''
#fim das telas

#variáveis
saldo = 10
saque = 0
depositar = 0
extrato = ''
cont_saque = 0
cont_deposito = 0
#LIMITE-SAQUE = 4

while True:

    ops = input(ms)
    
    if ops == '1':
        print( f'''
####### BANCO FREE 24 HORAS #########
            SALDO NA TELA
    SALDO ATUAL: R$ {saldo}
#####################################
 ''')    
        ops = input('deseja fazer outra operação? S/N')
        if ops == 'n':
            break
    
    ############### comdicional sacar #########################
    elif ops == '2':
        saque = int(input(SACAR))
        if saque > saldo:
            print('SALDO INSUFICIENTE!')
        elif saque <= saldo:
            saldo -= saque
            cont_saque += 1
            print('SAQUE EM ANDAMENTO CONTANDO AS NOTAS!')
            ops = input('deseja fazer outra operação? S/N')
        if ops == 'n':
            break

    ############ condicional para deposito #####################          

    elif ops == '3':
        depositar = int(input(DEPOSITO))
        saldo += depositar
        cont_deposito += 1
        print('DEPOSITO REALIZADO COM SUCESSO!!')
        ops = input('deseja fazer outra operação? S/N')
        if ops == 'n':
            break
 
   ############## CONDICIONAL EXTRATO  ######################### 
    elif ops == '4':
        print( f'''
####### BANCO FREE 24 HORAS #########
            EXTRATO NA TELA
    SALDO ATUAL: R$ {saldo}
    NUMEROS DE SAQUES: {cont_saque}
    QUANTIDADE DE DEPOSITOS {cont_deposito}
#####################################
 ''')  
        ops = input('deseja fazer outra operação? S/N')
        if ops == 'n':
            break
     ############## fim CONDICIONAL EXTRATO  #########################   
print()   
print(SAIDA)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    