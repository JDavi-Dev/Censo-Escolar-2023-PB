import csv
import json

# Caminho do arquivo CSV de entrada e o JSON de saída
arquivo_csv = "microdados_ed_basica_2023.csv"
arquivo_json = "censo_paraiba_2023.json"

# Lista de colunas desejadas
colunas_desejadas = [
    'NO_REGIAO', 'NO_UF', 'SG_UF',
    'NO_MUNICIPIO','NO_MESORREGIAO',
    'NO_MICRORREGIAO','NO_ENTIDADE',
    'QT_MAT_BAS', 'QT_MAT_INF', 'QT_MAT_FUND',
    'QT_MAT_MED', 'QT_MAT_PROF', 'QT_MAT_EJA',
    'QT_MAT_ESP'
]

# Lista para armazenar os dados filtrados
dados_paraiba = []

# Lendo o arquivo CSV
with open(arquivo_csv, mode='r', encoding='latin-1') as csv_file:
    leitor_csv = csv.DictReader(csv_file, delimiter=';')
    
    for linha in leitor_csv:
        # Filtrar somente os dados da Paraíba (SG_UF == 'PB')
        if linha['SG_UF'] == 'PB':
            # Criar um dicionário apenas com as colunas desejadas
            dados_filtrados = {coluna: linha[coluna] for coluna in colunas_desejadas}
            dados_paraiba.append(dados_filtrados)

# Salvando o resultado em um arquivo JSON
with open(arquivo_json, mode='w', encoding='utf-8') as json_file:
    json.dump(dados_paraiba, json_file, indent=4, ensure_ascii=False)

print(f"Dados da Paraíba exportados para {arquivo_json} com sucesso!")