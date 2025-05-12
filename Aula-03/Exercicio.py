s = 0
n = int(input("Digite o primeiro número: "))
 

if n % 2 == 1: 
    s = s + n


x = int(input("Digite outro número:"))

if x % 2 == 1: s = s + x


n = int(input("Digite mais um número:"))
if n % 2 == 1:
    s = s + n

print("Soma dos ímpares", s)