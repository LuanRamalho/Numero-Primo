#-*- coding:utf-8 -*-


print("Digite um n�mero inteiro")
num = int (input())

print("")

for i in range(2,num):
    if i != num:
        i = num % i
        if i == 0:
            print ("N�o � n�mero primo")
            break
        else:
            print ("� um n�mero Primo")
            break