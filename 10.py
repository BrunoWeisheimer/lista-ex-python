# Função para calcular o valor da compra com desconto
def calcular_valor_compra(camisetas, calcas, cintos):
    preco_camiseta = 25.00
    preco_calca = 100.00
    preco_cinto = 40.00
    
    # Calcula o valor total da compra
    total = (camisetas * preco_camiseta) + (calcas * preco_calca) + (cintos * preco_cinto)
    
    # Calcula o valor do desconto (10% do total)
    desconto = total * 0.10
    
    # Calcula o valor da compra com desconto
    valor_com_desconto = total - desconto
    
    return total, desconto, valor_com_desconto

# Função principal
def main():
    # Solicita ao usuário o número de camisetas, calças e cintos comprados
    camisetas = int(input("Digite o número de camisetas compradas: "))
    calcas = int(input("Digite o número de calças compradas: "))
    cintos = int(input("Digite o número de cintos comprados: "))

    # Calcula o valor da compra com desconto
    total, desconto, valor_com_desconto = calcular_valor_compra(camisetas, calcas, cintos)

    # Exibe o valor da compra, o valor do desconto e o valor final com desconto na tela
    print(f"Valor da compra: R${total:.2f}")
    print(f"Valor do desconto (10%): R${desconto:.2f}")
    print(f"Valor final com desconto: R${valor_com_desconto:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
