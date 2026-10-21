
import pandas as pd

dados = {
    "Carimbo de data/hora": [
        "20/10/2026 10:00:00",
        "20/10/2026 10:05:00",
        "20/10/2026 10:10:00"
    ],
    "RA": ["1001", "1002", "1003"],
    "Nome": ["Ana Silva", "Pedro Santos", "Maria Oliveira"],
    "Nota 1": [8.0, 3.0, 7.0],
    "Nota 2": [9.0, 4.0, 6.0],
    "TF01": [8.0, 5.0, 7.0],
    "TF02": [9.0, 4.0, 8.0],
    "Stuação": ["", "", ""],
    "Nota Final": [8.5, 3.5, 7.0]
}

planilha = pd.DataFrame(dados)

planilha.to_excel("notas_teste.xlsx", index=False)

print("Planilha de teste criada com sucesso!")
print(planilha[["RA", "Nome", "Nota Final"]])
