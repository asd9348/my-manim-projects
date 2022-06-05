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

q = 0.3
qq = 2 * q
qqq = 3 * q

L = LEFT
R = RIGHT
U = UP
D = DOWN


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

class backed_by(Scene):
    def construct(self):
        def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
            person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

            box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
            text = Text(asset_name, color=BLACK).scale(0.8*asset_height)

            asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

            return VGroup(person, asset)


        usdt = create_entity("A", 0.5, WHITE, "USDT", BLUE, 2, 1)[ 1 ].to_edge(UL, buff=1)
        usd = create_entity("A", 0.5, WHITE, "USD", GREEN, 2, 1)[ 1 ].to_edge(DL, buff=1)
        usg = LabeledDot(Tex(r'\emph{US\\Gov}',color=BLACK ), radius=1)[ 0].to_edge(D, buff=0.5)
        us_people = LabeledDot(Tex(r'\emph{US\\People}',color=BLACK), radius=1)[ 0].to_edge(DR, buff=0.5)

        backed_by_1 = Tex('Backed by').move_to(np.array([usdt.get_x(),0,0]))
        backed_by_2 = Tex('Backed by')
        backed_by_3 = Tex('Backed by').move_to(np.array([usg.get_x(),0,0]))


        self.play(Create(usdt))
        self.play(Create(backed_by_1))
        self.play(Create(usd))
        self.play(TransformFromCopy(usd, usd.copy().move_to(ORIGIN).to_edge(U, buff=1)))
        self.play(Create(backed_by_2))
        self.play(Create(usg))
        self.play(TransformFromCopy(usg, usg.copy().move_to(ORIGIN).to_edge(UR, buff=0.5)))
        self.play(Create(backed_by_3))
        self.play(Create(us_people))

        self.wait(q)





class dex_and_smart_contract(Scene):
    def construct(self):
        dex_text = MathTex('DEX').scale(2).shift(L * 4)
        cex_text = MathTex('CEX').scale(2).shift(R * 4)
        self.play(Create(dex_text), Create(cex_text))

        q_mark = Tex('?').scale(8)

        self.play(ReplacementTransform(VGroup(dex_text, cex_text), q_mark))

        self.play(Uncreate(q_mark))
        self.wait(q)
        chain1 = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        chain2 = Line(ORIGIN, L * 0.4).move_to(chain1).shift(L * 0.2)
        chain = VGroup()
        for i in range(3):
            chain.add(chain2.copy())
            chain.add(chain1.copy())
        chain.add(chain2.copy())
        chain.arrange(R, buff=-0.12)

        blocks = VGroup(*[ Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(5) ]).arrange(R,
                                                                                                                          buff=chain.width)
        scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.5) for i in range(5) ])

        blockchain = VGroup()
        for i in range(len(blocks)):
            blockchain.add(blocks[ i ])
            blockchain.add(scripts[ i ])
            blockchain.add(chain.copy().next_to(blocks[ i ], R, buff=0))

        blockchain.to_edge(L)

        self.play(Create(blockchain), run_time=10)

        self.play(Uncreate(blockchain))

        smart_c_text = Tex('Smart Contract').scale(2)

        self.play(Create(smart_c_text))
        self.play(Uncreate(smart_c_text))

        line1 = Line(LEFT * 3, RIGHT * 3, stroke_width=5)
        line2 = Line(DOWN * 3, UP * 3, stroke_width=5)
        dot = Dot(radius=0.3)
        rev_door = VGroup(dot, line1, line2).rotate(PI / 4)

        wall_line = Rectangle(height=10, width=0.7, stroke_width=25, )
        wall_sq = Square(7, fill_color=BLUE, fill_opacity=1)

        # self.play(Create(wall_sq))
        wall = Difference(wall_line, wall_sq, color=DARK_GREY, fill_color=DARK_GREY, fill_opacity=1)
        sector1 = AnnularSector(outer_radius=3.9, inner_radius=3.2, angle=PI / 2, color=DARK_GREY, fill_color=DARK_GREY,
                                fill_opacity=1).rotate_about_origin(PI / 4)
        sector2 = AnnularSector(outer_radius=3.9, inner_radius=3.2, angle=PI / 2, color=DARK_GREY, fill_color=DARK_GREY,
                                fill_opacity=1).rotate_about_origin(-PI / 4 - PI / 2)

        walls = VGroup(wall, sector1, sector2)
        self.play(GrowFromCenter(wall),
                  GrowFromCenter(sector1),
                  GrowFromCenter(sector2)
                  )
        self.play(Create(rev_door))
        self.play(Rotate(rev_door, angle=10 * PI), run_time=5, rate_func=rate_functions.exponential_decay)

        A = create_entity("A", 0.7, WHITE, "BTC", ORANGE, 0.8, 0.3).scale(1.2).to_edge(L)
        B = create_entity("B", 0.7, WHITE, "ETH", BLUE, 0.8, 0.3).scale(1.2).to_edge(R)

        A_asset = A[ 1 ]
        B_asset = B[ 1 ]
        A_asset_pos = A[ 1 ].get_center()
        B_asset_pos = B[ 1 ].get_center()

        A_asset_arc = Arc(radius=1.5, angle=-PI).flip(axis=UP)
        B_asset_arc = Arc(radius=1.5, angle=PI)

        self.play(Create(A),
                  Create(B))

        condition = Tex(r'A gives BTC to B\\B gives ETH to A').to_edge(UL)
        self.play(Create(condition))

        self.play(A_asset.animate.move_to(LEFT * 1.5),
                  B_asset.animate.move_to(RIGHT * 1.5))

        self.play(Rotate(rev_door),
                  MoveAlongPath(A_asset, A_asset_arc),
                  MoveAlongPath(B_asset, B_asset_arc))

        self.play(A_asset.animate.move_to(B_asset_pos),
                  B_asset.animate.move_to(A_asset_pos))

        self.play(Uncreate(condition))

        rev_door_text_1 = Tex(r'Company\\or Third Party Entity').scale(0.7).next_to(dot, R)
        rev_door_text_2 = Tex(r'Programming Language\\without Emotion').scale(0.7).next_to(dot, R)

        self.play(Create(rev_door_text_1))
        self.play(Uncreate(rev_door_text_1))

        self.play(Create(rev_door_text_2))
        self.play(Uncreate(rev_door_text_2))

        self.play(FadeOut(VGroup(walls, A, B, rev_door, rev_door_text_2)))
        self.wait(q)

class cons_of_smart_c(Scene):
    def construct(self):
        dex_text = MathTex('DEX').scale(2).shift(L * 4)
        cex_text = MathTex('CEX').scale(2).shift(R * 4)
        self.play(Create(dex_text), Create(cex_text))

        q_mark = Tex('?').scale(8)

        self.play(ReplacementTransform(VGroup(dex_text, cex_text), q_mark))

        self.play(Uncreate(q_mark))
        self.wait(q)
        chain1 = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        chain2 = Line(ORIGIN, L * 0.4).move_to(chain1).shift(L * 0.2)
        chain = VGroup()
        for i in range(3):
            chain.add(chain2.copy())
            chain.add(chain1.copy())
        chain.add(chain2.copy())
        chain.arrange(R, buff=-0.12).rotate(-PI/2)

        blocks = VGroup(*[ Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(2) ]).arrange(D,
                                                                                                                          buff=chain.height)
        scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.5) for i in range(2) ])

        blockchain = VGroup()
        for i in range(len(blocks)):
            blockchain.add(blocks[ i ])
            blockchain.add(scripts[ i ])
            blockchain.add(chain.copy().next_to(blocks[ i ], D, buff=0))

        blockchain.to_edge(U)

        self.play(Create(blockchain), run_time=10)

        # self.play(Uncreate(blockchain))

        def create_just_order(place_or_cancel, buy_or_sell, px, qty, asset):

            order_paper = Rectangle(height=1.8, width=1.5)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{qty} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order_request = VGroup(order_paper, order_text).scale(0.7)
            return order_request

        # [ 585, 793, 998, 481, 902, 418, 391, 281, 377, 806, 267, 436, 286, 715, 574 ]
        # [ 958, 548, 834, 667, 96, 464, 555, 890, 740, 404, 853, 329, 415, 579, 281 ]
        place_cancel_list_1 = [ 'Cancel', 'Place', 'Cancel', 'Cancel', 'Place', 'Cancel', 'Cancel', 'Cancel', 'Place', 'Place', 'Cancel',
                                'Cancel', 'Cancel',
                                'Cancel', 'Place' ]
        place_cancel_list_2 = [ 'Cancel', 'Place', 'Place', 'Cancel', 'Cancel', 'Place', 'Cancel', 'Place', 'Cancel', 'Cancel', 'Cancel',
                                'Place', 'Place',
                                'Place', 'Place' ]
        buy_sell_list_1 = [ 'BUY', 'SELL', 'SELL', 'SELL', 'SELL', 'SELL', 'BUY', 'BUY', 'BUY', 'SELL', 'SELL', 'BUY', 'BUY', 'BUY',
                            'SELL' ]
        buy_sell_list_2 = [ 'BUY', 'SELL', 'SELL', 'BUY', 'BUY', 'SELL', 'SELL', 'BUY', 'SELL', 'BUY', 'BUY', 'SELL', 'SELL', 'SELL',
                            'SELL' ]

        # [ 5559, 489, 6391, 5846, 53, 6524, 261, 4085, 7125, 1469, 992, 6371, 3573, 3977, 2597 ]
        px_list_1 = [ 1234, 4176, 2147, 1176, 7696, 6887, 7656, 3569, 987, 4132, 2648, 8526, 9250, 6579, 9631 ]
        px_list_2 = [ 1234, 4176, 2147, 1176, 7696, 6887, 7656, 3569, 987, 4132, 2648, 8526, 9250, 6579, 9631 ]
        qty_list_1 = [ 5791, 8883, 8891, 5444, 9804, 9794, 8271, 3465, 534, 2722, 7260, 2788, 8760, 6763, 7481 ]
        qty_list_2 = [ 4246, 4949, 4666, 1270, 8461, 1531, 3198, 8123, 6257, 3186, 883, 3460, 490, 9394, 4736 ]
        asset_list_1 = [ 'SOL', 'MATIC', 'MATIC', 'MATIC', 'ADA', 'MATIC', 'UNI', 'DOT', 'XLM', 'ADA', 'BTC', 'DOT', 'MATIC', 'TRX', 'ETH' ]
        asset_list_2 = [ 'DOT', 'MATIC', 'AVAX', 'TRX', 'ADA', 'SOL', 'UNI', 'XLM', 'XLM', 'ADA', 'UNI', 'AVAX', 'XLM', 'ETH', 'DOT' ]

        orders_left = VGroup()
        orders_left_list = []
        for i in range(15):
            element = create_just_order(place_cancel_list_1[i], buy_sell_list_1[i], px_list_1[i], qty_list_1[i], asset_list_1[i])
            orders_left.add(element)
            orders_left_list.append(element)
        orders_right = VGroup()
        orders_right_list = []
        for i in range(15):
            element = create_just_order(place_cancel_list_2[i], buy_sell_list_2[i], px_list_2[i], qty_list_2[i], asset_list_2[i])
            orders_right.add(element)
            orders_right_list.append(element)


        orders_left.arrange_in_grid(5, 3).to_edge(L)
        orders_right.arrange_in_grid(5,3, buff=0.4).to_edge(R)

        self.play(FadeIn(orders_right),
                  FadeIn(orders_left))

        self.play(LaggedStart(*[FadeOut(order, target_position=blocks[1]) for order in orders_left_list+orders_right_list]))

        # self.play(Uncreate(blockchain))

        # chain1 = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        # chain2 = Line(ORIGIN, L * 0.4).move_to(chain1).shift(L * 0.2)
        # chain = VGroup()
        # for i in range(3):
        #     chain.add(chain2.copy())
        #     chain.add(chain1.copy())
        # chain.add(chain2.copy())
        # chain.arrange(R, buff=-0.12)
        #
        # blocks = VGroup(*[ Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(3) ]).arrange(R,
        #                                                                                                                   buff=chain.width)
        # scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.5) for i in range(3) ])
        #
        # blockchain = VGroup()
        # for i in range(len(blocks)):
        #     blockchain.add(blocks[ i ])
        #     blockchain.add(scripts[ i ])
        #     blockchain.add(chain.copy().next_to(blocks[ i ], R, buff=0))
        #
        # blockchain.to_edge(L)
        #
        # self.play(Create(blockchain), run_time=10)

        fees = Tex('Lots of Fees').shift(L*4.5)
        fees_arrow = MathTex(r'\Uparrow').scale(2).next_to(fees, U,buff=0.5)
        speed = Tex('Slow Speed').shift(R*4.5)
        speed_arrow = MathTex(r'\Downarrow').scale(2).next_to(speed, D,buff=0.5)

        self.play(Create(fees))

        self.play(fees.animate.scale(2),
                  Create(fees_arrow))

        self.play(Create(speed))

        self.play(speed.animate.scale(2),
                  Create(speed_arrow))


class amm_xyk(Scene):
    def construct(self):

        amm_text = Tex('Automatic Market Maker').scale(2)


        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text))
        self.play(Write(xyk))

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt))
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

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4, 0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
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

        k_tracker.set_value(30000)

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
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )
        self.play(FadeOut(liq_provider))
        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=PURPLE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 20 ],
                    use_smoothing=False, color=GREY)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
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
        # self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        ########################################################################################올라갔을 때
        ######################################Scen1#############################올라갔을 때
        ########################################################################################올라갔을 때

        # user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "1286 USDT", BLUE,1.4, 0.3).next_to(liq_pool_rect, RIGHT,
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
        # scene1_7btc_fill_box.set_stroke(width=0, opacity=0)
        # scene1_13btc_fill_box.set_stroke(width=0, opacity=0)
        # scene1_7btc_fill_box.set_z_index(3)
        # scene1_13btc_fill_box.set_z_index(3)

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
        # origin_dot.set_color(GREEN)
        # origin_dot.set_z_index(1.5)
        # self.play(Create(origin_dot))
        # self.play(btc_tracker.animate.set_value(7),
        # #         usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
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
        # user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "3BTC", ORANGE, 1.4, 0.3).next_to(liq_pool_rect,
        #                                                                                                                 RIGHT, buff=2)
        # user_asset_btc = user[ 1 ]
        # user_asset_pos = user_asset_btc.get_center()
        # user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", BLUE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)
        #
        # user_line = Tex(r'I want to sell 3 BTC\\I dont have some USDT').scale(0.5).next_to(user, DOWN)
        #
        # self.play(Create(user))
        # self.play(Create(user_line))
        # self.play(Uncreate(user_line))
        #
        # # self.add(index_labels(btc_bar))###
        #
        # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(
        #     usdt_bar, UL)
        # scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
        #                              stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        #
        # scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(BLUE, opacity=1)
        # scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(ORANGE, opacity=1)
        #
        # scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        # scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        # scene2_2308usdt_fill_box.set_z_index(3)
        # scene2_13btc_fill_box.set_z_index(3)

        # self.play(Create(scene2_2308usdt_box))
        # self.play(Create(scene2_13btc_box))
        # scene2_2308usdt_brace = BraceBetweenPoints(scene2_2308usdt_box.get_corner(UR), scene2_2308usdt_box.get_corner(DR), color=RED_E,
        #                                            stroke_color=RED_E,
        #                                            stroke_width=3,
        #                                            ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene2_2308usdt_fill_box,
        #                                                                                          RIGHT)
        # scene2_13btc_brace = BraceBetweenPoints(scene2_13btc_box.get_corner(UL), scene2_13btc_box.get_corner(DL), color=GREEN_E,
        #                                         stroke_color=GREEN_E, stroke_width=3
        #                                         ).next_to(scene2_13btc_fill_box,
        #                                                   LEFT)
        #
        # scene2_2308usdt_brace_label = Integer(btc_tracker.get_value())
        # scene2_2308usdt_brace_label.add_updater(lambda label: label.become(
        #     Integer(692).scale(0.4).rotate(-PI / 2).next_to(scene2_2308usdt_brace, RIGHT, buff=0.3)))
        # scene2_13btc_brace_label = Integer(usdt_tracker.get_value())
        # scene2_13btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(3).scale(0.4).rotate(PI / 2).next_to(scene2_13btc_brace, LEFT, buff=0.3)))
        #
        # scene2_braces = VGroup(scene2_2308usdt_brace, scene2_13btc_brace)
        # scene2_brace_labels = VGroup(scene2_2308usdt_brace_label, scene2_13btc_brace_label)
        #
        # self.play(Create(scene2_braces),
        #           Create(scene2_brace_labels))
        #
        # usdt_bar.clear_updaters()
        # btc_bar.clear_updaters()
        #
        # self.add(scene2_2308usdt_fill_box)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height= 2307/ 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        # #     Rectangle(height=13 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        # #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))
        #
        # origin_dot = curr_dot.copy()
        # origin_dot.clear_updaters()
        # origin_dot.set_color(RED)
        # origin_dot.set_z_index(1.5)
        #
        # self.play(Create(origin_dot))
        # self.play(btc_tracker.animate.set_value(13),
        #           # usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
        #           Transform(scene2_2308usdt_fill_box, user_asset_usdt),
        #           Transform(user_asset_btc, scene2_13btc_fill_box))
        #
        # scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
        #     RIGHT * 0.3 + UP * 0.3)
        # scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)
        #
        # # bars.clear_updaters()
        # # vars.clear_updaters()
        # # k_var.clear_updaters()
        # # area.clear_updaters()
        # # curr_dot.clear_updaters()
        # # axis_labels.clear_updaters()
        # # markers.clear_updaters()
        # self.play(Create(scene2_arrow))
        #
        # # self.play(Restore(whole_mobs))
        #
        # scene2_slippage_text = Tex(r'I just sold 3 BTC \\and got 602 USDT').scale(0.5).next_to(user_asset_pos, DOWN)
        # scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        # scene2_slippage_result = MathTex(rf'{int(-(k_tracker.get_value() / btc_tracker.get_value()-3000)/3)}\$ \  per\ BTC ').move_to(scene2_slippage_form.get_center())
        #
        # self.play(Create(scene2_slippage_form),
        #           Create(scene2_slippage_text))
        #
        # self.play(ReplacementTransform(scene2_slippage_form,scene2_slippage_result))
        #
        #
        # self.wait(2)
        #
        # self.wait(2)
        #######################################################################################
        #################################scene3##############################################
        # 이건 k값 상승을 위한 것
        #######################################################################################
        # 아ㅣ거 유동성 5개 아니라 3개로 수정

        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # 유저 사라짐

        # self.play(FadeOut(user),
        #           FadeOut(user_asset_btc),
        #           FadeOut(user_asset_usdt))
        #
        # 리퀴디티 프로바이더 다시 생성
        # liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "5 BTC", ORANGE, 1.4, 0.3).next_to(
        #     liq_pool_rect, RIGHT, buff=1.5)
        # btc_asset = liq_provider[ 1 ]
        # usdt_asset = create_entity("A", 0.5, WHITE, "500 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        #
        # self.play(Create(VGroup(liq_provider, usdt_asset)))
        #
        # btc_bar.clear_updaters()
        # usdt_bar.clear_updaters()
        #
        # scene3_15btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.5, stroke_width=3,
        #                              stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        # scene3_4500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.5, stroke_width=3,
        #                                 stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)
        #
        # self.play(Create(VGroup(scene3_15btc_box, scene3_4500usdt_box)))
        #
        # scene3_4500usdt_fill_box = scene3_4500usdt_box.copy().set_fill(BLUE, opacity=1)
        # scene3_15btc_fill_box = scene3_15btc_box.copy().set_fill(ORANGE, opacity=1)
        # scene3_15btc_fill_box.set_stroke(width=0, opacity=0)
        # scene3_4500usdt_fill_box.set_stroke(width=0, opacity=0)
        #
        # scene3_15btc_fill_box.set_z_index(3)
        # scene3_4500usdt_fill_box.set_z_index(3)
        #
        #
        # scene3_4500usdt_brace = BraceBetweenPoints(scene3_4500usdt_box.get_corner(UR), scene3_4500usdt_box.get_corner(DR), color=GREEN_E,
        #                                            stroke_color=GREEN_E,
        #                                            stroke_width=3,
        #                                            ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene3_4500usdt_fill_box,
        #                                                                                          RIGHT)
        # scene3_15btc_brace = BraceBetweenPoints(scene3_15btc_box.get_corner(UL), scene3_15btc_box.get_corner(DL), color=GREEN_E,
        #                                         stroke_color=GREEN_E, stroke_width=3
        #                                         ).next_to(scene3_15btc_fill_box,
        #                                                   LEFT)
        #
        # scene3_4500usdt_brace_label = Integer(btc_tracker.get_value())
        # scene3_4500usdt_brace_label.add_updater(lambda label: label.become(
        #     Integer(1500).scale(0.4).rotate(-PI / 2).next_to(scene3_4500usdt_brace, RIGHT, buff=0.3)))
        # scene3_15btc_brace_label = Integer(usdt_tracker.get_value())
        # scene3_15btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(5).scale(0.4).rotate(PI / 2).next_to(scene3_15btc_brace, LEFT, buff=0.3)))
        #
        # scene3_braces = VGroup(scene3_4500usdt_brace, scene3_15btc_brace)
        # scene3_brace_labels = VGroup(scene3_4500usdt_brace_label, scene3_15btc_brace_label)
        #
        # new_liquidity_text = MathTex('5BTC', '=', '1500USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)
        #
        # scene3_origin_graph = xyk_graph_btc.copy()
        # scene3_origin_graph.clear_updaters()
        # scene3_origin_graph.set_color(RED)
        # scene3_origin_graph.set_z_index(-1)
        # self.add(scene3_origin_graph)
        #
        # # xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
        # #                         x_range=[ 0.00001, 6000 ],
        # #                         use_smoothing=False, color=PURPLE)
        # #
        # # xyk_graph_btc.add_updater(lambda graph: graph.become(
        # #     ax.plot(lambda x: k_tracker.get_value() / x,
        # #             x_range=[ k_tracker.get_value() / 6000, 20 ],
        # #             use_smoothing=False, color=PURPLE)))
        #
        # self.play(Create(scene3_braces),
        #           Create(scene3_brace_labels))
        #
        # # self.play(Create(origin_dot))
        # self.play(k_tracker.animate.set_value(67500),
        #           btc_tracker.animate.set_value(15),
        #           usdt_tracker.animate.set_value(67500/15),
        #           Transform(usdt_asset, scene3_4500usdt_fill_box),
        #           Transform(btc_asset, scene3_15btc_fill_box),
        #           run_time=6)
        #
        # self.wait(4)

        #######################################################################################
        #################################scene4##############################################
        #######################################################################################
        # 아ㅣ거 유동성 5개 아니라 3개로 수정

        # liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "5 BTC", ORANGE, 1.4, 0.3).next_to(
        #     liq_pool_rect, RIGHT, buff=1.5)
        # btc_asset = liq_provider[ 1 ]
        # usdt_asset = create_entity("A", 0.5, WHITE, "1500 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        #
        # self.play(Create(liq_provider[ 0 ]))
        #
        # btc_bar.clear_updaters()
        # usdt_bar.clear_updaters()
        #
        # # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        # #                                 stroke_color=RED_E).align_to(usdt_bar, UL)
        #
        # scene4_5btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.5, stroke_width=3,
        #                             stroke_color=RED_E).align_to(btc_bar, UL)
        # scene4_1500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.5, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(usdt_bar, UL)
        #
        # scene4_1500usdt_fill_box = scene4_1500usdt_box.copy().set_fill(BLUE, opacity=1)
        # scene4_5btc_fill_box = scene4_5btc_box.copy().set_fill(ORANGE, opacity=1)
        #
        # scene4_5btc_fill_box.set_stroke(width=0, opacity=0)
        # scene4_1500usdt_fill_box.set_stroke(width=0, opacity=0)
        # scene4_5btc_fill_box.set_z_index(3)
        # scene4_1500usdt_fill_box.set_z_index(3)
        #
        # self.play(Create(VGroup(scene4_5btc_box, scene4_1500usdt_box)))
        # self.add(scene4_5btc_fill_box,scene4_1500usdt_fill_box)
        #
        # scene4_1500usdt_brace = BraceBetweenPoints(scene4_1500usdt_box.get_corner(UR), scene4_1500usdt_box.get_corner(DR), color=RED_E,
        #                                            stroke_color=RED_E,
        #                                            stroke_width=3,
        #                                            ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene4_1500usdt_fill_box,
        #                                                                                          RIGHT)
        # scene4_5btc_brace = BraceBetweenPoints(scene4_5btc_box.get_corner(UL), scene4_5btc_box.get_corner(DL), color=RED_E,
        #                                        stroke_color=RED_E, stroke_width=3
        #                                        ).next_to(scene4_5btc_fill_box,
        #                                                  LEFT)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=1500 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=5 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))
        #
        # scene4_1500usdt_brace_label = Integer(btc_tracker.get_value())
        # scene4_1500usdt_brace_label.add_updater(lambda label: label.become(
        #     Integer(1500).scale(0.4).rotate(-PI / 2).next_to(scene4_1500usdt_brace, RIGHT, buff=0.3)))
        # scene4_5btc_brace_label = Integer(usdt_tracker.get_value())
        # scene4_5btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(5).scale(0.4).rotate(PI / 2).next_to(scene4_5btc_brace, LEFT, buff=0.3)))
        #
        # scene4_braces = VGroup(scene4_1500usdt_brace, scene4_5btc_brace)
        # scene4_brace_labels = VGroup(scene4_1500usdt_brace_label, scene4_5btc_brace_label)
        #
        # new_liquidity_text = MathTex('5BTC', '=', '1500USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)
        #
        # self.play(Create(new_liquidity_text))
        #
        # scene4_origin_graph = xyk_graph_btc.copy()
        # scene4_origin_graph.clear_updaters()
        # scene4_origin_graph.set_color(RED)
        # scene4_origin_graph.set_z_index(-1)
        # self.add(scene4_origin_graph)
        #
        # self.play(Create(scene4_braces),
        #           Create(scene4_brace_labels))
        #
        # # self.play(Create(origin_dot))
        # self.play(k_tracker.animate.set_value(7500),
        #           btc_tracker.animate.set_value(5),
        #           usdt_tracker.animate.set_value(7500 / 5),
        #           Transform(scene4_1500usdt_fill_box, usdt_asset),
        #           Transform(scene4_5btc_fill_box, btc_asset),
        #           run_time=6,rate_func=rate_functions.ease_in_out_quint)
        #
        # self.wait(4)

        #######################################################################################
        #################################scene5##############################################
        #######################################################################################
        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))

        # 가격 상승#####################################################################################

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_up = Tex('Price goes up')
        # self.play(Write(px_up))
        # self.play(Unwrite(px_up))

        # 가격이 올라간다는 건 btc가 usdt보다 상대적으로 인기가 많아진다는 것입니다.

        self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn = Tex('Price goes Down')
        # self.play(Write(px_dn))
        # self.play(Unwrite(px_dn))

        # 가격이 내려간다는 건 btc가 usdt보다 상대적으로 인기가 없어진다는 것

        self.wait(2)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 가격 원점#####################################################################################
        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_origin = Tex('Price origin').scale(0.7).next_to()
        # self.play(Write(px_origin))
        # self.play(Unwrite(px_origin))

        self.wait(2)

        # K 하락#####################################################################################
        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn = Tex('K goes down')
        # self.play(Write(k_dn))
        # self.play(Unwrite(k_dn))
        # 케이가 하락한다는 건 풀에서 누군가 유동성을 빼간 것입니다.
        # 명심할 것은 케이의 변동은 가격과 관계가 없음
        # 내가 유동성 풀에 제거하고 싶으면
        # 그냥 지금 가격에 맞게 빼가면 됨
        # 스왑처럼 내가 가격을 움직이며 하는 행위가 아님
        # 왜냐하면 가격이란 풀 내부의 비율인데
        # 지금 비율(1개에 300달러) 그대로 빼기 때문에
        # 가격은 움직이지 않고 그로인해 슬리피지등이 발생하지 않는다
        # 착각 금지

        self.wait(2)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_up = Tex('K goes up')
        # self.play(Write(k_up))
        # self.play(Unwrite(k_up))
        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(2)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # K 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin = Tex('K origin')
        # self.play(Write(k_origin))
        # self.play(Unwrite(k_origin))

        self.wait(2)

        # K 상승#####################################################################################
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        k_up = Tex('K goes up')
        self.play(Write(k_up))
        self.play(Unwrite(k_up))

        self.wait(2)

        # K 상승 가격 하락#####################################################################################
        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_up_px_dn = Tex('K up, Price goes down')
        # self.play(Write(k_up_px_dn))
        # self.play(Unwrite(k_up_px_dn))

        # 케이가 상승한 상황에서 가격이 하락
        # 가격이 하락한다는 건 누군가 풀에서 비티씨를 넣고 테더를 빼가는 것
        # 즉 풀에다 비티씨를 매도하는 것
        # 여기서 명심할 건
        # 케이가 상승했다는 건 풀 사이즈가 커진거곡
        # 그만큼 리퀴디티가 충분하다는 것입니다
        # 그러니까 같은 금액의 비티씨를 매도하더라도
        # 이전보다 더 슬리피지가 적습니다
        # 아까 봤을 때 300달러에서 3개 매도할 때는 슬리피지가 얼마 발생
        # 근데 지금은 유동성이 더 충분한 상태고 300달러에서 3개 매도했는데
        # 슬리피지 얼마 발생
        # 유동성이 크면 좋은 것이다
        # 같은 개수를 메도해도 내가 넣는 비티씨의 양이 풀내부에 차지하는 비율이
        # 더 적어졌기 때문입니다
        # 아까는 10개에서 3개 매도
        # 지금은 15개에서 3개 매도
        # 비율로 따지면 30퍼와 20퍼기 땨문에 풀에주는 영향력이 크다

        self.wait(2)

        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_E).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # K 상승 가격 상승#####################################################################################
        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_up_px_up = Tex('K up, Price goes up')
        # self.play(Write(k_up_px_up))
        # self.play(Unwrite(k_up_px_up))

        # 케이가 상승한 상황에서 가격이 올라가는 경우도 마찬가지
        # 가격이 오른다는 건 누군가 풀에서 비티씨를 빼고 테더를 넣는 것
        # 즉 풀에서 비티씨를 매수하는 것
        # 명심할 건
        # 케이가 상승한 건 풀사이즈가 커졌고
        # 마찬가지로 아까 비티씨를 살 때 슬리피지를 겪었던 것보다
        # 슬리피지를 적게 겪음
        # 아까 300달러에서 3개매수는 슬리피지 얼마
        # 근데 지금은 얼마
        # 같은 개수를 매수해도 내가 빼는 비티씨의 양이 풀내부에 차지하는 비율이
        # 더 적어졌기 때문입니다
        # 아까는 10개에서 3개 매수
        # 지금은 15개에서 3개 매ㅑ수
        # 비율로 따지면 30퍼와 20퍼기 땨문에 풀에주는 영향력이 크다

        self.wait(2)

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_E).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin_px_origin = Tex('K origin, px origin')
        # self.play(Write(k_origin_px_origin))
        # self.play(Unwrite(k_origin_px_origin))

        self.wait(2)

        # K 하락#####################################################################################
        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn = Tex('K goes down')
        # self.play(Write(k_dn))
        # self.play(Unwrite(k_dn))

        # 역으로 케이가 하락했는데
        # 그말은 유동성이 줄었다는 거하고
        # 아까 유동성이 늘었서 슬리피지가 덜 발행하던 것과 달리
        # 지금부터는 슬리피지가 더 발생합니다
        #

        self.wait(2)

        # K 하락 가격 하락#####################################################################################
        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn_px_dn = Tex('K down, Price goes dn')
        # self.play(Write(k_dn_px_dn))
        # self.play(Unwrite(k_dn_px_dn))

        # 케이가 하락한 상태에서 누군가 풀에다 비티씨를 매도해서
        # 가격도 하락합니다
        # 비티씨를 매도하는데 아까와 같이 300달러에서 매도하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마입니다
        # 당연히 아까는 10개에서 3개를 넣는 거였고
        # 지금은 5개에서 3개를 넣는거니까
        # 비율은 30퍼와 60퍼로
        # 완전 차이나게 된다

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        self.wait(2)

        # K 하락 가격 상승#####################################################################################
        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn_px_dn = Tex('K down, Price goes up')
        # self.play(Write(k_dn_px_dn))
        # self.play(Unwrite(k_dn_px_dn))

        # 케이가 하락한 상태에서 누군가 풀에서 비티씨를 빼가면서 즉 매수하면서
        # 가격도 상승합니다
        # 비티씨를 매수하는데 아까와 같이 300달러ㅓ에서 매수하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마
        # 당연히 아까는 10개에서 3개를 빼는 거였고
        # 지금은 5개에서 3개를 빼는 것
        # 비율은 30퍼와 60퍼로 상당히 차이난다

        self.wait(2)

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin_px_origin = Tex('K origin, px origin')
        # self.play(Write(k_origin_px_origin))
        # self.play(Unwrite(k_origin_px_origin))

        self.wait(2)

        # 가격 상승#####################################################################################
        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_up = Tex('Price goes up')
        # self.play(Write(px_up))
        # self.play(Unwrite(px_up))

        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        self.play(k_tracker.animate.set_value(3000000 / 49),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 49 / 10),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        px_up_k_up = Tex('Price goes up, K up')
        self.play(Write(px_up_k_up))
        self.play(Unwrite(px_up_k_up))

        # 아까와는 상황이 다릅니다
        # 현재 가격은 이미 움직여버렸습니다
        # 현재가격은 이미 300에서 올라왔고 여기서
        # 유동성을 넣기 때문에
        # 같은 2비티씨를 유동성을 추가한다고 하면
        # 1비티씨마다 상응하는 올라간 가격의 테더를 같이 넣어줘야합니다
        #

        self.wait(2)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################
        self.play(k_tracker.animate.set_value(480000 / 49),
                  btc_tracker.animate.set_value(4),
                  usdt_tracker.animate.set_value(480000 / 49 / 4),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_up_k_dn = Tex('Price goes up, K dn')
        # self.play(Write(px_up_k_dn))
        # self.play(Unwrite(px_up_k_dn))

        # 가격이 올랐을 때 케이가 떨어진다는 건
        # 즉 유동성을 공급했던 사람이 유동성을 회수한다는 것은
        # 풀 사이즈가 작아진다는 것입니다
        # 그 말은 공급자가 1비티씨를 뺄 때 오른 가격만큼의 테더를 회수한다는 애기입니다
        # 2비티씨를 빼면 얼마가 빠집니다

        self.wait(2)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin_px_origin = Tex('K origin, px origin')
        # self.play(Write(k_origin_px_origin))
        # self.play(Unwrite(k_origin_px_origin))

        # 가격 하락#####################################################################################
        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn = Tex('Price goes down')
        # self.play(Write(px_dn))
        # self.play(Unwrite(px_dn))

        # 가격이 하락한 상태에서 케이를 움직여보겟습니다

        self.wait(2)

        # 가격 하락에서 K상승#####################################################################################
        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn_k_up = Tex('Price goes down, K up')
        # self.play(Write(px_dn_k_up))
        # self.play(Unwrite(px_dn_k_up))

        # 가격이 하락한 상태에서 케이를 넣으렴녀 원래보다 돈이 적게 듭니다
        # 왜냐하면 비티씨 1개를 넣을 때 하락한 각겨만큼의 테더를 넣으면 됩니다

        self.wait(2)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # 가격 하락에서 K하락#####################################################################################
        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 11),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn_k_dn = Tex('Price goes down, K dn')
        # self.play(Write(px_dn_k_dn))
        # self.play(Unwrite(px_dn_k_dn))

        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        self.wait(2)

        # 가격 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_origin = Tex('Price origin')
        # self.play(Write(px_origin))
        # self.play(Unwrite(px_origin))

        self.wait(2)

        # 라인 생성#####################################################################################

        def making_a_line_3points(p1, p2, p3, color):
            l1 = Line(p1.get_center(), p2.get_center(), color=color)
            l2 = Line(p2.get_center(), p3.get_center(), color=color)
            l1.set_z_index(-2)
            l2.set_z_index(-2)
            line = VGroup(l1, l2)

            return line

        self.play(FadeOut(area),
                  FadeOut(area_text))
        k_px_org_line = making_a_line_3points(k_dn_px_org_dot, k_org_px_org_dot, k_up_px_org_dot, DARK_GREY)
        self.play(Create(k_px_org_line))
        k_px_up_line = making_a_line_3points(k_dn_px_up_dot, k_org_px_up_dot, k_up_px_up_dot, GREEN_E)
        self.play(Create(k_px_up_line))
        k_px_dn_line = making_a_line_3points(k_dn_px_dn_dot, k_org_px_dn_dot, k_up_px_dn_dot, RED_E)
        self.play(Create(k_px_dn_line))
        px_up_k_line = making_a_line_3points(px_up_k_dn_dot, k_org_px_up_dot, px_up_k_up_dot, TEAL_E)
        self.play(Create(px_up_k_line))
        px_dn_k_line = making_a_line_3points(px_dn_k_dn_dot, k_org_px_dn_dot, px_dn_k_up_dot, MAROON_E)
        self.play(Create(px_dn_k_line))

        self.wait(2)

