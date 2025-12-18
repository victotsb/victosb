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
print("ANÁLISE EXAUSTIVA - ROUND 3: PADRÕES AVANÇADOS E ESOTÉRICOS")
print("=" * 75)

# 25. GAPS ENTRE APARIÇÕES DO MESMO NÚMERO
print("\n25. GAPS MÉDIOS ENTRE APARIÇÕES (números frequentes):")
todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)
freq = Counter(todos_numeros)

aparicoes = defaultdict(list)
anos_ord = sorted(dados.keys())
for idx, ano in enumerate(anos_ord):
    for num in dados[ano]:
        aparicoes[num].append(idx)

print("   Núm | Gaps entre aparições")
for num, count in freq.most_common(10):
    if count > 1:
        indices = aparicoes[num]
        gaps = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
        gap_medio = np.mean(gaps) if gaps else 0
        print(f"   {num:2d}  | gaps={gaps}, média={gap_medio:.1f} anos")

# 26. ANÁLISE DE AUTOCORRELAÇÃO (número aparece depois de si mesmo?)
print("\n26. AUTOCORRELAÇÃO - números que aparecem em anos próximos:")
autocorr = defaultdict(int)
for idx in range(len(anos_ord)-1):
    ano_atual = anos_ord[idx]
    ano_prox = anos_ord[idx+1]
    nums_atual = set(dados[ano_atual])
    nums_prox = set(dados[ano_prox])
    
    for num in nums_atual & nums_prox:
        autocorr[num] += 1

print("   Números com alta autocorrelação (aparecem em anos seguidos):")
for num, count in sorted(autocorr.items(), key=lambda x: x[1], reverse=True)[:8]:
    print(f"   {num:2d}: {count} vezes em anos consecutivos")

# 27. SOMA MODULAR (resto da divisão)
print("\n27. ANÁLISE MODULAR - soma total mod 10:")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    soma = sum(nums)
    mod10 = soma % 10
    mod7 = soma % 7
    print(f"   {ano}: soma={soma}, mod10={mod10}, mod7={mod7}")

# 28. NÚMEROS QUADRADOS PERFEITOS
print("\n28. QUADRADOS PERFEITOS (1, 4, 9, 16, 25, 36, 49):")
quadrados = [1, 4, 9, 16, 25, 36, 49]
for ano, nums in sorted(dados.items(), reverse=True):
    match = [n for n in nums if n in quadrados]
    if match:
        print(f"   {ano}: {match}")

# 29. ANÁLISE DE SIMETRIA (números espelhados em relação a 30.5)
print("\n29. SIMETRIA EM RELAÇÃO AO CENTRO (30.5):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    distancias = [abs(n - 30.5) for n in nums]
    dist_media = np.mean(distancias)
    print(f"   {ano}: distância média do centro = {dist_media:.1f}")

# 30. NÚMEROS DIVISÍVEIS POR 3
print("\n30. DIVISIBILIDADE POR 3:")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    div3 = sum(1 for n in nums if n % 3 == 0)
    print(f"   {ano}: {div3} números divisíveis por 3")

# 31. PADRÃO DE TERMINAÇÃO (análise mais profunda)
print("\n31. COMBINAÇÕES DE TERMINAÇÕES:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    terminacoes = sorted([n % 10 for n in nums])
    print(f"   {ano}: terminações = {terminacoes}")

# 32. MAIOR GAP INTERNO (diferença máxima entre números consecutivos)
print("\n32. MAIOR GAP INTERNO POR ANO:")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    nums_sorted = sorted(nums)
    gaps = [nums_sorted[i+1] - nums_sorted[i] for i in range(5)]
    maior_gap = max(gaps)
    print(f"   {ano}: maior gap = {maior_gap} (entre {nums_sorted[gaps.index(maior_gap)]} e {nums_sorted[gaps.index(maior_gap)+1]})")

# 33. DENSIDADE (quantos números em cada intervalo de 10)
print("\n33. DENSIDADE POR DÉCADAS (últimos 5 anos):")
decadas = {i: 0 for i in range(1, 7)}
for ano in sorted(dados.keys(), reverse=True)[:5]:
    for num in dados[ano]:
        decada = ((num - 1) // 10) + 1
        decadas[decada] += 1

for dec, count in sorted(decadas.items()):
    barra = "█" * count
    print(f"   {(dec-1)*10+1:2d}-{dec*10:2d}: {barra} ({count})")

# 34. PRODUTO DOS NÚMEROS (overflow alert!)
print("\n34. PRODUTO DOS NÚMEROS (ordem de grandeza):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    produto = 1
    for n in nums:
        produto *= n
    ordem = math.floor(math.log10(produto)) if produto > 0 else 0
    print(f"   {ano}: ~10^{ordem} (produto tem {ordem+1} dígitos)")

# 35. RAZÃO ÁUREA CHECK (números próximos de phi = 1.618...)
print("\n35. NÚMEROS RELACIONADOS À RAZÃO ÁUREA:")
phi = 1.618033988749
fibonacci_extended = [1, 2, 3, 5, 8, 13, 21, 34, 55]
print("   Anos com 2+ números de Fibonacci:")
for ano, nums in sorted(dados.items(), reverse=True):
    fib_nums = [n for n in nums if n in fibonacci_extended]
    if len(fib_nums) >= 2:
        print(f"   {ano}: {fib_nums}")

# 36. MEDIANA vs MÉDIA
print("\n36. MEDIANA vs MÉDIA (detecta assimetria):")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    media = np.mean(nums)
    mediana = np.median(nums)
    dif = media - mediana
    print(f"   {ano}: média={media:.1f}, mediana={mediana:.1f}, dif={dif:+.1f}")

# 37. NÚMEROS EM PROGRESSÃO GEOMÉTRICA?
print("\n37. TESTE DE PROGRESSÃO GEOMÉTRICA:")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    nums_sorted = sorted(nums)
    razoes = [nums_sorted[i+1] / nums_sorted[i] for i in range(5) if nums_sorted[i] != 0]
    razao_media = np.mean(razoes)
    variacao = np.std(razoes)
    if variacao < 0.5:
        print(f"   {ano}: razão média={razao_media:.2f}, var={variacao:.2f} (quase geométrica!)")

# 38. ÍNDICE DE CONCENTRAÇÃO (Herfindahl)
print("\n38. CONCENTRAÇÃO EM FAIXAS (10 números por faixa):")
for ano, nums in sorted(dados.items(), reverse=True)[:5]:
    faixas = defaultdict(int)
    for n in nums:
        faixa = ((n-1) // 10) * 10 + 1
        faixas[faixa] += 1
    herfindahl = sum((count/6)**2 for count in faixas.values())
    print(f"   {ano}: H-index={herfindahl:.3f} (1=máxima concentração, {1/6:.3f}=uniforme)")

# 39. PARIDADE DO ANO vs PARIDADE DOS NÚMEROS
print("\n39. CORRELAÇÃO ANO PAR/ÍMPAR vs NÚMEROS PARES/ÍMPARES:")
for ano, nums in sorted(dados.items(), reverse=True)[:8]:
    ano_par = ano % 2 == 0
    pares = sum(1 for n in nums if n % 2 == 0)
    print(f"   {ano} ({'par' if ano_par else 'ímpar'}): {pares} números pares")

print("\n" + "=" * 75)
print("STATUS: ROUND 3 COMPLETO - 39 PADRÕES ANALISADOS ATÉ AGORA")
print("Faltam ~10-15 padrões mais esotéricos...")
print("=" * 75)