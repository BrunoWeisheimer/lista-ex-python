# Função para converter minutos em segundos
def minutos_para_segundos(minutos):
    segundos = minutos * 60  # 1 minuto = 60 segundos
    return segundos

# Função principal
def main():
    # Solicita ao usuário a quantidade de minutos
    minutos = float(input("Digite a quantidade de minutos: "))

    # Converte minutos para segundos
    segundos = minutos_para_segundos(minutos)

    # Exibe o resultado na tela
    print(f"{minutos} minutos equivalem a {segundos} segundos.")

# Chama a função principal
if __name__ == "__main__":
    main()
