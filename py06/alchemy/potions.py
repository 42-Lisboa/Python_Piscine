from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return (f"💖 Healing potion brewed with "
            f"{create_earth()}  and {create_air()}")


def strength_potion() -> str:
    return (f"🌟 Strength potion brewed with "
            f"{create_fire()} and {create_water()}")


"""
=============================================================================
           ⚗️ O GUIA ALQUÍMICO DAS IMPORTAÇÕES: LOCAL vs GLOBAL ⚗️
=============================================================================
Este resumo explica como o Python diferencia um ficheiro que está
DENTRO do teu pacote (Local) de um ficheiro na RAIZ do projeto (Global),
especialmente quando ambos têm exatamente o mesmo nome (ex: elements.py).
"""

# ---------------------------------------------------------------------------
# 1. IMPORTAÇÃO GLOBAL (Absoluta / Raiz do Projeto)
# ---------------------------------------------------------------------------
# Sintaxe    : Nome do módulo sem nenhum ponto antes.
# Propósito  : Aceder a ficheiros que estão FORA do pacote, na raiz do projeto.
# Comportamento: O Python procura no 'sys.path' (o mapa global), começando
#                pela pasta principal onde executaste o teu script terminal.

""" from elements import create_fire, create_water """

# 👆 Ao NÃO usar pontos, garantimos que o Python ignora os ficheiros da nossa
# pasta atual e vai buscar o 'elements.py' principal, evitando o "Shadowing".


# ---------------------------------------------------------------------------
# 2. IMPORTAÇÃO LOCAL (Relativa / Dentro do Pacote)
# ---------------------------------------------------------------------------
# Sintaxe    : Um ponto (.) antes do nome do módulo.
# Propósito  : Aceder a ficheiros que estão NA MESMA PASTA do ficheiro atual.
# Comportamento: O Python ignora o mapa global. O ponto (.) diz-lhe
#                literalmente "olha apenas para o ficheiro que está aqui
#                ao meu lado, nesta mesma pasta".

""" from .elements import create_earth, create_air """

# 👆 O ponto diz ao Python para usar o 'elements.py' que pertence ao pacote
# atual (ex: alchemy/elements.py), garantindo que os pacotes são independentes.


"""
=============================================================================
MAPA VISUAL DA ESTRUTURA:
=============================================================================
A árvore de diretórios e como o potions.py acede a cada um:

Meu_Projeto/
 ├── elements.py        <-- [GLOBAL] from elements import ...
 │
 └── alchemy/
      ├── potions.py    <-- (O ficheiro onde estás a escrever o código)
      └── elements.py   <-- [LOCAL]  from .elements import ...
=============================================================================
"""
