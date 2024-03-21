# Função para calcular o valor da compra com desconto
def calcular_valor_com_desconto(valor_compra):
    # Calcula o valor do desconto (quinze por cento do valor da compra)
    desconto = valor_compra * 0.15
    # Calcula o valor da compra com o desconto aplicado
    valor_com_desconto = valor_compra - desconto
    return valor_com_desconto

# Função principal
def main():
    # Solicita ao usuário o valor da compra
    valor_compra = float(input("Digite o valor da compra: R$"))

    # Calcula o valor da compra com desconto
    valor_com_desconto = calcular_valor_com_desconto(valor_compra)

    # Exibe o resultado na tela
    print(f"O valor da compra com desconto é: R${valor_com_desconto:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
