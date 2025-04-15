frase = input("Digite uma frase:")
ultimo_espaço = frase.rfind(" ")
ultima_palavra = frase[ultimo_espaço + 1:]
print(ultima_palavra)