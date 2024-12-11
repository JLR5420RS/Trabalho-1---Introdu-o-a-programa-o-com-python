# Trabalho - 1 Introdução a programação com python (Turma 09)
trabalho de Estrutura de Dados com o objetivo de inserir os valores de contrato de fornecedores de energia considerando os meses que o contrato vale, mais informações a seguir

Instruções do arquivo:

1 - Clonar ou baixar zip do repositório

2 - Abrir e rodar o código

3 - O código vai perguntar qual arquivo para carregar, caso seja o entradas.txt digitar 1, caso contrário digitar 2

Contexto: Mercado Livre de Energia

O Mercado Livre de Energia permite a comercialização independente de energia, estimulando a concorrência entre produtores e geradores, o que torna os custos de compra de energia mais acessíveis. Nesse modelo, consumidores podem escolher seus fornecedores de energia conforme o Sistema Interligado Nacional (SIN) e negociar preços, prazos e volumes. Eles podem adquirir energia diretamente de geradoras ou comercializadoras e pagar contas separadas pela distribuição e pelo valor da energia comprada. As vantagens incluem a liberdade de escolha entre diferentes fornecedores, flexibilidade entre fontes de energia do SIN, redução de preços devido à concorrência e um gerenciamento mais independente dos negócios.

Problematização

Considere que a sua equipe está sendo contratada por uma indústria para realizar, de forma econômica, a compra de contratos de energia para os próximos m meses (1, 2, …, m). No mercado, atuam n fornecedores de energia (1, 2, …, n) que oferecem contratos com diferentes horizontes de tempo e preços diversos. A sua equipe está encarregada em definir, uma estrutura dentre os contratos ofertados no mercado, um subconjunto que atenda de forma econômica a demanda de energia da indústria no período integral de m meses, sabendo que é possível manter contratos com diferentes fornecedores, ainda que se pague uma taxa t, paga à companhia de distribuição de energia, a cada mudança de fornecedor. Considere ainda que o consumo da empresa não varia ao longo dos meses. Assim, um contrato pode ser caracterizado por um fornecedor, um mês de início do fornecimento, um mês de fim do fornecimento e o valor do contrato.

Atividade

Dado um arquivo de entrada, implemente um algoritmo que inicialize uma matriz tridimensional que armazene os valores dos contratos de energia. A matriz deve ter as dimensões n × (m + 1) × (m + 1), onde cada elemento contratos[fornecedor][inicio][fim] representa o valor do contrato oferecido pelo fornecedor para o período do mês inicial ao mês final. Se não houver contrato específico para esse período, o valor deve ser ∞ (infinito).
