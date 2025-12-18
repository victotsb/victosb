import numpy as np
from collections import Counter, defaultdict
from itertools import combinations
import math

# Dados organizados
dados = {
    2024: [1, 17, 19, 29, 50, 57],
    2023: [21, 24, 33, 41, 48, 56],
    2022: [4, 5, 10, 34, 58, 59],
    2021: [12, 15, 23, 32, 33, 46],
    2020: [17, 20, 22, 35, 41, 42],
    2019: [3, 35, 38, 40, 57, 58],
    2018: [5, 10, 12, 18, 25, 33],
    2017: [3, 6, 10, 17, 34, 37],
    2016: [5, 11, 22, 24, 51, 53],
    2015: [2, 18, 31, 42, 51, 56],
    2014: [1, 5, 11, 16, 20, 56],
    2013: [20, 30, 36, 38, 47, 53],
    2012: [14, 32, 33, 36, 41, 52],
    2011: [3, 4, 29, 36, 45, 55],
    2010: [2, 10, 34, 37, 43, 50],
    2009: [10, 27, 40, 46, 49, 58]
}

print("=" * 75)
print("ANÁLISE EXAUSTIVA - ROUND 2: PADRÕES MATEMÁTICOS E ESTATÍSTICOS")
print("=" * 75)

# 13. TESTE DE UNIFORMIDADE (Chi-Quadrado simplificado)
print("\n13. TESTE DE UNIFORMIDADE DE DISTRIBUIÇÃO:")
todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)

freq = Counter(todos_numeros)
frequencia_esperada = len(todos_numeros) / 60
chi_quad = sum((count - frequencia_esperada)**2 / frequencia_esperada for count in freq.values())
print(f"   Chi-quadrado calculado: {chi_quad:.2f}")
print(f"   (Valores baixos = distribuição mais uniforme)")
print(f"   Frequência esperada por número: {frequencia_esperada:.2f}")

# 14. ENTROPIA (medida de aleatoriedade)
print("\n14. ENTROPIA DA DISTRIBUIÇÃO:")
total = len(todos_numeros)
entropia = -sum((count/total) * math.log2(count/total) for count in freq.values() if count > 0)
entropia_max = math.log2(60)
print(f"   Entropia observada: {entropia:.3f}")
print(f"   Entropia máxima (perfeita aleatoriedade): {entropia_max:.3f}")
print(f"   Percentual de aleatoriedade: {(entropia/entropia_max)*100:.1f}%")

# 15. ANÁLISE DE RUNS (sequências de pares ou ímpares)
print("\n15. ANÁLISE DE RUNS (sequências par/ímpar):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    nums_sorted = sorted(nums)
    runs = []
    current_run = nums_sorted[0] % 2
    run_length = 1
    
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] % 2 == current_run:
            run_length += 1
        else:
            runs.append(run_length)
            current_run = nums_sorted[i] % 2
            run_length = 1
    runs.append(run_length)
    print(f"   {ano}: runs = {runs} (alternância = {len(runs)} vezes)")

# 16. CORRELAÇÃO TEMPORAL (números saem mais em certos períodos?)
print("\n16. CORRELAÇÃO TEMPORAL - Anos 2009-2014 vs 2015-2024:")
periodo1 = []
periodo2 = []
for ano, nums in dados.items():
    if ano <= 2014:
        periodo1.extend(nums)
    else:
        periodo2.extend(nums)

freq1 = Counter(periodo1)
freq2 = Counter(periodo2)

print("   Top 5 no período 2009-2014:")
for num, count in freq1.most_common(5):
    print(f"   {num:2d}: {count} vezes")

print("   Top 5 no período 2015-2024:")
for num, count in freq2.most_common(5):
    print(f"   {num:2d}: {count} vezes")

# 17. DISTÂNCIA MÉDIA ENTRE NÚMEROS
print("\n17. DISTÂNCIA MÉDIA ENTRE NÚMEROS CONSECUTIVOS (ordenados):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    nums_sorted = sorted(nums)
    distancias = [nums_sorted[i+1] - nums_sorted[i] for i in range(5)]
    media_dist = np.mean(distancias)
    print(f"   {ano}: média = {media_dist:.1f}, range = [{min(distancias)}, {max(distancias)}]")

# 18. NÚMEROS COM DÍGITOS REPETIDOS
print("\n18. NÚMEROS COM DÍGITOS REPETIDOS (11, 22, 33, 44, 55):")
repetidos = [11, 22, 33, 44, 55]
for ano, nums in sorted(dados.items(), reverse=True):
    match = [n for n in nums if n in repetidos]
    if match:
        print(f"   {ano}: {match}")

# 19. RAZÃO ENTRE MAIOR E MENOR
print("\n19. RAZÃO MAX/MIN POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    razao = max(nums) / min(nums) if min(nums) != 0 else 0
    print(f"   {ano}: {max(nums)}/{min(nums)} = {razao:.2f}")

# 20. SOMA ACUMULADA (números crescem ou decrescem ao longo dos anos?)
print("\n20. TENDÊNCIA DA SOMA TOTAL AO LONGO DOS ANOS:")
anos = sorted(dados.keys())
somas = [sum(dados[ano]) for ano in anos]
print("   Ano | Soma")
for ano, soma in zip(anos, somas):
    print(f"   {ano}: {soma}")

# Calcular tendência simples
dif_soma = somas[-1] - somas[0]
print(f"   Diferença 2009→2024: {dif_soma:+d}")

# 21. NÚMEROS QUE APARECEM EM SEQUÊNCIA DE ANOS
print("\n21. NÚMEROS QUE SAÍRAM 2+ ANOS SEGUIDOS:")
anos_ord = sorted(dados.keys())
for i in range(len(anos_ord) - 1):
    ano1, ano2 = anos_ord[i], anos_ord[i+1]
    nums1, nums2 = set(dados[ano1]), set(dados[ano2])
    intersecao = nums1 & nums2
    if len(intersecao) >= 2:
        print(f"   {ano1}-{ano2}: {sorted(intersecao)}")

# 22. MÉDIA MÓVEL (tendência de certos números)
print("\n22. NÚMEROS COM TENDÊNCIA CRESCENTE (últimos 3 anos mais frequentes):")
ultimos3 = []
for ano in sorted(dados.keys(), reverse=True)[:3]:
    ultimos3.extend(dados[ano])
freq_ultimos3 = Counter(ultimos3)

primeiros3 = []
for ano in sorted(dados.keys())[:3]:
    primeiros3.extend(dados[ano])
freq_primeiros3 = Counter(primeiros3)

print("   Números 'aquecendo' (mais nos últimos 3 que nos primeiros 3):")
aquecendo = []
for num in range(1, 61):
    if freq_ultimos3[num] > freq_primeiros3[num]:
        aquecendo.append((num, freq_ultimos3[num], freq_primeiros3[num]))

for num, freq_rec, freq_ant in sorted(aquecendo, key=lambda x: x[1]-x[2], reverse=True)[:10]:
    print(f"   {num:2d}: {freq_ant}→{freq_rec} (Δ+{freq_rec-freq_ant})")

# 23. NÚMEROS EXTREMOS (muito baixos ou muito altos)
print("\n23. FREQUÊNCIA DE EXTREMOS (1-10 e 51-60):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    extremos_baixos = sum(1 for n in nums if 1 <= n <= 10)
    extremos_altos = sum(1 for n in nums if 51 <= n <= 60)
    print(f"   {ano}: {extremos_baixos} baixos (1-10), {extremos_altos} altos (51-60)")

# 24. COEFICIENTE DE VARIAÇÃO
print("\n24. COEFICIENTE DE VARIAÇÃO (dispersão relativa):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    media = np.mean(nums)
    desvio = np.std(nums)
    cv = (desvio / media) * 100
    print(f"   {ano}: CV = {cv:.1f}%")

print("\n" + "=" * 75)
print("STATUS: ROUND 2 COMPLETO - 24 PADRÕES ANALISADOS ATÉ AGORA")
print("Continuando na próxima rodada...")
print("=" * 75)