from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_color_consts import *

config.frame_width = 16
config.frame_height = 9

BTC = C_BTC
ETH = C_ETH
DOT = C_DOT
SOL2 = C_SOL2
USDT = C_USDT

class final(Scene):
    def construct(self):
        L_02_S_01_dex_pros_and_cons.construct(self)
        L_02_S_02_smart_contract.construct(self)

class L01S01(MovingCameraScene):
    def construct(self):
        speak(self, title='Scene2', txt=
        '이제 본격적으로 디파이에 대해 알아보겠습니다#1'
        '디파이의 가장 근간이 되는 것은 탈중앙화 거래소입니다#1'
        '탈중앙화 거래소는 디센트럴라이즈드 익스체인지로 줄여서 덱스라고 부릅니다#1'
        '탈중앙화 거래소는 말그대로 중앙화된 주체가 없는 거래소입니다#1'
        '모든 거래들이 중앙 주체를 거치지 않고 블록체인에 트랜잭션으로 기록되는 것입니다#1'
        '마치 비트코인 네트워크가 만든사람도 없어진 뒤에 스스로 혼자 계속 작동하듯#1'
        '덱스도 중앙화된 주체 없이 블록체인상에서 끊임없이 돌아갑니다#1'
              , keep_pitch=True, update=False, speed=1.4)

        self.wait(5)
