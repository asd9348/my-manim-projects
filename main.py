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


class working2(Scene):
    def construct(self):
        sqs = VGroup()
        j = 0

        for i in range(100):
            j += 0.01
            sqs.add(Square(i, color=Color(hue=1-(j/1), saturation=0.8, luminance=1-(j/1))).rotate(3.6 * i * 2 * PI / 360))

        sqs.scale(0.1)
        self.play(Create(sqs), run_time=30)


class working1(Scene):
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
                  axis_config={"include_numbers": True, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
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

        self.play(k_tracker.animate.set_value(300), run_time=4)

        xyk_fraction.save_state()

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(xyk_fraction),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=6, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4, 0.3)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider.next_to(liq_pool_rect, RIGHT, buff=1)))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 20, 4 ],
                  y_range=[ 0, 6000, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(DR, buff=0.8)

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool').rotate(PI / 2).scale(0.4), edge=LEFT, direction=LEFT, buff=0.5)
        # self.add(y_axis_label)

        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool').scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        # self.add(x_axis_label)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        # usdt_var_bar=usdt_var[ 1 ].copy()
        # btc_var_bar=usdt_var[ 1 ].copy()
        # usdt_var_bar.set_color(BLACK)
        # btc_var_bar.set_color(BLACK)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT)

        vars.next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        # self.play(Write(usdt_var_bar),
        #           Write(btc_var_bar))
        #
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
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR, buff=0.5)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))
        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))

        xyk_fraction.restore()
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=BLUE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 20 ],
                    use_smoothing=False, color=PURPLE)))

        curr_dot = Dot(radius=0.1, color=RED).move_to(ax.c2p(btc_tracker.get_value(),
                                                             xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line

        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

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

        # self.play(btc_tracker.animate.set_value(13),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))
        #
        # self.wait(1)
        #
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))
        #
        self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        ########################################################################################올라갔을 때
        ######################################Scen1#############################올라갔을 때
        ########################################################################################올라갔을 때

        # user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "USDT", BLUE, 0.8, 0.3).next_to(liq_pool_rect, RIGHT,
        #                                                                                                                buff=2)
        # user_asset_usdt = user[ 1 ]
        # user_asset_pos = user_asset_usdt.get_center()
        # user_asset_btc = create_entity("A", 0.5, WHITE, "3 BTC", ORANGE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)
        #
        # user_line = Tex(r'I want 3 BTC\\I have some USDT').scale(0.5).next_to(user, DOWN)
        #
        # self.play(Create(user))
        # self.play(Create(user_line))
        # self.play(Uncreate(user_line))
        #
        # # self.add(index_labels(btc_bar))###
        #
        # # scene1_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene1_7btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3, stroke_color=RED_E).align_to(
        #     btc_bar[ 0 ], UL)
        # scene1_13btc_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.4286, stroke_width=3,
        #                              stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)
        #
        # scene1_7btc_fill_box = scene1_7btc_box.copy().set_fill(ORANGE, opacity=1)
        # scene1_13btc_fill_box = scene1_13btc_box.copy().set_fill(BLUE, opacity=1)
        #
        # self.play(Create(scene1_7btc_box))
        # self.play(Create(scene1_13btc_box))
        # scene1_7btc_brace = BraceBetweenPoints(scene1_7btc_box.get_corner(UL), scene1_7btc_box.get_corner(DL), color=RED_E,
        #                                        stroke_color=RED_E,
        #                                        stroke_width=3,
        #                                        ).next_to(scene1_7btc_box, LEFT)
        # scene1_13btc_brace = BraceBetweenPoints(scene1_13btc_box.get_corner(UR), scene1_13btc_box.get_corner(DR), color=GREEN_E,
        #                                         stroke_color=GREEN_E, stroke_width=3
        #                                         ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene1_13btc_box,
        #                                                                                       RIGHT)
        #
        # scene1_7btc_brace_label = Integer(btc_tracker.get_value())
        # scene1_7btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(3).scale(0.4).rotate(PI / 2).next_to(scene1_7btc_brace, LEFT, buff=0.3)))
        # scene1_13btc_brace_label = Integer(usdt_tracker.get_value())
        # scene1_13btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(1286).scale(0.4).rotate(-PI / 2).next_to(scene1_13btc_brace, RIGHT, buff=0.3)))
        #
        # scene1_braces = VGroup(scene1_7btc_brace, scene1_13btc_brace)
        # scene1_brace_labels = VGroup(scene1_7btc_brace_label, scene1_13btc_brace_label)
        #
        # self.play(Create(scene1_braces),
        #           Create(scene1_brace_labels))
        #
        # usdt_bar.clear_updaters()
        # btc_bar.clear_updaters()
        #
        # self.add(scene1_7btc_fill_box)
        # # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        # #     Rectangle(height=4283 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        # #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=7 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))
        #
        # origin_dot = curr_dot.copy()
        # origin_dot.clear_updaters()
        #
        # self.play(Create(origin_dot))
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
        #           Transform(scene1_7btc_fill_box, user_asset_btc),
        #           Transform(user_asset_usdt, scene1_13btc_fill_box))
        #
        # scene1_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=-4, tip_length=0.25).shift(
        #     RIGHT * 0.3 + UP * 0.3)
        # scene1_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene1_arrow, UR)
        #
        # self.play(Create(scene1_arrow))
        #
        # scene1_slippage_text = Tex(r'I just used 1283 USDT \\to buy 3 BTC').scale(0.5).next_to(user_asset_pos, DOWN)
        # scene1_slippage_form = MathTex(r'1283 \divisionsymbol 3').next_to(scene1_slippage_text, DOWN)
        # scene1_slippage_result = MathTex(rf'{int((k_tracker.get_value() / btc_tracker.get_value()-3000)/3)}\$ \  per\ BTC ').move_to(scene1_slippage_form.get_center())
        #
        # self.play(Create(scene1_slippage_form),
        #           Create(scene1_slippage_text))
        #
        # self.play(ReplacementTransform(scene1_slippage_form,scene1_slippage_result))
        #
        # # self.play()
        #
        #
        #
        # # self.play(Restore(whole_mobs))
        #
        # self.wait(2)

        #######################################################################################
        #################################scene2##############################################
        #######################################################################################

        #
        user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "BTC", ORANGE, 0.8, 0.3).next_to(liq_pool_rect,
                                                                                                                        RIGHT, buff=2)
        user_asset_btc = user[ 1 ]
        user_asset_pos = user_asset_btc.get_center()
        user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", BLUE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want to sell 3 BTC\\I dont have some USDT').scale(0.5).next_to(user, DOWN)

        self.play(Create(user))
        self.play(Create(user_line))
        self.play(Uncreate(user_line))

        # self.add(index_labels(btc_bar))###

        # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
                                        stroke_color=RED_E).align_to(
            usdt_bar, UL)
        scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)

        scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(BLUE, opacity=1)
        scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(ORANGE, opacity=1)

        self.play(Create(scene2_2308usdt_box))
        self.play(Create(scene2_13btc_box))
        scene2_2308usdt_brace = BraceBetweenPoints(scene2_2308usdt_box.get_corner(UR), scene2_2308usdt_box.get_corner(DR), color=RED_E,
                                                   stroke_color=RED_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene2_2308usdt_fill_box,
                                                                                                 RIGHT)
        scene2_13btc_brace = BraceBetweenPoints(scene2_13btc_box.get_corner(UL), scene2_13btc_box.get_corner(DL), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).next_to(scene2_13btc_fill_box,
                                                          LEFT)

        scene2_2308usdt_brace_label = Integer(btc_tracker.get_value())
        scene2_2308usdt_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(-PI / 2).next_to(scene2_2308usdt_brace, RIGHT, buff=0.3)))
        scene2_13btc_brace_label = Integer(usdt_tracker.get_value())
        scene2_13btc_brace_label.add_updater(lambda label: label.become(
            Integer(692).scale(0.4).rotate(PI / 2).next_to(scene2_13btc_brace, LEFT, buff=0.3)))

        scene2_braces = VGroup(scene2_2308usdt_brace, scene2_13btc_brace)
        scene2_brace_labels = VGroup(scene2_2308usdt_brace_label, scene2_13btc_brace_label)

        self.play(Create(scene2_braces),
                  Create(scene2_brace_labels))

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene2_2308usdt_fill_box)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height= 2307/ 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=13 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()

        self.play(Create(origin_dot))
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  Transform(scene2_2308usdt_fill_box, user_asset_usdt),
                  Transform(user_asset_btc, scene2_13btc_fill_box))

        scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)

        # bars.clear_updaters()
        # vars.clear_updaters()
        # k_var.clear_updaters()
        # area.clear_updaters()
        # curr_dot.clear_updaters()
        # axis_labels.clear_updaters()
        # markers.clear_updaters()
        self.play(Create(scene2_arrow))

        # self.play(Restore(whole_mobs))
        
        scene2_slippage_text = Tex(r'I just sold 3 BTC \\and got 602 USDT').scale(0.5).next_to(user_asset_pos, DOWN)
        scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        scene2_slippage_result = MathTex(rf'{int(-(k_tracker.get_value() / btc_tracker.get_value()-3000)/3)}\$ \  per\ BTC ').move_to(scene2_slippage_form.get_center())

        self.play(Create(scene2_slippage_form),
                  Create(scene2_slippage_text))

        self.play(ReplacementTransform(scene2_slippage_form,scene2_slippage_result))


        self.wait(2)

        self.wait(2)
        #######################################################################################
        #################################scene2##############################################
        #######################################################################################
