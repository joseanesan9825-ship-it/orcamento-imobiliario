import csv

def calcular_aluguel():
    print("Tipos de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    #validação do tipo
    while True:
        try:
            tipo = int(input("Escolha o tipo (1-3): "))
            if tipo in [1, 2, 3]:
                break
            else:
                print("Opção  Inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Erro. Digite apenas números!")

    aluguel = 0

    # ================= APARTAMENTO =================
    if tipo == 1:
        aluguel = 700

        while True:
            try:
                quartos = int(input("Quantidade de quartos (1 ou 2): "))
                if quartos in [1, 2]:
                    break
                else:
                    print("Opção  Inválida. Escolha 1 ou 2.")
            except ValueError:
                print("Erro. Digite apenas números!")

        if quartos == 2:
            aluguel += 200

        while True:
            filhos = input("Possui filhos? (s/n): ").lower()
            if filhos in ['s', 'n']:
                break
            else:
                print("Opção  Inválida. Digite apenas 's' ou 'n'.")

        if filhos == 'n':
            aluguel *= 0.95

        while True:
            garagem = input("Deseja vaga de garagem? (s/n): ").lower()
            if garagem in ['s', 'n']:
                break
            else:
                print("Opção  Inválida. Digite apenas 's' ou 'n'.")

        if garagem == 's':
            aluguel += 300

    # ================= CASA =================
    elif tipo == 2:
        aluguel = 900

        while True:
            try:
                quartos = int(input("Quantidade de quartos (1 ou 2): "))
                if quartos in [1, 2]:
                    break
                else:
                    print("Escolha 1 ou 2.")
            except ValueError:
                print("Erro. Digite apenas números!")

        if quartos == 2:
            aluguel += 250

        while True:
            garagem = input("Deseja vaga de garagem? (s/n): ").lower()
            if garagem in ['s', 'n']:
                break
            else:
                print("Opção  Inválida. Digite apenas 's' ou 'n'.")

        if garagem == 's':
            aluguel += 300

    # ================= ESTÚDIO =================
    elif tipo == 3:
        aluguel = 1200

        while True:
            try:
                vagas = int(input("Quantas vagas de garagem? "))
                if vagas >= 0:
                    break
                else:
                    print("Digite um número maior ou igual a 0.")
            except ValueError:
                print("Erro. Digite apenas números!")

        if vagas >= 1:
            aluguel += 250

        if vagas > 2:
            aluguel += (vagas - 2) * 60

    return aluguel

def calcular_contrato():
    contrato = 2000

    while True:
        try:
            parcelas = int(input("Em quantas parcelas deseja pagar o contrato (1 a 5): "))
            if 1<= parcelas <=5:
                break
            else:
                print("Opção  Inválida. Escolha entre 1 e 5 parcelas.")
        except ValueError:
                print("Erro. Digite apenas números")

    valor_parcela = contrato / parcelas
    return contrato, parcelas, valor_parcela

def gerar_csv(valor_mensal):
    with open("parcelas.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Parcela", "Valor"])
        
        for i in range(1, 13):
            writer.writerow([i,f"R${valor_mensal:.2f}"])

def main():
    aluguel = calcular_aluguel()
    contrato, parcelas, valor_parcela = calcular_contrato()

    total_mensal = aluguel + (contrato / 12)

    print("\n--- ORÇAMENTO FINAL ---")
    print(f"Aluguel mensal: R$ {aluguel:.2f}")
    print(f"Contrato imobiliário total: R$ {contrato:.2f}")
    print(f"Contrato em {parcelas}x de R$ {valor_parcela:.2f}")
    print(f"Valor mensal total: R$ {total_mensal:.2f}")

    gerar_csv(total_mensal)
    print("\nArquivo 'parcelas.csv' gerado com sucesso!")

main()
