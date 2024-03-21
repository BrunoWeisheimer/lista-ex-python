# Função para calcular o valor a ser pago
def calcular_valor_a_pagar(peso_do_prato):
    preco_por_quilo = 40.00
    valor_a_pagar = preco_por_quilo * peso_do_prato
    return valor_a_pagar

# Função principal
def main():
    # Solicita ao usuário o peso do prato em quilos
    peso_do_prato = float(input("Digite o peso do prato em quilos: "))

    # Calcula o valor a ser pago
    valor_a_pagar = calcular_valor_a_pagar(peso_do_prato)

    # Exibe o resultado na tela
    print(f"O valor a ser pago é de R${valor_a_pagar:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
