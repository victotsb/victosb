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
print("ANÁLISE COMPLETA MEGA DA VIRADA 2008-2025 (17 ANOS)")
print("TESTANDO TODOS OS 54 PADRÕES")
print("=" * 80)

todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)

freq = Counter(todos_numeros)

# ============================================================================
# ROUND 1: PADRÕES BÁSICOS (1-12)
# ============================================================================
print("\n" + "="*80)
print("ROUND 1: PADRÕES BÁSICOS (1-12)")
print("="*80)

# 1. NÚMEROS MAIS FREQUENTES
print("\n1. NÚMEROS MAIS FREQUENTES:")
for num, count in freq.most_common(15):
    print(f"   {num:2d}: aparece {count} vezes")

# 2. DISTRIBUIÇÃO PAR/ÍMPAR
print("\n2. DISTRIBUIÇÃO PAR/ÍMPAR POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True):
    pares = sum(1 for n in nums if n % 2 == 0)
    impares = 6 - pares
    print(f"   {ano}: {pares} pares, {impares} ímpares")

# Análise última tendência
print("\n   ANÁLISE TENDÊNCIA (últimos 5 anos):")
ultimos_5 = sorted(dados.keys(), reverse=True)[:5]
total_pares = sum(sum(1 for n in dados[ano] if n % 2 == 0) for ano in ultimos_5)
total_impares = 30 - total_pares
print(f"   Total: {total_pares} pares, {total_impares} ímpares")
print(f"   Média: {total_pares/5:.1f} pares, {total_impares/5:.1f} ímpares por ano")

# 3. DISTRIBUIÇÃO POR DEZENA
print("\n3. DISTRIBUIÇÃO POR DEZENA:")
dezenas_count = {f"{i*10:02d}-{min(i*10+9, 60):02d}": 0 for i in range(6)}
for num in todos_numeros:
    if num == 60:
        dezena = 50
    else:
        dezena = (num // 10) * 10
    key = f"{dezena:02d}-{min(dezena+9, 60):02d}"
    dezenas_count[key] += 1
for dezena, count in sorted(dezenas_count.items()):
    print(f"   {dezena}: {count} números")

# 4. SOMA DOS NÚMEROS POR ANO
print("\n4. SOMA DOS NÚMEROS POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True):
    soma = sum(nums)
    media = soma / 6
    print(f"   {ano}: soma={soma:3d}, média={media:.1f}")

# 5. AMPLITUDE
print("\n5. AMPLITUDE (max - min) POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True)[:10]:
    amplitude = max(nums) - min(nums)
    print(f"   {ano}: {amplitude}")

# 6. NÚMEROS CONSECUTIVOS
print("\n6. PARES DE NÚMEROS CONSECUTIVOS:")
total_consecutivos = 0
for ano, nums in sorted(dados.items(), reverse=True):
    nums_sorted = sorted(nums)
    consecutivos = []
    for i in range(len(nums_sorted)-1):
        if nums_sorted[i+1] - nums_sorted[i] == 1:
            consecutivos.append(f"{nums_sorted[i]}-{nums_sorted[i+1]}")
            total_consecutivos += 1
    if consecutivos:
        print(f"   {ano}: {', '.join(consecutivos)}")
print(f"   TOTAL: {total_consecutivos} pares em 17 anos ({total_consecutivos/17*100:.1f}% dos anos)")

# 7. TERMINAÇÕES
print("\n7. TERMINAÇÕES MAIS COMUNS (último dígito):")
terminacoes = Counter([n % 10 for n in todos_numeros])
for term, count in sorted(terminacoes.items()):
    print(f"   Termina em {term}: {count} vezes")

# 8. NÚMEROS QUE NUNCA APARECERAM
print("\n8. NÚMEROS QUE NUNCA APARECERAM:")
todos_possiveis = set(range(1, 61))
apareceram = set(todos_numeros)
nunca_apareceram = sorted(todos_possiveis - apareceram)
print(f"   {len(nunca_apareceram)} números nunca apareceram:")
print(f"   {nunca_apareceram}")

# 9. PADRÃO DE GAPS
print("\n9. PADRÃO DE ESPAÇAMENTO (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums_sorted = sorted(dados[ano])
    gaps = [nums_sorted[i+1] - nums_sorted[i] for i in range(5)]
    print(f"   {ano}: gaps = {gaps}, média = {np.mean(gaps):.1f}")

# 10. PARES DE NÚMEROS QUE APARECEM JUNTOS
print("\n10. PARES MAIS FREQUENTES:")
pares_freq = Counter()
for nums in dados.values():
    for par in combinations(nums, 2):
        pares_freq[tuple(sorted(par))] += 1
for par, count in pares_freq.most_common(10):
    if count > 1:
        print(f"   {par[0]:2d}-{par[1]:2d}: {count} vezes")

# 11. NÚMEROS 'QUENTES' (últimos 5 anos)
print("\n11. NÚMEROS 'QUENTES' (últimos 5 anos):")
ultimos_5_nums = []
for ano in sorted(dados.keys(), reverse=True)[:5]:
    ultimos_5_nums.extend(dados[ano])
freq_recente = Counter(ultimos_5_nums)
print("   Top 10:")
for num, count in freq_recente.most_common(10):
    print(f"   {num:2d}: {count} vezes")

# 12. ANÁLISE DE PRIMOS
def eh_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("\n12. NÚMEROS PRIMOS vs NÃO-PRIMOS (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = dados[ano]
    primos = sum(1 for n in nums if eh_primo(n))
    print(f"   {ano}: {primos} primos, {6-primos} não-primos")

print("\n" + "="*80)
print("ROUND 1 COMPLETO - Continue para ver Round 2...")
print("="*80)