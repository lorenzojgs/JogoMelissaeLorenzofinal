# Penaltis - Copa do Mundo 🇧🇷 x 🇩🇪

**Autores:** Lorenzo Santos e Melissa Kheir
**Disciplina:** Design de Software — Insper

## Descricao

Jogo de cobrança de penaltis desenvolvido em Python com Pygame.
O jogador controla o atacante do Brasil (#10) e tenta marcar gols
contra o goleiro da Alemanha (#1), que se move de lado a lado e
aprende os cantos favoritos do jogador ao longo da partida.

## Como instalar

```bash
pip install pygame
```

## Como executar

```bash
python3 penalti.py
```

## Controles

| Tecla(s)              | Acao                      |
|-----------------------|---------------------------|
| Seta Dir + Cima       | Canto superior direito    |
| Seta Dir              | Centro direito            |
| Seta Dir + Baixo      | Canto inferior direito    |
| Seta Esq + Cima       | Canto superior esquerdo   |
| Seta Esq              | Centro esquerdo           |
| Seta Esq + Baixo      | Canto inferior esquerdo   |
| Cima                  | Centro alto               |
| **ESPACO**            | **Centro (sempre gol!)**  |
| Baixo                 | Centro baixo              |

> **Dica:** Segure a tecla antes de soltar — quanto mais tempo segurar, mais forte o chute!

## Regras

- Faca **4 gols em 7 cobranças** para vencer
- Voce tem **3 vidas** — cada defesa do goleiro custa uma vida
- O goleiro fica mais esperto a cada cobrança

## Estrutura do projeto

```
penalti_jogo/
├── penalti.py      # Arquivo principal (execute este)
├── config.py       # Constantes e configuracoes
├── assets.py       # Carregamento de fontes e musica
├── sprites.py      # Classes dos sprites (Bola, Jogador, Goleiro, Placar)
├── cenario.py      # Desenho do campo, gol, ceu e mira
├── game_screen.py  # Loop principal e logica do jogo
├── telas.py        # Telas de intro, resultado, vitoria e derrota
└── README.md       # Este arquivo
```

## Uso de IA

Este projeto foi desenvolvido com auxilio do Claude (Anthropic) e CHAT GPT.
A estrutura em multiplos arquivos, as classes com docstrings e a
logica de jogo adaptadas em colaboracao com a IA. Também tiramos dúvidas. 

## Vídeo 

