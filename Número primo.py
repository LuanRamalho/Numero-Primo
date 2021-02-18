#-*- coding:utf-8 -*-


print("Digite um número inteiro")
num = int (input())

print("")

for i in range(2,num):
    if i != num:
        i = num % i
        if i == 0:
            print ("Não é número primo")
            break
        else:
            print ("É um número Primo")
            break