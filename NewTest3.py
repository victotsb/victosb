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
print("ROUND 3: PADRÕES AVANÇADOS E ESOTÉRICOS (25-39)")
print("=" * 80)

todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)
freq = Counter(todos_numeros)

# 25. GAPS ENTRE APARIÇÕES
print("\n25. GAPS MÉDIOS ENTRE APARIÇÕES (números mais frequentes):")
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

# 26. AUTOCORRELAÇÃO
print("\n26. AUTOCORRELAÇÃO - números em anos consecutivos:")
autocorr = defaultdict(int)
for idx in range(len(anos_ord)-1):
    ano_atual = anos_ord[idx]
    ano_prox = anos_ord[idx+1]
    nums_atual = set(dados[ano_atual])
    nums_prox = set(dados[ano_prox])
    
    for num in nums_atual & nums_prox:
        autocorr[num] += 1

if autocorr:
    print("   Top números com autocorrelação:")
    for num, count in sorted(autocorr.items(), key=lambda x: x[1], reverse=True)[:8]:
        print(f"   {num:2d}: {count} vezes em anos consecutivos")
else:
    print("   Nenhum número com autocorrelação significativa")

# 27. ANÁLISE MODULAR
print("\n27. ANÁLISE MODULAR - soma mod 10 (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    soma = sum(nums)
    mod10 = soma % 10
    mod7 = soma % 7
    print(f"   {ano}: soma={soma}, mod10={mod10}, mod7={mod7}")

# 28. QUADRADOS PERFEITOS
print("\n28. QUADRADOS PERFEITOS (1, 4, 9, 16, 25, 36, 49):")
quadrados = [1, 4, 9, 16, 25, 36, 49]
for ano in sorted(dados.keys(), reverse=True):
    match = [n for n in dados[ano] if n in quadrados]
    if match:
        print(f"   {ano}: {match}")

# 29. SIMETRIA EM RELAÇÃO AO CENTRO
print("\n29. SIMETRIA EM RELAÇÃO AO CENTRO (30.5) - últimos 8 anos:")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    distancias = [abs(n - 30.5) for n in nums]
    dist_media = np.mean(distancias)
    print(f"   {ano}: distância média = {dist_media:.1f}")

# 30. DIVISIBILIDADE POR 3
print("\n30. DIVISIBILIDADE POR 3 (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    div3 = sum(1 for n in nums if n % 3 == 0)
    print(f"   {ano}: {div3} números divisíveis por 3")

# 31. COMBINAÇÕES DE TERMINAÇÕES
print("\n31. COMBINAÇÕES DE TERMINAÇÕES (últimos 6 anos):")
for ano in sorted(dados.keys(), reverse=True)[:6]:
    nums = dados[ano]
    terminacoes = sorted([n % 10 for n in nums])
    # Verificar repetições
    term_counter = Counter(terminacoes)
    repetidas = [t for t, c in term_counter.items() if c > 1]
    rep_str = f" → REPETIDAS: {repetidas}" if repetidas else ""
    print(f"   {ano}: {terminacoes}{rep_str}")

# 32. MAIOR GAP INTERNO
print("\n32. MAIOR GAP INTERNO (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = sorted(dados[ano])
    gaps = [nums[i+1] - nums[i] for i in range(5)]
    maior_gap = max(gaps)
    idx = gaps.index(maior_gap)
    print(f"   {ano}: gap={maior_gap} (entre {nums[idx]} e {nums[idx+1]})")

# 33. DENSIDADE POR DÉCADAS
print("\n33. DENSIDADE POR DÉCADAS (últimos 5 anos):")
decadas = {i: 0 for i in range(1, 7)}
for ano in sorted(dados.keys(), reverse=True)[:5]:
    for num in dados[ano]:
        decada = ((num - 1) // 10) + 1
        decadas[decada] += 1

for dec, count in sorted(decadas.items()):
    barra = "█" * count
    print(f"   {(dec-1)*10+1:2d}-{dec*10:2d}: {barra} ({count})")

# 34. PRODUTO DOS NÚMEROS
print("\n34. PRODUTO DOS NÚMEROS - ordem de grandeza (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = dados[ano]
    produto = 1
    for n in nums:
        produto *= n
    ordem = math.floor(math.log10(produto)) if produto > 0 else 0
    print(f"   {ano}: ~10^{ordem} ({ordem+1} dígitos)")

# 35. FIBONACCI
print("\n35. NÚMEROS DE FIBONACCI:")
fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55]
for ano in sorted(dados.keys(), reverse=True):
    fib_nums = [n for n in dados[ano] if n in fibonacci]
    if len(fib_nums) >= 2:
        print(f"   {ano}: {fib_nums}")

# 36. MEDIANA vs MÉDIA
print("\n36. MEDIANA vs MÉDIA (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    media = np.mean(nums)
    mediana = np.median(nums)
    dif = media - mediana
    assimetria = "direita" if dif > 2 else "esquerda" if dif < -2 else "simétrico"
    print(f"   {ano}: média={media:.1f}, mediana={mediana:.1f}, dif={dif:+.1f} ({assimetria})")

# 37. PROGRESSÃO GEOMÉTRICA
print("\n37. TESTE DE PROGRESSÃO GEOMÉTRICA (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = sorted(dados[ano])
    razoes = [nums[i+1] / nums[i] for i in range(5) if nums[i] != 0]
    razao_media = np.mean(razoes)
    variacao = np.std(razoes)
    if variacao < 0.3:
        print(f"   {ano}: razão={razao_media:.2f}, var={variacao:.2f} (quase geométrica)")

# 38. CONCENTRAÇÃO (Herfindahl)
print("\n38. ÍNDICE DE CONCENTRAÇÃO (últimos 5 anos):")
for ano in sorted(dados.keys(), reverse=True)[:5]:
    nums = dados[ano]
    faixas = defaultdict(int)
    for n in nums:
        faixa = ((n-1) // 10) * 10 + 1
        faixas[faixa] += 1
    herfindahl = sum((count/6)**2 for count in faixas.values())
    print(f"   {ano}: H={herfindahl:.3f} (0.167=uniforme, 1=concentrado)")

# 39. CORRELAÇÃO ANO PAR/ÍMPAR
print("\n39. CORRELAÇÃO ANO PAR/ÍMPAR (últimos 8 anos):")
for ano in sorted(dados.keys(), reverse=True)[:8]:
    nums = dados[ano]
    ano_par = ano % 2 == 0
    pares = sum(1 for n in nums if n % 2 == 0)
    print(f"   {ano} ({'par' if ano_par else 'ímpar'}): {pares} números pares")

print("\n" + "="*80)
print("ROUND 3 COMPLETO - 39 padrões analisados")
print("Próximo: Round 4 Final...")
print("="*80)