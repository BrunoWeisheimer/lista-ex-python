# Função para calcular a média final
def calcular_media_final(nota_grau_a, nota_grau_b):
    # Calcula a média ponderada
    media_final = (nota_grau_a * (1/3)) + (nota_grau_b * (2/3))
    return media_final

# Função principal
def main():
    # Solicita ao usuário a nota do Grau A e do Grau B
    nota_grau_a = float(input("Digite a nota do Grau A: "))
    nota_grau_b = float(input("Digite a nota do Grau B: "))

    # Calcula a média final
    media_final = calcular_media_final(nota_grau_a, nota_grau_b)

    # Exibe o resultado na tela
    print("A média final é:", media_final)

# Chama a função principal
if __name__ == "__main__":
    main()
