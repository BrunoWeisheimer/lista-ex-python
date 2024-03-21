# Função para calcular o total arrecadado
def calcular_total_arrecadado(qtd_smartphones, qtd_tablets):
    preco_smartphone = 1000.00
    preco_tablet = 1500.00
    
    total_smartphones = qtd_smartphones * preco_smartphone
    total_tablets = qtd_tablets * preco_tablet
    
    total_arrecadado = total_smartphones + total_tablets
    return total_arrecadado

# Função principal
def main():
    # Solicita ao usuário o número de smartphones e tablets vendidos
    qtd_smartphones = int(input("Digite o número de smartphones vendidos: "))
    qtd_tablets = int(input("Digite o número de tablets vendidos: "))

    # Calcula o total arrecadado
    total_arrecadado = calcular_total_arrecadado(qtd_smartphones, qtd_tablets)

    # Exibe o resultado na tela
    print(f"O total arrecadado foi de R${total_arrecadado:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
