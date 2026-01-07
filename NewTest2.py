import numpy as np
from collections import Counter, defaultdict
from itertools import combinations
import math

# Dados atualizados com 2025
dados = {
    2025: [9, 13, 21, 32, 33, 59],
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
    2009: [10, 27, 40, 46, 49, 58],
    2008: [1, 11, 26, 51, 59, 60]
}

print("=" * 80)
print("ROUND 2: PADRÕES ESTATÍSTICOS AVANÇADOS (13-24)")
print("=" * 80)

todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)

freq = Counter(todos_numeros)

# 13. TESTE DE UNIFORMIDADE (Chi-Quadrado)
print("\n13. TESTE DE UNIFORMIDADE DE DISTRIBUIÇÃO:")
frequencia_esperada = len(todos_numeros) / 60
chi_quad = sum((count - frequencia_esperada)**2 / frequencia_esperada for count in freq.values())
print(f"   Chi-quadrado calculado: {chi_quad:.2f}")
print(f"   Frequência esperada por número: {frequencia_esperada:.2f}")
print(f"   (Valores baixos = distribuição mais uniforme)")

# 14. ENTROPIA
print("\n14. ENTROPIA DA DISTRIBUIÇÃO:")
total = len(todos_numeros)
entropia = -sum((count/total) * math.log2(count/total) for count in freq.values() if count > 0)
entropia_max = math.log2(60)
print(f"   Entropia observada: {entropia:.3f}")
print(f"   Entropia máxima (aleatoriedade perfeita): {entropia_max:.3f}")
print(f"   Percentual de aleatoriedade: {(entropia/entropia_max)*100:.1f}%")

# 15. ANÁLISE DE RUNS
print("\n15. ANÁLISE DE RUNS (sequências par/ímpar) - últimos 5 anos:")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = sorted(dados[ano])
    runs = []
    current_run = nums[0] % 2
    run_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] % 2 == current_run:
            run_length += 1
        else:
            runs.append(run_length)
            current_run = nums[i] % 2
            run_length = 1
    runs.append(run_length)
    print(f"   {ano}: runs = {runs} (alternância = {len(runs)} vezes)")

# 16. CORRELAÇÃO TEMPORAL
print("\n16. CORRELAÇÃO TEMPORAL - 2008-2016 vs 2017-2025:")
periodo1 = []
periodo2 = []
for ano, nums in dados.items():
    if ano <= 2016:
        periodo1.extend(nums)
    else:
        periodo2.extend(nums)

freq1 = Counter(periodo1)
freq2 = Counter(periodo2)

print("   Top 5 período 2008-2016:")
for num, count in freq1.most_common(5):
    print(f"   {num:2d}: {count} vezes")

print("   Top 5 período 2017-2025:")
for num, count in freq2.most_common(5):
    print(f"   {num:2d}: {count} vezes")

# 17. DISTÂNCIA MÉDIA ENTRE NÚMEROS
print("\n17. DISTÂNCIA MÉDIA ENTRE NÚMEROS (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = sorted(dados[ano])
    distancias = [nums[i+1] - nums[i] for i in range(5)]
    media_dist = np.mean(distancias)
    print(f"   {ano}: média = {media_dist:.1f}, range = [{min(distancias)}, {max(distancias)}]")

# 18. NÚMEROS COM DÍGITOS REPETIDOS
print("\n18. NÚMEROS COM DÍGITOS REPETIDOS (11, 22, 33, 44, 55):")
repetidos = [11, 22, 33, 44, 55]
for ano in sorted(dados.keys(), reverse=True):
    match = [n for n in dados[ano] if n in repetidos]
    if match:
        print(f"   {ano}: {match}")

# 19. RAZÃO MAX/MIN
print("\n19. RAZÃO MAX/MIN POR ANO (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    razao = max(nums) / min(nums) if min(nums) != 0 else 0
    print(f"   {ano}: {max(nums)}/{min(nums)} = {razao:.2f}")

# 20. TENDÊNCIA DA SOMA TOTAL
print("\n20. TENDÊNCIA DA SOMA TOTAL:")
anos = sorted(dados.keys())
somas = [sum(dados[ano]) for ano in anos]
print("   Ano  | Soma")
for ano, soma in zip(anos, somas):
    print(f"   {ano}: {soma}")
dif_soma = somas[-1] - somas[0]
print(f"   Diferença 2008→2025: {dif_soma:+d}")

# 21. NÚMEROS EM ANOS SEGUIDOS
print("\n21. NÚMEROS QUE SAÍRAM EM ANOS CONSECUTIVOS:")
anos_ord = sorted(dados.keys())
repeticoes_totais = 0
for i in range(len(anos_ord) - 1):
    ano1, ano2 = anos_ord[i], anos_ord[i+1]
    nums1, nums2 = set(dados[ano1]), set(dados[ano2])
    intersecao = nums1 & nums2
    if len(intersecao) >= 1:
        print(f"   {ano1}→{ano2}: {len(intersecao)} repetidos: {sorted(intersecao)}")
        repeticoes_totais += len(intersecao)
print(f"   TOTAL: {repeticoes_totais} repetições em 16 transições")

# 22. NÚMEROS AQUECENDO
print("\n22. NÚMEROS COM TENDÊNCIA CRESCENTE (últimos 3 vs primeiros 3):")
ultimos3 = []
for ano in sorted(dados.keys(), reverse=True)[:3]:
    ultimos3.extend(dados[ano])
freq_ultimos3 = Counter(ultimos3)

primeiros3 = []
for ano in sorted(dados.keys())[:3]:
    primeiros3.extend(dados[ano])
freq_primeiros3 = Counter(primeiros3)

aquecendo = []
for num in range(1, 61):
    if freq_ultimos3[num] > freq_primeiros3[num]:
        aquecendo.append((num, freq_ultimos3[num], freq_primeiros3[num]))

print("   Top 10 números 'aquecendo':")
for num, freq_rec, freq_ant in sorted(aquecendo, key=lambda x: x[1]-x[2], reverse=True)[:10]:
    print(f"   {num:2d}: {freq_ant}→{freq_rec} (Δ+{freq_rec-freq_ant})")

# 23. FREQUÊNCIA DE EXTREMOS
print("\n23. FREQUÊNCIA DE EXTREMOS (1-10 e 51-60) - últimos 8 anos:")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    extremos_baixos = sum(1 for n in nums if 1 <= n <= 10)
    extremos_altos = sum(1 for n in nums if 51 <= n <= 60)
    print(f"   {ano}: {extremos_baixos} baixos (1-10), {extremos_altos} altos (51-60)")

# 24. COEFICIENTE DE VARIAÇÃO
print("\n24. COEFICIENTE DE VARIAÇÃO (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = dados[ano]
    media = np.mean(nums)
    desvio = np.std(nums)
    cv = (desvio / media) * 100
    print(f"   {ano}: CV = {cv:.1f}%")

print("\n" + "="*80)
print("ROUND 2 COMPLETO - 24 padrões analisados até agora")
print("Continue para Round 3...")
print("="*80)