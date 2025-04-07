#Receber número de 1 a 12 e informar mês correspondente
recebimento = int(input("Informe um número de 1 a 12: "))
if recebimento > 12:
    recebimento = print("Valor inválido")
elif recebimento == 1:
    print("Janeiro")
elif recebimento == 2:
    print("Fevereiro")
elif recebimento == 3:
    print("Março")
elif recebimento == 4:
    print("abril")
elif recebimento == 5:
    print("Maio")
elif recebimento == 6:
    print("Junho")
elif recebimento == 7:
    print("Julho")
elif recebimento == 8:
    print("Agosto")
elif recebimento == 9:
    print("Setembro")
elif recebimento == 10:
    print("Outubro")
elif recebimento == 11:
    print("Novembro")
elif recebimento == 12:
    print("Dezembro")
else:
    print("Valor inválido")
