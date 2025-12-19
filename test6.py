import random
import numpy as np
from itertools import combinations

print("=" * 80)
print("GERADOR MEGA DA VIRADA 2025 - BASEADO EM 9 PADRÕES VALIDADOS")
print("=" * 80)

def verificar_padrao_3_3(nums):
    """Padrão 1: 3 pares + 3 ímpares"""
    pares = sum(1 for n in nums if n % 2 == 0)
    return pares == 3

def verificar_assimetria_positiva(nums):
    """Padrão 2: Maioria dos números entre 30-60"""
    faixa_alta = sum(1 for n in nums if 30 <= n <= 60)
    return faixa_alta >= 3  # Pelo menos metade

def verificar_distribuicao_espalhada(nums):
    """Padrão 3: Boa distribuição (gaps não muito grandes)"""
    nums_sorted = sorted(nums)
    gaps = [nums_sorted[i+1] - nums_sorted[i] for i in range(5)]
    maior_gap = max(gaps)
    return maior_gap <= 25  # Evita gaps gigantes

def verificar_correlacao_linear(nums):
    """Padrão 4: Números bem distribuídos pelo range"""
    nums_sorted = sorted(nums)
    # Verifica se números não estão muito concentrados
    amplitude = nums_sorted[-1] - nums_sorted[0]
    return amplitude >= 25  # Amplitude mínima razoável

def verificar_terminacoes_repetidas(nums):
    """Padrão 5: Pelo menos 1 par com mesma terminação"""
    terminacoes = [n % 10 for n in nums]
    return len(terminacoes) != len(set(terminacoes))

def tem_numero_10(nums):
    """Padrão 6: Inclui o número 10 (autocorrelação)"""
    return 10 in nums

def calcular_assimetria(nums):
    """Padrão 7: Verifica se distribuição é assimétrica"""
    media = np.mean(nums)
    mediana = np.median(nums)
    dif = abs(media - mediana)
    return dif  # Retorna diferença para análise

def verificar_mod10(nums):
    """Padrão 8: Soma mod 10 = 3"""
    soma = sum(nums)
    return soma % 10 == 3

def calcular_distancia_2024(nums):
    """Padrão 9: Distância euclidiana em relação a 2024"""
    nums_2024 = [1, 17, 19, 29, 50, 57]
    nums_sorted = sorted(nums)
    dist = np.sqrt(sum((a - b)**2 for a, b in zip(nums_sorted, nums_2024)))
    return dist

def gerar_combinacao_inteligente():
    """Gera combinação seguindo os padrões TIER S obrigatoriamente"""
    max_tentativas = 10000
    
    for _ in range(max_tentativas):
        # Gera 3 pares e 3 ímpares
        pares = random.sample([n for n in range(2, 61, 2)], 3)
        impares = random.sample([n for n in range(1, 60, 2)], 3)
        nums = sorted(pares + impares)
        
        # Verifica TIER S (obrigatórios)
        if not verificar_assimetria_positiva(nums):
            continue
        if not verificar_distribuicao_espalhada(nums):
            continue
        if not verificar_correlacao_linear(nums):
            continue
            
        return nums
    
    # Fallback: retorna combinação aleatória 3+3
    pares = random.sample([n for n in range(2, 61, 2)], 3)
    impares = random.sample([n for n in range(1, 60, 2)], 3)
    return sorted(pares + impares)

def avaliar_combinacao(nums):
    """Avalia quantos padrões a combinação atende"""
    score = 0
    detalhes = []
    
    # TIER S (obrigatórios)
    if verificar_padrao_3_3(nums):
        score += 2
        detalhes.append("✓ 3+3")
    else:
        detalhes.append("✗ 3+3")
    
    if verificar_assimetria_positiva(nums):
        score += 2
        detalhes.append("✓ Assimetria+")
    else:
        detalhes.append("✗ Assimetria+")
    
    if verificar_distribuicao_espalhada(nums):
        score += 1
        detalhes.append("✓ Espalhado")
    else:
        detalhes.append("✗ Espalhado")
    
    if verificar_correlacao_linear(nums):
        score += 1
        detalhes.append("✓ LinearOK")
    else:
        detalhes.append("✗ LinearOK")
    
    # TIER A (bônus)
    if verificar_terminacoes_repetidas(nums):
        score += 1
        detalhes.append("✓ TermRep")
    else:
        detalhes.append("✗ TermRep")
    
    if tem_numero_10(nums):
        score += 1
        detalhes.append("✓ Tem10")
    else:
        detalhes.append("✗ Tem10")
    
    if verificar_mod10(nums):
        score += 1
        detalhes.append("✓ Mod10=3")
    else:
        detalhes.append("✗ Mod10=3")
    
    return score, detalhes

# Gera 10 combinações
print("\nGERANDO 10 COMBINAÇÕES OTIMIZADAS...\n")

combinacoes = []
for i in range(10):
    nums = gerar_combinacao_inteligente()
    
    # Tenta incluir padrões TIER A (50% de chance de forçar número 10)
    if i < 5 and 10 not in nums and random.random() > 0.5:
        # Substitui um número par por 10
        pares = [n for n in nums if n % 2 == 0]
        if pares:
            nums.remove(random.choice(pares))
            nums.append(10)
            nums = sorted(nums)
    
    combinacoes.append(nums)

# Ordena por score
combinacoes_avaliadas = [(nums, *avaliar_combinacao(nums)) for nums in combinacoes]
combinacoes_avaliadas.sort(key=lambda x: x[1], reverse=True)

# Exibe resultados
print("RANKING DAS COMBINAÇÕES (Score = padrões atendidos)")
print("=" * 80)

for idx, (nums, score, detalhes) in enumerate(combinacoes_avaliadas, 1):
    soma = sum(nums)
    pares = sum(1 for n in nums if n % 2 == 0)
    terminacoes = [n % 10 for n in nums]
    dist_2024 = calcular_distancia_2024(nums)
    assimetria = calcular_assimetria(nums)
    
    print(f"\n#{idx} | SCORE: {score}/9 | {nums}")
    print(f"    Padrões: {' | '.join(detalhes)}")
    print(f"    Soma: {soma} (mod10={soma%10}) | P/I: {pares}/{6-pares}")
    print(f"    Terminações: {terminacoes}")
    print(f"    Assimetria: {assimetria:.1f} | Dist2024: {dist_2024:.1f}")

print("\n" + "=" * 80)
print("LEGENDA DOS PADRÕES:")
print("=" * 80)
print("TIER S (Obrigatórios):")
print("  ✓ 3+3       = 3 pares + 3 ímpares")
print("  ✓ Assimetria+ = Maioria entre 30-60")
print("  ✓ Espalhado = Gaps menores que 25")
print("  ✓ LinearOK  = Amplitude >= 25")
print("\nTIER A (Bônus):")
print("  ✓ TermRep   = Terminações repetidas")
print("  ✓ Tem10     = Inclui número 10")
print("  ✓ Mod10=3   = Soma mod 10 = 3")
print("=" * 80)

print("\n💡 RECOMENDAÇÃO:")
print("   Use as combinações com SCORE 7-9 (máximo alinhamento)")
print("   Ou escolha as TOP 3 para jogar em bolão")
print("\n⚠️  LEMBRETE:")
print("   Mesmo com todos os padrões, a chance é 1 em 50.063.860")
print("   Isso NÃO garante vitória, apenas alinha com histórico")
print("=" * 80)