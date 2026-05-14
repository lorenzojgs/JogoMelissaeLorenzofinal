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