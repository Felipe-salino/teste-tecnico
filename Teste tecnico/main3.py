#exercico 3 usando o dados.json

import json

with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)

dias_com_faturamento = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0.0]
menor_faturamento = min(dias_com_faturamento)
maior_faturamento = max(dias_com_faturamento)
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
