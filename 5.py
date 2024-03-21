# Função para calcular quantos litros podem ser abastecidos
def calcular_litros_abastecidos(preco_litro, valor_disponivel):
    litros_abastecidos = valor_disponivel / preco_litro
    return litros_abastecidos

# Função principal
def main():
    # Solicita ao usuário o preço do litro da gasolina
    preco_litro = float(input("Digite o preço do litro da gasolina: R$"))

    # Solicita ao usuário o valor disponível para abastecer
    valor_disponivel = float(input("Digite o valor disponível para abastecer: R$"))

    # Calcula quantos litros podem ser abastecidos
    litros_abastecidos = calcular_litros_abastecidos(preco_litro, valor_disponivel)

    # Exibe o resultado na tela
    print(f"Você pode abastecer {litros_abastecidos:.2f} litros.")

# Chama a função principal
if __name__ == "__main__":
    main()
