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


def reverse(t: float) -> float:
    return -t + 1


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


class intro_and_barter(Scene):
    def construct(self):
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)


class stablecoin(Scene):
    def construct(self):
        # 스테이블 코인 텍스트 보여줌
        stablecoin = Tex('Stablecoin').scale(2)
        self.play(Create(stablecoin))

        self.wait(q)
        self.play(Uncreate(stablecoin))
        #

        # 기업 혹은 거래소 박스 형성 (중앙ㅇ에 할거고 이건 왼쪽은 은행이나 채권 만들고)
        tether_company_rect = RoundedRectangle(height=8, width=4, corner_radius=0.5)
        tether_company_text = Tex('Company or Exchange').next_to(tether_company_rect, UP)

        tether_company = VGroup(tether_company_rect, tether_company_text).move_to(ORIGIN)

        tether_company.set_z_index(3)

        # self.add(index_labels(tether_company[0]))
        self.play(Create(tether_company))

        #
        # 고객 엔터티 오른 쪽에 생성하고 법정화폐 붙임

        def create_entity_tether(person_name, person_radius, person_color, asset_name, how_many, asset_color, asset_width, asset_height):
            person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

            box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
            text = Text(asset_name, color=BLACK).scale(asset_height)

            asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)
            assets = VGroup(asset)

            assets = VGroup(*[ asset.copy() for i in range(how_many) ])
            # for i in range(how_many):
            #     VGroup.add(asset.copy())

            assets.arrange(DOWN, buff=0.1).next_to(person, DOWN)

            return VGroup(person, assets)

        A = create_entity_tether("A", 0.5, WHITE, "USD", 15, GREEN, 0.7, 0.3)
        B = create_entity_tether("B", 0.5, WHITE, "USD", 10, GREEN, 0.7, 0.3)
        C = create_entity_tether("C", 0.5, WHITE, "USD", 3, GREEN, 0.7, 0.3)
        D = create_entity_tether("D", 0.5, WHITE, "USD", 8, GREEN, 0.7, 0.3)


        people_list = [ A, B, C, D ]
        people = VGroup(A, B, C, D).arrange(RIGHT, buff=0.2, aligned_edge=UP).to_edge(UR)

        self.play(Create(people))
        #
        # 그리고 고객들 돈을 기업으로 전송
        each_money = VGroup()
        for person in people_list:
            for i in range(len(person[ 1 ])):
                each_money.add(person[ 1 ][ i ])

        self.play(each_money.animate.arrange_in_grid(9, 4, buff=0.1).move_to(tether_company[ 0 ]))
        #
        # 기업에서 테더 발행 원래 받은 USD는 위로 밀리면서 새로운 USDT 뭉치가 생겨남

        tether_1ea = create_entity_tether("A", 0.5, WHITE, "USDT", 36, BLUE, 0.7, 0.3)[ 1 ]

        tethers = VGroup()
        for i in range(len(tether_1ea)):
            tethers.add(tether_1ea[ i ])
        tethers.arrange_in_grid(9, 4, buff=0.1).move_to(tether_company[ 0 ])
        self.play(GrowFromCenter(tethers))
        # tethers.arrange()
        self.play(VGroup(each_money, tethers).animate.arrange(DOWN, buff=0.25).move_to(tether_company[ 0 ]))

        #
        # 테더는 다시 엔터티에게 전송
        self.play(tethers[ 0:15 ].animate.arrange(DOWN, buff=0.1).next_to(A[ 0 ], DOWN))
        self.play(tethers[ 15:25 ].animate.arrange(DOWN, buff=0.1).next_to(B[ 0 ], DOWN))
        self.play(tethers[ 25:28 ].animate.arrange(DOWN, buff=0.1).next_to(C[ 0 ], DOWN))
        self.play(tethers[ 28:36 ].animate.arrange(DOWN, buff=0.1).next_to(D[ 0 ], DOWN))
        #
        # 그리고 달러 중 일부는 은행이나 채권등으로 투자
        invest = LabeledRectangle('Banks Bonds etc', width=4, height=6, direction=UP, corner_radius=0.5).to_edge(LEFT)

        self.play(Create(invest))

        self.play(each_money[ 0:16 ].animate.arrange_in_grid(4, 4, buff=0.1).move_to(invest))

        #
        # 엔터티 중 한명이 테더를 반납하면 달러로 돌려줌
        self.play(tethers[ 0:15 ].animate.arrange_in_grid(4, 4, buff=0.1).next_to(each_money[ 28:36 ], DOWN, buff=0.25))
        # self.play(VGroup(each_money[16:36],tethers[ 0:15 ]).animate.arrange(DOWN))

        self.play(each_money[ 23:36 ].animate.arrange(DOWN, buff=0.1).next_to(A[ 0 ], DOWN))

        self.play(Uncreate(tethers[ 0:15 ]))
        #
        # 전부 ㅇ벗어지고 알고리드믹 스테이블코인, 코인담보 스테이블 등이 있으나 나중에 알아보자

        self.play(FadeOut(each_money),
                  FadeOut(tethers),
                  FadeOut(tether_company),
                  FadeOut(invest),
                  FadeOut(people),
                  )


class backed_by(Scene):
    def construct(self):
        def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
            person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

            box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
            text = Text(asset_name, color=BLACK).scale(0.8 * asset_height)

            asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

            return VGroup(person, asset)

        usdt = create_entity("A", 0.5, WHITE, "USDT", BLUE, 2, 1)[ 1 ].to_edge(UL, buff=1)
        usd = create_entity("A", 0.5, WHITE, "USD", GREEN, 2, 1)[ 1 ].to_edge(DL, buff=1)
        usg = LabeledDot(Tex(r'\emph{US\\Gov}', color=BLACK), radius=1)[ 0 ].to_edge(D, buff=0.5)
        us_people = LabeledDot(Tex(r'\emph{US\\People}', color=BLACK), radius=1)[ 0 ].to_edge(D, buff=0.5).to_edge(R, buff=1)

        usd_copy = usd.copy().move_to(ORIGIN).to_edge(U, buff=1)

        usg_copy = usg.copy().move_to(ORIGIN).to_edge(U, buff=0.5).to_edge(R, buff=1)

        backed_by_1 = Tex('Backed by').move_to(np.array([ usdt.get_x(), 0, 0 ]))
        backed_by_2 = Tex('Backed by')
        backed_by_3 = Tex('Backed by').move_to(np.array([ us_people.get_x(), 0, 0 ]))

        self.play(Create(usdt))
        self.play(Create(backed_by_1))
        self.play(Create(usd))
        self.play(TransformFromCopy(usd, usd_copy))
        self.play(Create(backed_by_2))
        self.play(Create(usg))
        self.play(TransformFromCopy(usg, usg_copy))
        self.play(Create(backed_by_3))
        self.play(Create(us_people))

        self.play(FadeOut(VGroup(usd, backed_by_1)))
        self.play(Uncreate(usdt))

        self.play(FadeOut(VGroup(usg, backed_by_2)))
        self.play(Uncreate(usd_copy))

        self.play(FadeOut(VGroup(us_people, backed_by_3)))
        self.play(Uncreate(usg_copy))

        self.wait(q)


class pair(Scene):
    def construct(self):
        BTC_slash_USD_text = Tex("BTC/USD").scale(2)
        BTC_dash_USD_text = Tex("BTC-USD").scale(2)
        BTC_none_USD_text = Tex("BTCUSD", substrings_to_isolate=[ 'BTC', 'USD' ]).scale(2)
        self.play(Write(BTC_slash_USD_text))
        self.play(TransformMatchingShapes(BTC_slash_USD_text, BTC_dash_USD_text))
        self.play(TransformMatchingShapes(BTC_dash_USD_text, BTC_none_USD_text))

        base_asset = Tex("Base asset").shift(DOWN + LEFT * 4)
        base_asset_arrow = Arrow(start=base_asset.get_corner(UR), end=BTC_none_USD_text.get_corner(DL))
        quote_asset = Tex("Quote asset").shift(DOWN + RIGHT * 4)
        quote_asset_arrow = Arrow(start=quote_asset.get_corner(UL), end=BTC_none_USD_text.get_corner(DR))

        base_and_quote = VGroup(base_asset, base_asset_arrow, quote_asset, quote_asset_arrow)
        self.play(Create(base_and_quote))

        self.wait(q)

        expl_text_1 = Text("If price of BTCUSD is 100, then it means 1BTC is 100$", font='Batang').scale(0.5).shift(DOWN * 2.5)

        # self.play(Write(text))
        self.play(Write(expl_text_1))
        self.play(Unwrite(expl_text_1))
        eth_text = Tex('ETH').move_to(BTC_none_USD_text[ 0 ]).scale(2)
        btc_text = Tex('BTC').move_to(BTC_none_USD_text[ 1 ]).scale(2)

        self.play(Transform(BTC_none_USD_text[ 0 ], eth_text))
        self.play(Transform(BTC_none_USD_text[ 1 ], btc_text))

        expl_text_2 = Text("If price of ETHBTC is 0.1., then it means 1BTC is 0.1BTC", font='Batang').scale(0.5).shift(DOWN * 2.5)
        self.play(Write(expl_text_2))
        self.play(Unwrite(expl_text_2))

        self.wait(q)


class price(Scene):
    def construct(self):
        def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
            person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

            box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
            text = Text(asset_name, color=BLACK).scale(0.8 * asset_height)

            asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

            return VGroup(person, asset)

        price = Tex('Price').scale(2)

        self.play(Create(price))

        price_text = Tex(
            r'A price is the (usually not negative) quantity of payment \\or compensation given by one party to another\\in return for goods or services.').next_to(
            price, D)
        self.play(Create(price_text))

        self.play(Uncreate(price),
                  Uncreate(price_text))

        btc_equal_38000 = Tex('1 BTC = 38000')
        cross = Cross(stroke_width=25).scale(3)
        btc_equal_38000dollars = Tex('1 BTC = 38000 USD')
        circle = Circle(color=GREEN, radius=3, stroke_width=25).rotate(PI / 2)
        self.play(Create(btc_equal_38000))

        self.play(Create(cross))

        self.play(FadeOut(cross))
        self.play(TransformMatchingShapes(btc_equal_38000, btc_equal_38000dollars))

        self.play(Create(circle))

        self.play(Uncreate(circle),
                  Uncreate(btc_equal_38000dollars))

        self.wait(q)



class order_book_market_and_limit_order(Scene):
    def construct(self):
        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text).move_to(ORIGIN)

        self.play(Create(pair, run_time=q))

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

        curr_px_valuetracker = ValueTracker(100)
        curr_px_val = str(int(curr_px_valuetracker.get_value()))
        # curr_px_number = Tex(rf'{curr_px_val}\$').move_to(curr_px_rect)
        curr_px_number_100 = Integer(100, unit=r"\$", color=RED).move_to(curr_px_rect)
        curr_px_number_101 = Integer(101, unit=r"\$", color=GREEN).move_to(curr_px_rect)

        # curr_px_number.add_updater(lambda x : x.become(Integer(curr_px_valuetracker.get_value(), unit=r"\$")))

        # curr_px =VGroup(curr_px_rect,curr_px_number_100)

        int_valuetracker = ValueTracker(100)

        my_int = Integer(int_valuetracker.get_value(), unit=r"\$").to_edge(UR)

        # my_int.add_updater()
        self.play(Create(curr_px_rect))
        # self.play(curr_px_valuetracker.animate.set_value(120))

        self.play(FadeIn(curr_px_number_100), run_time=0.01)

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

        # order_book_table.add_highlighted_cell((2,2),fill_opacity=0.2, color=RED_A)
        order_book_long_table.set_row_colors(GREEN, GREEN, GREEN, GREEN, GREEN)

        # order_book_table.add(order_book_table.get_cell((2,2), color=RED))

        # self.add(index_labels(order_book_table))

        def change_waiting_order(self, table, r, c, new_val, run_time):
            a = table.get_entries(pos=(r, c))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        def change_waiting_order_by_perc(self, table, r, c, perc, run_time):
            a = table.get_entries(pos=(r, c))

            new_val = int(a.get_value() * ((100 + perc) / 100))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        self.play(Create(order_book_long_table), Create(order_book_shrt_table))
        self.wait(1)
        # self.play(curr_px_number_100)

        negative_nums = rd.sample(range(-40, -25, 1), k=8)
        negative_nums.sort(reverse=True)
        trade_occurred = Tex('A trade has occurred!').scale(0.8).to_corner(UR)
        market_occurred = Tex('Market order!').scale(0.8).next_to(trade_occurred, DOWN).align_to(trade_occurred, LEFT)

        self.play(Write(trade_occurred))
        self.play(Write(market_occurred))

        repetition = 8
        each_100_101 = [ 1, 0, 1, 0, 1, 0, 1, 0, 1 ]
        each_change = [ -10, -20, -30, -40, -50, -60, -70, -75 ]

        order_book_runtime = 0.2
        for i in range(repetition):

            if_100_or_101 = each_100_101[ i ]
            change = each_change[ i ]

            if if_100_or_101 == 0:
                self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
                self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=1)
                curr_px_rect.set_color(RED)
                self.play(
                    change_waiting_order_by_perc(self, order_book_long_table, 1, 2, change, order_book_runtime),
                    run_time=order_book_runtime)
                self.play(FadeIn(curr_px_number_100), FadeOut(curr_px_number_101), run_time=0.1)

                # self.remove(curr_px_number_101)

                self.wait(1)

                # self.play(Uncreate(trade_occurred), run_time=0.01)

                # if i != 7:
                #     self.remove(curr_px_number_100)
                # else:
                curr_px_number = curr_px_number_100


            else:
                self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
                self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=1)

                # self.play(Uncreate(curr_px_number_100),Uncreate(curr_px_number_101),Create)
                curr_px_rect.set_color(GREEN)
                self.play(
                    change_waiting_order_by_perc(self, order_book_shrt_table, 5, 2, change, order_book_runtime),
                    run_time=order_book_runtime)
                self.play(FadeIn(curr_px_number_101), FadeOut(curr_px_number_100), run_time=0.1)

                # self.play(Uncreate(trade_occurred), run_time=0.01)
                # self.play(Uncreate(curr_px_number_101))
                self.wait(1)

                # if i != 7:
                #     self.remove(curr_px_number_101)
                # else:
                curr_px_number = curr_px_number_101

        self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
        self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=1)

        curr_px_rect.set_color(RED)
        self.play(
            change_waiting_order(self, order_book_long_table, 1, 2, 10, order_book_runtime),
            run_time=order_book_runtime)
        self.play(FadeIn(curr_px_number_100), FadeOut(curr_px_number_101), run_time=0.1)

        self.wait(round(rd.uniform(0.1, 2), 2))

        self.play(Uncreate(trade_occurred), run_time=1)
        self.play(Uncreate(market_occurred), run_time=1)

        def create_order(self, place_or_cancel, buy_or_sell, px, qty, asset):

            target_pos = order_book_long_table if buy_or_sell == "BUY" else order_book_shrt_table
            start_from = LEFT if place_or_cancel == "Place" else RIGHT

            order_paper = Rectangle(height=1.5, width=1.2)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{abs(qty)} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order = VGroup(order_paper, order_text).to_edge(start_from)

            self.play(Create(order))
            self.wait(q)
            self.play(FadeOut(order, target_position=target_pos))
            # change_waiting_order(self, target_pos, 3, 2, 1300, 1)

            return

            #
            # else:
            #     order_cancel_paper = Rectangle(height=1.5, width=1.2)
            #     order_cancel_text_1 = Tex("Cancel").scale(0.4)
            #     order_cancel_text_2 = Tex(rf"{buy_or_sell} {qty} {asset}").scale(0.4)
            #     order_cancel_text_3 = Tex(rf"at {px}\$").scale(0.4)
            #     order_cancel_text = VGroup(order_cancel_text_1, order_cancel_text_2, order_cancel_text_3).arrange(DOWN, buff=0.1).move_to(
            #         order_cancel_paper)
            #     order_cancel = VGroup(order_cancel_paper, order_cancel_text).to_edge(RIGHT)
            #
            #     self.play(Create(order_cancel))
            #     self.wait(q)
            #     self.play(FadeOut(order_cancel, target_position=target_pos))
            #     change_waiting_order(self, order_book_long_table, 3, 2, 990, 1)

        order_send_reps = 7

        px_plan = [ 96, 102, 98, 104, 97, 103, 99 ]
        place_or_cancel_plan = [ 0, 1, 0, 0, 1, 1, 0 ]
        qty_plan = [ 50000, 30, 400, 2300, 3800, 293, 22 ]

        for i in range(order_send_reps):
            # random_num =rd.randint(1, 2)
            # perc = rd.randint(2, 5)
            place_or_cancel = "Place" if place_or_cancel_plan[ i ] == 1 else "Cancel"
            px = px_plan[ i ]

            buy_or_sell = "BUY" if px <= 100 else "SELL"
            table = order_book_long_table if buy_or_sell == 'BUY' else order_book_shrt_table

            asset = 'BTC'

            px_dict = {105: 1,
                       104: 2,
                       103: 3,
                       102: 4,
                       101: 5,
                       100: 1,
                       99: 2,
                       98: 3,
                       97: 4,
                       96: 5,
                       }

            row = px_dict[ px ]
            org_qty = table.get_entries(pos=(row, 2)).get_value()
            qty = qty_plan[ i ]

            final_qty = qty if place_or_cancel_plan[ i ] == 1 else -qty

            create_order(self, place_or_cancel, buy_or_sell, px, abs(qty), asset)
            self.play(change_waiting_order(self, table, row, 2, org_qty + final_qty, order_book_runtime))
            self.wait(order_book_runtime)

        self.wait(q)

        mark_px_text = Tex('Mark Price').scale(0.7).next_to(curr_px_rect, RIGHT)
        last_px_text = Tex('Last Price').scale(0.7).next_to(curr_px_rect, LEFT)

        self.play(curr_px_number.animate.shift(LEFT * 0.5))
        curr_px_number_101.shift(LEFT * 0.5)
        # curr_px_number_100.shift(LEFT * 0.5)

        print(curr_px_number.get_value())
        print(type(curr_px_number.get_value()))
        mark_px_val_tracker = ValueTracker(curr_px_number.get_value())
        mark_px_number = Integer(int(mark_px_val_tracker.get_value())).scale(0.6).next_to(curr_px_number).align_to(curr_px_number, DOWN)
        # self.play(Create(mark_px_number))
        print("still it is fine")
        mark_px_pos = mark_px_number.get_center()
        mark_px_number.add_updater(lambda x: x.become(Integer(int(mark_px_val_tracker.get_value())).scale(0.6).move_to(mark_px_pos)))
        self.play(Create(mark_px_number))

        self.wait(q)

        self.play(mark_px_val_tracker.animate.set_value(101))
        self.play(mark_px_val_tracker.animate.set_value(100))
        self.play(mark_px_val_tracker.animate.set_value(101))
        self.play(mark_px_val_tracker.animate.set_value(100))
        self.play(mark_px_val_tracker.animate.set_value(101))
        self.play(mark_px_val_tracker.animate.set_value(100))

        self.play(Create(trade_occurred))
        self.play(Create(market_occurred))

        self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
        self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=1)

        # self.play(Uncreate(curr_px_number_100),Uncreate(curr_px_number_101),Create)
        curr_px_rect.set_color(GREEN)
        self.play(
            change_waiting_order(self, order_book_shrt_table, 5, 2, 8, order_book_runtime),
            run_time=order_book_runtime)
        self.play(FadeIn(curr_px_number_101), FadeOut(curr_px_number_100), run_time=0.1)
        self.play(mark_px_val_tracker.animate.set_value(101))

        self.play(Uncreate(trade_occurred))
        self.play(Uncreate(market_occurred))

        last_px_eg = Tex(r"Somebody just bought BTC at 101\$").scale(0.6).next_to(pair_rect, RIGHT)
        self.play(ApplyWave(last_px_eg, amplitude=0.4), run_time=1)
        # self.play(Uncreate(trade_occurred), run_time=0.01)
        last_px_expl_text_1 = Tex("The latest trade ").to_edge(UL)
        last_px_expl_text_2 = Tex("was done at 101 dollars").next_to(last_px_expl_text_1, DOWN).align_to(last_px_expl_text_1, LEFT)
        last_px_expl_text = VGroup(last_px_expl_text_1, last_px_expl_text_2)
        self.play(Write(last_px_expl_text))
        self.play(Unwrite(last_px_expl_text))
        self.play(Unwrite(last_px_eg))

        limit_order_text = Tex(r'Limit Order\\지정가 주문').next_to(pair_rect, LEFT).shift(UP)
        market_order_text = Tex(r'Market Order\\시장가 주문').next_to(pair_rect, LEFT).shift(DOWN)
        self.play(Create(limit_order_text),
                  Create(market_order_text))

        self.wait(1)


class mark_price(Scene):
    def construct(self):
        mark_price = MathTex(r'Mark\ Price').shift(UP)

        m_px_formula = MathTex(r'Median(Price1,\ Price2,\ ContractPrice)')
        px_1 = MathTex(r'Price 1 = Price Index\times (1 + Last Funding Rate\times (Time Until Funding / 8))').scale(0.8).next_to(
            m_px_formula, DOWN)
        px_2 = MathTex(r'Price 2 = Price Index + Moving Average (30-minute Basis)').scale(0.8).next_to(px_1, DOWN)
        cont_px = MathTex('ContractPrice')

        vol_multiplier = 0.7
        vol_color = ORANGE
        vol_scaler = 2.8
        Bitstamp_text = Tex('Bitstamp', color=BLUE)
        Bitstamp_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.05 * vol_scaler).next_to(Bitstamp_text, RIGHT)
        Bitstamp_perc = Tex(r'10\%', color=BLUE).next_to(Bitstamp_dot, RIGHT)
        Bitstamp = VGroup(Bitstamp_text, Bitstamp_dot)

        CoinbasePro_text = Tex('CoinbasePro', color=BLUE_B)
        CoinbasePro_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.2 * vol_scaler).next_to(CoinbasePro_text, RIGHT)
        CoinbasePro = VGroup(CoinbasePro_text, CoinbasePro_dot)

        Kraken_text = Tex('Kraken', color=PURPLE_C)
        Kraken_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.15 * vol_scaler).next_to(Kraken_text, RIGHT)
        Kraken_perc = Tex(r'10\%', color=BLUE).next_to(Kraken_dot, RIGHT)
        Kraken = VGroup(Kraken_text, Kraken_dot)

        Bittrex_text = Tex('Bittrex', color=BLUE_E)
        Bittrex_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.05 * vol_scaler).next_to(Bittrex_text, RIGHT)
        Bittrex = VGroup(Bittrex_text, Bittrex_dot)

        Binance_text = Tex('Binance', color=YELLOW)
        Binance_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.3 * vol_scaler).next_to(Binance_text, LEFT)
        Binance = VGroup(Binance_text, Binance_dot)

        Huobi_text = Tex('Huobi', color=BLUE)
        Huobi_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.15 * vol_scaler).next_to(Huobi_text, LEFT)
        Huobi = VGroup(Huobi_text, Huobi_dot)

        FTX_text = Tex('FTX', color=BLUE_C)
        FTX_dot = LabeledDot('Vol', radius=vol_multiplier, color=vol_color).scale(0.1 * vol_scaler).next_to(FTX_text, LEFT)
        FTX = VGroup(FTX_text, FTX_dot)

        ex_group1 = VGroup(Bitstamp, Bittrex, Kraken, CoinbasePro).arrange(DOWN, aligned_edge=LEFT, buff=1.7).move_to(
            ORIGIN).to_edge(LEFT)
        ex_group2 = VGroup(Binance, Huobi, FTX).arrange(DOWN, aligned_edge=RIGHT, buff=2.5).move_to(ORIGIN).to_edge(RIGHT)

        vols = VGroup(*[ entity[ 1 ] for entity in ex_group1 ] + [ entity[ 1 ] for entity in ex_group2 ])
        vols_list = [ entity[ 1 ] for entity in ex_group1 ] + [ entity[ 1 ] for entity in ex_group2 ]

        aggr_vol = LabeledDot('Aggr. Volume', radius=1)
        aggr_vol = LabeledDot(Tex(r'\emph{Aggr.\\Vol}', color=BLACK), radius=1.5, color=ORANGE).scale(1.3)

        self.play(Create(mark_price))

        self.play(Create(m_px_formula))

        self.play(*[ Write(element) for element in [ px_1, px_2 ] ])
        self.play(*[ Unwrite(element) for element in [ m_px_formula, px_1, px_2, mark_price ] ])

        self.play(*[ Create(element) for element in [ ex_group1, ex_group2 ] ])

        self.wait(1)

        self.play(ReplacementTransform(vols.copy(), aggr_vol))

        # self.play(Create(aggr_vol),run_time = 0.3)

        frac_line = Line(start=LEFT * 2, end=RIGHT * 2).shift(UP)

        self.play(aggr_vol.animate.shift(DOWN * 1.5), Create(frac_line))

        self.play(LaggedStart(
            *[ ApplyMethod(element.next_to, frac_line, UP, 0.4, rate_func=there_and_back_with_pause, run_time=2) for element in
               vols_list ], lag_ratio=1), run_time=5)

        # vols = VGroup(*[ entity[ 1 ] for entity in ex_group1 ] + [ entity[ 1 ] for entity in ex_group2 ])

        Bitstamp_perc = Tex(r'5\%', color=Bitstamp_text.color).next_to(Bitstamp_dot, RIGHT)
        CoinbasePro_perc = Tex(r'20\%', color=CoinbasePro_text.color).next_to(CoinbasePro_dot, RIGHT)
        Kraken_perc = Tex(r'15\%', color=Kraken_text.color).next_to(Kraken_dot, RIGHT)
        Bittrex_perc = Tex(r'5\%', color=Bittrex_text.color).next_to(Bittrex_dot, RIGHT)
        Binance_perc = Tex(r'30\%', color=Binance_text.color).next_to(Binance_dot, LEFT)
        Huobi_perc = Tex(r'15\%', color=Huobi_text.color).next_to(Huobi_dot, LEFT)
        FTX_perc = Tex(r'10\%', color=FTX_text.color).next_to(FTX_dot, LEFT)

        Bitstamp.add(Bitstamp_perc)
        Bittrex.add(Bittrex_perc)
        Kraken.add(Kraken_perc)
        CoinbasePro.add(CoinbasePro_perc)
        Binance.add(Binance_perc)
        Huobi.add(Huobi_perc)
        FTX.add(FTX_perc)

        perc_list = [ entity[ 2 ] for entity in ex_group1 ] + [ entity[ 2 ] for entity in ex_group2 ]

        # sq= Square(1)
        #
        # self.add(index_labels(Binance[1][0]))
        # self.play(Binance[1][0][0][1].animate.move_to(ORIGIN))

        self.play(*[ Write(element) for element in perc_list ] + [ Uncreate(aggr_vol), Uncreate(frac_line) ])

        self.wait(1)

        Bitstamp_px = Tex(r'104\$', color=Bitstamp_text.color).next_to(Bitstamp_text, DOWN).align_to(Bitstamp_text, LEFT)
        CoinbasePro_px = Tex(r'100\$', color=CoinbasePro_text.color).next_to(CoinbasePro_text, DOWN).align_to(CoinbasePro_text, LEFT)
        Kraken_px = Tex(r'102\$', color=Kraken_text.color).next_to(Kraken_text, DOWN).align_to(Kraken_text, LEFT)
        Bittrex_px = Tex(r'96\$', color=Bittrex_text.color).next_to(Bittrex_text, DOWN).align_to(Bittrex_text, LEFT)
        Binance_px = Tex(r'97\$', color=Binance_text.color).next_to(Binance_text, DOWN).align_to(Binance_text, RIGHT)
        Huobi_px = Tex(r'99\$', color=Huobi_text.color).next_to(Huobi_text, DOWN).align_to(Huobi_text, RIGHT)
        FTX_px = Tex(r'100\$', color=FTX_text.color).next_to(FTX_text, DOWN).align_to(FTX_text, RIGHT)

        Bitstamp.add(Bitstamp_px)
        Bittrex.add(Bittrex_px)
        Kraken.add(Kraken_px)
        CoinbasePro.add(CoinbasePro_px)
        Binance.add(Binance_px)
        Huobi.add(Huobi_px)
        FTX.add(FTX_px)

        px_list = [ entity[ 3 ] for entity in ex_group1 ] + [ entity[ 3 ] for entity in ex_group2 ]

        self.play(*[ Write(element) for element in px_list ])
        perc_and_px_list = [ ]

        for i in range(len(px_list)):
            px = px_list[ i ]
            perc = perc_list[ i ]

            perc_and_px_list.append(px)
            perc_and_px_list.append(MathTex(r'\times'))
            perc_and_px_list.append(perc)
            perc_and_px_list.append(Tex(r'+'))

        perc_and_px_list = perc_and_px_list[ 0:-1 ]

        print(UP)
        print(type(UP))

        weighted_px_formula = VGroup(*perc_and_px_list)

        text_and_dot_list = [ ]

        for i in range(len(px_list)):
            text = [ entity[ 0 ] for entity in ex_group1 ] + [ entity[ 0 ] for entity in ex_group2 ]
            text = text[ i ]
            dot = [ entity[ 1 ] for entity in ex_group1 ] + [ entity[ 1 ] for entity in ex_group2 ]
            dot = dot[ i ]

            text_and_dot_list.append(dot)
            text_and_dot_list.append(text)

        texts_and_dots = VGroup(*text_and_dot_list)

        # self.play(LaggedStart(*[Create(text_and_dot,rate_func=reverse) for text_and_dot in text_and_dot_list],lag_ratio=0),
        #           weighted_px_formula.animate.arrange(RIGHT).move_to(ORIGIN), run_time= 5)
        self.play(FadeOut(texts_and_dots),
                  weighted_px_formula.animate.arrange(RIGHT).move_to(ORIGIN).scale(0.7), run_time=2)
        px_index = MathTex('99.25').scale(1.5)
        self.play(ReplacementTransform(weighted_px_formula, px_index))

        self.wait(1)


class slippage(Scene):
    def construct(self):
        slippage = Tex('Slippage').scale(2)

        self.play(Create(slippage))

        self.wait(q)
        self.play(Uncreate(slippage))

        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text).move_to(ORIGIN)
        pair.set_z_index(3)

        self.play(Create(pair, run_time=q))

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

        # my_int.add_updater()
        self.play(Create(curr_px_rect))
        # self.play(curr_px_valuetracker.animate.set_value(120))

        self.play(FadeIn(curr_px_number_100), run_time=0.01)

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
        self.play(Create(shrt_black_sheet), run_time=0.1)
        self.play(Create(long_black_sheet), run_time=0.1)
        self.play(Create(separated_shrt_table),
                  Create(separated_long_table))

        def create_order(self, place_or_cancel, buy_or_sell, px, qty, asset):

            target_pos = order_book_long_table if buy_or_sell == "BUY" else order_book_shrt_table
            start_from = LEFT if place_or_cancel == "Place" else RIGHT

            order_paper = Rectangle(height=1.5, width=1.2)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{qty} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order = VGroup(order_paper, order_text).to_edge(start_from)

            self.play(Create(order))
            self.wait(q)
            self.play(FadeOut(order, target_position=target_pos))
            # change_waiting_order(self, target_pos, 3, 2, 1300, 1)

        create_order(self, "Place", 'BUY', 'Market', 20, 'BTC')
        long_table_px_pos = separated_long_table[ 0 ].get_center()
        long_table_order_pos = separated_long_table[ 1 ].get_center()

        # curr_px_rect.set_color(GREEN)
        self.play(Circumscribe(separated_shrt_table[ 12 ]))

        # self.play(Transform(separated_shrt_table[13][0],Integer(30, fill_color=separated_shrt_table[ 13 ][ 0 ].fill_color,
        #                                                                 font_size=separated_shrt_table[ 13 ][ 0 ].font_size).move_to(
        #     separated_shrt_table[ 13 ][ 0 ]).align_to(
        #     separated_shrt_table[ 13 ][ 0 ], LEFT)))

        self.play(curr_px_rect.animate.set_color(GREEN),
                  Transform(curr_px_number_100, Integer(101, unit=r"\$", color=GREEN).move_to(curr_px_rect)),
                  Transform(separated_shrt_table[ 13 ][ 0 ], Integer(30, fill_color=separated_shrt_table[ 13 ][ 0 ].fill_color,
                                                                     font_size=separated_shrt_table[ 13 ][ 0 ].font_size).move_to(
                      separated_shrt_table[ 13 ][ 0 ]).align_to(
                      separated_shrt_table[ 13 ][ 0 ], LEFT)))

        create_order(self, "Place", 'BUY', 'Market', 280, 'BTC')

        self.play(FadeOut(separated_shrt_table[ 12 ], shift=LEFT),
                  FadeOut(separated_shrt_table[ 13 ], shift=RIGHT),
                  curr_px_rect.animate.set_color(GREEN),
                  separated_long_table.animate.shift(DOWN * separated_shrt_table[ 0 ].height),
                  Transform(curr_px_number_100, Integer(101, unit=r"\$", color=GREEN).move_to(curr_px_rect)))

        separated_shrt_table.remove(separated_shrt_table[ 12 ], separated_shrt_table[ 13 ])
        self.play(separated_shrt_table.animate.next_to(curr_px_rect, UP, buff=0),
                  FadeIn(separated_long_table_org[ 2 ].move_to(long_table_px_pos), shift=RIGHT),
                  FadeIn(separated_long_table_org[ 3 ].move_to(long_table_order_pos), shift=LEFT))

        separated_long_table.add(separated_long_table_org[ 2 ].move_to(long_table_px_pos),
                                 separated_long_table_org[ 3 ].move_to(long_table_order_pos))
        self.play(FadeOut(separated_shrt_table[ 10 ], shift=LEFT),
                  FadeOut(separated_shrt_table[ 11 ], shift=RIGHT),
                  separated_long_table.animate.shift(DOWN * separated_shrt_table[ 0 ].height),
                  Transform(curr_px_number_100, Integer(102, unit=r"\$", color=GREEN).move_to(curr_px_rect)))

        separated_shrt_table.remove(separated_shrt_table[ 10 ], separated_shrt_table[ 11 ])
        self.play(separated_shrt_table.animate.next_to(curr_px_rect, UP, buff=0),
                  FadeIn(separated_long_table_org[ 0 ].move_to(long_table_px_pos), shift=RIGHT),
                  FadeIn(separated_long_table_org[ 1 ].move_to(long_table_order_pos), shift=LEFT))

        # self.add(index_labels(separated_shrt_table)[ 9 ])
        slippage_new_val = Integer(870, fill_color=separated_shrt_table[ 9 ][ 0 ].fill_color,
                                   font_size=separated_shrt_table[ 9 ][ 0 ].font_size).move_to(
            separated_shrt_table[ 9 ][ 0 ].get_center()).align_to(separated_shrt_table[ 9 ][ 0 ], LEFT)

        self.play(Transform(separated_shrt_table[ 9 ][ 0 ], slippage_new_val),
                  Transform(curr_px_number_100, Integer(103, unit=r"\$", color=GREEN).move_to(curr_px_rect)))

        # self.add(index_labels(separated_long_table_org))

        # curr_px_rect.set_color(GREEN)
        # self.play(Transform(curr_px_number_100,Integer(101, unit=r"\$", color=GREEN).move_to(curr_px_rect)),run_time=1)

        # separated_long_table.add(separated_shrt_table[ 12 ], separated_shrt_table[ 13 ])

        # self.play(FadeIn(separated_long_table_org[ 2 ].move_to(long_table_px_pos), shift=RIGHT),
        # FadeIn(separated_long_table_org[ 3 ].move_to(long_table_order_pos), shift=LEFT))

        # entry = order_book_shrt_table.get_entries().next_to(pair_rect,LEFT)

        # self.play(Create(order_book_shrt_table.get_entries().next_to(pair_rect,LEFT)))
        # self.add(index_labels(separated_shrt_table))
        def change_waiting_order(self, table, r, c, new_val, run_time):
            a = table.get_entries(pos=(r, c))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        def change_waiting_order_by_perc(self, table, r, c, perc, run_time):
            a = table.get_entries(pos=(r, c))

            new_val = int(a.get_value() * ((100 + perc) / 100))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        #
        # curr_px_number_100.add_updater(
        #     lambda x: x.become(Integer(curr_px_valuetracker.get_value(), unit=r"\$", color=GREEN).move_to(curr_px_rect)))

        create_order(self, "Place", 'BUY', '101', 30, 'BTC')

        self.play(Transform(separated_long_table_org[ 3 ][ 0 ], Integer(30, fill_color=separated_long_table_org[ 3 ][ 0 ].fill_color,
                                                                        font_size=separated_long_table_org[ 3 ][ 0 ].font_size).move_to(
            separated_long_table_org[ 3 ][ 0 ]).align_to(
            separated_long_table_org[ 3 ][ 0 ], LEFT)))

        create_order(self, "Place", 'BUY', '102', 15, 'BTC')

        self.play(Transform(separated_long_table_org[ 1 ][ 0 ], Integer(15, fill_color=separated_long_table_org[ 1 ][ 0 ].fill_color,
                                                                        font_size=separated_long_table_org[ 1 ][ 0 ].font_size).move_to(
            separated_long_table_org[ 1 ][ 0 ]).align_to(
            separated_long_table_org[ 1 ][ 0 ], LEFT)))

        # self.add(index_labels(separated_long_table))
        self.play(*[ FadeOut(mobject) for mobject in
                     [ pair, curr_px_rect, separated_long_table, separated_shrt_table, separated_long_table_org, curr_px_number_100 ] ])
        slippage_form = MathTex('SlippageCost', '=', 'CurrentPrice', r'\times', 'Quantity', '-', 'AveragePurchasePrice', r'\times',
                                'Quantity').scale(0.9)
        # 'Slippage']).scale(0.8)

        # self.add(index_labels(slippage_form))

        self.play(Write(slippage_form.move_to(ORIGIN)))
        self.play(slippage_form.animate.shift(UP * 2),
                  slippage_form[ 6 ].animate.move_to(ORIGIN))

        avrg_101_text = MathTex('50BTC', '\  at\  ', r'101\$')
        avrg_102_text = MathTex('100BTC', '\  at\  ', r'102\$')
        avrg_103_text = MathTex('150BTC', '\  at\  ', r'103\$')

        avrg_text = VGroup(avrg_101_text, avrg_102_text, avrg_103_text).arrange(DOWN, center=False, aligned_edge=RIGHT, buff=0.3).next_to(
            slippage_form[ 6 ], DOWN)

        self.play(Write(avrg_text))

        avrg_101_multi_text = MathTex(r'\times').scale(0.8).move_to(avrg_101_text[ 1 ].get_center())
        avrg_102_multi_text = MathTex(r'\times').scale(0.8).move_to(avrg_102_text[ 1 ].get_center())
        avrg_103_multi_text = MathTex(r'\times').scale(0.8).move_to(avrg_103_text[ 1 ].get_center())

        self.play(Transform(avrg_101_text[ 1 ], avrg_101_multi_text),
                  Transform(avrg_102_text[ 1 ], avrg_102_multi_text),
                  Transform(avrg_103_text[ 1 ], avrg_103_multi_text))

        avrg_101_equal_text = MathTex(r'=').scale(0.8).next_to(avrg_101_text[ 2 ], RIGHT)
        avrg_102_equal_text = MathTex(r'=').scale(0.8).next_to(avrg_102_text[ 2 ], RIGHT)
        avrg_103_equal_text = MathTex(r'=').scale(0.8).next_to(avrg_103_text[ 2 ], RIGHT)

        avrg_101_text.add(avrg_101_equal_text)
        avrg_102_text.add(avrg_102_equal_text)
        avrg_103_text.add(avrg_103_equal_text)

        self.play(Write(avrg_101_equal_text),
                  Write(avrg_102_equal_text),
                  Write(avrg_103_equal_text))

        avrg_101_result_text = MathTex(r'5050\$').scale(0.9).next_to(avrg_101_equal_text, RIGHT)
        avrg_102_result_text = MathTex(r'10200\$').scale(0.9).next_to(avrg_102_equal_text, RIGHT)
        avrg_103_result_text = MathTex(r'15450\$').scale(0.9).next_to(avrg_103_equal_text, RIGHT)

        self.play(Write(avrg_101_result_text),
                  Write(avrg_102_result_text),
                  Write(avrg_103_result_text))
        avrg_result_text = VGroup(avrg_101_result_text, avrg_102_result_text, avrg_103_result_text)

        self.play(FadeOut(avrg_text, shift=LEFT),
                  avrg_result_text.animate.arrange(DOWN, center=False, aligned_edge=RIGHT, buff=0.3).next_to(slippage_form, DOWN))

        bar = Line(start=LEFT, end=RIGHT).next_to(avrg_103_result_text, DOWN)
        plus_sign = MathTex('+').next_to(avrg_103_result_text, LEFT, buff=0.5)

        avrg_result_text.add(bar, plus_sign)

        self.play(Create(bar),
                  Create(plus_sign))

        final_cost = MathTex(r'30700\$').scale(0.9).next_to(bar, DOWN).align_to(avrg_103_result_text, RIGHT)

        self.play(Create(final_cost))

        self.play(FadeOut(avrg_result_text, shift=UP),
                  final_cost.animate.next_to(slippage_form[ 6 ], DOWN))

        divide_sign = MathTex(r'\divisionsymbol \   300BTC').next_to(final_cost, RIGHT)

        self.play(Create(divide_sign))
        final_cost_group = VGroup(final_cost, divide_sign)

        avrg_price = MathTex(r'102.33\$')
        self.play(Transform(VGroup(slippage_form[ 6 ], final_cost_group), avrg_price.shift(DOWN)))
        # self.play(Transform(slippage_form[6],avrg_price))
        # Transform(slippage_form[6],avrg_price)

        # avrg_price.move_to(slippage_form[6].get_center())

        # self.play(Transform(,avrg_price))

        # self.play()
        # slippage_form[ 6 ].set_color(RED)
        final_cost_group.set_color(GREEN)
        avrg_price.set_color(BLUE)
        self.play(slippage_form.animate.arrange(RIGHT))

        curr_px_slippage = MathTex(r'101\$').move_to(slippage_form[ 2 ])

        self.play(Transform(slippage_form[ 2 ], curr_px_slippage))

        qty_curr = Tex('300BTC').move_to(slippage_form[ 4 ])
        qty_avrg = Tex('300BTC').move_to(slippage_form[ 8 ])

        self.play(Transform(slippage_form[ 4 ], qty_curr),
                  Transform(slippage_form[ 8 ], qty_avrg))

        self.play(slippage_form.animate.arrange(RIGHT))

        fianl_slippage = MathTex(r'-399\$')
        self.play(ReplacementTransform(slippage_form[ 2: ], fianl_slippage))
        self.play(VGroup(slippage_form[ 0:2 ], fianl_slippage).animate.arrange(RIGHT))
        self.play(Transform(slippage_form[ 1 ], MathTex(r'\approx').move_to(slippage_form[ 1 ].get_center())))

        self.wait(5)


class supply_and_demand(Scene):
    def construct(self):
        x_range = 20
        ax = Axes(x_range=[ 0, x_range, x_range / 10 ],
                  y_range=[ 0, 256, 25.6 ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": False}
                  )

        supply_val_tracker = ValueTracker(0)
        demand_val_tracker = ValueTracker(0)
        supply_graph = ax.plot(lambda x: (x - supply_val_tracker.get_value()) ** 2,
                               x_range=[ x_range * 0.2 + supply_val_tracker.get_value(), x_range * 0.8 + supply_val_tracker.get_value() ],
                               use_smoothing=False, color=BLUE)
        demand_graph = ax.plot(lambda x: (x_range - (x - demand_val_tracker.get_value())) ** 2,
                               x_range=[ x_range * 0.2 + demand_val_tracker.get_value(), x_range * 0.8 + demand_val_tracker.get_value() ],
                               use_smoothing=False, color=RED)

        supply_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: (x - supply_val_tracker.get_value()) ** 2,
                    x_range=[ x_range * 0.2 + supply_val_tracker.get_value(), x_range * 0.8 + supply_val_tracker.get_value() ],
                    use_smoothing=False, color=BLUE)))
        demand_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: (x_range - (x - demand_val_tracker.get_value())) ** 2,
                    x_range=[ x_range * 0.2 + demand_val_tracker.get_value(), x_range * 0.8 + demand_val_tracker.get_value() ],
                    use_smoothing=False, color=RED)))

        supply_graph_label = Tex('Supply').next_to(supply_graph, UR)
        supply_graph_label.add_updater(lambda label: label.become(Tex('Supply').next_to(supply_graph, UR).shift(LEFT)))
        demand_graph_label = Tex('Demand').next_to(demand_graph, DR)
        demand_graph_label.add_updater(lambda label: label.become(Tex('Demand').next_to(demand_graph, UL).shift(RIGHT)))

        labels = ax.get_axis_labels("Quantity", "Price")

        x_label = ax.get_x_axis_label(
            Tex("Quantity").scale(0.65), edge=DOWN, direction=DOWN, buff=0.5
        )
        y_label = ax.get_y_axis_label(
            Tex('Price').scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,
        )

        axis_labels = VGroup(x_label, y_label)

        supply_graph.add(supply_graph_label)
        demand_graph.add(demand_graph_label)

        # label_rect = LabeledRectangle('Government',4,5)
        self.play(Create(ax),
                  Create(supply_graph),
                  Create(demand_graph),
                  Create(axis_labels))

        lines = ax.get_lines_to_point(ax.c2p(1, 3))
        lines.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
            ax.c2p((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2,
                   supply_graph.underlying_function((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2)))))
        self.add(lines)

        # horizontal_line = ax.get_horizontal_line(supply_graph)
        def reverse(t: float) -> float:
            return -t + 1

        # self.play(Create(lines[ 0 ]),
        #           Create(lines[ 1 ]))
        cross_dot = Dot(0.7).move_to(ax.c2p((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2,
                                            supply_graph.underlying_function(
                                                (20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2)))
        cross_dot_text = MathTex('Equalibrium')
        cross_dot.add_updater(lambda x: x.move_to(ax.c2p((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2,
                                                         supply_graph.underlying_function(
                                                             (20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2))))
        cross_dot_text.add_updater(lambda x: x.next_to(cross_dot, RIGHT))
        self.play(Create(cross_dot),
                  Write(cross_dot_text))

        self.play(supply_val_tracker.animate.set_value(-3))
        self.play(demand_val_tracker.animate.set_value(-3))
        self.play(demand_val_tracker.animate.set_value(3))
        self.play(supply_val_tracker.animate.set_value(3))

        supply_func = supply_graph.get_function()

        print(supply_func)
        print(type(supply_func))
        print(supply_func(5))
        print(type(supply_func(5)))

        # new_dot = Dot(0.5, color=RED).move_to(ax.c2p(5, supply_graph.underlying_function(5)))
        #
        # self.play(Create(new_dot))
        #

        self.play(FadeOut(self.mobjects, shift=UP))
        self.wait(3)


class A_and_B_withdrawal(Scene):
    def construct(self):
        A = create_entity("A", 0.5, WHITE, "1 BTC", ORANGE, 0.7, 0.3).shift(RIGHT * 4 + UP * 1)
        B = create_entity("B", 0.5, WHITE, "100 $", GREEN, 0.7, 0.3).shift(RIGHT * 4 + DOWN * 1)
        AB_bar = Line(start=np.array([ A.get_x() - 1, A.get_y() - (A.get_y() - B.get_y()) / 2, 0 ]),
                      end=np.array([ A.get_x() + 1, A.get_y() - (A.get_y() - B.get_y()) / 2, 0 ]))

        seoul_text = Tex("Seoul").next_to(A[ 0 ], UP, buff=0.25).scale(0.7)
        busan_text = Tex("Busan").next_to(B[ 1 ], DOWN, buff=0.25).scale(0.7)

        self.play(DrawBorderThenFill(A),
                  DrawBorderThenFill(B),
                  # DrawBorderThenFill(AB_bar),
                  Write(seoul_text),
                  Write(busan_text), run_time=q)

        self.wait(q)

        A_line = Text("I want USD").next_to(A, LEFT).scale(0.6)
        B_line = Text("I want BTC").next_to(B, LEFT).scale(0.6)

        self.play(AnimationGroup(Write(A_line),
                                 Write(B_line), lag_ratio=1, run_time=q))
        self.play(AnimationGroup(Unwrite(A_line),
                                 Unwrite(B_line), lag_ratio=1, run_time=q))

        A_asset_btc = A[ 1 ]
        B_asset_usd = B[ 1 ]

        A_asset_btc.set_z_index(3)
        B_asset_usd.set_z_index(3)

        A_asset_pos = A_asset_btc.get_center()
        B_asset_pos = B_asset_usd.get_center()

        self.play(CyclicReplace(A_asset_btc, B_asset_usd, rate_func=there_and_back, path_arc=3))

        ex_rect = RoundedRectangle(corner_radius=0.5, height=8, width=6)
        ex_rect_text = Tex("Exchange").next_to(ex_rect, UP, buff=0.2).scale(0.8)
        ex = VGroup(ex_rect, ex_rect_text).move_to(ORIGIN).to_edge(LEFT)

        self.play(Create(ex, run_time=q))
        self.wait(q)

        ex_server_rect = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.1)
        ex_server_led_1 = Dot(radius=0.05, fill_color=GREEN).shift(RIGHT * 0.2)
        ex_server_led_2 = Dot(radius=0.05, fill_color=GREEN).shift(RIGHT * 0.4)

        ex_server = VGroup(ex_server_rect, ex_server_led_1, ex_server_led_2).next_to(ex_rect, UP, aligned_edge=UP, buff=-0.5).shift(
            LEFT * 1.5)
        self.play(Create(ex_server))
        self.wait(q)

        ex_ledger = MathTable(
            [ [ "Ex", r"a " ],
              [ "A", r"aaaaaa " ],
              [ "B", r"a " ] ],
            include_outer_lines=True).scale(0.4).next_to(ex_server, RIGHT).align_to(ex_server, UP).shift(RIGHT)
        ex_ledger[ 0 ][ 5 ].set_color(BLACK)
        ex_ledger[ 0 ][ 1 ].set_color(BLACK)
        ex_ledger[ 0 ][ 3 ].set_color(BLACK)
        ex_ex_ledger = ex_ledger[ 0 ][ 1 ]
        A_ex_ledger = ex_ledger[ 0 ][ 3 ]
        B_ex_ledger = ex_ledger[ 0 ][ 5 ]

        self.play(Create(ex_ledger))

        A_wallet_rect = RoundedRectangle(0.1, width=1, height=1)
        A_wallet_text = Tex(r"A wallet").next_to(A_wallet_rect, UP, buff=0.2).scale(0.6)
        A_wallet = VGroup(A_wallet_rect, A_wallet_text)

        B_wallet_rect = RoundedRectangle(0.1, width=1, height=1)
        B_wallet_text = Tex("B wallet").next_to(B_wallet_rect, UP, buff=0.2).scale(0.6)
        B_wallet = VGroup(B_wallet_rect, B_wallet_text)

        ex_wallet_rect = RoundedRectangle(0.1, width=1, height=1)
        ex_wallet_text = Tex("ex wallet").next_to(ex_wallet_rect, UP, buff=0.2).scale(0.6)
        ex_wallet = VGroup(ex_wallet_rect, ex_wallet_text)

        wallets = VGroup(ex_wallet, A_wallet, B_wallet).arrange(DOWN).next_to(ex_rect, RIGHT, aligned_edge=RIGHT, buff=-1).shift(DOWN)

        self.play(Create(wallets))

        self.play(A_asset_btc.animate.move_to(A_wallet_rect),
                  B_asset_usd.animate.move_to(B_wallet_rect), rate_func=there_and_back)

        # self.play(Create(wallets[ 0 ]))

        wallet_expl = Text("Wallet means a group of wallets and bank account. it is better to say it is an account")

        bank_rect = RoundedRectangle(corner_radius=0.2, height=1.8, width=4)
        bank_rect_text = Tex("Bank").next_to(bank_rect, UP, buff=0.1).scale(0.5)
        bank_server = ex_server.copy().next_to(bank_rect, UP, aligned_edge=UP, buff=-0.5).shift(LEFT)
        bank = VGroup(bank_rect, bank_rect_text, bank_server).to_edge(UP).shift(RIGHT)

        B_bank_bal_tracker = ValueTracker(0)

        bank_ledger = MathTable(
            [ [ "Ex", r"a " ],
              [ "A", r"aaaaaa " ],
              [ "B", r"a " ] ],
            include_outer_lines=True).scale(0.4).next_to(bank_server, RIGHT).align_to(bank_server, UP)

        # self.add(index_labels(bank_ledger[ 0 ]))
        # position = bank_ledger[0][5].get_center()
        # print(type(bank_ledger[0][5]))
        # bank_ledger[0][5].add_updater(lambda x: Integer(number = B_bank_bal_tracker.get_value()).move_to(position))
        # new_num.number = 65
        num = Integer(50).move_to(bank_ledger[ 0 ][ 5 ])
        bank_ledger[ 0 ][ 5 ].set_color(BLACK)
        bank_ledger[ 0 ][ 1 ].set_color(BLACK)
        bank_ledger[ 0 ][ 3 ].set_color(BLACK)

        ex_bank_ledger = bank_ledger[ 0 ][ 1 ]
        A_bank_ledger = bank_ledger[ 0 ][ 3 ]
        B_bank_ledger = bank_ledger[ 0 ][ 5 ]

        self.play(B_bank_bal_tracker.animate.set_value(35))

        self.play(Create(bank, run_time=q))
        self.play(Create(bank_ledger))
        self.wait(q)

        self.play(B_asset_usd.animate.next_to(bank_server, DOWN))
        B_100usd_bank = create_entity("B", 0.5, GRAY, "100 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_bank_ledger)
        self.play(FadeIn(B_100usd_bank, target_position=bank_server, scale=0.2))
        self.wait(1)
        self.play(B_100usd_bank.animate.move_to(ex_bank_ledger))

        # B_100usd = MathTex(r"100\$").scale(0.5).next_to(ex_server, DOWN)
        B_100usd = create_entity("B", 0.5, WHITE, "100 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_ex_ledger)
        self.play(FadeIn(B_100usd, target_position=ex_server, scale=0.2))
        self.play(B_100usd.animate.move_to(B_ex_ledger))
        self.wait(q)

        blocks = VGroup(*[ Square(0.7, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(10) ]).arrange(DOWN).to_edge(
            RIGHT)
        scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.3) for i in range(10) ])
        chain = Rectangle(height=9, width=0.05, color=WHITE).move_to(blocks)

        for i in range(len(blocks)):
            chain = Difference(chain, blocks[ i ])

        scripts.set_z_index(2)
        blocks.set_z_index(1)
        chain.set_z_index(0)
        blockchain_bar = DashedLine(start=blocks[ 0 ].get_top(), end=blocks[ 9 ].get_bottom(), dash_length=0.4, dashed_ratio=0.6,
                                    stroke_color=WHITE).shift(LEFT)
        blockchain = VGroup(blocks, chain, scripts)
        self.play(Create(VGroup(blocks, scripts)), FadeIn(chain))
        # self.play()
        self.wait(q)

        # self.play(A_asset_btc.animate.next_to(bank_server, RIGHT))
        self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))
        self.play(A_asset_btc.animate.move_to(ex_wallet_rect))
        self.play(A_asset_btc.animate.move_to(ex_server))
        self.play(A_asset_btc.animate.move_to(A_wallet_rect))

        AB_wallet = VGroup(A_wallet, B_wallet)

        ex_wallet_rect_incl = RoundedRectangle(0.1, width=1.3, height=4).move_to(AB_wallet)

        self.play(Transform(ex_wallet_rect, ex_wallet_rect_incl), ex_wallet_text.animate.next_to(ex_wallet_rect_incl, UP, buff=0.1))

        self.play(VGroup(wallets, A_asset_btc).animate.shift(UP * 0.8))

        # self.play(wallets.animate, A_asset_btc.animate.shift, B_100usd.animate.shift(DOWN * 0.5))

        pair_rect = RoundedRectangle(corner_radius=0.1, height=ex_wallet_rect.height, width=3)
        pair_rect_text = Tex("BTC/USD").scale(0.5).next_to(pair_rect, UP, buff=0.1)
        pair = VGroup(pair_rect, pair_rect_text).next_to(ex_rect, LEFT, aligned_edge=LEFT, buff=-2).align_to(ex_wallet_rect, DOWN)

        self.play(Create(pair, run_time=q))
        A_1btc = create_entity("B", 0.5, WHITE, "1BTC", WHITE, 0.7, 0.3)[ 1 ].move_to(A_ex_ledger)

        self.play(Create(A_1btc))

        btc_usd = VGroup(A_1btc, B_100usd)

        self.play(btc_usd.animate.arrange(RIGHT).move_to(pair_rect))

        # gov_rect = RoundedRectangle(corner_radius=0.2, height=2, width=4)
        # gov_rect_text = Tex("Gov").next_to(gov_rect, UP, buff=0.1).scale(0.5)
        # # gov_server = ex_server.copy().next_to(gov_rect, UP, aligned_edge=UP, buff=-0.5).shift(LEFT)
        # gov = VGroup(gov_rect, gov_rect_text).to_edge(DOWN).shift(RIGHT)
        #
        # self.play(Create(gov, run_time=q))
        # self.wait(q)

        pair_group = Group(pair, A_1btc, B_100usd)

        whole_scene = self.mobjects

        btc_usd.save_state()
        pair.save_state()

        self.play(FadeOut(Group(*self.mobjects)), pair.animate.move_to(ORIGIN), btc_usd.animate.move_to(ORIGIN))

        btc_usd.restore()
        pair.restore()

        self.play(FadeIn(*whole_scene))

        # VGroup(pair, A_asset_btc, B_100usd).animate.move_to(ORIGIN)
        self.wait(1)

        # A_asset = A[ 1 ]
        # B_asset = B[ 1 ]
        # AB_asset = VGroup(A_asset, B_asset)

        curr_px = Integer(100, unit=r'\$')

        # self.play(Create(curr_px.move_to(pair_rect)))

        def create_personal_order(self, entity, place_or_cancel, buy_or_sell, px, qty, asset):
            target_pos = ex_server
            start_from = entity

            order_paper = Rectangle(height=1.5, width=1.2)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{qty} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order = VGroup(order_paper, order_text).scale(0.7).next_to(start_from[ 0 ], LEFT)

            self.play(Create(order))
            self.wait(q)
            return FadeOut(order, target_position=target_pos)
            # change_waiting_order(self, target_pos, 3, 2, 1300, 1)

        self.play(create_personal_order(self, A, "Place", 'SELL', r'120\$', 1, 'BTC'))
        self.play(create_personal_order(self, B, "Place", 'BUY', r'80\$', 1, 'BTC'))

        ask_val_track = ValueTracker(120)
        bid_val_track = ValueTracker(80)

        ask = Tex(r'- 120\$')
        bid = Tex(r'- 80\$')
        ask.add_updater(lambda ask: ask.become(Tex(rf'SELL at {int(ask_val_track.get_value())}\$').scale(0.4).next_to(A_1btc, RIGHT)))
        bid.add_updater(lambda bid: bid.become(Tex(rf'BUY at {int(bid_val_track.get_value())}\$').scale(0.4).next_to(B_100usd, RIGHT)))

        # _1btc_group =VGroup(A_1btc,ask)
        # _100usd = VGroup(B_100usd,bid)

        self.play(VGroup(A_1btc, B_100usd).animate.arrange(DOWN, buff=2).move_to(pair_rect).shift(LEFT * 0.5),
                  Create(curr_px.move_to(pair_rect)))

        self.play(Create(ask),
                  Create(bid))

        self.play(create_personal_order(self, A, "Cancel", 'SELL', r'120\$', 1, 'BTC'),
                  create_personal_order(self, B, "Cancel", 'BUY', r'80\$', 1, 'BTC'))
        self.play(create_personal_order(self, A, "Place", 'SELL', r'110\$', 1, 'BTC'),
                  create_personal_order(self, B, "Place", 'BUY', r'90\$', 1, 'BTC'))

        self.play(ask_val_track.animate.set_value(110),
                  bid_val_track.animate.set_value(90), rate_func=linear)

        self.play(create_personal_order(self, A, "Cancel", 'SELL', r'110\$', 1, 'BTC'),
                  create_personal_order(self, B, "Cancel", 'BUY', r'90\$', 1, 'BTC'))
        self.play(create_personal_order(self, A, "Place", 'SELL', r'101\$', 1, 'BTC'),
                  create_personal_order(self, B, "Place", 'BUY', r'100\$', 1, 'BTC'))

        self.wait(1)
        self.play(ask_val_track.animate.set_value(101),
                  bid_val_track.animate.set_value(100), rate_func=linear)

        self.play(create_personal_order(self, A, "Place", 'SELL', r'101\$', 1, 'BTC'))
        self.play(create_personal_order(self, A, "Cancel", 'SELL', r'101\$', 1, 'BTC'))
        self.play(create_personal_order(self, A, "Place", 'SELL', r'Market', 1, 'BTC'))

        self.play(ask_val_track.animate.set_value(100), rate_func=linear)

        # ask.clear_updaters()
        # bid.clear_updaters()

        # self.play(Unwrite(VGroup(ask),VGroup(bid)))
        self.play(CyclicReplace(VGroup(A_1btc), VGroup(B_100usd)),
                  Unwrite(ask),
                  Unwrite(bid))

        self.play(A_1btc.animate.move_to(B_ex_ledger),
                  B_100usd.animate.move_to(A_ex_ledger))

        A_line = Text("Give my USD").next_to(A[ 0 ], LEFT).scale(0.6)
        B_line = Text("Give my BTC").next_to(B[ 0 ], LEFT).scale(0.6)

        self.play(AnimationGroup(Write(A_line),
                                 Write(B_line), lag_ratio=1, run_time=q))
        self.play(AnimationGroup(Unwrite(A_line),
                                 Unwrite(B_line), lag_ratio=1, run_time=q))

        # self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))

        # self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))

        self.play(A_asset_btc.animate.move_to(ex_server))
        self.play(A_asset_btc.animate.move_to(blocks[ 8 ]))
        self.play(A_asset_btc.animate.move_to(B_asset_pos))
        self.play(Uncreate(A_1btc))

        self.play(B_100usd_bank.animate.move_to(A_bank_ledger))
        self.play(Uncreate(B_100usd))
        self.play(Uncreate(B_100usd_bank))
        self.play(B_asset_usd.animate.move_to(A_asset_pos))
        # self.play(A_asset_btc.animate.move_to(B_asset_pos))

        self.wait(1)


class eliptical(Scene):
    def construct(self):
        var = Variable(-2, Tex("x value"), num_decimal_places=3)
        my_tracker = var.tracker

        ax = Axes().move_to(ORIGIN)
        graph = ax.plot(
            lambda x: x + 3,
            color=RED, )

        # c2p_point2 = plane.c2p(my_tracker.get_value(), graph.get_point_from_function(my_tracker.get_value()))
        graph1 = ax.plot_implicit_curve(lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3, color=RED
                                        )

        def get_my_dot():
            # c2p_point2 = ax.c2p(my_tracker.get_value(), graph.get_point_from_function(1))
            # c2p_point2 = ax.c2p(*graph.get_point_from_function(my_tracker.get_value()))
            c2p_point2 = ax.c2p(my_tracker.get_value(),
                                graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 0 ])

            c2p_point1 = ax.c2p(my_tracker.get_value(),
                                graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 0 ])
            c2p_point2 = ax.c2p(my_tracker.get_value(),
                                graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 1 ])
            point2_y_val = graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 1 ]
            dot1 = Dot(c2p_point1, color=YELLOW)
            dot2 = Dot(c2p_point2, color=BLUE)

            arrow1 = Arrow(ax.get_center(), dot1.get_center(), buff=0)
            arrow1 = Arrow(ax.get_center(), dot2.get_center(), buff=0)
            # label = Tex(f"({my_tracker.get_value()},{point2_y_val})").next

            group = VGroup(dot1, dot2, arrow1)
            return group

        dots = always_redraw(lambda: get_my_dot())
        self.play(Create(var))
        self.play(Create(dots), Create(ax), Create(graph1))
        self.play(my_tracker.animate.set_value(3))
        self.wait(1)
        self.play(my_tracker.animate.set_value(-2))


class working_aside(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[ -10, 10 ], y_range=[ -10, 10 ], background_line_style={"stroke_opacity": 0.8},
                            axis_config={"include_numbers": True, "stroke_width": 10, "color": PURPLE})

        # graph = ImplicitFunction(
        #     lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3,
        #     color=YELLOW
        # )
        # plane.plot(graph)

        ax = Axes(
            x_range=[ -10, 10, 1 ],
            y_range=[ -100, 100, 1 ],
            tips=False,

        )

        graph1 = plane.plot_implicit_curve(lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3, color=RED
                                           )

        point = ax.c2p(5, 3)

        dot = Dot(point)
        v_line = plane.get_line_from_axis_to_point(1, point, line_func=Line, line_config={}, color=BLUE, stroke_width=5)

        my_tracker = ValueTracker(3)

        c2p_point1 = plane.c2p(my_tracker.get_value(),
                               graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 0 ])
        c2p_point2 = plane.c2p(my_tracker.get_value(),
                               graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 1 ])

        dot1 = always_redraw(lambda: Dot(c2p_point1, color=YELLOW))
        dot2 = Dot(c2p_point2, color=BLUE, radius=0.2)
        # dot1.add_updater(lambda mob : mob.ne)

        # h_line = Line(start=plane.c2p(0,graph.get_point_from_function(1)), end=plane.c2p(-2,graph.get_curve_functions(1)))

        # label = plane.get_graph_label(graph=graph1,label=Tex("this is a point"),x_val=4.798567064438934, dot=True, direction=DR, dot_config={"color":BLUE})
        # t_label = plane.get_T_label(x_val=4, graph=graph1, label=Tex("x-value"))

        # area = plane.get_area(graph1, x_range=(-1,5))
        # self.play(Create(graph1), Create(plane), Create(dot), Create(v_line), Create(h_line))
        self.play(Create(NumberPlane()), Create(graph1), Create(dot1), Create(dot2))
        self.play(my_tracker.animate.set_value(5))
        self.wait(0.5)
        self.play(Create(dot1))
        self.wait(0.5)

        # self.play(my_tracker.animate.set_value(0))
        # self.play(ApplyMethod(my_tracker.set_value(),2, run_time=2))

        #
        # backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
        # backg_plane.add_coordinates()
        #
        # my_plane = NumberPlane(x_range = [-6,6], x_length = 5,
        # y_range = [-10,10], y_length=5)
        # my_plane.add_coordinates()
        # my_plane.shift(RIGHT*3)
        #
        # my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5),
        # x_range=[-6,6], color = GREEN_B)
        #
        # label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(
        #     my_plane, UP, buff=0.2)
        #
        # area = my_plane.get_area(graph = my_function,
        # x_range = [-5,5], color = BLUE)
        #
        # horiz_line = Line(
        #     start = my_plane.c2p(0, my_function.underlying_function(-2)),
        # end = my_plane.c2p(-2, my_function.underlying_function(-2)),
        # stroke_color = YELLOW, stroke_width = 10)
        #
        # self.play(backg_plane.animate.set_opacity(0.2))
        # self.wait()
        # self.play(DrawBorderThenFill(my_plane), run_time=2)
        # self.wait()
        # self.play(Create(my_function), Write(label), run_time=2)
        # self.wait()
        # self.play(FadeIn(area), run_time = 2)
        # self.wait()
        # self.play(Create(horiz_line), run_time = 2)
        # self.wait()

        # banner = ManimBanner()
        title = Title("How does a computer understand a letter?")
        # btc_msg1 = sha256_tex_mob("BTC")
        # btc_msg2 = Tex(sha256_bit_string("BTC"))
        # btc_msg3 = bit_string_to_mobject("BTC")
        # self.play(Create(btc_msg3))

        # self.play(Write(title, run_time=1))

        ascii_table = MathTable(
            [ [ "Alpha", "Decimal", "Hex" ],
              [ "A", 65, 41 ],
              [ "B", 66, 42 ],
              [ "L", 76, "4C" ],
              [ "X", 88, 58 ],
              [ "Y", 89, 59 ],
              [ "Z", 90, "5A" ]
              ],
            include_outer_lines=True)

        ascii_table.scale(0.7)

        def dot_position(mobject):
            mobject.set_value(dot.get_center()[ 0 ])
            mobject.next_to(dot)

        dot = Dot(RIGHT * 3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        # self.add(dot, label)
        Text1 = Text("BTC")
        # text_int = Va
        # tracker = ValueTracker(sha256_bit_int(5))

        a = Integer(0)

        a.add_updater(lambda a: a.set_value(tracker.get_value()))
        # decimal = MathTex(r"")

        # def int_to_bin(int_mob):
        #     val = int(int_mob.get_value())
        #     bin1 = format(val, '0256b')[0:63]
        #     # bin2 = format(val, '0256b')[64:127]
        #     # bin3 = format(val, '0256b')[128:191]
        #     bin4 = format(val, '0256b')[192:255]
        #
        #     return VGroup(Tex(bin1),MathTex(r"\vdots"),Tex(bin4)).arrange_in_grid(3,1,buff=0.2)
        # def bin_list(int_mob):
        #     val = int(int_mob.get_value())
        #     bin1 = format(val, '0256b')[0:63]
        #     bin2 = format(val, '0256b')[64:127]
        #     bin3 = format(val, '0256b')[128:191]
        #     bin4 = format(val, '0256b')[192:255]
        #     bin_list=[bin1,bin2,bin3,bin4]
        #
        #     return bin_list

        # decimal= always_redraw(int_to_bin(tracker).next_to(a, DOWN))
        # decimal= Text("2").add_updater(lambda x : int_to_bin(tracker).next_to(a, DOWN))
        # decimal= always_redraw(lambda : int_to_bin(tracker).move_to(DOWN).scale(0.7))

        circle = Circle(radius=1, color=RED)

        square = Square(1, color=BLUE)
        # group = VGroup(circle)

        circle.add(square)
        circle.arrange_in_grid(2, 1, buff=2)
        #
        self.add(msg_to_mob("BTC", 32, 4))

        # self.play(Create(Text1))
        # self.play(Create(a), Create(decimal))
        # self.play(tracker.animate.set_value(1565645),run_time=1)
        # self.play(Text1.animate.set_value("djfkd"),run_time=1)
        # self.play(ApplyMethod(tracker.set_value(),1231231231231236456789789789789789879789789789789789, run_time=2)

        # tracker.set_value(12312312312312123131312312312313123123113123123121233)
        # a.set_value(50)
        # self.wait(2)

        # start = 2.0
        #
        # x_var = Variable(start, 'x', num_decimal_places=3)
        # sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
        # Group(x_var, sqr_var).arrange(DOWN)
        #
        # sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))
        #
        # self.add(x_var, sqr_var)
        # self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
        # self.wait(0.1)
