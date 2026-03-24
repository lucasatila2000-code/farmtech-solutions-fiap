opcao = 0

culturas = []
bases = []
alturas = []
areas = []
insumos = []
qtd_insumos = []

DOSE_SOJA = 0.005   # L de herbicida por m²
DOSE_MILHO = 0.030  # kg de fertilizante por m²

while opcao != 5:

    print("\n--- FARMTECH SOLUTIONS ---")
    print("1 - Entrada de dados (Cadastrar plantio)")
    print("2 - Saída de dados (Exibir plantios)")
    print("3 - Atualizar dados")
    print("4 - Deletar dados")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print("\n------------------------")
        print("Opção inválida! Escolha uma das opções abaixo:")
        print("------------------------")
        print("\n--- FARMTECH SOLUTIONS ---")
        print("1 - Entrada de dados (Cadastrar plantio)")
        print("2 - Saída de dados (Exibir plantios)")
        print("3 - Atualizar dados")
        print("4 - Deletar dados")
        print("5 - Sair")
        opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n-- CADASTRAR PLANTIO --")

        cultura_opcao = input("\nQual a cultura?\nA: Soja\nB: Milho\nDigite o valor da opção (Ex: A): ")

        while cultura_opcao.upper() != "A" and cultura_opcao.upper() != "B":
            print("\n------------------------")
            print("Valor inválido! Escolha uma das opções abaixo:")
            print("------------------------")
            cultura_opcao = input("\nQual a cultura?\nA: Soja\nB: Milho\nDigite o valor da opção (Ex: A): ")

        if cultura_opcao.upper() == "A":
            cultura = "Soja"
            insumo = "Herbicida"
            dose = DOSE_SOJA
            unidade = "L"
        else:
            cultura = "Milho"
            insumo = "Fertilizante"
            dose = DOSE_MILHO
            unidade = "kg"

        base = float(input("\nDigite a base da área em m\n(Ex: 10): "))
        altura = float(input("\nDigite a altura da área em m\n(Ex: 20): "))
        area = base * altura
        qtd = dose * area

        culturas.append(cultura)
        bases.append(base)
        alturas.append(altura)
        areas.append(area)
        insumos.append(insumo)
        qtd_insumos.append(qtd)

        print(f"\n------------------------")
        print(f"Plantio cadastrado com sucesso!")
        print(f"Cultura : {cultura}")
        print(f"Base    : {base:.1f} m")
        print(f"Altura  : {altura:.1f} m")
        print(f"Área    : {area:.1f} m²")
        print(f"Insumo  : {insumo} — {qtd:.2f} {unidade} necessários")
        print("------------------------")

    elif opcao == 2:
        print("\n-- EXIBIR PLANTIOS --")

        if len(culturas) == 0:
            print("\n------------------------")
            print("Nenhum plantio cadastrado.")
            print("------------------------")
        else:
            for i in range(len(culturas)):
                if culturas[i] == "Soja":
                    unidade = "L"
                else:
                    unidade = "kg"

                print(f"\n[{i}] ------------------------")
                print(f"  Cultura : {culturas[i]}")
                print(f"  Base    : {bases[i]:.1f} m")
                print(f"  Altura  : {alturas[i]:.1f} m")
                print(f"  Área    : {areas[i]:.1f} m²")
                print(f"  Insumo  : {insumos[i]} — {qtd_insumos[i]:.2f} {unidade}")

    elif opcao == 3:
        print("\n-- ATUALIZAR DADOS --")

        if len(culturas) == 0:
            print("\n------------------------")
            print("Não há dados para atualizar!")
            print("------------------------")
        else:
            print("\nPlantios cadastrados:")
            for i in range(len(culturas)):
                print(f"  [{i}] {culturas[i]} — {areas[i]:.1f} m²")

            indice = int(input("\nDigite o número do plantio que deseja atualizar: "))

            while indice < 0 or indice >= len(culturas):
                print("\n------------------------")
                print("Índice inválido! Escolha um dos plantios abaixo:")
                print("------------------------")
                for i in range(len(culturas)):
                    print(f"  [{i}] {culturas[i]} — {areas[i]:.1f} m²")
                indice = int(input("\nDigite o número do plantio que deseja atualizar: "))

            nova_opcao = input("\nNova cultura?\nA: Soja\nB: Milho\nDigite o valor da opção (Ex: A): ")

            while nova_opcao.upper() != "A" and nova_opcao.upper() != "B":
                print("\n------------------------")
                print("Valor inválido! Escolha uma das opções abaixo:")
                print("------------------------")
                nova_opcao = input("\nNova cultura?\nA: Soja\nB: Milho\nDigite o valor da opção (Ex: A): ")

            if nova_opcao.upper() == "A":
                culturas[indice] = "Soja"
                insumos[indice] = "Herbicida"
                dose = DOSE_SOJA
                unidade = "L"
            else:
                culturas[indice] = "Milho"
                insumos[indice] = "Fertilizante"
                dose = DOSE_MILHO
                unidade = "kg"

            bases[indice] = float(input("\nNova base em m\n(Ex: 10): "))
            alturas[indice] = float(input("\nNova altura em m\n(Ex: 20): "))
            areas[indice] = bases[indice] * alturas[indice]
            qtd_insumos[indice] = dose * areas[indice]

            print(f"\n------------------------")
            print(f"Plantio [{indice}] atualizado com sucesso!")
            print(f"  Cultura : {culturas[indice]}")
            print(f"  Base    : {bases[indice]:.1f} m")
            print(f"  Altura  : {alturas[indice]:.1f} m")
            print(f"  Área    : {areas[indice]:.1f} m²")
            print(f"  Insumo  : {insumos[indice]} — {qtd_insumos[indice]:.2f} {unidade}")
            print("------------------------")

    elif opcao == 4:
        print("\n-- DELETAR DADOS --")

        if len(culturas) == 0:
            print("\n------------------------")
            print("Não há dados para apagar!")
            print("------------------------")
        else:
            print("\nPlantios cadastrados:")
            for i in range(len(culturas)):
                print(f"  [{i}] {culturas[i]} — {areas[i]:.1f} m²")

            indice = int(input("\nDigite o número do plantio que deseja deletar: "))

            while indice < 0 or indice >= len(culturas):
                print("\n------------------------")
                print("Índice inválido! Escolha um dos plantios abaixo:")
                print("------------------------")
                for i in range(len(culturas)):
                    print(f"  [{i}] {culturas[i]} — {areas[i]:.1f} m²")
                indice = int(input("\nDigite o número do plantio que deseja deletar: "))

            confirmacao = input(f"\nTem certeza que deseja apagar os dados de {culturas[indice]}?\nDigite:\nA: SIM\nB: NÃO\n")

            while confirmacao.upper() != "A" and confirmacao.upper() != "B":
                print("\n------------------------")
                print("Opção inválida! Escolha uma das opções abaixo:")
                print("------------------------")
                confirmacao = input(f"Tem certeza que deseja apagar os dados de {culturas[indice]}?\nDigite:\nA: SIM\nB: NÃO\n")

            if confirmacao.upper() == "A":
                print(f"\n------------------------")
                print(f"Plantio de {culturas[indice]} deletado com sucesso!")
                print("------------------------")
                culturas.pop(indice)
                bases.pop(indice)
                alturas.pop(indice)
                areas.pop(indice)
                insumos.pop(indice)
                qtd_insumos.pop(indice)
            else:
                print(f"\n------------------------")
                print("Operação cancelada.")
                print("------------------------")

    elif opcao == 5:
        print(f"\n------------------------")
        print("Encerrando o sistema...")
        print("------------------------")
