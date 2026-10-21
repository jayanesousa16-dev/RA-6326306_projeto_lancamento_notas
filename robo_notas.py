
import pandas as pd

# Configurações
ARQUIVO = "notas_teste.xlsx"
MEDIA_MINIMA = 7.0

# Ler a planilha de teste
dados = pd.read_excel(ARQUIVO)

# Conferir se existem alunos
if dados.empty:
    print("A planilha não possui alunos cadastrados.")

else:
    aprovados = []
    reprovados = []

    # Analisar cada aluno
    for _, aluno in dados.iterrows():
        nome = aluno["Nome"]
        ra = aluno["RA"]
        nota = float(aluno["Nota Final"])

        if nota >= MEDIA_MINIMA:
            situacao = "APROVADO"
            aprovados.append(nome)
        else:
            situacao = "REPROVADO"
            reprovados.append(nome)

        print("-" * 35)
        print(f"Aluno: {nome}")
        print(f"RA: {ra}")
        print(f"Nota final: {nota:.1f}")
        print(f"Situação: {situacao}")

    # Mostrar o resumo
    print("\n========== RESUMO ==========")
    print(f"Total de alunos: {len(dados)}")
    print(f"Total de aprovados: {len(aprovados)}")
    print(f"Total de reprovados: {len(reprovados)}")

    print("\nAlunos aprovados:")
    for nome in aprovados:
        print(f"- {nome}")

    print("\nAlunos reprovados:")
    for nome in reprovados:
        print(f"- {nome}")

    # Salvar relatório sem alterar a planilha original
    dados["Situação Calculada"] = dados["Nota Final"].apply(
        lambda nota: "APROVADO"
        if nota >= MEDIA_MINIMA
        else "REPROVADO"
    )

    dados.to_csv(
        "relatorio_aprovacao.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("\nRelatório salvo em relatorio_aprovacao.csv")

