# -*- coding: utf-8 -*-
"""
assets.py
---------
Responsavel por carregar todos os recursos do jogo:
fontes de texto, musica de fundo e efeitos sonoros.

Como funciona:
- carregar_assets() e chamada uma vez no inicio do jogo
- Retorna um dicionario com todas as fontes e sons prontos para uso
- A musica toca automaticamente se houver musica.mp3 na pasta do jogo
- Os efeitos sonoros sao gerados pelo proprio pygame (sem arquivos externos)
"""

import pygame        
import numpy as np   
import os            
from config import * 


# =============================================================================
# PARTE 1 — CARREGAMENTO DE FONTES
# Cria todas as fontes usadas no jogo em diferentes tamanhos
# SysFont usa fontes ja instaladas no sistema operacional
# bold=True deixa o texto em negrito para melhor o jogador conseguir ler melhor
# =============================================================================
def carregar_assets():
    """
    Inicializa e carrega todos os recursos do jogo.

    Cria as fontes em diferentes tamanhos para cada parte do jogo,
    gera os efeitos sonoros e tenta carregar a musica de fundo.

    Returns
    -------
    dict
        Dicionario com os recursos do jogo prontos para uso:
        - font_big    : fonte grande para titulos (44px)
        - font_med    : fonte media para mensagens (30px)
        - font_small  : fonte pequena para instrucoes (20px)
        - font_num    : fonte para numeros nas camisas (13px)
        - font_hud    : fonte para o HUD do jogo (14px)
        - som_gol     : efeito sonoro de gol marcado
        - som_defesa  : efeito sonoro de defesa do goleiro
    """
    assets = {}  # Dicionario que vai guardar todos os recursos do jogo

    # Fontes em tamanhos diferentes para cada parte do jogo
    assets['font_big']   = pygame.font.SysFont('Arial', 44, bold=True)  # Titulos
    assets['font_med']   = pygame.font.SysFont('Arial', 30, bold=True)  # Mensagens
    assets['font_small'] = pygame.font.SysFont('Arial', 20)             # Instrucoes
    assets['font_num']   = pygame.font.SysFont('Arial', 13, bold=True)  # Numeros
    assets['font_hud']   = pygame.font.SysFont('Arial', 14, bold=True)  # HUD

    # Gera os efeitos sonoros do jogo
    assets['som_gol']    = _gerar_som_gol()     # Som de gol marcado
    assets['som_defesa'] = _gerar_som_defesa()  # Som de defesa do goleiro

    # Tenta carregar a musica de fundo
    _tentar_carregar_musica()

    return assets  # Retorna o dicionario com todos os recursos prontos

# =============================================================================
