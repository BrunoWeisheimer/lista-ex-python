# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

# Função principal
def main():
    # Solicita ao usuário a temperatura em Celsius
    temp_celsius = float(input("Digite a temperatura em Celsius: "))

    # Converte Celsius para Fahrenheit
    temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)

    # Exibe o resultado na tela
    print(f"A temperatura equivalente em Fahrenheit é: {temp_fahrenheit:.2f}°F")

# Chama a função principal
if __name__ == "__main__":
    main()
