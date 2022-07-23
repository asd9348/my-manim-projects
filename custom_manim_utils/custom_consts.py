from manim import *
from colour import Color
import numpy as np
from manim.constants import *

from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *

q: float = 0.3
qq: float = 2 * q
qqq: float = 3 * q
t: float = 3
tt: float = 5
ttt: float = 7
DG = DEGREES
O: np.ndarray = ORIGIN
LEFT : np.ndarray = np.array((-1.0, 0.0, 0.0))
L: np.ndarray = np.array((-1.0, 0.0, 0.0))
R: np.ndarray = np.array((1.0, 0.0, 0.0))
U: np.ndarray = np.array((0.0, 1.0, 0.0))
D: np.ndarray = np.array((0.0, -1.0, 0.0))

X: np.ndarray = np.array((1.0, 0.0, 0.0))
Y: np.ndarray = np.array((0.0, 1.0, 0.0))
Z: np.ndarray = np.array((0.0, 0.0, 1.0))

# ETH_COIN = create_circle_asset(Tex(r'\textbf{ETH}',color=WHITE, font_size =30),  fill_color=C_ETH)
# USDT_COIN = create_circle_asset(Tex(r'\textbf{USDT}',color=WHITE, font_size =25),  fill_color=C_USDT)
# BTC_COIN = create_circle_asset(Tex(r'\textbf{BTC}',color=WHITE, font_size =30),  fill_color=C_BTC)
# ATOM_COIN = create_circle_asset(Tex(r'\textbf{ATOM}',color=C_ATOM2, font_size =25),  fill_color=C_ATOM1)
# DOT_COIN = create_circle_asset(Tex(r'\textbf{DOT}',color=WHITE, font_size =30),  fill_color=C_DOT)
# XRP_COIN = create_circle_asset(Tex(r'\textbf{XRP}',color=WHITE, font_size =30),  fill_color=C_XRP)
# BNB_COIN = create_circle_asset(Tex(r'\textbf{BNB}',color=C_BNB2, font_size =30), fill_color=C_BNB1)
# ADA_COIN = create_circle_asset(Tex(r'\textbf{ADA}',color=WHITE, font_size =30),  fill_color=C_ADA)
# XMR_COIN = create_circle_asset(Tex(r'\textbf{XMR}',color=C_XMR1, font_size =30),  fill_color=C_XMR2)
# USDC_COIN = create_circle_asset(Tex(r'\textbf{USDC}',color=WHITE, font_size =25),  fill_color=C_USDC)
# MATIC_COIN = create_circle_asset(Tex(r'\textbf{MATIC}',color=WHITE, font_size =20), fill_color=C_MATIC)
# LINK_COIN = create_circle_asset(Tex(r'\textbf{LINK}',color=WHITE, font_size =25),  fill_color=C_LINK)
# FTX_COIN = create_circle_asset(Tex(r'\textbf{FTX}',color=WHITE, font_size =30), fill_color=C_FTX)
# DOGE_COIN = create_circle_asset(Tex(r'\textbf{DOGE}',color=WHITE, font_size =25),  fill_color=C_DOGE)
# TRON_COIN = create_circle_asset(Tex(r'\textbf{TRON}',color=WHITE, font_size =25),fill_color=C_TRON)
# SHIT_COIN = create_circle_asset(Tex(r'\textbf{SHIT}',color=WHITE, font_size =25),fill_color=C0492)
# POOP_COIN = create_circle_asset(Tex(r'\textbf{POOP}',color=WHITE, font_size =25),fill_color=C0493)
# sol_text = Tex(r'\textbf{SOL}', substrings_to_isolate=[ 'S', 'O', 'L' ])
# SOL_COIN = create_circle_asset(Tex(r'\textbf{SOL}',color=C_SOL3, font_size =30), fill_color=C_SOL0)
# sol_text.set_color_by_tex('S', color=C_SOL3)
# sol_text.set_color_by_tex('O', color=C_SOL2)
# sol_text.set_color_by_tex('L', color=C_SOL1)
# ETH_COIN = create_circle_asset(Tex(r'\textbf{ETH}',color=WHITE), font_size =10, WHITE, fill_color=C_ETH, stroke_color=GREEN, stroke_width=0)
# BTC_COIN = create_circle_asset(Tex(r'\textbf{BTC}',color=WHITE), font_size =10, WHITE, fill_color=C_BTC, stroke_color=GREEN, stroke_width=0)
# ATOM_COIN = create_circle_asset(Tex(r'\textbf{AT}',color=C_ATOM2), font_size =10, C_ATOM2, fill_color=C_ATOM1, stroke_color=GREEN, stroke_width=0)
# DOT_COIN = create_circle_asset(Tex(r'\textbf{DOT}',color=WHITE), font_size =10, WHITE, fill_color=C_DOT, stroke_color=GREEN, stroke_width=0)
# XRP_COIN = create_circle_asset(Tex(r'\textbf{XRP}',color=WHITE), font_size =10, WHITE, fill_color=C_XRP, stroke_color=GREEN, stroke_width=0)
# BNB_COIN = create_circle_asset(Tex(r'\textbf{BNB}',color=C_BNB2), font_size =10, C_BNB2, fill_color=C_BNB1, stroke_color=GREEN, stroke_width=0)
# ADA_COIN = create_circle_asset(Tex(r'\textbf{ADA}',color=WHITE), font_size =10, WHITE, fill_color=C_ADA, stroke_color=GREEN, stroke_width=0)
# XMR_COIN = create_circle_asset(Tex(r'\textbf{XMR}',color=C_XMR1), font_size =10, C_XMR1, fill_color=C_XMR2, stroke_color=GREEN, stroke_width=0)
# USDC_COIN = create_circle_asset(Tex(r'\textbf{USDC}',color=WHITE), font_size =10, WHITE, fill_color=C_USDC, stroke_color=GREEN, stroke_width=0)
# USDT_COIN = create_circle_asset(Tex(r'\textbf{USDT}',color=WHITE), font_size =10, WHITE, fill_color=C_USDT, stroke_color=GREEN, stroke_width=0)
# MATIC_COIN = create_circle_asset(Tex(r'\textbf{MATIC}',color=WHITE), 20, WHITE, fill_color=C_MATIC, stroke_color=GREEN, stroke_width=0)
# LINK_COIN = create_circle_asset(Tex(r'\textbf{LINK}',color=WHITE), font_size =10, WHITE, fill_color=C_LINK, stroke_color=GREEN, stroke_width=0)
# FTX_COIN = create_circle_asset(Tex(r'\textbf{FTX}',color=WHITE), font_size =10, WHITE, fill_color=C_FTX, stroke_color=GREEN, stroke_width=0)
# DOGE_COIN = create_circle_asset(Tex(r'\textbf{DOGE}',color=WHITE), font_size =10, WHITE, fill_color=C_DOGE, stroke_color=GREEN, stroke_width=0)
# TRON_COIN = create_circle_asset(Tex(r'\textbf{TRON}',color=WHITE), font_size =10, WHITE, fill_color=C_TRON, stroke_color=GREEN, stroke_width=0)

# COINS = VGroup(BTC_COIN, USDT_COIN, ETH_COIN, XRP_COIN, ADA_COIN, BNB_COIN, TRON_COIN, MATIC_COIN,ATOM_COIN, DOT_COIN)
# COINS.add(SOL_COIN)
# COINS.add(LINK_COIN,XMR_COIN, USDC_COIN,FTX_COIN, DOGE_COIN)
# COINS_BACKUP = COINS.copy()
# COINS_BACKUP1 = COINS.copy()
# COINS_BACKUP2 = COINS.copy()
# COINS_BACKUP3 = COINS.copy()
# COINS_BACKUP4 = COINS.copy()
