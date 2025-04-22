def comparar_números():

    print("Digite dois valores inteiros:")
    num1 = int(input())
    num2 = int(input())


    if num1 > num2:
        print(f"Maior = {num1}")
    elif num2  > num1:
        print(F"Maior = {num2}")
    else:
        print("Números iguais")

if __name__ == "__main__":
    comparar_números()