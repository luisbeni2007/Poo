def maior(x,y,z):

    maior_xy = x if x > y else y
    return maior_xy  if maior_xy > z else z

def main():
   num1 = float(input("Digite o primeiro número"))
   num2 = float(input("Digite o segundo número"))
   num3 = float(input("Digite o terceiro número"))

   resultado = maior(num1,num2,num3)
   print(f"o resultado maior entre {num1}, {num2} e {num3} é: {resultado}")

   if __name__ == "__main__":
    main()
