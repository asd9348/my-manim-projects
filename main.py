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
        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Write(xyk))

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt),
                  Create(x_arrow),
                  Create(y_arrow)
                  )
        self.play(Uncreate(A_coin_amt),
                  Uncreate(B_coin_amt),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        #
        # 와이는 엑스부느이 케이로 변형
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)

        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.to_edge(UP).scale(0.6))

        self.wait(1)
        #

        # 풀도 만들기

        xyk_and_liq = VGroup(xyk_fraction)

        self.play(xyk_and_liq.animate.to_edge(LEFT).shift(RIGHT))
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": True, 'font_size':20,'tip_width':0.1, 'tip_height':0.1},
                  )

        self.play(Create(ax))

        k_var = Variable(1, MathTex("k"), var_type=Integer)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        # var = 10.5
        self.wait()

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(xyk_graph))
        k_var.next_to(ax, UR)
        self.play(Create(k_var))

        self.play(k_tracker.animate.set_value(100), run_time=4)

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=5, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).next_to(xyk_fraction, DOWN, buff=0.8)

        liq_pool.set_z_index(3)

        self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4, 0.3)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider.next_to(liq_pool_rect, RIGHT, buff=0.8)))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 20, 4 ],
                  y_range=[ 0, 6000, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'include_ticks':False,'font_size':20,'tip_width':0.1, 'tip_height':0.1},
                  y_axis_config={"include_numbers": False, 'font_size':20}
                  ).to_edge(RIGHT)

        y_axis_label =ax.get_y_axis_label(MathTex('Amount of USDT in Pool').rotate(PI/2).scale(0.4),edge=LEFT,direction=LEFT)
        # self.add(y_axis_label)

        x_axis_label =ax.get_x_axis_label(MathTex('Amount of BTC in Pool').scale(0.4),edge=DOWN,direction=DOWN)
        # self.add(x_axis_label)

        axis_labels =VGroup(x_axis_label,y_axis_label)


        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=DecimalNumber, num_decimal_places=2).scale(0.8)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=DecimalNumber, num_decimal_places=2).scale(0.8).next_to(btc_var, DOWN,
                                                                                                                    aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        vars = VGroup(btc_var, usdt_var)

        vars.next_to(xyk_fraction, RIGHT, buff=2)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        self.play(Write(usdt_var),
                  Write(btc_var))

        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # usdt_bar.add_updater(lambda usdt_bar : usdt_bar.become(Rectangle(height=usdt_tracker.get_value()/10, width=1.2, color=BLUE).align_to(usdt_bar_pos, DOWN)))

        # self.play(usdt_tracker.animate.set_value(4000))
        # self.play(btc_tracker.animate.set_value(30))

        # self.play(k_var.animate.set_value(30000))
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))

        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=BLUE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 20 ],
                    use_smoothing=False, color=BLUE)))

        curr_dot = Dot(radius=0.1, color=RED).move_to(ax.c2p(btc_tracker.get_value(),
                                                             xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                     xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                        xyk_graph_btc.underlying_function(
                                                                                            btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))

        x_marker= Triangle(color=ORANGE, fill_color=ORANGE).scale(0.2).move_to(vertical_line,DOWN,)
        x_marker_val = Integer(btc_tracker.get_value()).move

        lines = VGroup(vertical_line, horizontal_line)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)

        # 사각형을 만들고 그 넓이와 길이는 점선 그리고 정렬을 원점에 nexxt to DR buff 0
        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        # area.add_updater(lambda)
        # print(ax.get_origin()-curr_dot.get_x())
        # print(ax.get_origin().get-curr_dot.get_y())

        self.play(Create(area))
        self.play(Create(area_text))

        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))

        self.wait(1)

        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))

        # self.play(Create(ax))

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
