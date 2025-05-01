def calcular_media_e_comparar():
    print("Digite quatro valores inteiros")
    números = []
    for i in range(4):
        números.append(int(input()))
        media = sum (números) / len (números)
        print(f"Média= {int(media)}")

    for num in números:
        if num < media:
            print(num)
            print("Números menores que a media ")
            
            for num in números:
                if num >= media:
                    print(num)
                    print("Números maiores  ou iguais a média ")