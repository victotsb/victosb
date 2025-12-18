import numpy as np
from collections import Counter

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

print("=" * 60)
print("ANÁLISE DE PADRÕES NOS NÚMEROS")
print("=" * 60)

# 1. FREQUÊNCIA DE CADA NÚMERO
todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)

freq = Counter(todos_numeros)
print("\n1. NÚMEROS MAIS FREQUENTES:")
for num, count in freq.most_common(15):
    print(f"   {num:2d}: aparece {count} vezes")

# 2. ANÁLISE DE PARES/ÍMPARES
print("\n2. DISTRIBUIÇÃO PAR/ÍMPAR POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True):
    pares = sum(1 for n in nums if n % 2 == 0)
    impares = 6 - pares
    print(f"   {ano}: {pares} pares, {impares} ímpares")

# 3. ANÁLISE POR DEZENA
print("\n3. DISTRIBUIÇÃO POR DEZENA:")
dezenas_count = {f"{i*10:02d}-{i*10+9:02d}": 0 for i in range(6)}
for num in todos_numeros:
    dezena = (num // 10) * 10
    key = f"{dezena:02d}-{dezena+9:02d}"
    dezenas_count[key] += 1

for dezena, count in sorted(dezenas_count.items()):
    print(f"   {dezena}: {count} números")

# 4. SOMA DOS NÚMEROS POR ANO
print("\n4. SOMA DOS NÚMEROS POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True):
    soma = sum(nums)
    media = soma / 6
    print(f"   {ano}: soma={soma:3d}, média={media:.1f}")

# 5. AMPLITUDE (DIFERENÇA ENTRE MAIOR E MENOR)
print("\n5. AMPLITUDE (max - min) POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True):
    amplitude = max(nums) - min(nums)
    print(f"   {ano}: {amplitude}")

# 6. NÚMEROS CONSECUTIVOS
print("\n6. PARES DE NÚMEROS CONSECUTIVOS:")
for ano, nums in sorted(dados.items(), reverse=True):
    nums_sorted = sorted(nums)
    consecutivos = []
    for i in range(len(nums_sorted)-1):
        if nums_sorted[i+1] - nums_sorted[i] == 1:
            consecutivos.append(f"{nums_sorted[i]}-{nums_sorted[i+1]}")
    if consecutivos:
        print(f"   {ano}: {', '.join(consecutivos)}")

# 7. ANÁLISE DE TERMINAÇÕES
print("\n7. TERMINAÇÕES MAIS COMUNS (último dígito):")
terminacoes = Counter([n % 10 for n in todos_numeros])
for term, count in sorted(terminacoes.items()):
    print(f"   Termina em {term}: {count} vezes")

# 8. NÚMEROS QUE NUNCA APARECERAM
print("\n8. NÚMEROS QUE NUNCA APARECERAM (assumindo range 1-60):")
todos_possiveis = set(range(1, 61))
apareceram = set(todos_numeros)
nunca_apareceram = sorted(todos_possiveis - apareceram)
print(f"   {len(nunca_apareceram)} números nunca apareceram:")
print(f"   {nunca_apareceram}")

# 9. DIFERENÇAS ENTRE NÚMEROS CONSECUTIVOS (ordenados)
print("\n9. PADRÃO DE ESPAÇAMENTO (gaps entre números ordenados):")
for ano in [2024, 2023, 2022]:  # últimos 3 anos
    nums_sorted = sorted(dados[ano])
    gaps = [nums_sorted[i+1] - nums_sorted[i] for i in range(5)]
    print(f"   {ano}: gaps = {gaps}, média = {np.mean(gaps):.1f}")

print("\n" + "=" * 60)