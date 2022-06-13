from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_functions import *
from gtts import gTTS
from io import BytesIO
from gtts import gTTS
from tempfile import NamedTemporaryFile
from pathlib import Path
import shutil
from pprint import pprint

config.frame_width = 16
config.frame_height = 9
# config.background_color=WHITE

q = 0.3
qq = 2 * q
qqq = 3 * q

t = 3
tt = 5
ttt = 7

L = LEFT
R = RIGHT
U = UP
D = DOWN


class final(Scene):
    def construct(self):
        pass

        # lec1_s1.construct(self)
        # lec1_s2.construct(self)
        # lec1_s3.construct(self)
        # lec1_s4.construct(self)
        # working.construct(self)


class working2(Scene):
    def construct(self):
        dot = LabeledDot('Fuck')
        title = 'L02S04'

        # 씬 1에써 디센트럴 네트워크 메인 선 2개 더 끊어져야됨
        # 씬1에서 이밸앤 오딧 바 짧게
        # 씬1에서 설사 코인 좀 더 크게

        # 씬3에서 체인이 생기기 전까지만 재생하고 그 다음 체인은 롯츠오브피 슬로우스피드와 같이 재생하면서 존나 느리게
        # 씬4에서 테더 자산 색 변경

        # 씬5부터 전부 해당 엑스춛 레이블 간격
        # 안 맞음
        # 씬5에서 케이값 변경에 따라서 좌표값 안 움직임
        # 씬6에서 쉐어에 178분의 87이라고 값 한 번 주기
        # 씬6에서 오리지널 그래프느 녹색으로 가자
        # 씬7에서는 이닛 제공자 없애지 말고 그냥 냅두기
        # 씬8에 색 안 맞음
        # 씬10 유저 돈트 오타

        circles = VGroup()

        for i in range(0, 360, 10):
            circle = Circle(radius=0.5, stroke_width=0, fill_color=Color(hsl=(i / 360, 1, 0.5)), fill_opacity=1)
            text = Tex(f'{int((i + 10) / 10)}', color=BLACK).move_to(circle)
            circle.add(text)

            circles.add(circle)

        sat = 0
        for i in range(9):
            sat += 0.1
            circle = Circle(radius=0.5, stroke_width=0, fill_color=Color(hsl=(10 / 360, sat, 0.5)), fill_opacity=1)
            text = Tex(f'{i + 1}', color=BLACK).move_to(circle)
            circle.add(text)
            circles.add(circle)

        lum = 0
        for i in range(9):
            lum += 0.1
            circle = Circle(radius=0.5, stroke_width=0, fill_color=Color(hsl=(10 / 360, 1, lum)), fill_opacity=1)
            text = Tex(f'{i + 1}', color=BLACK).move_to(circle)
            circle.add(text)
            circles.add(circle)

        circles.arrange_in_grid(6, 9).scale(1.1)

        test_circle = Circle(fill_color=W02, fill_opacity=1)

        speak(self, title='테스트입니다', txt=
        '그렇다면 이 덱스라는 게 존재하는 이유는 무엇일까요#1'
        '일단 중앙화 주체 없이 운영되는 거래소이기 때문에 오는 장점이 잇습니다#1'
        '덱스는 중앙화 서버가 없고 탈중앙화된 네트워크에 의존하기 때문에 #1'
        '전쟁과 같은 물리적인 위험에서도 중앙서버가 망가지면 네트워크가 마비되는 중앙화 거래소와 달리 훨씬 안전합니다#1'
        '#1'
        '그러나 블록체인 네트워크도 트래픽이 많으면 느려지고#1'
        '심지어 최근 솔라나나 클레이튼 같은 대형체인도 정지하는 일이 심심치 않게 발생합니다#1'
        '그래서 무작정 중앙서버보다 좋다고만은 할 수도 없습니다#1'
        '또 덱스는 정부의 검열으로부터 자유로울 수 있고 프라이버시를 보호할 수 있습니다#1'
        '모든 기록이 블록체인에 남지만 그 주소가 누군지 매칭이 안 되기 때문에 익명성이 보장됩니다#1'
        '그리고 거래소의 심사 없이 코인을 자유롭게 상장할 수 있습니다#1'
        '크립토 프로젝트들은 거래소에서 심사를 거쳐 상장이 되야하는데 이 기준이 엄격하다보니, 거래소에는 한정된 코인들만 있습니다.#1'
        '그러나 덱스에서는 누구나 유동성 풀을 만들어 다른 사람들의 거래를 도울 수 있습니다#1'
              ,keep_pitch=True, update=True, speed=1.4)

        self.play(Create(test_circle, run_time=5))

        self.add(test_circle)

        # self.wait(5)


class working1(Scene):
    def construct(self):
        title = 'L02S04'

        # print(self.my_title)

        circle = Circle()
        self.play(Create(circle))
