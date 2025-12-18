import numpy as np
from collections import Counter, defaultdict
from itertools import combinations, permutations
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
print("ANÁLISE EXAUSTIVA - ROUND 4 FINAL: OS PADRÕES MAIS OBSCUROS")
print("=" * 75)

# 40. ÍNDICE DE DIVERSIDADE DE SHANNON (ecologia aplicada a loteria!)
print("\n40. ÍNDICE DE DIVERSIDADE DE SHANNON:")
todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)
freq = Counter(todos_numeros)
total = len(todos_numeros)
shannon = -sum((count/total) * math.log(count/total) for count in freq.values() if count > 0)
print(f"   Índice Shannon: {shannon:.3f}")
print(f"   (Maior = mais diversidade/aleatoriedade)")

# 41. TESTE DE BENFORD (primeira lei de Benford)
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
    print(f"   {d}      | {obs:3d}       | {benford_esperado:5.1f}")

# 42. NÚMEROS PALÍNDROMOS (11, 22, 33, 44, 55)
print("\n42. FREQUÊNCIA DE PALÍNDROMOS:")
palindromos = [11, 22, 33, 44, 55]
pal_count = sum(1 for n in todos_numeros if n in palindromos)
print(f"   Total de palíndromos: {pal_count}")
print(f"   Frequência: {pal_count/len(todos_numeros)*100:.1f}%")

# 43. NÚMEROS COMPOSTOS vs PRIMOS
print("\n43. ANÁLISE COMPOSTOS vs PRIMOS (últimos 8 anos):")
def eh_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    primos = sum(1 for n in nums if eh_primo(n))
    compostos = sum(1 for n in nums if n > 1 and not eh_primo(n))
    print(f"   {ano}: {primos} primos, {compostos} compostos, {6-primos-compostos} especiais (0,1)")

# 44. QUARTIS (distribuição em 4 partes)
print("\n44. DISTRIBUIÇÃO POR QUARTIS:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    q1 = sum(1 for n in nums if n <= 15)
    q2 = sum(1 for n in nums if 16 <= n <= 30)
    q3 = sum(1 for n in nums if 31 <= n <= 45)
    q4 = sum(1 for n in nums if n >= 46)
    print(f"   {ano}: Q1={q1} Q2={q2} Q3={q3} Q4={q4}")

# 45. COEFICIENTE DE ASSIMETRIA (Skewness)
print("\n45. COEFICIENTE DE ASSIMETRIA (Skewness):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    media = np.mean(nums)
    desvio = np.std(nums)
    n = len(nums)
    skew = sum((x - media)**3 for x in nums) / (n * desvio**3) if desvio > 0 else 0
    print(f"   {ano}: skew={skew:+.2f} ({'direita' if skew > 0 else 'esquerda' if skew < 0 else 'simétrico'})")

# 46. CURTOSE (achatamento da distribuição)
print("\n46. CURTOSE (forma da distribuição):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    media = np.mean(nums)
    desvio = np.std(nums)
    n = len(nums)
    kurt = sum((x - media)**4 for x in nums) / (n * desvio**4) - 3 if desvio > 0 else 0
    print(f"   {ano}: curtose={kurt:+.2f} ({'leptocúrtica' if kurt > 0 else 'platicúrtica'})")

# 47. RANGE INTERQUARTIL
print("\n47. RANGE INTERQUARTIL (IQR):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    nums_sorted = sorted(nums)
    q1 = np.percentile(nums_sorted, 25)
    q3 = np.percentile(nums_sorted, 75)
    iqr = q3 - q1
    print(f"   {ano}: Q1={q1:.1f}, Q3={q3:.1f}, IQR={iqr:.1f}")

# 48. NÚMEROS COM SOMA DE DÍGITOS ESPECÍFICA
print("\n48. SOMA DE DÍGITOS = 10 (numerologia):")
for ano, nums in sorted(dados.items(), reverse=True):
    soma10 = [n for n in nums if sum(int(d) for d in str(n)) == 10]
    if soma10:
        print(f"   {ano}: {soma10}")

# 49. PADRÃO DE VIZINHANÇA (números adjacentes no cartão)
print("\n49. NÚMEROS ADJACENTES (diferença = 1):")
total_adjacentes = 0
for ano, nums in sorted(dados.items(), reverse=True):
    nums_sorted = sorted(nums)
    adjacentes = []
    for i in range(len(nums_sorted)-1):
        if nums_sorted[i+1] - nums_sorted[i] == 1:
            adjacentes.append(f"{nums_sorted[i]}-{nums_sorted[i+1]}")
    if adjacentes:
        print(f"   {ano}: {', '.join(adjacentes)}")
        total_adjacentes += len(adjacentes)
print(f"   Total de pares adjacentes em 16 anos: {total_adjacentes}")

# 50. TESTE DE ALEATORIEDADE (Runs Test simplificado)
print("\n50. TESTE DE RUNS (aleatoriedade de par/ímpar):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    nums_sorted = sorted(nums)
    sequencia = ''.join(['P' if n % 2 == 0 else 'I' for n in nums_sorted])
    runs = 1
    for i in range(1, len(sequencia)):
        if sequencia[i] != sequencia[i-1]:
            runs += 1
    print(f"   {ano}: {sequencia}, runs={runs} (ideal=3-4)")

# 51. NÚMEROS TRIANGULARES (1, 3, 6, 10, 15, 21, 28, 36, 45, 55)
print("\n51. NÚMEROS TRIANGULARES:")
triangulares = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
for ano, nums in sorted(dados.items(), reverse=True):
    tri = [n for n in nums if n in triangulares]
    if tri:
        print(f"   {ano}: {tri}")

# 52. DISTÂNCIA EUCLIDIANA ENTRE ANOS CONSECUTIVOS
print("\n52. DISTÂNCIA EUCLIDIANA ENTRE ANOS (similaridade):")
anos_ord = sorted(dados.keys())
for i in range(len(anos_ord)-1):
    ano1, ano2 = anos_ord[i], anos_ord[i+1]
    nums1, nums2 = sorted(dados[ano1]), sorted(dados[ano2])
    dist = math.sqrt(sum((a-b)**2 for a, b in zip(nums1, nums2)))
    print(f"   {ano1}→{ano2}: distância={dist:.1f}")

# 53. COEFICIENTE DE CORRELAÇÃO (entre posição e valor)
print("\n53. CORRELAÇÃO POSIÇÃO-VALOR (números crescem uniformemente?):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    nums_sorted = sorted(nums)
    posicoes = list(range(1, 7))
    corr = np.corrcoef(posicoes, nums_sorted)[0, 1]
    print(f"   {ano}: correlação={corr:.3f} (1=linear perfeito)")

# 54. NÚMEROS POTÊNCIAS DE 2 (2, 4, 8, 16, 32)
print("\n54. POTÊNCIAS DE 2:")
potencias2 = [2, 4, 8, 16, 32]
for ano, nums in sorted(dados.items(), reverse=True):
    pot = [n for n in nums if n in potencias2]
    if pot:
        print(f"   {ano}: {pot}")

print("\n" + "=" * 75)
print("🎯 ANÁLISE COMPLETA FINALIZADA! 🎯")
print("=" * 75)
print(f"TOTAL: 54 PADRÕES DIFERENTES ANALISADOS")
print()
print("CONCLUSÃO DEFINITIVA:")
print("- Alguns padrões aparecem por pura variância estatística")
print("- NENHUM tem valor preditivo real para o próximo sorteio")
print("- A aleatoriedade é robusta e bem distribuída")
print("- Qualquer 'padrão' encontrado é coincidência ou ruído")
print()
print("💡 INSIGHT: Se houvesse um padrão explorável, a Caixa já teria")
print("   corrigido o sistema há décadas. Bilhões estão em jogo.")
print("=" * 75)