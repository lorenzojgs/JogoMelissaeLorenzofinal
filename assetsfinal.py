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



 
def _gerar_som_gol():
    """
    Gera o efeito sonoro de gol marcado.
 
    Cria um som com frequencia crescente que soa como uma
    comemoração — nota musical subindo de tom.
    Gerado matematicamente usando ondas senoidais (numpy).
 
    Returns
    -------
    pygame.mixer.Sound or None
        O som gerado ou None se houver erro.
    """
    try:
        sample_rate = 44100  # Qualidade do audio (amostras por segundo)
        duracao     = 0.6    # Duracao do som em segundos
 
        # Cria um array de tempo de 0 ate a duracao
        t = np.linspace(0, duracao, int(sample_rate * duracao))
 
        # Frequencia começa em 400Hz e sobe ate 800Hz (som alegre)
        frequencia = np.linspace(400, 800, len(t))
 
        # Gera a onda senoidal com a frequencia variavel
        onda = np.sin(2 * np.pi * frequencia * t)
 
        # Aplica envelope: o som cresce no inicio e some no final
        envelope = np.ones(len(t))
        fade_in  = int(sample_rate * 0.05)   # 5% de fade in
        fade_out = int(sample_rate * 0.2)    # 20% de fade out
        envelope[:fade_in]  = np.linspace(0, 1, fade_in)
        envelope[-fade_out:] = np.linspace(1, 0, fade_out)
        onda *= envelope
 
        # Converte para formato de 16 bits que o pygame entende
        onda_int = (onda * 32767).astype(np.int16)
        # Duplica para stereo (canal esquerdo e direito)
        stereo = np.column_stack([onda_int, onda_int])
        return pygame.sndarray.make_sound(stereo)
    except Exception as e:
        print(f'[Som] Erro ao gerar som de gol: {e}')
        return None
 
 
def _gerar_som_defesa():
    """
    Gera o efeito sonoro de defesa do goleiro.
 
    Cria um som com frequencia decrescente que soa como um
    impacto — nota musical descendo de tom.
    Gerado matematicamente usando ondas senoidais (numpy).
 
    Returns
    -------
    pygame.mixer.Sound or None
        O som gerado ou None se houver erro.
    """
    try:
        sample_rate = 44100  # Qualidade do audio
        duracao     = 0.4    # Duracao do som em segundos
 
        # Cria array de tempo
        t = np.linspace(0, duracao, int(sample_rate * duracao))
 
        # Frequencia começa em 300Hz e cai ate 100Hz (som grave de impacto)
        frequencia = np.linspace(300, 100, len(t))
 
        # Gera a onda senoidal
        onda = np.sin(2 * np.pi * frequencia * t)
 
        # Envelope: fade out rapido para soar como impacto
        envelope = np.ones(len(t))
        fade_out = int(sample_rate * 0.3)
        envelope[-fade_out:] = np.linspace(1, 0, fade_out)
        onda *= envelope
 
        # Converte para formato pygame
        onda_int = (onda * 32767).astype(np.int16)
        stereo = np.column_stack([onda_int, onda_int])
        return pygame.sndarray.make_sound(stereo)
    except Exception as e:
        print(f'[Som] Erro ao gerar som de defesa: {e}')
        return None
 
 
def _tentar_carregar_musica():
    """
    Tenta carregar e tocar musica de fundo em loop infinito.
 
    Procura por arquivos de musica nesta ordem:
    1. musica.mp3  (formato mais comum)
    2. musica.ogg  (formato aberto, menor tamanho)
    3. musica.wav  (formato sem compressao)
 
    Se encontrar, toca em loop com volume em 45%.
    Se nao encontrar, o jogo roda normalmente sem musica.
 
    Para adicionar musica:
    - Baixe qualquer musica em formato mp3
    - Renomeie para musica.mp3
    - Coloque na mesma pasta do jogo
    """
    formatos_aceitos = ['musica.mp3', 'musica.ogg', 'musica.wav']
 
    for nome in formatos_aceitos:
        if os.path.exists(nome):  # Verifica se o arquivo existe na pasta
            try:
                pygame.mixer.music.load(nome)       # Carrega o arquivo
                pygame.mixer.music.set_volume(0.45) # Volume em 45%
                pygame.mixer.music.play(-1)         # Loop infinito
                print(f'[Musica] Carregado: {nome}')
            except Exception as e:
                print(f'[Musica] Erro ao carregar {nome}: {e}')
            return
 
    print('[Musica] Nenhum arquivo encontrado. Coloque musica.mp3 na pasta do jogo.')
