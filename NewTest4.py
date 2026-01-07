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
print("ROUND 4 FINAL: OS PADRÕES MAIS OBSCUROS (40-54)")
print("=" * 80)

todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)
freq = Counter(todos_numeros)

# 40. ÍNDICE DE DIVERSIDADE DE SHANNON
print("\n40. ÍNDICE DE DIVERSIDADE DE SHANNON:")
total = len(todos_numeros)
shannon = -sum((count/total) * math.log(count/total) for count in freq.values() if count > 0)
print(f"   Índice Shannon: {shannon:.3f}")
print(f"   (Maior = mais diversidade/aleatoriedade)")

# 41. LEI DE BENFORD
print("\n41. LEI DE BENFORD (primeiro dígito):")
primeiro_digito = Counter()
for nums in dados.values():
    for num in nums:
        primeiro = int(str(num)[0])
        primeiro_digito[primeiro] += 1

print("   Dígito | Observado | Esperado Benford")
for d in range(1, 10):
    obs = primeiro_digito[d]
    benford_esperado = math.log10(1 + 1/d) * len(todos_numeros)
    desvio = "!" if abs(obs - benford_esperado) > 10 else ""
    print(f"   {d}      | {obs:3d}       | {benford_esperado:5.1f} {desvio}")

# 42. PALÍNDROMOS
print("\n42. FREQUÊNCIA DE PALÍNDROMOS (11, 22, 33, 44, 55):")
palindromos = [11, 22, 33, 44, 55]
pal_count = sum(1 for n in todos_numeros if n in palindromos)
print(f"   Total: {pal_count} ({pal_count/len(todos_numeros)*100:.1f}%)")

# 43. COMPOSTOS vs PRIMOS
def eh_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("\n43. COMPOSTOS vs PRIMOS (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    primos = sum(1 for n in nums if eh_primo(n))
    compostos = sum(1 for n in nums if n > 1 and not eh_primo(n))
    print(f"   {ano}: {primos} primos, {compostos} compostos")

# 44. DISTRIBUIÇÃO POR QUARTIS
print("\n44. DISTRIBUIÇÃO POR QUARTIS (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = dados[ano]
    q1 = sum(1 for n in nums if n <= 15)
    q2 = sum(1 for n in nums if 16 <= n <= 30)
    q3 = sum(1 for n in nums if 31 <= n <= 45)
    q4 = sum(1 for n in nums if n >= 46)
    print(f"   {ano}: Q1={q1} Q2={q2} Q3={q3} Q4={q4}")

# 45. COEFICIENTE DE ASSIMETRIA (Skewness)
print("\n45. COEFICIENTE DE ASSIMETRIA (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    media = np.mean(nums)
    desvio = np.std(nums)
    n = len(nums)
    skew = sum((x - media)**3 for x in nums) / (n * desvio**3) if desvio > 0 else 0
    direcao = "direita" if skew > 0.2 else "esquerda" if skew < -0.2 else "simétrico"
    print(f"   {ano}: skew={skew:+.2f} ({direcao})")

# 46. CURTOSE
print("\n46. CURTOSE (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = dados[ano]
    media = np.mean(nums)
    desvio = np.std(nums)
    n = len(nums)
    kurt = sum((x - media)**4 for x in nums) / (n * desvio**4) - 3 if desvio > 0 else 0
    tipo = "lepto" if kurt > 0 else "plati"
    print(f"   {ano}: curtose={kurt:+.2f} ({tipo}cúrtica)")

# 47. RANGE INTERQUARTIL
print("\n47. RANGE INTERQUARTIL (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = sorted(dados[ano])
    q1 = np.percentile(nums, 25)
    q3 = np.percentile(nums, 75)
    iqr = q3 - q1
    print(f"   {ano}: Q1={q1:.1f}, Q3={q3:.1f}, IQR={iqr:.1f}")

# 48. SOMA DE DÍGITOS = 10
print("\n48. NÚMEROS COM SOMA DE DÍGITOS = 10:")
for ano in sorted(dados.keys(), reverse=True):
    soma10 = [n for n in dados[ano] if sum(int(d) for d in str(n)) == 10]
    if soma10:
        print(f"   {ano}: {soma10}")

# 49. NÚMEROS ADJACENTES
print("\n49. NÚMEROS ADJACENTES (diferença = 1):")
total_adj = 0
for ano in sorted(dados.keys(), reverse=True):
    nums = sorted(dados[ano])
    adjacentes = []
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            adjacentes.append(f"{nums[i]}-{nums[i+1]}")
            total_adj += 1
    if adjacentes:
        print(f"   {ano}: {', '.join(adjacentes)}")
print(f"   TOTAL: {total_adj} pares em 17 anos ({total_adj/17*100:.1f}%)")

# 50. TESTE DE RUNS
print("\n50. TESTE DE RUNS (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = sorted(dados[ano])
    sequencia = ''.join(['P' if n % 2 == 0 else 'I' for n in nums])
    runs = 1
    for i in range(1, len(sequencia)):
        if sequencia[i] != sequencia[i-1]:
            runs += 1
    print(f"   {ano}: {sequencia}, runs={runs}")

# 51. NÚMEROS TRIANGULARES
print("\n51. NÚMEROS TRIANGULARES (1, 3, 6, 10, 15, 21, 28, 36, 45, 55):")
triangulares = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
for ano in sorted(dados.keys(), reverse=True):
    tri = [n for n in dados[ano] if n in triangulares]
    if tri:
        print(f"   {ano}: {tri}")

# 52. DISTÂNCIA EUCLIDIANA
print("\n52. DISTÂNCIA EUCLIDIANA ENTRE ANOS:")
anos_ord = sorted(dados.keys())
for i in range(len(anos_ord)-1):
    ano1, ano2 = anos_ord[i], anos_ord[i+1]
    nums1, nums2 = sorted(dados[ano1]), sorted(dados[ano2])
    dist = math.sqrt(sum((a-b)**2 for a, b in zip(nums1, nums2)))
    print(f"   {ano1}→{ano2}: distância={dist:.1f}")

# 53. CORRELAÇÃO POSIÇÃO-VALOR
print("\n53. CORRELAÇÃO POSIÇÃO-VALOR (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = sorted(dados[ano])
    posicoes = list(range(1, 7))
    corr = np.corrcoef(posicoes, nums)[0, 1]
    print(f"   {ano}: correlação={corr:.3f}")

# 54. POTÊNCIAS DE 2
print("\n54. POTÊNCIAS DE 2 (2, 4, 8, 16, 32):")
potencias2 = [2, 4, 8, 16, 32]
for ano in sorted(dados.keys(), reverse=True):
    pot = [n for n in dados[ano] if n in potencias2]
    if pot:
        print(f"   {ano}: {pot}")

print("\n" + "="*80)
print("🎯 ANÁLISE COMPLETA FINALIZADA - 54 PADRÕES TESTADOS!")
print("="*80)
print("\nRESUMO:")
print("- Dataset: 17 anos (2008-2025)")
print("- Total de números sorteados: 102")
print("- Padrões analisados: 54")
print("\nAgora você pode testar cada padrão e verificar o que mudou com 2025!")
print("="*80)