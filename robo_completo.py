
import pandas as pd
import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Ler a planilha fictícia
dados = pd.read_excel("notas_teste.xlsx")

MEDIA_MINIMA = 7.0

# Ordem dos campos no Google Forms
campos = [
    "RA",
    "Nome",
    "Nota 1",
    "Nota 2",
    "TF01",
    "TF02",
    "Nota Final",
    "Stuação"
]

aprovados = 0
reprovados = 0

print("O robô começará em 5 segundos.")
print("Deixe o formulário vazio, com o campo RA visível.")
time.sleep(5)

for indice_aluno, (_, aluno) in enumerate(dados.iterrows()):

    nota_final = float(aluno["Nota Final"])

    if nota_final >= MEDIA_MINIMA:
        situacao = "APROVADO"
        aprovados += 1
    else:
        situacao = "REPROVADO"
        reprovados += 1

    # Começar no campo RA
    pyautogui.click(685, 522)

    for indice_campo, campo in enumerate(campos):

        if campo == "Stuação":
            valor = situacao
        else:
            valor = str(aluno[campo])

        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(valor, interval=0.08)

        if indice_campo < len(campos) - 1:
            pyautogui.press("tab")
            time.sleep(0.3)

    print("----------------------------")
    print("Aluno:", aluno["Nome"])
    print("Nota final:", nota_final)
    print("Situação:", situacao)

    # Esperar a conferência
    print("Confira os dados no formulário.")
    print("NÃO clique em Enviar.")

    if indice_aluno < len(dados) - 1:
        print("O próximo aluno começará em 15 segundos.")
        print("Limpe o formulário e volte ao campo RA.")
        time.sleep(15)

print("\n===== RESUMO =====")
print("Total de alunos:", len(dados))
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)
print("Demonstração finalizada!")
