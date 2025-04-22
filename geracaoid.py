def identificar_geracao(ano_nascimento):
    if ano_nascimento >= 2013:
        return "Geração Alpha"
    elif 1997 <= ano_nascimento <= 2012:
        return "Geração Z"
    elif 1981 <= ano_nascimento <= 1996:
        return "Geração Y (Millennials)"
    elif 1965 <= ano_nascimento <= 1980:
        return "Geração X"
    elif 1946 <= ano_nascimento <= 1964:
        return "Baby Boomer"
    elif ano_nascimento < 1946:
        return "Geração Silenciosa ou anterior"
    else:
        return "Ano inválido"

# Programa principal com repetição
while True:
    try:
        ano = int(input("Digite seu ano de nascimento: "))
        geracao = identificar_geracao(ano)
        print(f"Você pertence à {geracao}.")
    except ValueError:
        print("Por favor, digite um ano válido.")

    reiniciar = input("Deseja verificar outro ano? (s/n): ").strip().lower()
    if reiniciar != 's':
        print("Programa encerrado. Até mais!")
        break
