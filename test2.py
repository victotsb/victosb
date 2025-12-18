import numpy as np
from collections import Counter
import random

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
print("10 COMBINAÇÕES GERADAS")
print("(AVISO: Puramente aleatório, sem valor preditivo)")
print("=" * 60)

# Coletar estatísticas dos dados históricos
todos_numeros = []
for nums in dados.values():
    todos_numeros.extend(nums)

freq = Counter(todos_numeros)

# Calcular médias históricas
medias_soma = [sum(nums) for nums in dados.values()]
media_soma_historica = np.mean(medias_soma)

# ESTRATÉGIA 1-5: Mix de abordagens diferentes
estrategias = []

# 1. Pura aleatoriedade
estrategias.append(("Aleatório puro", 
                   lambda: sorted(random.sample(range(1, 61), 6))))

# 2. Favorecendo números mais frequentes (leve viés)
numeros_frequentes = [num for num, _ in freq.most_common(30)]
estrategias.append(("Viés frequentes", 
                   lambda: sorted(random.sample(numeros_frequentes + list(range(1, 61)), 6))))

# 3. Evitando números muito frequentes (contrarian)
numeros_raros = [i for i in range(1, 61) if freq[i] <= 2]
estrategias.append(("Contrarian (raros)", 
                   lambda: sorted(random.sample(numeros_raros + list(range(1, 61)), 6))))

# 4. Balanceado par/ímpar (3 de cada)
def gerar_balanceado():
    pares = random.sample([i for i in range(2, 61, 2)], 3)
    impares = random.sample([i for i in range(1, 60, 2)], 3)
    return sorted(pares + impares)
estrategias.append(("3 pares + 3 ímpares", gerar_balanceado))

# 5. Distribuído por dezenas
def gerar_distribuido():
    resultado = []
    for dezena in range(0, 6):
        inicio = dezena * 10 + 1
        fim = min(dezena * 10 + 10, 60)
        if random.random() > 0.5 and fim <= 60:
            resultado.append(random.randint(inicio, fim))
    while len(resultado) < 6:
        resultado.append(random.randint(1, 60))
    return sorted(list(set(resultado))[:6])
estrategias.append(("Dezenas distribuídas", gerar_distribuido))

# 6-10: Mais variações aleatórias
for i in range(5):
    estrategias.append((f"Variação aleatória {i+1}", 
                       lambda: sorted(random.sample(range(1, 61), 6))))

print("\n")
for idx, (nome, func) in enumerate(estrategias, 1):
    numeros = func()
    while len(numeros) < 6:  # garantir 6 números únicos
        numeros = func()
    
    soma = sum(numeros)
    pares = sum(1 for n in numeros if n % 2 == 0)
    
    print(f"{idx:2d}. [{nome:20s}]  {numeros}")
    print(f"    Soma: {soma:3d} | Pares: {pares} | Ímpares: {6-pares}")
    print()

print("=" * 60)
print("AVISO IMPORTANTE:")
print("=" * 60)
print("Essas combinações têm ZERO valor preditivo.")
print("Cada uma tem exatamente 1 em 50.063.860 de chance (Mega-Sena).")
print("Jogar baseado nisso é matematicamente equivalente a")
print("escolher números com os olhos fechados.")
print()
print("A casa sempre ganha no longo prazo.")
print("=" * 60); import numpy as np
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