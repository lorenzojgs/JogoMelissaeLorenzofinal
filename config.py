# -*- coding: utf-8 -*-
"""
config.py
---------
Arquivo de configuracoes globais do jogo de penaltis.
Todas as constantes do jogo estao aqui.
Altere este arquivo para ajustar tamanho da tela, dificuldade, cores, etc.
"""
# =============================================================================
# PARTE 1 — CONFIGURACOES DA JANELA
# Define o tamanho da tela e a velocidade do jogo
# FPS = Frames Per Second = quantas vezes a tela e redesenhada por segundo
# =============================================================================
TITULO  = 'Penaltis - Brasil x Alemanha'  
WIDTH   = 1000                             
HEIGHT  = 750                              
FPS     = 60                              
# =============================================================================
# PARTE 2 — CORES BASICAS
# Cada cor (R, G, B) com valores de 0 a 255
# R = vermelho, G = verde, B = azul
# algumas cores já estavam definidas dos arquivos que nos foram fornecidos(você vai lembrar disso Márcio) . As outras procuramos na internet quais padrões usar =============================================================================
WHITE       = (255, 255, 255)  # Branco — postes do gol e bola
BLACK       = (0,   0,   0)    # Preto — contornos e chuteiras
GREEN       = (34,  139, 34)   # Verde —  campo
DARK_GREEN  = (0,   100, 0)    # Verde escuro — listras do campo
YELLOW      = (255, 215, 0)    # Amarelo — destaques e textos 
RED         = (220, 20,  60)   # Vermelho — vidas e mensagens de erro
BLUE        = (30,  144, 255)  # Azul — shorts do jogador brasileiro
GRAY        = (180, 180, 180)  # Cinza — rede do gol
DARK_GRAY   = (60,  60,  60)   # Cinza escuro — sombras
SKY_TOP     = (80,  160, 220)  # Azul escuro —  ceu
SKY_BOT     = (180, 220, 255)  # Azul claro — ceu 
ORANGE      = (255, 140, 0)    # Laranja — luvas do goleiro
LIGHT_GREEN = (124, 252, 0)    # Verde claro — mensagem de GOL!
GOLD        = (255, 200, 0)    # Dourado — tela de vitoria
# =============================================================================
# PARTE 3 — CORES DAS CAMISAS E CONFIGURACOES DO GOL
# Cores oficiais das selecoes Brasil e Alemanha
# e posicao e tamanho do gol na tela
# =============================================================================
 
# Brasil — camisa amarela com detalhes verdes e calcao azul
BRA_AMARELO = (250, 220,   0)  # Amarelo da camisa do Brasil
BRA_VERDE   = (0,   155,  58)  # Verde da gola e do numero 10
BRA_AZUL    = (0,    39, 118)  # Azul do calcao brasileiro
 
# Alemanha — camisa preta com listras brancas e gola vermelha
ALE_PRETO   = (20,   20,  20)  # Preto da camisa do goleiro alemao
ALE_VERM    = (200,   0,  30)  # Vermelho da gola da camisa alema
 
# Configuracoes do gol
# O gol e centralizado horizontalmente usando WIDTH // 2
# GOL_X e calculado para que o gol fique exatamente no meio da tela
GOL_X = WIDTH  // 2 - 200  # Posicao X do canto esquerdo do gol
GOL_W = 400                # Largura total do gol em pixels
GOL_Y = 50                 # Distancia do topo da tela ate o gol
GOL_H = 220                # Altura total do gol em pixels
 
# =============================================================================
# PARTE 4 — REGRAS, ESTADOS E ZONAS DO GOL
# Define a dificuldade do jogo, os estados possiveis
# e as 9 zonas onde a bola pode ser chutada
# =============================================================================
 
# Regras do jogo — altere para deixar mais facil ou dificil
MAX_COBRANÇAS    = 7   # Total de cobranças por partida
GOLS_PARA_VENCER = 4   # Gols necessarios para vencer
VIDAS_INICIO     = 3   # Vidas (erros permitidos) no inicio
MAX_CHARGE       = 90  # Frames para carregar potencia maxima do chute
 
# Estados do jogo
# O jogo sempre esta em um desses estados
# Cada estado define o que acontece e o que e desenhado na tela
STATE_INTRO   = 'intro'    # Tela inicial com instrucoes de como jogar
STATE_PLAYING = 'playing'  # Jogador esta cobrando o penalti agora
STATE_RESULT  = 'result'   # Mostra GOL ou Defendido entre cobranças
STATE_WIN     = 'win'      # Jogador fez gols suficientes — vitoria!
STATE_LOSE    = 'lose'     # Jogador perdeu todas as vidas ou cobranças
 
# Zonas do gol
# O gol e dividido em 9 regioes onde a bola pode ser chutada
# fx: 0.0 = extrema esquerda | 0.5 = centro | 1.0 = extrema direita
# fy: 0.0 = topo do gol      | 0.5 = meio   | 1.0 = base do gol
ZONAS = {
    'canto_sup_esq': (0.12, 0.18),  # Canto superior esquerdo
    'centro_esq':    (0.12, 0.60),  # Meio do lado esquerdo
    'canto_inf_esq': (0.12, 0.88),  # Canto inferior esquerdo
    'centro_alto':   (0.50, 0.18),  # Centro do gol no alto
    'centro':        (0.50, 0.55),  # Centro exato do gol (sempre gol!)
    'centro_baixo':  (0.50, 0.88),  # Centro do gol embaixo
    'canto_sup_dir': (0.88, 0.18),  # Canto superior direito
    'centro_dir':    (0.88, 0.60),  # Meio do lado direito
    'canto_inf_dir': (0.88, 0.88),  # Canto inferior direito
}
 
# Nomes das zonas para mostrar na tela durante o carregamento do chute
NOMES_ZONA = {
    'canto_sup_esq': 'Canto sup. esq',
    'centro_esq':    'Centro esq',
    'canto_inf_esq': 'Canto inf. esq',
    'centro_alto':   'Centro alto',
    'centro':        'Centro',
    'centro_baixo':  'Centro baixo',
    'canto_sup_dir': 'Canto sup. dir',
    'centro_dir':    'Centro dir',
    'canto_inf_dir': 'Canto inf. dir',
}
 
# Zonas centrais — goleiro NUNCA pula para o centro, entao sao sempre gol
ZONAS_CENTRO = ('centro', 'centro_alto', 'centro_baixo')
 
# Zonas laterais — goleiro pode mergulhar para qualquer uma dessas regioes
ZONAS_GOLEIRO = [
    'canto_sup_esq', 'centro_esq', 'canto_inf_esq',
    'canto_sup_dir', 'centro_dir', 'canto_inf_dir',
]