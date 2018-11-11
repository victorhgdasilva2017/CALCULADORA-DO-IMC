# -*- CODING UTF:40 -*-
#
# VICTOR HUGO
#
# ------------------------------------

import time
import random

print("\t PESO IDEAL: \n")

print("PRIMEIRAMENTE, VAMOS CALCULAR SEU IMC: ")


p = input("DIGITE SEU PESO EM QUILOGRAMAS: ")
e = input("DIGITE SUA ESTATURA EM METROS: ")

resp = (float(p)) / (float(e) * float(e))

print("\t CALCULANDO....\n")

loop = 0
time.sleep(1.2)

print("\t O RESULTADO DE SEU IMC FOI DE:",resp,"\n")


print("AGORA, VAMOS VER SE SEU PESO ESTÁ CORRETO!")

peso = input("DIGITE O RESULTADO DE SEU IMC ARREDONDANDO O VALOR: ")

print("\t CARREGANDO....\n")

loop = 0
time.sleep(1.2)

if peso < '17':
    print("\t VOCÊ ESTÁ ABAIXO DO PESO, GANHE MASSA!!\n")


elif peso > '40':
    print("\t VOCÊ ESTÁ MUITO ACIMA DO PESO, PERCA MASSA IMEDIATAMENTE!!\n")


elif peso == '17':
    print("\t VOCÊ ESTÁ ABAIXO DO PESO, GANHE MASSA!!\n")


elif peso == '18':
    print("\t VOCÊ ESTÁ ABAIXO DO PESO, GANHE MASSA!!\n")


elif peso == '19':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '20':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '21':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '22':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '23':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '24':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '25':
    print("\t PARABÉNS, VOCÊ ESTÁ EM SEU PESO IDEAL!!\n")


elif peso == '26':
    print("\t CUIDADO, VOCÊ ESTÁ ACIMA DO PESO!!\n")


elif peso == '27':
    print("\t CUIDADO, VOCÊ ESTÁ ACIMA DO PESO!!\n")


elif peso == '28':
    print("\t CUIDADO, VOCÊ ESTÁ ACIMA DO PESO!!\n")


elif peso == '29':
    print("\t CUIDADO, VOCÊ ESTÁ ACIMA DO PESO!!\n")


elif peso == '30':
    print("\t VOCÊ ESTÁ OBESO, PERCA MASSA!!\n")


elif peso == '31':
    print("\t VOCÊ ESTÁ OBESO, PERCA MASSA!!\n")


elif peso == '32':
    print("\t VOCÊ ESTÁ OBESO, PERCA MASSA!!\n")


elif peso == '33':
    print("\t VOCÊ ESTÁ OBESO, PERCA MASSA!!\n")


elif peso == '34':
    print("\t VOCÊ ESTÁ OBESO, PERCA MASSA!!\n")


elif peso == '35':
    print("\t VOCÊ ESTÁ VOCÊ ESTÁ MUITO ACIMA DO PESO, PERCA MASSA!!\n")


elif peso == '36':
    print("\t VOCÊ ESTÁ MUITO ACIMA DO PESO, PERCA MASSA!!\n")


elif peso == '37':
    print("\t VOCÊ ESTÁ MUITO ACIMA DO PESO, PERCA MASSA!!\n")


elif peso == '38':
    print("\t VOCÊ ESTÁ MUITO ACIMA DO PESO, PERCA MASSA!!\n")


elif peso == '39':
    print("\t VOCÊ ESTÁ MUITO ACIMA DO PESO, PECA MASSA!!\n")




print("SATISFEITO COM SEUS RESULTADOS??")

print("NOSSO SISTEMA POSSUÍ 90% DE PRECISÃO")


print("QUER OLHAR A TABELA DE PESOS DO IMC?")

enter = input("SE SIM, PRECIONE 'Y', SE NÃO PRECIONE 'N'")


if enter == 'n':
    print("\t CARREGANDO....\n")

    loop = 0
    time.sleep(1)

    exit()


elif enter == 'y':
    print("\t CARREGANDO....\n")

    loop = 0
    time.sleep(1)


    print("DÊ UMA OLHADA COMO CÁLCULAMOS O IMC:")

    print("PESO / ESTATURA * ESTATURA")

    print("DIVIDIMOS SEU PESO PELA SUA ESTATURA AO QUADRADO")

    print("AINDA CURIOSO?? DÊ UMA OLHADA NA TABELA DE PESO DO IMC")

    print("\t CARREGANDO....\n")

    loop = 0
    time.sleep(1.1)


    print(" ABAIXO DE 17 ----> MUITO ABAIXO DO PESO"
            " ENTRE 17 E 18,49 ----> ABAIXO DO PESO"
            " ENTRE 18,5 E 24,99 ----> PESO NORMAL"
            " ENTRE 25 E 29,99 ----> ACIMA DO PESO"
            " ENTRE 30 E 34,99 ----> OBESIDADE"
            " ENTRE 35 E 39,99 ----> OBESIDADE SEVERA"
            " ACIMA DE 40 ----> OBESIDADE MÓRBIDA")





