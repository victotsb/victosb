import numpy as np
from collections import Counter, defaultdict
from itertools import combinations

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

print("=" * 70)
print("ANÁLISE AVANÇADA DE PADRÕES - MEGA DA VIRADA")
print("=" * 70)

# 1. ANÁLISE DE PARES (duplas que saem juntas)
print("\n1. PARES DE NÚMEROS QUE APARECEM JUNTOS:")
pares_freq = Counter()
for nums in dados.values():
    for par in combinations(nums, 2):
        pares_freq[tuple(sorted(par))] += 1

print("   Top 10 pares mais frequentes:")
for par, count in pares_freq.most_common(10):
    if count > 1:
        print(f"   {par[0]:2d}-{par[1]:2d}: {count} vezes")

# 2. ANÁLISE DE TRIOS
print("\n2. TRIOS DE NÚMEROS QUE APARECEM JUNTOS:")
trios_freq = Counter()
for nums in dados.values():
    for trio in combinations(nums, 3):
        trios_freq[tuple(sorted(trio))] += 1

print("   Trios que apareceram mais de 1 vez:")
trios_repetidos = [(trio, count) for trio, count in trios_freq.items() if count > 1]
if trios_repetidos:
    for trio, count in sorted(trios_repetidos, key=lambda x: x[1], reverse=True)[:5]:
        print(f"   {trio}: {count} vezes")
else:
    print("   Nenhum trio se repetiu (esperado em dados aleatórios)")

# 3. ANÁLISE DE SEQUÊNCIAS (padrões tipo 1-2-3 ou espaçamento regular)
print("\n3. ANÁLISE DE SEQUÊNCIAS E PROGRESSÕES:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    nums_sorted = sorted(nums)
    diferencas = [nums_sorted[i+1] - nums_sorted[i] for i in range(5)]
    
    # Verificar se há padrão aritmético
    if len(set(diferencas)) == 1:
        print(f"   {ano}: PROGRESSÃO ARITMÉTICA! Gaps = {diferencas}")
    elif max(diferencas) - min(diferencas) <= 3:
        print(f"   {ano}: Gaps quase uniformes = {diferencas}")

# 4. NÚMEROS "QUENTES" vs "FRIOS" (últimos 5 anos)
print("\n4. NÚMEROS 'QUENTES' (mais frequentes últimos 5 anos):")
ultimos_5 = []
for ano in sorted(dados.keys(), reverse=True)[:5]:
    ultimos_5.extend(dados[ano])

freq_recente = Counter(ultimos_5)
print("   Top 10 'quentes':")
for num, count in freq_recente.most_common(10):
    print(f"   {num:2d}: {count} vezes")

print("\n5. NÚMEROS 'FRIOS' (não saíram nos últimos 5 anos):")
saiu_recente = set(ultimos_5)
todos_possiveis = set(range(1, 61))
frios = sorted(todos_possiveis - saiu_recente)
print(f"   {len(frios)} números frios: {frios[:20]}...")

# 6. ANÁLISE DE PRIMOS
def eh_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("\n6. NÚMEROS PRIMOS vs NÃO-PRIMOS:")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    primos = sum(1 for n in nums if eh_primo(n))
    print(f"   {ano}: {primos} primos, {6-primos} não-primos")

# 7. SOMA DOS DÍGITOS (numerologia básica)
print("\n7. ANÁLISE DA SOMA DOS DÍGITOS:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    soma_digitos = sum(sum(int(d) for d in str(n)) for n in nums)
    print(f"   {ano}: soma dos dígitos = {soma_digitos}")

# 8. QUADRANTES (dividindo 1-60 em 4 partes)
print("\n8. DISTRIBUIÇÃO POR QUADRANTES:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    q1 = sum(1 for n in nums if 1 <= n <= 15)
    q2 = sum(1 for n in nums if 16 <= n <= 30)
    q3 = sum(1 for n in nums if 31 <= n <= 45)
    q4 = sum(1 for n in nums if 46 <= n <= 60)
    print(f"   {ano}: Q1={q1} Q2={q2} Q3={q3} Q4={q4}")

# 9. NÚMEROS REPETIDOS DE ANOS ANTERIORES
print("\n9. REPETIÇÃO DO ANO ANTERIOR:")
anos_ordenados = sorted(dados.keys())
for i in range(1, len(anos_ordenados)):
    ano_atual = anos_ordenados[i]
    ano_anterior = anos_ordenados[i-1]
    nums_atual = set(dados[ano_atual])
    nums_anterior = set(dados[ano_anterior])
    repeticoes = nums_atual & nums_anterior
    if repeticoes:
        print(f"   {ano_anterior}→{ano_atual}: {len(repeticoes)} repetidos: {sorted(repeticoes)}")

# 10. ANÁLISE DE VARIÂNCIA (dispersão dos números)
print("\n10. DISPERSÃO DOS NÚMEROS (desvio padrão):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    desvio = np.std(nums)
    print(f"   {ano}: desvio padrão = {desvio:.1f}")

# 11. PADRÃO DE MÚLTIPLOS
print("\n11. MÚLTIPLOS DE 5 e 10:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    mult_5 = sum(1 for n in nums if n % 5 == 0)
    mult_10 = sum(1 for n in nums if n % 10 == 0)
    print(f"   {ano}: {mult_5} múltiplos de 5, {mult_10} múltiplos de 10")

# 12. FIBONACCI CHECK
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print("\n12. NÚMEROS DE FIBONACCI:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    fib_count = sum(1 for n in nums if n in fibonacci)
    if fib_count > 0:
        fib_nums = [n for n in nums if n in fibonacci]
        print(f"   {ano}: {fib_count} fibonacci: {fib_nums}")

print("\n" + "=" * 70)
print("CONCLUSÃO:")
print("=" * 70)
print("Foram analisados 12 padrões diferentes.")
print("Qualquer 'padrão' encontrado é variância estatística normal.")
print("Nenhum deles tem valor preditivo para o próximo sorteio.")
print("=" * 70)