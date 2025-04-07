#Receber número e mostrar números ímpares de 1 até o digitado
Num = int(input("Digite um número: "))
for x in range(1,Num+1):
    if x%2 != 0:
     print(x)
