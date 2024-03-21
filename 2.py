# Função para calcular o valor total em reais
def calcular_total_em_reais(cotacao_dolar, quantidade_dolar):
    total_em_reais = cotacao_dolar * quantidade_dolar
    return total_em_reais

# Função principal
def main():
    # Solicita ao usuário a cotação do dólar para real
    cotacao_dolar = float(input("Digite a cotação do dólar para real: "))

    # Solicita ao usuário a quantidade de dólares desejada
    quantidade_dolar = float(input("Digite a quantidade de dólares que deseja comprar: "))

    # Calcula o valor total em reais
    total_em_reais = calcular_total_em_reais(cotacao_dolar, quantidade_dolar)

    # Exibe o resultado na tela
    print(f"O total a ser pago em reais é de R${total_em_reais:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
