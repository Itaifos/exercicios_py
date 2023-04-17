# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado 
# teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

valor_total = sp + rj + mg + es + outros

porcentagem_sp = sp*100/valor_total
porcentagem_rj = rj*100/valor_total
porcentagem_mg = mg*100/valor_total
porcentagem_es = es*100/valor_total

print(f'o porcentagem do estado SP no faturamento é de: {porcentagem_sp:.2f}%')
print(f'o porcentagem do estado RJ no faturamento é de: {porcentagem_rj:.2f}%')
print(f'o porcentagem do estado MG no faturamento é de: {porcentagem_mg:.2f}%')
print(f'o porcentagem do estado ES no faturamento é de: {porcentagem_es:.2f}%')

