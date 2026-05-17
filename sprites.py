# -*- coding: utf-8 -*-
"""
sprites.py
----------
Define todas as classes de sprites do jogo de penaltis.
Um sprite e um objeto visual que aparece na tela do jogo.
Todas as classes herdam de pygame.sprite.Sprite, que e a
classe base do pygame para objetos visuais do jogo.

Classes definidas neste arquivo:
- Bola    : a bola de futebol animada (Lorenzo — 16/05)
- Jogador : o cobrador com camisa do Brasil (Melissa — 16/05 noite)
- Goleiro : o goleiro com camisa da Alemanha (Lorenzo — 17/05)
- Placar  : exibe gols, vidas e numero da cobranca (Melissa — 17/05 noite)
"""

import pygame  # Biblioteca principal do jogo
import math    # Usado para calculos de angulo e seno (animacoes)
import random  # Usado para sortear comportamentos do goleiro
from config import *  # Importa todas as constantes do jogo


def zona_para_pixel(zona):
    """
    Converte o nome de uma zona do gol em coordenadas de pixel.
    Usa as fracoes definidas em ZONAS (config.py) para calcular
    a posicao exata em pixels dentro do gol.

    Parameters
    ----------
    zona : str
        Nome da zona conforme definido em ZONAS (config.py).

    Returns
    -------
    tuple[int, int]
        Coordenadas (x, y) em pixels dentro do gol.
    """
    fx, fy = ZONAS[zona]  # Pega as fracoes da zona
    return int(GOL_X + GOL_W * fx), int(GOL_Y + GOL_H * fy)


# =============================================================================
# PARTE 1 — CLASSE BOLA
# Representa a bola de futebol na tela.
# A bola gira e cresce conforme se aproxima do gol (perspectiva)
# =============================================================================
class Bola(pygame.sprite.Sprite):
    """
    Sprite da bola de futebol.

    A bola e desenhada com circulos pretos simulando as manchas
    de uma bola de futebol oficial. Durante o chute, ela:
    - Cresce de tamanho (efeito de perspectiva)
    - Gira (animacao de rotacao)
    - Faz um arco no ar (trajetoria realista)

    Attributes
    ----------
    pos_x, pos_y : float
        Posicao atual da bola na tela.
    scale : float
        Escala atual (1.0 = tamanho normal, menor = mais longe).
    spin : int
        Angulo de rotacao atual para animacao de giro.
    """

    RAIO_BASE = 15  # Raio da bola em pixels no tamanho normal

    def __init__(self, x, y):
        """
        Inicializa a bola na posicao (x, y).

        Parameters
        ----------
        x, y : int
            Posicao inicial da bola na tela.
        """
        super().__init__()  # Inicializa a classe pai (pygame.sprite.Sprite)
        self.pos_x  = x     # Posicao horizontal da bola
        self.pos_y  = y     # Posicao vertical da bola
        self.scale  = 1.0   # Escala inicial (tamanho normal)
        self.spin   = 0     # Angulo de rotacao inicial
        self._atualizar_image()  # Desenha a bola pela primeira vez

    def _atualizar_image(self):
        """
        Reconstroi a surface da bola com escala e rotacao atuais.
        Chamado sempre que a bola precisa ser redesenhada.
        """
        r = max(5, int(self.RAIO_BASE * self.scale))  # Raio atual
        tamanho = r * 2 + 4                            # Tamanho da surface
        surf = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
        cx = cy = tamanho // 2  # Centro da surface

        # Desenha o circulo branco principal da bola
        pygame.draw.circle(surf, WHITE, (cx, cy), r)
        # Desenha o contorno preto
        pygame.draw.circle(surf, BLACK, (cx, cy), r, 2)

        # Desenha as manchas pretas da bola (5 manchas em circulo)
        for ang in range(0, 360, 72):  # 72 graus = 360/5 manchas
            a2 = ang + self.spin  # Aplica a rotacao atual
            px = cx + int(r * 0.55 * math.cos(math.radians(a2)))
            py = cy + int(r * 0.55 * math.sin(math.radians(a2)))
            pygame.draw.circle(surf, BLACK, (px, py), max(2, r // 5))

        self.image = surf
        self.rect  = self.image.get_rect(center=(int(self.pos_x), int(self.pos_y)))

    def update(self, animando=False, anim_t=0.0, alvo_x=0, alvo_y=0,
               origem_x=0, origem_y=0, zona='centro'):
        """
        Atualiza posicao e animacao da bola a cada frame.

        Quando animando=True, a bola se move em arco do jogador ate o gol.
        O arco e calculado com seno para parecer uma trajetoria real de chute.

        Parameters
        ----------
        animando : bool
            True quando a bola esta em trajetoria de chute.
        anim_t : float
            Progresso da animacao de 0.0 (inicio) a 1.0 (fim).
        alvo_x, alvo_y : int
            Posicao destino da bola no gol.
        origem_x, origem_y : int
            Posicao de onde a bola foi chutada.
        zona : str
            Zona do gol para calcular altura do arco.
        """
        if animando:
            self.spin  += 8   # Gira a bola 8 graus por frame
            self.scale  = 0.45 + 0.55 * anim_t  # Cresce conforme se aproxima
            self.pos_x  = int(origem_x + (alvo_x - origem_x) * anim_t)
            # Calcula o arco: zonas altas tem arco menor, zonas baixas tem arco maior
            fy   = ZONAS[zona][1]
            arco = 90 * (1 - abs(fy - 0.5) * 1.4)
            self.pos_y  = int(origem_y + (alvo_y - origem_y) * anim_t
                              - arco * math.sin(math.pi * anim_t))
        else:
            self.scale = 1.0  # Volta ao tamanho normal quando parada
        self._atualizar_image()

    def resetar(self, x, y):
        """
        Reposiciona a bola na posicao inicial para nova cobranca.

        Parameters
        ----------
        x, y : int
            Nova posicao inicial da bola.
        """
        self.pos_x = x
        self.pos_y = y
        self.scale = 1.0
        self.spin  = 0
        self._atualizar_image()
# =============================================================================
# PARTE 2 — CLASSE JOGADOR
# Representa o cobrador com camisa amarela do Brasil numero 10
# Quando chutando, a perna e levantada para mostrar o movimento
# A barra de potencia aparece acima do jogador ao carregar o chute
# =============================================================================
class Jogador(pygame.sprite.Sprite):
    """
    Sprite do jogador cobrador com camisa do Brasil (#10).
 
    O jogador e desenhado com:
    - Camisa amarela com gola verde e numero 10 em verde
    - Calcao azul escuro
    - Chuteiras pretas
    - Animacao de perna levantada ao chutar
    - Barra de potencia ao carregar o chute
 
    Attributes
    ----------
    chutando : bool
        True quando o jogador esta na animacao de chute.
    charge : int
        Nivel de carga da potencia (0 a MAX_CHARGE).
    """
 
    def __init__(self, x, y):
        """
        Inicializa o jogador na posicao (x, y).
 
        Parameters
        ----------
        x, y : int
            Posicao central do jogador na tela.
        """
        super().__init__()
        self.pos_x    = x      # Posicao horizontal
        self.pos_y    = y      # Posicao vertical
        self.chutando = False  # Estado inicial: nao esta chutando
        self.charge   = 0     # Carga inicial da potencia: zero
        self._desenhar()       # Desenha o jogador pela primeira vez
 
    def _desenhar(self):
        """
        Gera a surface do jogador conforme o estado atual.
        Redesenhado sempre que chutando ou charge mudam.
        """
        surf = pygame.Surface((60, 120), pygame.SRCALPHA)
        cx = 30  # Centro horizontal da surface
 
        # Sombra no chao embaixo do jogador
        pygame.draw.ellipse(surf, (0, 80, 0, 100), (cx - 20, 108, 40, 10))
 
        # Pernas — muda conforme esta chutando ou nao
        if self.chutando:
            # Perna direita levantada para simular o chute
            pygame.draw.line(surf, BRA_AZUL, (cx - 5, 70), (cx + 26, 48), 10)
            pygame.draw.rect(surf, ALE_PRETO, (cx + 18, 42, 16, 10))  # Chuteira
            pygame.draw.rect(surf, BRA_AZUL,  (cx - 17, 70, 14, 33))  # Perna esq
            pygame.draw.rect(surf, ALE_PRETO, (cx - 18, 99, 16, 10))  # Chuteira esq
        else:
            # Posicao normal com as duas pernas no chao
            pygame.draw.rect(surf, BRA_AZUL,  (cx - 17, 70, 14, 33))  # Perna esq
            pygame.draw.rect(surf, BRA_AZUL,  (cx + 3,  70, 14, 33))  # Perna dir
            pygame.draw.rect(surf, ALE_PRETO, (cx - 18, 99, 16, 10))  # Chuteira esq
            pygame.draw.rect(surf, ALE_PRETO, (cx + 2,  99, 16, 10))  # Chuteira dir
 
        # Meias brancas acima das chuteiras
        pygame.draw.rect(surf, WHITE, (cx - 17, 90, 13, 10))
        pygame.draw.rect(surf, WHITE, (cx + 3,  90, 13, 10))
 
        # Camisa amarela do Brasil com gola verde
        pygame.draw.rect(surf, BRA_AMARELO, (cx - 17, 26, 34, 46))  # Corpo amarelo
        pygame.draw.rect(surf, BRA_VERDE,   (cx - 17, 26, 34,  8))  # Gola verde
 
        # Numero 10 em verde no centro da camisa
        fn = pygame.font.SysFont('Arial', 13, bold=True)
        surf.blit(fn.render('10', True, BRA_VERDE), (cx - 8, 38))
 
        # Cabeca com tom de pele e cabelo escuro
        pygame.draw.circle(surf, (220, 180, 140), (cx, 18), 15)      # Cabeca
        pygame.draw.arc(surf, (60, 30, 10),
                        (cx - 15, 3, 30, 20), 0, math.pi, 5)         # Cabelo
 
        # Barra de potencia — aparece acima do jogador ao carregar o chute
        if self.charge > 0:
            pct  = self.charge / MAX_CHARGE                           # Percentual de carga
            cor  = (int(255 * pct), int(255 * (1 - pct)), 0)         # Verde -> Vermelho
            pygame.draw.rect(surf, DARK_GRAY, (cx - 34, 0, 68, 10),
                             border_radius=4)                          # Fundo cinza
            pygame.draw.rect(surf, cor,
                             (cx - 34, 0, int(68 * pct), 10),
                             border_radius=4)                          # Barra colorida
            fnt = pygame.font.SysFont('Arial', 10)
            surf.blit(fnt.render('POTENCIA', True, WHITE), (cx - 24, -12))
 
        self.image = surf
        self.rect  = self.image.get_rect(midbottom=(self.pos_x, self.pos_y + 60))
 
    def update(self, chutando=False, charge=0):
        """
        Atualiza o estado visual do jogador.
 
        Parameters
        ----------
        chutando : bool
            Se True, exibe a perna levantada.
        charge : int
            Nivel atual de carga da potencia (0 a MAX_CHARGE).
        """
        self.chutando = chutando
        self.charge   = charge
        self._desenhar()
 # =============================================================================
 
