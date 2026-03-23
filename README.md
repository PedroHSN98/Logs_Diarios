# Analisador de Logs (Python)

Este projeto contém um script simples para análise de logs em formato XML (especificamente `log4j`) no diretório `logs_servidor/logs.xml`.

## O que o script faz

- Lê `logs_servidor/logs.xml`
- Procura várias mensagens / padrões de erro (definidos em `padroes_busca`)
- Conta quantas vezes cada padrão aparece
- Exibe um relatório resumido no console

## Estrutura de arquivos

- `analisador_logs.py`: código principal
- `logs_servidor/logs.xml`: arquivo de entrada (deve existir)
- `README.md`: este arquivo

## Requisitos

- Python 3.x instalado
- Arquivo `logs_servidor/logs.xml` disponível

## Uso

1. Abra terminal/cmd na pasta do projeto:

```bash
cd c:\Users\SEU USER\Pictures\Base64\projeto_automacao
```

2. Execute:

```bash
python analisador_logs.py
```

3. Veja a saída com o relatório de contagens por padrão.

## O que deve ser feito para funcionar

1. Verificar se existe pasta `logs_servidor` no mesmo nível do script.
2. Verificar se dentro dela há `logs.xml`.
3. Confirmar que `logs.xml` é legível e está em `UTF-8` (ou então usar fallback `errors='ignore'` como no script).
4. Se houver log em outro formato, ajustar ou adicionar padrões em `padroes_busca`.

## Customização

- Para adicionar novo tipo de erro, inclua um novo par `chave: valor` em `padroes_busca`.
- Chave: texto exato a buscar na linha do log.
- Valor: nome amigável que aparece no relatório.

## Melhorias possíveis

- Uso de `argparse` para parâmetro de caminho do arquivo
- Suporte para JSON / CSV de resultado
- Interpretar XML em vez de `in` em linha (mais seguro e preciso)
- Gerar arquivo de relatório (`.txt` / `.csv` / `.json`)

## Exemplo de saída

```
------------------------------
RELATÓRIO DE ERROS
------------------------------
1- ElasticSearchException = 12
2- Notfound = 5
...
```

## Observações

- Caso `logs.xml` não exista, o script informa e encerra.
- Caso ocorra erro de leitura, o script exibe exceção e encerra.
