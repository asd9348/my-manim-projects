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


def there_and_back_expo(t: float) -> float:
    return -t + 1


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
        ##### 다음으로 넘어가기 전에 수수료예 대해 알아보겠스빈다.
        # fee 제목 만들기
        fees = Tex('Fees').scale(2)

        self.play(Create(fees))
        self.play(Uncreate(fees))

        ##### 덱스에서 수수료는 독특한 방식으로 작동합니다.
        ##### 거래를 하기 위해 코인을 풀로 보내면 코인이 풀에 도착하기 전에 수수료를 떼고
        ##### 남은 금액만 풀에 들어가서 그거에 맞게 거래가 일어납니다. 그리고 거래가 종료되면 풀에 그냥 수수료를 추가합니다.
        ##### 수수료는 거래가 발생할 때마다 풀에 쌓이기 때문에 매번 거래가 종료되면 케이값은 증가합니다
        # 풀박스 만들고 코인덩어리까지 세팅 이전 거 활용
        # 코인이들어가다 멈추고 분리됨
        # 수수료는 따로 빠져서 가만히 있고 거래완료 그리고 풀로 수수료가 들어감

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        self.play(Create(pool_rect_text),
                  Create(pool_rect))

        btc_lump = LabeledDot('BTC', radius=1, color=ORANGE).shift(L * 1.5)
        usdt_lump = LabeledDot('USDT', radius=1, color=GREEN_C).shift(R * 1.5)
        # btc_lump.save_state()
        # usdt_lump.save_state()
        # btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        # usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump))

        btc_lump_inflow = LabeledDot('BTC', radius=1, color=ORANGE).shift(R * 5.5)

        self.play(Create(btc_lump_inflow))
        self.play(btc_lump_inflow.animate.next_to(pool_rect, buff=1))

        btc_lump_fee = LabeledDot(MathTex('Fee', font_size=20, color=BLACK), radius=0.3, color=ORANGE).move_to(btc_lump_inflow)
        btc_lump_fee.set_z_index(-1)

        self.play(btc_lump_inflow.animate.scale(0.8),
                  btc_lump_fee.animate.shift(D * 2))

        self.play(FadeOut(btc_lump_inflow, target_position=btc_lump),
                  btc_lump.animate.scale(1.1))
        # self.play(btc_lump.animate.scale(1.1))

        usdt_lump_outflow = LabeledDot('USDT', radius=1, color=GREEN).shift(R * 5.5)
        self.play(FadeIn(usdt_lump_outflow, target_position=usdt_lump),
                  usdt_lump.animate.scale(1 / 1.1))

        self.play(FadeOut(btc_lump_fee, target_position=btc_lump),
                  btc_lump.animate.scale(1.05))
        self.play(FadeOut(usdt_lump_outflow, shift=R))

        k_increase = Tex('K increased a bit', 'after every trade').arrange(D).next_to(pool_rect, D)

        self.play(Create(k_increase))

        self.play(VGroup(pool_rect, pool_rect_text, btc_lump, usdt_lump, k_increase).animate.to_edge(L))

        ##### 중앙화 거래소에서는 거래소가 가져가니 우리의 수수료가 가격에 영향을 줄 일은 없었습니다
        ##### 그러나 덱스에서는 수수료가 풀 내부의 비트 테더 비율을 조금씩 바꾸기 때문에 우리가 생각한 것과 미세하게 가격이 차이가 납니다
        ##### 수수료가 1퍼인 상황을 생각해 보겠ㅅ빈다
        ##### 비트 10개 3000테더가 있는 풀에 1비트를 보내면 수수료를 뗀 0.99비트가 전송됩니다
        ##### 그리고 0.99에 대한 교환이 일어나고 풀에서 3000-30000분에 10.99테더가 빠져나가고 30000나누기 10.99인 2729테더가 남습니다
        ##### 지금까지는 케이는 여전히 30000입니다
        ##### 그뒤에 풀에 빼놨던 수수료인 0.01비트를 넣습니다. 풀에는 이제 11비트와 2729테더가 남아있습니다
        ##### 케이는 30027.297로 약간 증가했습니다 현재 비트의 가격은 248.159테더입니다
        # 오른쪽은 수수료 있는 경우 위에 타이틀 달아주고
        # 케이 바리어블 비티씨바리어블 테더 바리어블 가격 바리어블 다 만들어줌
        fee_situation = Tex(r'1\% Fee').shift(R * 4 + U * 3)

        k_var_fee = Variable(30000, 'k', var_type=Integer)
        btc_var_fee = Variable(10.00, 'BTC')
        usdt_var_fee = Variable(3000.00, 'USDT')
        price_var_fee = Variable(300.00, 'Price')

        k_tracker_fee = k_var_fee.tracker
        btc_tracker_fee = btc_var_fee.tracker
        usdt_tracker_fee = usdt_var_fee.tracker
        price_tracker_fee = price_var_fee.tracker
        price_unit = Tex(r'USDT', color=WHITE).next_to(price_var_fee, buff=0.1)
        price_unit.add_updater(lambda unit: unit.next_to(price_var_fee, R, buff=0.1))
        # price_var_fee.add(price_unit)
        price_var_fee.add_updater(lambda v: price_tracker_fee.set_value(usdt_tracker_fee.get_value() / btc_tracker_fee.get_value()))

        VGroup(k_var_fee, btc_var_fee, usdt_var_fee, price_var_fee).arrange(D, aligned_edge=L).shift(R * 3.5, U * 1)

        self.play(Create(fee_situation))
        self.play(Create(VGroup(k_var_fee, btc_var_fee, usdt_var_fee, price_var_fee, price_unit)))

        self.play(btc_tracker_fee.animate.set_value(10.99),
                  usdt_tracker_fee.animate.set_value(30000 / 10.99), run_time=5)

        self.wait(2)
        self.play(btc_tracker_fee.animate.set_value(11),
                  k_tracker_fee.animate.set_value(11 * (30000 / 10.99)), run_time=5)

        # self.play(btc_tracker_fee.animate.set_value(10.99))

        ##### 원래 1비트를 매도했다고 생각하면 가격은 30000나누기 11나누기 11인 247.933테더가 되어야합니다
        ##### 그러나 수수료가 있었다면 30000나누기 10.99 나누기 11인 248.159 테더가 됩니다.
        ##### 즉 이전 거래자의 행동에 따라서 미세하게 이익이 바뀝니다.
        # 윈쪽에 수수료가 없는 겨웅 타이틀 달고
        # 케이 바리어블 비티씨바리어블 테더 바리어블 가격 바리어블 다 만들어줌
        if_fee = Tex(r'If it were 11 BTC', 'It would be 247.93 USDT').arrange(D).next_to(price_var_fee, D, buff=1).align_to(price_var_fee,
                                                                                                                            L)
        self.play(Create(if_fee))

        ##### 비트를 매도하는 행위에서 수수료가 있던 경우가 가격이 덜 떨어졌으므로
        ##### 같은 방향 즉 이후에 매도할 사람은 원래 앞사람이 거래하고 247테더를 생각하고 있었으나
        ##### 예상보다 돈을 좀 더 건질 수 있게 됐습니다
        ##### 반대로 앞사람과 반대방향 즉 매수를 하려던 사람은 자신이 앞사람을 보고 생각하던 247달러보다
        ##### 높은 248테더에 매수를 해야해서 예상보다 지출이 늘었습니다
        #

        self.wait(5)


class working1(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))

        ##### ###############################################################################################################

        ##### 이번에는 비티씨를 파는 경우입니다
        ##### 아까와 같은 원리로 비티씨를 팔면 가격이 내려가고
        ##### 여기서도 프라이스 임팩트를 막을 수는 없습니다.
        #####
        ##### 가격은 예상대로 내려가고 매도자는 여전히 기분이 좋지 않습니다
        ##### 300달러를 보고 3개를 판매했지만 900달러가 아닌 692달러 밖에 못 받았기 때문입니다.
        ##### 이 거대한 괴리는 유동성즉 풀의 크기가 작기 때문입니다.
        #####

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider))

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        # ax[0].move_to(np.array([ax[0].g() ,liq_pool_rect.get_bottom()[1],0]))
        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(GREEN)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=WHITE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=WHITE)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

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

        y_marker = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

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

        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        self.play(Create(area))
        self.play(Create(area_text))

        ##### DIVERGE
        #####
        user = create_entity(Tex(r' \emph{User}', color=BLACK), 1, WHITE, "3BTC", ORANGE, 1.4, 0.3).next_to(liq_pool_rect,
                                                                                                            RIGHT, buff=1.5)
        user_asset_btc = user[ 1 ]
        user_asset_pos = user_asset_btc.get_center()
        user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", GREEN, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

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

        scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(GREEN, opacity=1)
        scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(ORANGE, opacity=1)

        scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        scene2_2308usdt_fill_box.set_z_index(3)
        scene2_13btc_fill_box.set_z_index(3)

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
            Integer(692).scale(0.4).rotate(-PI / 2).next_to(scene2_2308usdt_brace, RIGHT, buff=0.3)))
        scene2_13btc_brace_label = Integer(usdt_tracker.get_value())
        scene2_13btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene2_13btc_brace, LEFT, buff=0.3)))

        scene2_braces = VGroup(scene2_2308usdt_brace, scene2_13btc_brace)
        scene2_brace_labels = VGroup(scene2_2308usdt_brace_label, scene2_13btc_brace_label)

        self.play(Create(scene2_braces),
                  Create(scene2_brace_labels))

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene2_2308usdt_fill_box)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=2307 / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=13 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(RED)
        origin_dot.set_z_index(1.5)

        self.play(Create(origin_dot))
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  Transform(scene2_2308usdt_fill_box, user_asset_usdt),
                  Transform(user_asset_btc, scene2_13btc_fill_box))

        scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)

        self.play(Create(scene2_arrow))

        scene2_slippage_text = Tex(r'I sold 3 BTC \\and got 692 USDT').scale(0.7).next_to(user_asset_pos, DOWN)
        scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        scene2_slippage_result = MathTex(rf'{int(-(k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}\$ \  per\ BTC ').move_to(
            scene2_slippage_form.get_center())

        self.play(Create(scene2_slippage_form),
                  Create(scene2_slippage_text))

        self.play(ReplacementTransform(scene2_slippage_form, scene2_slippage_result))

        self.wait(2)
        ##### ###############################################################################################################
        #####

        #####
        ###################################################################################################################
        #####
        ##### 다음으로 넘어가기 전에 수수료예 대해 알아보겠스빈다.
        #####
        ##### 수수료는 거래가 발생할 때마다 풀에 쌓이기 때문에 매번 거래가 종료되면 케이값은 증가합니다
        ##### 덱스에서 수수료는 독특한 방식으로 작동합니다.
        ##### 거래를 하기 위해 코인을 풀로 보내면 코인이 풀에 도착하기 전에 수수료를 떼고
        ##### 남은 금액만 풀에 들어가서 그거에 맞게 거래가 일어납니다. 그리고 거래가 종료되면 풀에
        ##### 그냥 수수료를 추가합니다.
        ##### 중앙화 거래소에서는 거래소가 가져가니 우리의 수수료가 가격에 영향을 줄 일은 없었습니다
        ##### 그러나 덱스에서는 수수료가 풀 내부의 비트 테더 비율을 조금씩 바꾸기 때문에 우리가 생각한 것과 미세하게 가격이 차이가 납니다
        #####
        ##### 수수료가 1퍼인 상황을 생각해 보겠ㅅ빈다
        ##### 비트 10개 3000테더가 있는 풀에 1비트를 보내면 수수료를 뗀 0.99비트가 전송됩니다
        ##### 그리고 0.99에 대한 교환이 일어나고 풀에서 3000-30000분에 10.99테더가 빠져나가고 30000나누기 10.99인 2729테더가 남습니다
        ##### 지금까지는 케이는 여전히 30000입니다
        ##### 그뒤에 풀에 빼놨던 수수료인 0.01비트를 넣습니다. 풀에는 이제 11비트와 2729테더가 남아있습니다
        ##### 케이는 30027.297로 약간 증가했습니다 현재 비트의 가격은 248.159테더입니다
        #####
        ##### 원래 1비트를 매도했다고 생각하면 가격은 30000나누기 11나누기 11인 247.933테더가 되어야합니다
        ##### 그러나 수수료가 있었다면 30000나누기 10.99 나누기 11인 248.159 테더가 됩니다.
        #####
        ##### 즉 이전 거래자의 행동에 따라서 미세하게 이익이 바뀝니다.
        #####
        ##### 비트를 매도하는 행위에서 수수료가 있던 경우가 가격이 덜 떨어졌으므로
        ##### 같은 방향 즉 이후에 매도할 사람은 원래 앞사람이 거래하고 247테더를 생각하고 있었으나
        ##### 예상보다 돈을 좀 더 건질 수 있게 됐습니다
        ##### 반대로 앞사람과 반대방향 즉 매수를 하려던 사람은 자신이 앞사람을 보고 생각하던 247달러보다
        ##### 높은 248테더에 매수를 해야해서 예상보다 지출이 늘었습니다
        #####
        #####
        ##### ###############################################################################################################
        #####
        ##### 잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다
        #####
        ##### 케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게
        ##### 가격이 내려가는 것은 빨간샊 올라가는 것은 초록색으로 표시했습니다.
        ##### 원점은 회색입니다
        #####
        ##### 가격상승
        ##### 가격하락
        #####
        ##### 케이상승
        ##### 케이하락
        ##### 다시한번명심할 것은 유동성 공급 제거는 가격과 관계가 없습니다
        ##### 그냥 지금 가격에 맞게 풀전체 비중에서 나의 지분을 없애는 것이므로 가격을 움직이는 행위가 아닙니다.
        ##### 프라이스 임팩트와 관계가 없습니다
        #####
        ##### 케이상승 후 가격상승 및 하락
        ##### 케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 13분에 3
        ##### 퍼센트로 따지면 33퍼와 23퍼센트
        #####
        #####
        ##### 케이하락 후 가격상승 및 하락
        ##### 케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 7 분에 3
        ##### 퍼센트로 따지면 33퍼와 42퍼센트
        #####
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        #####
        ##### 각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        ##### 동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다

        self.wait(5)
