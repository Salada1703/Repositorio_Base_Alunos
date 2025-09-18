import os
print(os.getcwd())
#os.mkdir("d")
#os.mkdir("e")
#os.mkdir("f")

arquivo_path = "arquivo_path"
for i in range(1, 51):
    nome_pasta= f"pasta_{i}"
    try:
        os.mkdir(nome_pasta)
        print(f"""\033[0;32m Pasta '{nome_pasta}' removida com sucesso! ;D""")
    except FileNotFoundError:
        print(f"""\033[0;33m Pasta '{nome_pasta}' não encontrada... @ @""")
    except OSError:
        print(f"""\033[0;34m '{nome_pasta}' é um arquivo, não uma pasta!!! +_+""")

    caminho_arquivo = os.path.join(nome_pasta, "arquivo.txt")
    with open(caminho_arquivo, "w") as f:
        f.write("oi")

    print(f"\033[0;34mArquivo criado em '{caminho_arquivo}' com conteúdo 'oi'.")