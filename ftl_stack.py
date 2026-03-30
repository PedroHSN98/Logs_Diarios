import os
import re  # Importamos o módulo de Expressões Regulares

def analisar_logs():
    pasta_logs = "logs_servidor"
    nome_arquivo = "logs.xml"
    caminho_completo = os.path.join(pasta_logs, nome_arquivo)

    # Dicionário para armazenar as variações: { "conteúdo_do_colchete": quantidade }
    variacoes_encontradas = {}
    total_erros_ftl = 0

    if not os.path.exists(caminho_completo):
        print(f"Erro: O ficheiro não foi encontrado em: {caminho_completo}")
        return

    try:
        with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as ficheiro:
            for linha in ficheiro:
                # Verificamos se a linha contém o erro FTL
                if "FTL stack trace" in linha or "Failed at:" in linha:
                    # Regex explicada: Procura algo entre [ e ]
                    # \[ e \] escapam os caracteres especiais. (.*?) captura o conteúdo dentro.
                    resultado = re.search(r'\[(.*?)\]', linha)
                    
                    if resultado:
                        conteudo_extraido = resultado.group(1)
                        total_erros_ftl += 1
                        
                        # Adiciona ao dicionário e conta as ocorrências
                        if conteudo_extraido in variacoes_encontradas:
                            variacoes_encontradas[conteudo_extraido] += 1
                        else:
                            variacoes_encontradas[conteudo_extraido] = 1

    except Exception as e:
        print(f"Ocorreu um erro ao ler o ficheiro: {e}")
        return

    # --- RELATÓRIO ---
    print("-" * 50)
    print("RELATÓRIO DE ANÁLISE DE LOGS")
    print("-" * 50)
    print(f"Total de ocorrências de erros FTL: {total_erros_ftl}")
    print(f"Total de variações diferentes encontradas: {len(variacoes_encontradas)}")
    print("-" * 50)

    for i, (info, total) in enumerate(variacoes_encontradas.items(), 1):
        print(f"{i}. Info: [{info}] | Ocorrências: {total}")

    # Alerta se houver informações diferentes
    if len(variacoes_encontradas) > 1:
        print("\n[ALERTA]: Foram encontradas informações DIFERENTES dentro dos colchetes!")
    elif len(variacoes_encontradas) == 1:
        print("\n[INFO]: Todas as informações encontradas são IGUAIS.")

if __name__ == "__main__":
    analisar_logs()