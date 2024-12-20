import os, csv
from gdown import download

# faz o download do dataset para uso e cria o caminho \dataset
def download_dataset(link,filename):

    file_id = link.split('/')[5]
    url = f'https://drive.google.com/uc?id={file_id}'

    if not os.path.exists(filename): 
        os.mkdir("dataset") 
    download(url, filename, quiet = False)
    return None

# cria a matriz de contrato e insere os valores nela
def preencher_matriz_contratos(nome_arquivo: str):
    
    arquivo=open(nome_arquivo).readlines()
    # armazena a linha sobre o pedido de contrato que a empresa quer
    pedido_empresa = arquivo[0].strip().split()
    # elimina essa linha do arquivo carregado
    arquivo.pop(0)
    # retira a quebra de linha (\n) entre as variáveis
    for linha in range(len(arquivo)):
        arquivo[linha]=arquivo[linha].strip()
    # determinar o tamanho da matriz de valores de contrato
    n = int(pedido_empresa[1]) # fornecedor
    m = int(pedido_empresa[0]) # meses de contrato
    t = float(pedido_empresa[2]) # multa de mudança de contrato
    # construir a matriz de contratos e incluir os valores infinitos
    contratos = []
    for fornecedor in range(n):
        contratos.append([])
        for inicio in range(m+1):
            contratos[fornecedor].append([])
            for fim in range(m+1):
                contratos[fornecedor][inicio].append(float('inf'))
    # inserir os valores de contratos que estão no arquivo dentro de uma matriz
    for linha in arquivo:
        dados = linha.split()
        dados = [int(dados[0]), int(dados[1]), int(dados[2]), float(dados[3])]
        fornecedor = (dados[0])-1
        mes_inicial = dados[1]
        mes_final = dados[2]
        valor_contrato = dados[3]
        contratos[fornecedor][mes_inicial][mes_final] = valor_contrato
    return m, n, t, contratos     

# mostra a matriz no terminal
def imprimir_matriz(matriz, k=None):
    if k is None:
        for fornecedor in matriz:
            print("\n")
            for linha in fornecedor:
                print(linha)
    else:
        for linha in matriz[k]:
            print(linha)
    return None

# cria, preenche e exporta o arquivo com os valores de contrato em formato .csv
def exportar_csv(nome_arquivo, matriz):
    # criar o diretório \resultados
    if not os.path.exists(nome_arquivo): 
        os.mkdir("resultados")
    # escrever no arquivo os valores
    with open(nome_arquivo, 'w', newline='') as resultado:
        writer = csv.writer(resultado)
        for fornecedor in range(len(matriz)):
            writer.writerow([f'Fornecedor {fornecedor + 1}',])
            writer.writerows(matriz[fornecedor])
    return None
