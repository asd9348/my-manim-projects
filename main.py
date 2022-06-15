import manim
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

BTC = C_BTC
ETH = C_ETH


class final(Scene):
    def construct(self):
        pass

        # lec1_s1.construct(self)
        # lec1_s2.construct(self)
        # lec1_s3.construct(self)
        # lec1_s4.construct(self)
        # working.construct(self)


class working3(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[RPvoltages]{circuitikz}")

        salikop = MathTex(
            r"""\draw (6,0) to[battery2] (0,0) ;""",
            r"""\draw (0,0) to[short] (0,2) ;""",
            r"""\draw (0,2) to[L] (6,2) ;""",
            r"""\draw (6,2) to[short] (6,0) ;""",
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=1,
            tex_environment="circuitikz",
            tex_template=template
        ).scale(1)

        template.get_texcode_for_expression_in_env(salikop, "circuitikz")

        self.wait()
        self.play(Create(salikop), run_time=4)
        self.wait(2)

class working2(Scene):
    def construct(self):
        self.add(NumberPlane())
        script = speak(self, title='Scene2', txt=
        '그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다#1'
                       , keep_pitch=True, update=True, speed=1.4)

        mtex_1 = MathTex('dfjk')
        tex_1 = Tex('dkfjkd')

        amm_text = Tex('{{A}}utomatic {{M}}arket {{M}}aker').scale(2)
        self.play(Create(amm_text))
        amm_acronym_text = Tex('{{A}}{{M}}{{M}}').scale(2).move_to(amm_text)
        self.play(TransformMatchingTex(amm_text, amm_acronym_text), run_time=t)


        self.wait(5)



class working1(Scene):
    def construct(self):
        dummy_for_order_book = Tex('djfk',color = WHITE).scale(4)
        # self.play(Create())
        self.play(Uncreate(dummy_for_order_book), run_time = 0.001)

        self.add(NumberPlane())
        speak(self, title='강의1', txt=
        '그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다#1'
        '대신 오토매틱 마켓 메이커라는 것을 사용합니다#1'
        '에이엠엠은 오토매틱 마켓 메이커의 약자로 오더북없이 가격을 결정하는 방식 혹은 알고리즘이라고 생각하면 됩니다#1'
        '일반적으로 엑스 와이는 케이라는 식을 사용하여 가격을 결정합니다#1'
        '이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다#1'
        '원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다#1'
        '최초의 뎩스가 탄생하고 사람들은 비트코인과 테더의 거래쌍을 만들고 싶었습니다.#1'
        '그래서 중앙화 거래소에서 비트코인 가격이 300테더인 걸 보고#1'
        '비트코인 10개와 3000테더를 함께 유동성 풀이라는 것에 넣었습니다#1'
        '이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.#1'
        '이제 이 유동성 제공자로 인하여 덱스참여자는 비트코인과 테더 거래쌍을 이용할 수 있습니다#1'
              , keep_pitch=True, update=True, speed=1.4)


        # TODO 3.697 secs그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다
        # TODO 1.0 secs pause
        # TODO 3.141 secs대신 오토매틱 마켓 메이커라는 것을 사용합니다
        # TODO 1.0 secs pause

        amm_text = Tex('{{A}}utomatic {{M}}arket {{M}}aker').scale(2)
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)

        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)

        dummy = IntegerTable(
            [
                [ 1000000 ]
            ],
            row_labels=[ Tex(r"105\$") ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5)

        curr_px_height = dummy[ 1 ].get_y() - dummy[ 2 ].get_y()
        curr_px_width = dummy[ 4 ].get_x() - dummy[ 3 ].get_x()
        curr_px_rect = Rectangle(width=curr_px_width, height=curr_px_height, color=RED)

        curr_px_number_100 = Integer(100, unit=r"\$", color=RED).move_to(curr_px_rect)

        self.play(Create(curr_px_rect),run_time=0.25)

        self.play(FadeIn(curr_px_number_100), run_time=0.25)

        order_book_shrt_table = IntegerTable(
            [ [ 100000 ],
              [ 10000 ],
              [ 1000 ],
              [ 100 ],
              [ 50 ]
              ],
            row_labels=[ Tex(r"105\$"),
                         Tex(r"104\$"),
                         Tex(r"103\$"),
                         Tex(r"102\$"),
                         Tex(r"101\$")
                         ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5).next_to(curr_px_rect, UP, buff=0)

        for i in range(1, 6):
            for j in range(1, 3):
                order_book_shrt_table.add_highlighted_cell((i, j), fill_opacity=0.2, color=RED_A)

        order_book_shrt_table.set_row_colors(RED, RED, RED, RED, RED)

        order_book_long_table = IntegerTable(
            [ [ 50 ],
              [ 100 ],
              [ 1000 ],
              [ 10000 ],
              [ 100000 ]
              ],
            row_labels=[ Tex(r"100\$"),
                         Tex(r"99\$"),
                         Tex(r"98\$"),
                         Tex(r"97\$"),
                         Tex(r"96\$")
                         ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5).next_to(curr_px_rect, DOWN, buff=0)

        for i in range(1, 6):
            for j in range(1, 3):
                order_book_long_table.add_highlighted_cell((i, j), fill_opacity=0.2, color=GREEN_A)

        order_book_long_table.set_row_colors(GREEN, GREEN, GREEN, GREEN, GREEN)

        self.play(Create(order_book_long_table), Create(order_book_shrt_table),run_time=0.5)

        self.wait(1)


        order_book_cross = Cross(stroke_width=25).scale(3)
        order_book_stuff = VGroup(curr_px_rect, curr_px_number_100, order_book_long_table, order_book_shrt_table, order_book_cross)
        self.play(Create(order_book_cross), run_time=1)
        self.wait(0.5)

        self.play(AnimationGroup(ReplacementTransform(order_book_stuff,dummy_for_order_book),
                                 GrowFromCenter(amm_text),lag_ratio=0.2), run_time=2.5)
        self.wait(0.5)

        # TODO 7.007 secs에이엠엠은 오토매틱 마켓 메이커의 약자로 오더북없이 가격을 결정하는 방식 혹은 알고리즘이라고 생각하면 됩니다
        # TODO 1.0 secs pause


        amm_acronym_text = Tex('{{A}}{{M}}{{M}}').scale(2).move_to(amm_text)
        self.play(TransformMatchingTex(amm_text, amm_acronym_text), run_time=t)
        self.wait(t)

        ##### 그냥 프로그램 혹은 가격을 정하는 방식같은 추상적 개념이라고 생각하시면 됩니다
        # 에이엠엠 텍스트 밑에 프로그램 혹은 컨셉
        program_or_concept_text = Tex('Program or Concept?').next_to(amm_text, D)
        self.play(Create(program_or_concept_text), run_time=t)
        self.wait(t)



        # TODO 4.192 secs일반적으로 엑스 와이는 케이라는 식을 사용하여 가격을 결정합니다
        # TODO 1.0 secs pause

        # TODO 3.684 secs이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다

        # TODO 1.0 secs pause

        # TODO 9.894 secs원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다

        # TODO 1.0 secs pause

        # TODO 5.134 secs최초의 뎩스가 탄생하고 사람들은 비트코인과 테더의 거래쌍을 만들고 싶었습니다.

        # TODO 1.0 secs pause

        # TODO 3.987 secs그래서 중앙화 거래소에서 비트코인 가격이 300테더인 걸 보고

        # TODO 1.0 secs pause

        # TODO 4.506 secs비트코인 10개와 3000테더를 함께 유동성 풀이라는 것에 넣었습니다

        # TODO 1.0 secs pause

        # TODO 5.182 secs이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.

        # TODO 1.0 secs pause

        # TODO 5.823 secs이제 이 유동성 제공자로 인하여 덱스참여자는 비트코인과 테더 거래쌍을 이용할 수 있습니다

        # TODO 1.0 secs pause


        self.play(Create(xyk), run_time=tt)
        self.wait(t)

        # TODO 3.684 secs이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다
        # TODO 1.0 secs pause

        # TODO 9.894 secs원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다
        # TODO 1.0 secs pause



        # TODO 5.919 secs최초의 뎩스가 탄생하고 사람들은 비트코인과 usdt의 거래쌍을 만들고 싶었습니다.
        # TODO 1.0 secs pause

        expl_plain_text = Text(
            'DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n그래서 중앙화 거래소에서 BTC 가격이 300 USDT인 걸 보고\n10 BTC와 3000USDT를 함께 유동성 풀이라는 것에 넣었습니다\n스마트 컨트랙트를 통해 자신의 자산을 유동성으로 제공한다는 것입니다.\n이제 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다.',
            font='Batang', line_spacing=3, font_size=25)
        self.play(Create(expl_plain_text), run_time=ttt)
        self.wait(t)

        self.play(Uncreate(expl_plain_text), run_time=t)
        self.wait(t)



        # TODO 4.011 secs그래서 중앙화 거래소에서 비트코인 가격이 300달러인 걸 보고
        # TODO 1.0 secs pause

        # TODO 4.506 secs비트코인 10개와 3000달러를 함께 유동성 풀이라는 것에 넣었습니다
        # TODO 1.0 secs pause

        # TODO 5.182 secs이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.
        # TODO 1.0 secs pause

        # TODO 5.823 secs이제 이 유동성 제공자로 인하여 덱스참여자는 비트코인과 테더 거래쌍을 이용할 수 있습니다
        # TODO 1.0 secs pause


        expl_plain_text = Text(
            'DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n그래서 중앙화 거래소에서 BTC 가격이 300 USDT인 걸 보고\n10 BTC와 3000USDT를 함께 유동성 풀이라는 것에 넣었습니다\n스마트 컨트랙트를 통해 자신의 자산을 유동성으로 제공한다는 것입니다.\n이제 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다.',
            font='Batang', line_spacing=3, font_size=25)
        self.play(Create(expl_plain_text), run_time=ttt)
        self.wait(t)

        self.play(Uncreate(expl_plain_text), run_time=t)
        self.wait(t)
        # TODO 3.854 secs몇 대 맞을래. 너희들 하는 거 보니 주먹에서 눈물이 흐른다
        # TODO 1.0 secs pause

        self.wait(5)
