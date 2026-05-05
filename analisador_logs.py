import os

def analisar_logs():

    pasta_logs = "logs_servidor"
    nome_arquivo = "logs.xml"  
    caminho_completo = os.path.join(pasta_logs, nome_arquivo)

    # Dicionário que mapeia o que buscar (Chave) para o Nome de Exibição (Valor)
    padroes_busca = {
        '<log4j:message><![CDATA[org.elasticsearch.ElasticsearchStatusException:': "ElasticSearchException",
        '<log4j:message><![CDATA[{code="404", msg="Not Found",': "Notfound",
        '<log4j:message><![CDATA[java.io.IOException: Broken pipe]]></log4j:message>': "Broken Pipe",
        '<log4j:message><![CDATA[java.io.IOException: Connection reset by peer]]></log4j:message>': "Conection Reset By Peer",
        'ldap.internal.exportimport.LDAPUserImporterImpl': "ldap.internal.exportimport.LDAPUserImporterImpl",
        '<log4j:message><![CDATA[Problem accessing LDAP server]]></log4j:message>': "Problem accessing LDAP server",
        '(ldap.internal.authenticator.LDAPAuth)': "ldap.internal.authenticator.LDAPAuth",
        '<log4j:message><![CDATA[Skip /o/js/resolved-module/frontend-js-metal-web$metal': "Skip /frontend-js-metal-web$metal",
        '<log4j:message><![CDATA[No theme found for specified theme id mtportal_WAR_mtportaltheme.': "No theme found for specified theme id mtportal_WAR_mtportaltheme",
        '<log4j:message><![CDATA[{code="404"': 'Error {code="404"',
        '<log4j:message><![CDATA[SAX Security Manager': "SAX Security Manager",
        'uri=/mt-portal-theme/images/ajax-loader.gif': "Ajax-Loader",
        'com.liferay.change.tracking.internal.servlet.filter.CTCollectionPreviewFilter': "CTCollectionPreviewFilter",
        'FTL stack trace' : 'FTL stack trace',
        'log4j:throwable><![CDATA[com.liferay.document.library.kernel.exception.NoSuchFileEntryException: No FileEntry exists with the key {fileEntryId=46846350}': "NoSuchFileEntryException",
        'InvalidRepositoryIdException': "InvalidRepositoryIdException",
        '[PaginationLimitFilter] Applying limit: bot UA detected': '[PaginationLimitFilter] Applying limit: bot UA detected',
    }

    contagem = {nome: 0 for nome in padroes_busca.values()}

    if not os.path.exists(caminho_completo):
        print(f"Erro: O ficheiro não foi encontrado em: {caminho_completo}")
        print(f"Certifica-te de que a pasta '{pasta_logs}' existe e o ficheiro está lá dentro.")
        return

    try:
        with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as ficheiro:
            for linha in ficheiro:
                for termo_busca, nome_exibicao in padroes_busca.items():
                    if termo_busca in linha:
                        contagem[nome_exibicao] += 1
    except Exception as e:
        print(f"Ocorreu um erro ao ler o ficheiro: {e}")
        return

    print("-" * 30)
    print("RELATÓRIO DE ERROS")
    print("-" * 30)
    

    for i, (erro, total) in enumerate(contagem.items(), 1):
        print(f"{i}- {erro} = {total}")

if __name__ == "__main__":
    analisar_logs()