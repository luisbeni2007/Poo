def maior( x, y):
    if x > y:
        return x
    else:
        return y
def main():
        
 num1 = float(input("Digite o primeiro número"))
 num2 = float(input("Digite o segundo número"))

 resultado = maior(num1,num2)
 print(f"O maior número entre{num1} e {num2} é: {resultado}")

if__name = "___main__"
main()