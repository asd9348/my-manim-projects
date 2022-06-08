from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color

config.frame_width = 16
config.frame_height = 9

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


class working2(Scene):
    def construct(self):

        dot = LabeledDot('Fuck')

        self.add(dot[0][0])

class working1(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))
        ##### 그리하여 오늘은 에이엠엠ㅇ과 엑스와잉는 케이 공식에 대해 알아보겠습니다
        # 에이엠엠 타이틀과
        # 엑스와이는 케이 띄움
        amm_text = Tex('Automatic Market Maker').scale(2)
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text))
        self.play(Create(xyk))
        self.play(Uncreate(amm_text))
        self.play(Uncreate(xyk))

        ##### 원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 wbtc같이 이더리움 체인에서
        ##### 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠스빈다

        ##### 뎩스가 탄생하고 사람들은 비트코인과 usdt의 거래쌍을 만들고 싶었습니다.
        ##### 그래서 중앙화 거래소에서 비트코인 가격이 300달러인 걸 보고
        ##### 비트코인 10개와 3000달러를 함께 유동성 풀이라는 것에 넣었습니다
        ##### 이것은 스마트 컨트랙트를 통해 자신의 자산으로 유동성으로 제공하곘다는 것입니다.
        ##### 이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다
        ##### 말만 들으면 뭔지 이해가 안 될테니 이제 자세히 알아보겠습니다
        # 그냥 텍스트만
        expl_plain_text = Text(
            'DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n그래서 중앙화 거래소에서 비트코인 가격이 300달러인 걸 보고\n비트코인 10개와 3000달러를 함께 유동성 풀이라는 것에 넣었습니다\n스마트 컨트랙트를 통해 자신의 자산을 유동성으로 제공한다는 것입니다.\n이제 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다',
            font='Batang', line_spacing=3, font_size=25)
        self.play(Create(expl_plain_text))
        self.play(Uncreate(expl_plain_text))

        ##### 일단 우리가 알고있는 오더북이 없이 어떻게 거래를 하는가가 궁금하실 겁니다
        ##### 오더북에서는 그저 사람들이 거래하는 것을 바탕으로 알아서 각겨이 정해집니다
        # 오더북 열고
        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text).move_to(ORIGIN)

        # self.play(Create(pair, run_time=q))
        self.wait(q)

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

        curr_px_valuetracker = ValueTracker(100)
        curr_px_number_100 = Integer(100, unit=r"\$", color=RED).move_to(curr_px_rect)

        int_valuetracker = ValueTracker(100)

        self.play(Create(curr_px_rect))

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

        order_book_long_table.set_row_colors(GREEN, GREEN, GREEN, GREEN, GREEN)

        self.play(Create(order_book_long_table), Create(order_book_shrt_table))

        self.wait(1)

        ##### 덱스에서는 오더북대신 오토매틱마켓메이커를 사용하고
        # 오더북 엑스자 치고 에이엠엠 텍스트로 트랜스폼
        order_book_cross = Cross(stroke_width=25).scale(3)
        order_book_shit = VGroup(curr_px_rect, curr_px_number_100, order_book_long_table, order_book_shrt_table, order_book_cross)
        self.play(Create(order_book_cross))
        self.play(ReplacementTransform(order_book_shit, amm_text))

        amm_text = Tex('Automatic Market Maker').scale(2)
        self.play(GrowFromCenter(amm_text))

        ##### 오토매틱마켓메이커는 줄여서 amm이라고 부르고
        # 풀네임 약자로 줄이고
        amm_acronym_text = Tex('AMM').scale(2).move_to(amm_text)
        self.play(ReplacementTransform(amm_text, amm_acronym_text))

        ##### 그냥 프로그램 혹은 가격을 정하는 방식같은 추상적 개념이라고 생각하시면 됩니다
        # 에이엠엠 텍스트 밑에 프로그램 혹은 컨셉
        program_or_concept_text = Tex('Program or Concept?').next_to(amm_text, D)
        self.play(Create(program_or_concept_text))

        ##### 오토매틱마켓메이커를 돌리는데는 일반적으로 유동성 풀이 필요합니다
        # 에이엠엠이 풀박스로 트랜스폼

        pool_rect = RoundedRectangle(width=6, height=4, corner_radius=0.5)
        pool_rect_text = Tex('Pool').next_to(pool_rect, U)
        self.play(ReplacementTransform(program_or_concept_text, pool_rect_text),
                  ReplacementTransform(amm_acronym_text, pool_rect))

        ##### 이 유동성 풀은 우리가 중앙화 거래소에서 봤던 거래쌍이라고 생각하시면 됩니ㅏㄷ
        ##### 우리가 비티씨나 테더를 들고 중앙화 거래소에서 비티씨테더 거래쌍 창으로 가듯이
        ##### 덱스에서는 유동성 풀에 접근해서 거래를 하게됩니다
        ##### 그렇다면 비티씨테더 풀이라는 것은 이더리움 같은게 아니라 비티씨와 테더를 가지고 있어야할 것입니다
        # 풀위에 비티씨 테더라고 텍스트 하나 더 생기고
        # 비티씨 덩어리 테더 덩어리 풀로 풍덩

        btc_usdt_text = Tex('BTC/USDT').next_to(pool_rect_text, U)
        btc_usdt_text_final = Tex('BTC/USDT Pool').move_to(pool_rect_text)

        self.play(Create(btc_usdt_text))
        self.play(ReplacementTransform(VGroup(pool_rect_text, btc_usdt_text), btc_usdt_text_final))

        btc_lump = LabeledDot('BTC', radius=1, color=ORANGE).shift(L * 5.5)
        usdt_lump = LabeledDot('USDT', radius=1, color=GREEN_C).shift(R * 5.5)
        btc_lump.save_state()
        usdt_lump.save_state()
        btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump))
        self.play(MoveAlongPath(btc_lump, btc_lump_arc),
                  MoveAlongPath(usdt_lump, usdt_lump_arc))

        ##### 중앙화 거래소 비티씨테더 페어에서 사람들이 이더리움을 들고 모인게 아니라
        ##### 비티씨와 테더를 들고 모인것 처럼 말입니다
        # 옆에 이더리움 솔라나 생기고 엑스자 후 페이드 아웃

        sol_lump = LabeledDot('SOL', radius=1, color=PURPLE_E).shift(L * 5.5 + U * 1)
        eth_lump = LabeledDot('ETH', radius=1, color=DARK_BLUE).shift(R * 5.5 + U * 2)
        dot_lump = LabeledDot('DOT', radius=1, color=MAROON_C).shift(R * 5.5 + D * 3)
        sol_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(sol_lump)
        eth_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(eth_lump)
        dot_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(dot_lump)
        other_coins = VGroup(sol_lump, eth_lump, dot_lump)
        other_coins_cross = VGroup(sol_lump_cross, eth_lump_cross, dot_lump_cross)

        self.play(Create(other_coins))
        self.play(Create(other_coins_cross))
        self.play(Uncreate(other_coins),
                  Uncreate(other_coins_cross))

        ##### 당연한 얘기지만 비티씨 테더 페어에 만약 비티씨만 존재한다면 아무것도 일어나지 않을 것입니다
        ##### 왜냐하면 비티씨 테더 페어라는 것은 두가지의 교환이 일어나는 공간이라는 것인데
        ##### 둘 중 하나만 있으면 교환이 성립하지 않으니까요
        # 먼저 테더 없애고 풀에 비티씨만 남은 거 보여주면서 정지
        # 사이클릭 리플레이스 데어 앤 백
        # 그 다음은 테더가 다시 생기고 비티씨가 없어진 상태를 보여주면 서 정지
        # 사임클릭 리플레이스 데어 앤 백

        exchange_speech_text_1 = Tex(r'I am here to\\get USDT with my BTC').shift(5.5 * R + 3 * D).scale(0.7)
        long_face_1 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_1).scale(3)
        btc_lump_long_face = btc_lump.copy().shift(R * 15)

        self.play(FadeOut(usdt_lump))
        self.play(Create(exchange_speech_text_1),
                  btc_lump_long_face.animate.move_to(R * 5))
        self.play(ReplacementTransform(exchange_speech_text_1, long_face_1))
        self.play(Uncreate(long_face_1),
                  Uncreate(btc_lump_long_face))
        self.play(FadeIn(usdt_lump))

        exchange_speech_text_2 = Tex(r'I am here to\\get BTC with my USDT').shift(5.5 * L + 3 * D).scale(0.7)
        long_face_2 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_2).scale(3)
        usdt_lump_long_face = usdt_lump.copy().shift(L * 15)

        self.play(FadeOut(btc_lump))
        self.play(Create(exchange_speech_text_2), usdt_lump_long_face.animate.move_to(L * 5))
        self.play(ReplacementTransform(exchange_speech_text_2, long_face_2))
        self.play(Uncreate(long_face_2),
                  Uncreate(usdt_lump_long_face))
        self.play(FadeIn(btc_lump))

        ##### 그래서 우리는 풀에 사람들이 거래할 수 있도록 유동성을 공급하고
        ##### 유동성을 공급한다는 것은 비티씨와 테더를 같이 넣어준다는 것입니다
        ##### 반드시 같이 넣어야하는 이유는 곧 알게됩니다
        # 왼쪽에서 비티씨하고 테더 같이 들어감
        # 오른쪽에서 비티씨하고 테더하고 같이 들어감
        btc_lump_liq_prov_1 = btc_lump.copy().move_to(np.array([ -6, 2, 0 ]))
        usdt_lump_liq_prov_1 = usdt_lump.copy().move_to(np.array([ -6, -2, 0 ]))
        btc_lump_liq_prov_2 = btc_lump.copy().move_to(np.array([ 6, 2, 0 ]))
        usdt_lump_liq_prov_2 = usdt_lump.copy().move_to(np.array([ 6, -2, 0 ]))

        self.play(Create(VGroup(btc_lump_liq_prov_1, usdt_lump_liq_prov_1, btc_lump_liq_prov_2, usdt_lump_liq_prov_2)))
        self.play(FadeOut(btc_lump_liq_prov_1, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_1, target_position=pool_rect))
        self.play(FadeOut(btc_lump_liq_prov_2, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_2, target_position=pool_rect))

        ##### 덱스의 있는 참여자는 크게 두 종류입니다
        ##### 유동성 제공자와 거래자입니다
        ##### 유동성 제공자는 영어로 줄여서 엘피라고도 부릅니다
        # 중앙에는 여전히 풀이 있고 그 위에 덱스 파티시 펀트라고 텍스트 생김
        # 덱스파티시펀트 트리로 갈라지고 유동성제공자
        dex_participants_text = Tex('DEX Participants').scale(1.2).to_edge(U)
        liq_prov_text = Tex('Liq Provider').shift(L * 5.5 + U * 2.5)
        trader_text = Tex('Trader').shift(R * 5.5 + U * 2.5)
        line_to_liq_prov = Line(dex_participants_text.get_corner(DL), liq_prov_text.get_top())
        line_to_trader = Line(dex_participants_text.get_corner(DR), trader_text.get_top())

        self.play(Create(dex_participants_text))
        self.play(Create(line_to_liq_prov),
                  Create(line_to_trader))
        self.play(Create(liq_prov_text),
                  Create(trader_text))

        ##### 유동성 제공자는 아까처럼 말한 것처럼 비티씨와 테더를 같이 넣어주거나 빼면서
        ##### 유동성을 조절합니다. 즉 풀 사이즈를 키우거나 줄입니다. 이것은 나중에 보겠지만
        ##### 케이값을 움직이는 것입니다. 곧 보게 될테니 걱정 안 하셔도 됩니다
        # 유동성 제공자 텍스트 밑에 엔터티 만들고 엔터티가 비티씨와 테더를 함께 풀에 넣는 모션
        # 그리고 밑에 텍스트로 체인징 케이 옆에 조그맣게 그래프 케이값 왔다 갔다
        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_prov_text, D)
        liq_prov_btc_asset = liq_provider[ 1 ]
        liq_prov_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(liq_prov_usdt_asset)
        self.play(Create(liq_provider))

        moving_k_text = Tex('Moving K').shift(L * 5.5 + D*1.5)
        liq_prov_tracker = ValueTracker(5)

        coor_sys_liq_prov = Axes(x_range=[ 0, 10, 2 ], y_range=[ 0, 10, 2 ], x_length=2, y_length=2, tips=False,
                                 y_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                                'tip_height': 5},
                                 x_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                                'tip_height': 5}
                                 ).next_to(moving_k_text, D)

        liq_prov_graph = coor_sys_liq_prov.plot(lambda x: 5 / x, x_range=[ 5 / 8, 8 ], use_smoothing=False, color=WHITE)
        liq_prov_graph.add_updater(lambda graph: graph.become(
            coor_sys_liq_prov.plot(lambda x: liq_prov_tracker.get_value() / x, x_range=[ liq_prov_tracker.get_value() / 8, 8 ],
                                   use_smoothing=False, color=WHITE)))

        self.play(Create(moving_k_text))
        self.play(Create(coor_sys_liq_prov),
                  Create(liq_prov_graph))
        self.play(liq_prov_tracker.animate.set_value(9))
        self.play(liq_prov_tracker.animate.set_value(1))
        liq_prov_btc_asset.save_state()
        liq_prov_usdt_asset.save_state()
        self.play(liq_prov_tracker.animate.set_value(9),
                  FadeOut(liq_prov_btc_asset,target_position=btc_lump),
                  FadeOut(liq_prov_usdt_asset,target_position=usdt_lump))
        liq_prov_btc_asset.restore()
        liq_prov_usdt_asset.restore()
        self.play(liq_prov_tracker.animate.set_value(1),
                  FadeIn(liq_prov_btc_asset,target_position=btc_lump),
                  FadeIn(liq_prov_usdt_asset,target_position=usdt_lump))



        ##### 거래자들은 풀에 자신이 테더를 넣고 그에 상응하는 비트코인을 빼가든지
        ##### 가진 비트코인을 넣고 그에 상응하는 테더를 빼가든지 할 수 있습니다
        ##### 각각 비트코인 매도와 매수에 대응하는 행위입니다
        ##### 이것은 그래프위의 점을 이동시키는 행위입니다.
        ##### 이것또한 곳 보게 될테니 걱정 안 하셔도 됩니다
        ##### 유동성제공자는 케이값을 움직이고 거래자는 점을 이동시킨다라고만 기억해두십시오
        ##### 그리고 유동성 제공자는 거래자들이 내는 수수료를 받으면서 수익을 냅니다
        ##### 거래자들은 코인을 사고 팔며 가격차익을 얻습니다
        # 거래자 텍스트 밑에 엔터티 만들고 엔터티가 비티씨넣고 풀에서 테더 돌려받고
        # 테더 넣고 비티씨 돌렵받는 모션
        # 그리고 무빙 닷 텍스트 밑에ㅔ 띄우거 옆에는 작은 그래프에서 점왔다갔다
        # 트리 구조 전부 사라짐
        trader = create_entity(Tex(r' \emph{Trader}', color=BLACK).scale(0.9), 1, WHITE, "BTC", ORANGE, 1.4,
                               0.3).next_to(trader_text, D)
        trader_btc_asset = trader[ 1 ]
        trader_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(trader, DOWN, buff=0.1)
        trader_usdt_asset_copy = create_entity("A", 0.5, WHITE, "USDT", BLUE, 1.4, 0.3)[ 1 ].move_to(trader_btc_asset)
        trader.add(trader_usdt_asset)
        self.play(Create(trader))

        moving_dot_text = Tex('Moving Dot').shift(R * 5.5 + D*1.5)
        trader_tracker = ValueTracker(3)

        coor_sys_trader = Axes(x_range=[ 0, 10, 2 ], y_range=[ 0, 10, 2 ], x_length=2, y_length=2, tips=False,
                               y_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                              'tip_height': 5},
                               x_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                              'tip_height': 5}
                               ).next_to(moving_dot_text, D)

        trader_graph = coor_sys_trader.plot(lambda x: 5 / x, x_range=[ 5 / 8, 8 ], use_smoothing=False, color=WHITE)
        curr_dot = Dot(radius=0.1, color=RED).move_to(coor_sys_trader.c2p(trader_tracker.get_value(),
                                                                          trader_graph.underlying_function(trader_tracker.get_value())))
        curr_dot.set_z_index(2)
        curr_dot.add_updater(lambda dot: dot.move_to(coor_sys_trader.c2p(trader_tracker.get_value(),
                                                                         trader_graph.underlying_function(trader_tracker.get_value()))))


        self.play(Create(moving_dot_text))

        self.play(Create(coor_sys_trader),
                  Create(trader_graph),
                  Create(curr_dot))
        
        self.play(trader_tracker.animate.set_value(6),
                  FadeOut(trader_btc_asset,target_position=btc_lump),
                  FadeIn(trader_usdt_asset_copy,target_position= usdt_lump))
        self.play(trader_tracker.animate.set_value(1),
                  FadeIn(trader_btc_asset,target_position=btc_lump),
                  FadeOut(trader_usdt_asset_copy,target_position=usdt_lump))



        self.play(trader_tracker.animate.set_value(1))
        self.play(trader_tracker.animate.set_value(6))
        # self.play(trader_tracker.animate.set_value(1),
        #           liq_prov_tracker.animate.set_value(9))
        # self.play(trader_tracker.animate.set_value(6),
        #           liq_prov_tracker.animate.set_value(1))
        # self.play(trader_tracker.animate.set_value(1),
        #           liq_prov_tracker.animate.set_value(9))
        # self.play(trader_tracker.animate.set_value(6),
        #           liq_prov_tracker.animate.set_value(1))


        ##### 풀이 운영되는 기본 원칙은 언제나 같은 가치의 자산이 들어있게 한다는 것입니다
        ##### 그래서 이걸 기반으로 오토매틱 마켔메이커는 가격을 산정합니다
        ##### 현재 풀의 상태를 10비티씨와 3000테더라고 하겠습니다
        ##### 10비트와 3000테더가 같은 가치기 때문에
        ##### 비티씨는 1개에 300테더입니다

        # 올웨이즈 이퀄 밸류 우측 상단에 띄우면서 풀 내부에 비티씨 테더 사이에 이콜 싸인
        # 올웨이즈 이퀄 밸류 텍스트가 에이엠엠 프라이스 디터미네이션으로 트랜스폼
        equal_sign = Tex('=').scale(1.5)
        always_equal_value = Tex('Always Equal Values')
        price_determination = Tex('Price determined')
        always_equal_value_texts = VGroup(always_equal_value, price_determination).arrange(D).shift(D*3)

        value_equal_1 = MathTex(r'Value\  of\  BTC in Pool', '=', r'Value\  of\   USDT in Pool').arrange(D).scale(0.94).shift(D*3)
        value_equal_2 = MathTex(r'10 BTC', '=', r'3000 USDT').shift(D*3)

        price_frac = MathTex(r'\frac{3000 USDT}{10 BTC}').shift(D*3)

        final_price_per_btc = MathTex(r'300 USDT\  per \  BTC').shift(D*3)



        self.play(Create(always_equal_value_texts))
        self.play(Create(equal_sign))

        self.play(ReplacementTransform(always_equal_value_texts, value_equal_1))
        self.play(ReplacementTransform(value_equal_1, value_equal_2))
        self.play(ReplacementTransform(value_equal_2, price_frac))
        self.play(ReplacementTransform(price_frac, final_price_per_btc))




        ##### 이것은 모두 미리 작성된 프로그래밍 언어의 스크립트를 실행하는 것으로 이루어집니다
        ##### 스마트 컨트랙트 덕분에 우리는 중앙화 거래서와 같은 제3자를 거치지 않을 수 있게 됐습니다
        all_thanks_to = Tex('Everything without 3rd entity','All thanks to Smart Contract').arrange(D).shift(D*3)
        self.play(ReplacementTransform( final_price_per_btc,all_thanks_to))

