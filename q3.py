# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
# na linguagem que desejar, que calcule e retorne:

# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média;

import json


class Dia:
    def __init__(self, dia, valor):
        self.dia = dia
        self.valor = valor

lista_faturamento = []


def carregar_json():
    with open('dados.json') as arquivo:
        dados = json.load(arquivo)

    for dia in dados:
        dia_faturamento = Dia(dia['dia'], dia['valor'])
        lista_faturamento.append(dia_faturamento)

def menor_valor():
    """os feriados e finais de semana foram tirados da conta"""
    dia_menor_valor = lista_faturamento[0]
    for i in range(len(lista_faturamento)):
        if dia_menor_valor.valor > lista_faturamento[i].valor and lista_faturamento[i].valor != 0:
            dia_menor_valor = lista_faturamento[i]

    
    print(f'O dia de menor valor foi: {dia_menor_valor.dia} com faturameto de: {dia_menor_valor.valor}')

def maior_valor():
    dia_maior_valor = lista_faturamento[0]
    for i in range(len(lista_faturamento)):
        if dia_maior_valor.valor < lista_faturamento[i].valor:
            dia_maior_valor = lista_faturamento[i]
    
    print(f'O dia de maior valor foi: {dia_maior_valor.dia} com faturameto de: {dia_maior_valor.valor}')

def media():
    valor_media = 0
    soma = 0
    for i in range(len(lista_faturamento)):
        if lista_faturamento[i].valor != 0:
            soma += lista_faturamento[i].valor
    
    valor_media = soma/len(lista_faturamento)
    return valor_media
        

def dias_maior_media():
    qtd = 0
    for i in range(len(lista_faturamento)):
        if lista_faturamento[i].valor > media() :
            qtd += 1
    
    print(f'\nA quantidade de dias com valor superior à média mensal é: {qtd}')

######################################################################
carregar_json()
menor_valor()
maior_valor()
dias_maior_media()