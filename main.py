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

t = 3
tt = 5
ttt = 7

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

        mtex_1 = MathTex('for', 'dkjfkd').arrange(D)
        self.play(Create(mtex_1))


class working1(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))

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

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R*0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool),run_time=t)
        self.wait(t)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider),run_time=t)
        self.wait(t)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR,buff = 0.8)

        ax.shift(U*(liq_pool_rect.get_bottom()[1]-ax[0].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
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
                  ReplacementTransform(btc_asset, btc_bar),run_time=t)
        self.wait(t)
        self.play(Write(usdt_var),
                  Write(btc_var),run_time=t)
        self.wait(t)
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
        self.wait(t)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)),run_time=tt
                  )
        self.wait(t)

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1),run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2),run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3),run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int),run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int),run_time=t)
        self.wait(t)

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset),run_time=t)
        self.wait(t)

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

        self.play(Create(xyk_graph_btc),run_time=t)
        self.wait(t)

        self.play(Create(curr_dot),run_time=t)
        self.wait(t)

        self.play(Create(lines),run_time=t)
        self.play(Create(markers),run_time=t)
        self.wait(t)

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

        self.play(Create(area),run_time=t)
        self.play(Create(area_text),run_time=t)
        self.wait(t)


        ##### DIVERGE############################################################################################################

        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))

        # 가격 상승#####################################################################################
        px_up = MathTex(r'Price \  \Uparrow').move_to(liq_provider[0])
        self.play(Write(px_up))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 가격이 올라간다는 건 btc가 usdt보다 상대적으로 인기가 많아진다는 것입니다.

        self.wait(2)
        self.play(Unwrite(px_up))
        self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################
        px_dn = MathTex(r'Price \  \Downarrow').move_to(liq_provider[0])
        self.play(Write(px_dn))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 가격이 내려간다는 건 btc가 usdt보다 상대적으로 인기가 없어진다는 것

        self.wait(2)
        self.play(Unwrite(px_dn))
        self.wait(2)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[0])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # K 하락#####################################################################################
        k_dn = MathTex(r'K \  \Downarrow').move_to(liq_provider[0])
        self.play(Write(k_dn))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

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
        self.play(Unwrite(k_dn))
        self.wait(2)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################
        k_up = MathTex(r'K \  \Uparrow').move_to(liq_provider[0])
        self.play(Write(k_up))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(2)
        self.play(Unwrite(k_up))
        self.wait(2)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # K 원점#####################################################################################
        k_origin = MathTex(r'ORIGIN').move_to(liq_provider[0])
        self.play(Write(k_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(k_origin))
        self.wait(2)

        # K 상승#####################################################################################
        ##### 케이상승 후 가격상승 및 하락
        ##### 케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 13분에 3
        ##### 퍼센트로 따지면 33퍼와 23퍼센트
        k_up_px_dn = MathTex(r'K \  \Uparrow', r'Price\  \Downarrow').arrange(D).move_to(liq_provider[0])
        k_up_px_up = MathTex(r'K \  \Uparrow', r'Price\  \Uparrow').arrange(D).move_to(liq_provider[0])
        self.play(Write(k_up_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)

        # K 상승 가격 하락#####################################################################################
        ##### 케이상승 후 가격상승 및 하락
        ##### 케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 13분에 3
        ##### 퍼센트로 따지면 33퍼와 23퍼센트
        #####
        self.play(Write(k_up_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)


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
        self.play(Unwrite(k_up_px_dn[ 1 ]))
        self.wait(2)

        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_E).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # K 상승 가격 상승#####################################################################################
        self.play(Write(k_up_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)


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
        self.play(Unwrite(k_up_px_up[ 1 ]), Unwrite(k_up_px_dn[ 0 ]))
        self.wait(2)

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_E).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[0])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # K 하락#####################################################################################
        k_dn_px_dn = MathTex( r'K\  \Downarrow',r'Price \  \Downarrow').arrange(D).move_to(liq_provider[0])
        k_dn_px_up = MathTex(r'K\  \Downarrow',r'Price \  \Uparrow').arrange(D).move_to(liq_provider[0])
        self.play(Write(k_dn_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        # 그말은 유동성이 줄었다는 거하고
        # 아까 유동성이 늘었서 슬리피지가 덜 발행하던 것과 달리
        # 지금부터는 슬리피지가 더 발생합니다
        #

        self.wait(2)
        # 역으로 케이가 하락했는데

        # K 하락 가격 하락#####################################################################################
        #####
        ##### 케이하락 후 가격상승 및 하락
        ##### 케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 7 분에 3
        ##### 퍼센트로 따지면 33퍼와 42퍼센트
        #####
        self.play(Write(k_dn_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 케이가 하락한 상태에서 누군가 풀에다 비티씨를 매도해서
        # 가격도 하락합니다
        # 비티씨를 매도하는데 아까와 같이 300달러에서 매도하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마입니다
        # 당연히 아까는 10개에서 3개를 넣는 거였고
        # 지금은 5개에서 3개를 넣는거니까
        # 비율은 30퍼와 60퍼로
        # 완전 차이나게 된다

        self.wait(2)
        self.play(Unwrite(k_dn_px_dn[ 1 ]))
        self.wait(2)

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        # K 하락 가격 상승#####################################################################################
        self.play(Write(k_dn_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 케이가 하락한 상태에서 누군가 풀에서 비티씨를 빼가면서 즉 매수하면서
        # 가격도 상승합니다
        # 비티씨를 매수하는데 아까와 같이 300달러ㅓ에서 매수하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마
        # 당연히 아까는 10개에서 3개를 빼는 거였고
        # 지금은 5개에서 3개를 빼는 것
        # 비율은 30퍼와 60퍼로 상당히 차이난다

        self.wait(2)
        self.play(Unwrite(k_dn_px_up[ 1 ]),
                  Unwrite(k_dn_px_dn[ 0 ]))
        self.wait(2)

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[0])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # 가격 상승#####################################################################################
        px_up_k_up = MathTex(r'Price \  \Uparrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[0])
        px_up_k_dn = MathTex(r'Price \  \Uparrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[0])
        self.play(Write(px_up_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        self.play(Write(px_up_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 49),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 49 / 10),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 아까와는 상황이 다릅니다
        # 현재 가격은 이미 움직여버렸습니다
        # 현재가격은 이미 300에서 올라왔고 여기서
        # 유동성을 넣기 때문에
        # 같은 2비티씨를 유동성을 추가한다고 하면
        # 1비티씨마다 상응하는 올라간 가격의 테더를 같이 넣어줘야합니다
        #

        self.wait(2)
        self.play(Unwrite(px_up_k_up[ 1 ]))
        self.wait(2)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################
        self.play(Write(px_up_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(480000 / 49),
                  btc_tracker.animate.set_value(4),
                  usdt_tracker.animate.set_value(480000 / 49 / 4),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 가격이 올랐을 때 케이가 떨어진다는 건
        # 즉 유동성을 공급했던 사람이 유동성을 회수한다는 것은
        # 풀 사이즈가 작아진다는 것입니다
        # 그 말은 공급자가 1비티씨를 뺄 때 오른 가격만큼의 테더를 회수한다는 애기입니다
        # 2비티씨를 빼면 얼마가 빠집니다

        self.wait(2)
        self.play(Unwrite(px_up_k_dn[ 1 ]),
                  Uncreate(px_up_k_up[ 0 ]))
        self.wait(2)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################

        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[0])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # 가격 하락#####################################################################################
        px_dn_k_up = MathTex(r'Price \  \Downarrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[0])
        px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[0])

        # 가격이 하락한 상태에서 케이를 움직여보겟습니다
        self.play(Write(px_dn_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(px_dn))
        self.wait(2)

        # 가격 하락에서 K상승#####################################################################################

        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        px_dn_k_up = MathTex(r'Price \  \Downarrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[0])
        self.play(Write(px_dn_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 가격이 하락한 상태에서 케이를 넣으렴녀 원래보다 돈이 적게 듭니다
        # 왜냐하면 비티씨 1개를 넣을 때 하락한 각겨만큼의 테더를 넣으면 됩니다

        self.wait(2)
        self.play(Unwrite(px_dn_k_up[ 1 ]))
        self.wait(2)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # 가격 하락에서 K하락#####################################################################################
        px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[0])
        self.play(Write(px_dn_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 11),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)


        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        self.wait(2)
        self.play(Unwrite(px_dn_k_dn[ 1 ]),
                  Uncreate(px_dn_k_up[ 0 ]))
        self.wait(2)

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        # 가격 원점#####################################################################################
        px_origin = MathTex(r'ORIGIN').move_to(liq_provider[0])
        self.play(Write(px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)


        self.wait(2)
        self.play(Unwrite(px_origin))
        self.wait(2)

        # 라인 생성#####################################################################################

        ##### 각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        ##### 동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다

        def making_a_line_3points(p1, p2, p3, color):
            l1 = Line(p1.get_center(), p2.get_center(), color=color)
            l2 = Line(p2.get_center(), p3.get_center(), color=color)
            l1.set_z_index(-2)
            l2.set_z_index(-2)
            line = VGroup(l1, l2)

            return line

        self.play(Uncreate(area),
                  Uncreate(area_text))
        k_px_org_line = making_a_line_3points(k_dn_px_org_dot, k_org_px_org_dot, k_up_px_org_dot, DARK_GREY)
        self.wait(2)

        self.play(Create(k_px_org_line))
        k_px_up_line = making_a_line_3points(k_dn_px_up_dot, k_org_px_up_dot, k_up_px_up_dot, GREEN_E)
        self.wait(2)
        self.play(Create(k_px_up_line))
        k_px_dn_line = making_a_line_3points(k_dn_px_dn_dot, k_org_px_dn_dot, k_up_px_dn_dot, RED_E)
        self.wait(2)
        self.play(Create(k_px_dn_line))
        px_up_k_line = making_a_line_3points(px_up_k_dn_dot, k_org_px_up_dot, px_up_k_up_dot, TEAL_E)
        self.wait(2)
        self.play(Create(px_up_k_line))
        px_dn_k_line = making_a_line_3points(px_dn_k_dn_dot, k_org_px_dn_dot, px_dn_k_up_dot, MAROON_E)
        self.wait(2)
        self.play(Create(px_dn_k_line))

        self.wait(2)
