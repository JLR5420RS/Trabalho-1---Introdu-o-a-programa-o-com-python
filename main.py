#Trabalho 1 - X552 Introdução a programação com python

# carrega o arquivo de dados
resposta=(input("qual arquivo você deseja selecionar? digite 1 para entrada.txt ou digite 2 para entradagrande.txt: "))
while resposta != "1" and resposta != "2":
    resposta=(input("qual arquivo você deseja selecionar? digite 1 para entrada.txt ou digite 2 para entradagrande.txt: "))
if resposta == "1":
    arquivo=open("entrada.txt").readlines()
else:
    arquivo=open("entradagrande.txt").readlines()
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
multa = float(pedido_empresa[2]) # multa de mudança de contrato
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
print(contratos)









