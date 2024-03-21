# Função para calcular a quantidade total de ração necessária por dia
def calcular_racao_diaria(num_passaros):
    # Cada pássaro consome 30 gramas de ração por dia
    consumo_por_passaro = 30
    # Calcula a quantidade total de ração necessária
    racao_diaria = num_passaros * consumo_por_passaro
    return racao_diaria

# Função principal
def main():
    # Solicita ao usuário o número de pássaros que o criador possui
    num_passaros = int(input("Digite o número de pássaros que você possui: "))

    # Calcula a quantidade total de ração necessária por dia
    racao_diaria = calcular_racao_diaria(num_passaros)

    # Exibe o resultado na tela
    print(f"A quantidade total de ração necessária por dia é de {racao_diaria} gramas.")

# Chama a função principal
if __name__ == "__main__":
    main()
