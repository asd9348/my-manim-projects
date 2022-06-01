import math

from manim import *
import itertools as it
import random as rd
import numpy as np

config.frame_width = 16
config.frame_height = 9
from hashlib import sha256
import binascii

from colour import Color


# utils.tex.TexTemplate(tex_compiler="latex")


def sha256_bit_string(message):
    hexdigest = sha256(message.encode('utf-8')).hexdigest()
    return bin(int(hexdigest, 16))[ 2: ]


q = 0.3


def reverse(t: float) -> float:
    return -t + 1


# class SimpleLine(Line):


def create_asset_mob(text, width=0.5, height=0.3, fill_color=GREEN, stroke_color=GREEN):
    box = Rectangle(width=width, height=height, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1)
    text = Text(text, color=BLACK).scale(height)

    return VGroup(box, text)


def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
    person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

    box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
    text = Text(asset_name, color=BLACK).scale(asset_height)

    asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

    return VGroup(person, asset)


#
# def bit_string_to_mobject(bit_string):
#     line = Tex("0" * 32)
#     pre_result = VGroup(*[
#         line.copy() for row in range(8)
#     ])
#     pre_result.arrange(DOWN, buff=SMALL_BUFF)
#     result = VGroup(*it.chain(*pre_result))
#     result.scale(0.7)
#     bit_string = (256 - len(bit_string)) * "0" + bit_string
#     result
#
#     for i, (bit, part) in enumerate(zip(bit_string, result)):
#         if bit == "1":
#             one = Tex("1")[ 0 ]
#             one.replace(part, dim_to_match=1)
#             result.submobjects[ i ] = one
#
#     return result
#


class LabeledRectangle(RoundedRectangle):

    def __init__(
            self,
            label: str or SingleStringMathTex or Text or Tex,
            width: float or None = None,
            height: float or None = None,
            corner_radius: float or None = None,
            direction: np.ndarray = UP,
            **kwargs, ) -> None:

        if isinstance(label, str):
            from manim import Tex

            rendered_label = Tex(label, color=WHITE)
        else:
            rendered_label = label

        if width is None:
            width = 0.2 + max(rendered_label.width, rendered_label.height)
        if height is None:
            height = 0.2 + max(rendered_label.height, rendered_label.height)

        if corner_radius is None:
            corner_radius = 0.2

        super().__init__(width=width, height=height, corner_radius=corner_radius, **kwargs)
        rendered_label.next_to(self, direction)
        self.add(rendered_label)


def msg_to_mob(msg, width, rows, buff=0.2):
    if rows % 2 != 0:
        raise Exception('2의 배수가 아닙니다.')

    msg = sha256_bit_string(msg)

    half_rows = int(rows / 2)
    i = 0
    chopped_list = [ msg[ i: i + width ] for i in range(0, len(msg), width) ]
    starts = chopped_list[ :half_rows - 1 ]
    ends = chopped_list[ -half_rows - 1: ]

    starts.extend(ends)
    starts.insert(half_rows, r"\vdots")

    mobs = VGroup()
    for row in range(rows + 1):
        mobs.add(MathTex(starts[ row ]))
        # if row= half_rows:
        # mobs.add(MathTex(""))

    mobs.arrange_in_grid(6, 1, buff=buff)

    return mobs


#
# def sha256_tex_mob(message, n_forced_start_zeros=30):
#     true_bit_string = sha256_bit_string(message)
#     n = n_forced_start_zeros
#     bit_string = "0" * n + true_bit_string[ n: ]
#     return bit_string_to_mobject(bit_string)
#

def create_asset_mob(text, width=0.5, height=0.3, fill_color=GREEN, stroke_color=GREEN):
    box = Rectangle(width=width, height=height, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1)
    text = Text(text, color=BLACK).scale(height)

    return VGroup(box, text)


def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
    person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

    box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
    text = Text(asset_name, color=BLACK).scale(asset_height)

    asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

    return VGroup(person, asset)


class final(Scene):
    def construct(self):
        pass
        # lec1_s1.construct(self)
        # lec1_s2.construct(self)
        # lec1_s3.construct(self)
        # lec1_s4.construct(self)
        # working.construct(self)
        self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))
        self.play(A_asset_btc.animate.move_to(B_asset_pos))
        self.play(A_asset_btc.animate.move_to(A_asset_pos))
        self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))
        self.play(A_asset_btc.animate.move_to(A_wallet_rect))
        # self.play(A_asset_btc.animate.move_to(ex_wallet_rect))
        self.play(A_asset_btc.animate.move_to(ex_server))


class working(Scene):
    def construct(self):
        # 스테이블 코인 텍스트 보여줌
        stablecoin = Tex('Stablecoin').scale(2)
        self.play(Create(stablecoin))

        self.wait(q)
        self.play(Uncreate(stablecoin))
        #


        # 기업 혹은 거래소 박스 형성 (중앙ㅇ에 할거고 이건 왼쪽은 은행이나 채권 만들고)
        tether_company = LabeledRectangle('Company or Exchange', height=8,width=4 corner_radius=0.5, direction=UP)
        self.play(Create(tether_company))
        #
        # 고객 엔터티 오른 쪽에 생성하고 법정화폐 붙임
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)

        #
        # 그리고 고객들 돈을 기업으로 전송
        #
        # 기업에서 테더 발행
        #
        # 테더는 다시 엔터티에게 전송
        #
        # 그리고 달러 중 일부는 은행이나 채권등으로 투자
        #
        # 엔터티 중 한명이 테더를 반납하면 달러로 돌려줌
        #
        # 전부 ㅇ벗어지고 알고리드믹 스테이블코인, 코인담보 스테이블 등이 있으나 나중에 알아보자
        #




        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text).move_to(ORIGIN)
        pair.set_z_index(3)

        # self.add(pair, ru))

        self.wait(q)

        dummy = IntegerTable(
            [
                [ 1000000 ]
            ],
            row_labels=[ Tex(r"105\$") ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5)

        # self.play(Create(dummy))
        # self.add(index_labels(dummy))

        curr_px_height = dummy[ 1 ].get_y() - dummy[ 2 ].get_y()
        curr_px_width = dummy[ 4 ].get_x() - dummy[ 3 ].get_x()
        curr_px_rect = Rectangle(width=curr_px_width, height=curr_px_height, color=RED)
        curr_px_rect.set_z_index(3)

        curr_px_valuetracker = ValueTracker(100)
        curr_px_val = str(int(curr_px_valuetracker.get_value()))
        # curr_px_number = Tex(rf'{curr_px_val}\$').move_to(curr_px_rect)
        curr_px_number_100 = Integer(curr_px_valuetracker.get_value(), unit=r"\$", color=RED).move_to(curr_px_rect)
        curr_px_number_103 = Integer(curr_px_valuetracker.get_value(), unit=r"\$", color=GREEN).move_to(curr_px_rect)

        # curr_px_number.add_updater(lambda x : x.become(Integer(curr_px_valuetracker.get_value(), unit=r"\$")))

        # curr_px =VGroup(curr_px_rect,curr_px_number_100)

        int_valuetracker = ValueTracker(100)

        my_int = Integer(int_valuetracker.get_value(), unit=r"\$").to_edge(UR)

        # # my_int.add_updater()
        # self.play(Create(curr_px_rect))
        # # self.play(curr_px_valuetracker.animate.set_value(120))
        #
        # self.play(FadeIn(curr_px_number_100), run_time=0.01)
        #
        order_book_shrt_table = IntegerTable(
            [ [ 300000 ],
              [ 200000 ],
              [ 100000 ],
              [ 10000 ],
              [ 1000 ],
              [ 100 ],
              [ 50 ]
              ],
            row_labels=[ Tex(r"107\$"),
                         Tex(r"106\$"),
                         Tex(r"105\$"),
                         Tex(r"104\$"),
                         Tex(r"103\$"),
                         Tex(r"102\$"),
                         Tex(r"101\$")
                         ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 1}).scale(0.5).next_to(curr_px_rect, UP, buff=0)

        for i in range(1, 8):
            for j in range(1, 3):
                order_book_shrt_table.add_highlighted_cell((i, j), fill_opacity=0.2, color=RED_A)

        order_book_shrt_table.set_row_colors(RED, RED, RED, RED, RED, RED, RED)

        order_book_long_table = IntegerTable(
            [ [ 0 ],
              [ 0 ],
              [ 50 ],
              [ 100 ],
              [ 1000 ],
              [ 10000 ],
              [ 100000 ]
              ],
            row_labels=[ Tex(r"102\$"),
                         Tex(r"101\$"),
                         Tex(r"100\$"),
                         Tex(r"99\$"),
                         Tex(r"98\$"),
                         Tex(r"97\$"),
                         Tex(r"96\$")
                         ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 1}).scale(0.5).next_to(curr_px_rect, DOWN, buff=0)

        for i in range(1, 6):
            for j in range(1, 3):
                order_book_long_table.add_highlighted_cell((i, j), fill_opacity=0.2, color=GREEN_A)

        order_book_long_table.set_row_colors(GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN)

        def change_waiting_order(self, table, r, c, new_val, run_time):
            a = table.get_entries(pos=(r, c))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        def change_waiting_order_by_perc(self, table, r, c, perc, run_time):
            a = table.get_entries(pos=(r, c))

            new_val = int(a.get_value() * ((100 + perc) / 100))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        # self.play(Create(order_book_long_table), Create(order_book_shrt_table))

        # self.play(curr_px_number_100)

        def table2cells(table, r, c, opa, color):
            cells = VGroup()
            for i in range(1, r + 1):
                for j in range(1, c + 1):
                    text = table.get_entries(pos=(i, j)).copy()
                    box = table.get_cell((i, j), stroke_width=table.line_config[ "stroke_width" ],
                                         stroke_opacity=table.line_config[ "stroke_opacity" ],
                                         stroke_color=table.line_config[ "stroke_color" ])
                    bg_rect = table.get_highlighted_cell(pos=(i, j), fill_opacity=opa, color=color)
                    cell = VGroup(text, box, bg_rect)
                    cells.add(cell)

            return cells

        separated_shrt_table = table2cells(order_book_shrt_table, 7, 2, 0.2, RED_A)
        separated_shrt_table.set_z_index(1)

        shrt_black_sheet = Rectangle(width=4, height=5, fill_color=BLACK, fill_opacity=1, stroke_opacity=0, stroke_width=0).next_to(
            separated_shrt_table[ 4 ], UP, buff=0.01).shift(RIGHT)
        shrt_black_sheet.set_z_index(2)

        separated_long_table_org = table2cells(order_book_long_table, 7, 2, 0.2, GREEN_A)
        separated_long_table = separated_long_table_org[ 4: ].next_to(curr_px_rect, DOWN, buff=0.01)

        long_black_sheet = Rectangle(width=4, height=5, fill_color=BLACK, fill_opacity=1, stroke_opacity=0, stroke_width=0).next_to(
            separated_long_table[ 9 ], DOWN, buff=0).shift(LEFT)
        long_black_sheet.set_z_index(2)

        # self.add(index_labels(separated_long_table))
        # self.play(Create(shrt_black_sheet), run_time=0.1)
        # self.play(Create(long_black_sheet), run_time=0.1)
        # self.play(Create(separated_shrt_table),
        #           Create(separated_long_table))

        self.add(shrt_black_sheet, long_black_sheet)
        order_book = VGroup(pair, curr_px_number_100, curr_px_rect, separated_shrt_table, separated_long_table)


        self.play(Create(order_book))


        self.wait(q)

        cross = Cross(stroke_width=25).scale(3)

        self.play(Create(cross))

        # self.play(FadeOut(*[self.mobjects]))

        self.play(FadeOut(VGroup(order_book,cross)))
        self.remove(shrt_black_sheet, long_black_sheet)



        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        #
        # 와이는 엑스부느이 케이로 변형
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        #
        # 중학교 때 배운 반비례 그래프
        #
        # 전부 없어짐
        #
        # 최초의 덱스 렉탱글 만들고 btc usd 풀로 만듦
        #
        #
        # 유동성 거래자 엔터티 만듦
        #
        #
        # 중앙화 거래혹 조그만 거 만듦,  가격 인테저 만듦
        #
        # 유동성 거래자가 중앙화 거래소 가격이 300달러인 걸 보고 비트코인 10개와 3000테더를 전송
        #



        self.wait(q)