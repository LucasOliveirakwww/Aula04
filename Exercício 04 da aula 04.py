#Receber número aleatório e realizar a tabuada até 10
num = int(input("Digite um número: "))
for x in range(1,11):
    soma = num * x
    print(f"{num} x {x} = {soma}")