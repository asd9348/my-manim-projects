from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_functions import *

config.frame_width = 16
config.frame_height = 9


class final(Scene):
    def construct(self):
        pass
        # lec1_s1.construct(self)


class working2(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=
        '#9'
        '#9'
        '#9'
        '#9'
        '#1'
        '잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다#1'
        '케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게, 가격이 내려가는 것은 빨간색 올라가는 것은 초록색으로 표시했습니다. 원점은 회색입니다#1'

        '비티씨 매수로 가격이 상승하는 상황입니다#1'
        '비티씨 매도로 가격이 하락하는 상황입니다#3'
        '유동성 공급으로 케이가 상승하는 상황입니다#1'
        '유동성 제거로 케이가 하락하는 상황입니다#1'
        '다시 한번 명심할 것은 유동성 공급, 제거는 가격과 관계가 없습니다#1'
        '그냥 지금 가격에 맞게 풀 사이즈만 변화시키기에 가격을 움직이는 행위가 아닙니다#1'
        '그러므로 거래자 활동과 달리 프라이스 임팩트와 관계가 전혀 없습니다#1'

        '기본적인 상황들을 복습해봤습니다#1'

        '케이상승 후 가격상승 또는 하락하는 경우를 보겠습니다#1'
        '케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다#1'
        '아까 300테더에서 3개를 매도할 때는 프라이스 임팩트가 23퍼센트 발생했지만#1'
        '지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 19퍼센트만 발생했습니다#1'
        '아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만#1'
        '지금은 유동성이 풍부하고 3개 매수할 때  프라이스 임팩트가 30퍼센트 발생했습니다#1'
        '같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다#1'
        '아까는 10분에 3 지금은 13분에 3, 퍼센트로 따지면 33퍼와 23퍼센트입니다#1'

        '케이하락 후 가격상승 또는 하락하는 경우를 보겠습니다#1'
        '케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다#1'
        '아까 300데터에서 3개를 매도할 때는 프라이스 임팩트가  23퍼센트 발생했지만 #1'
        '지금은 유동성으 적어졌고 3개 매도할 때 프라이스 임팩트가 30퍼센트 발생했습니다#1'
        '아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만#1'
        '지금은 유동성으 적어졌고 3개 매수할 때 프라이스 임팩트가 75퍼센트 발생했습니다#1'
        '같은 3비티씨지만 풀에서 차지하는 비율이 커졌습니다#1'
        '아까는 10분에 3 지금은 7 분에 3, 퍼센트로 따지면 33퍼와 42퍼센트입니다#1'

        '이번에는 가격이 먼저 상승하고 케이상승 또는 하락하는 상황입니다#1'
        '아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다#1'
        '아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 올라버린 가격인 612 테더를 넣어줘야합니다#1'
        '그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됐습니다#1'
        '만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 올라가있는 현재 가격대로 비티씨 한 개당 612테더를 돌려받게 됩니다#3'

        '이번에는 가격이 먼저 하락하고 케이상승 및 하락하는 상황입니다#1'
        '어번에도 현재가격에 맞게 같은 가치를 넣어줘야합니다#1'
        '아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 내려버린 가격인 177 테더를 넣어줘야합니다#1'
        '그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다#1'
        '만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 내려가있는 현재 가격대로 비티씨 한 개당 177테더를 돌려받게 됩니다#3'

        '각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다#1'
        '동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3, asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN,
                                                                                                                        buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Create(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.play(Uncreate(liq_provider), run_time=0.5)
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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)

        # E##############################################

        # TODO 3.479 secs잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다
        # TODO 0:00:37.000  ~  0:00:40.479
        # TODO 1.0secs pause
        # TODO 0:00:40.479  ~  0:00:41.479

        # TODO 10.16 secs케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게, 가격이 내려가는 것은 빨간색 올라가는 것은
        #  초록색으로 표시했습니다. 원점은 회색입니다
        # TODO 0:00:41.479  ~  0:00:51.639
        # TODO 1.0secs pause
        # TODO 0:00:51.639  ~  0:00:52.639

        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))
        self.wait(14.639)

        # 가격 상승#####################################################################################
        # TODO 2.899 secs비티씨 매수로 가격이 상승하는 상황입니다
        # TODO 0:00:52.639  ~  0:00:55.538
        # TODO 1.0secs pause
        # TODO 0:00:55.538  ~  0:00:56.538

        px_up = MathTex(r'Price \  \Uparrow').move_to(liq_provider[ 0 ])
        self.play(Write(px_up))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)
        self.play(Unwrite(px_up), run_time=0.899)
        # self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################

        # TODO 2.875 secs비티씨 매도로 가격이 하락하는 상황입니다

        # TODO 0:00:56.538  ~  0:00:59.413

        # TODO 1.0secs pause

        # TODO 0:00:59.413  ~  0:01:00.413
        px_dn = MathTex(r'Price \  \Downarrow').move_to(liq_provider[ 0 ])
        self.play(Write(px_dn))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)
        self.play(Unwrite(px_dn), run_time=0.875)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)

        # K 하락#####################################################################################
        # TODO 2.851 secs유동성 제거로 케이가 하락하는 상황입니다

        # TODO 0:01:04.301  ~  0:01:07.152
        # TODO 1.0secs pause
        # TODO 0:01:07.152  ~  0:01:08.152
        k_dn = MathTex(r'K \  \Downarrow').move_to(liq_provider[ 0 ])
        self.play(Write(k_dn), run_time=1)

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 하락한다는 건 풀에서 누군가 유동성을 빼간 것입니다.
        # 명심할 것은 케이의 변동은 가격과 관계가 없음
        # 내가 유동성 풀에 제거하고 싶으면
        # 그냥 지금 가격에 맞게 빼가면 됨
        # 스왑처럼 내가 가격을 움직이며 하는 행위가 아님
        # 왜냐하면 가격이란 풀 내부의 비율인데
        # 지금 비율(1개에 300달러) 그대로 빼기 때문에
        # 가격은 움직이지 않고 그로인해 슬리피지등이 발생하지 않는다
        # 착각 금지

        self.wait(1)
        self.play(Unwrite(k_dn), run_time=0.851)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################

        # TODO 2.888 secs유동성 공급으로 케이가 상승하는 상황입니다
        # TODO 0:01:00.413  ~  0:01:03.301
        # TODO 1.0secs pause
        # TODO 0:01:03.301  ~  0:01:04.301

        k_up = MathTex(r'K \  \Uparrow').move_to(liq_provider[ 0 ])
        self.play(Write(k_up), run_time=1)

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(1)
        self.play(Unwrite(k_up), run_time=0.888)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # TODO 4.7 secs다시 한번 명심할 것은 유동성 공급, 제거는 가격과 관계가 없습니다
        # TODO 0:01:08.152  ~  0:01:12.852
        # TODO 1.0secs pause
        # TODO 0:01:12.852  ~  0:01:13.852
        # TODO 4.977 secs그냥 지금 가격에 맞게 풀 사이즈만 변화시키기에 가격을 움직이는 행위가 아닙니다
        # TODO 0:01:13.852  ~  0:01:18.829
        # TODO 1.0secs pause
        # TODO 0:01:18.829  ~  0:01:19.829
        # TODO 4.349 secs그러므로 거래자 활동과 달리 프라이스 임팩트와 관계가 전혀 없습니다
        # TODO 0:01:19.829  ~  0:01:24.178
        # TODO 1.0secs pause
        # TODO 0:01:24.178  ~  0:01:25.178
        # TODO 2.175 secs기본적인 상황들을 복습해봤습니다
        # TODO 0:01:25.178  ~  0:01:27.353
        # TODO 1.0secs pause
        # TODO 0:01:27.353  ~  0:01:28.353

        # K 원점#####################################################################################
        k_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin), run_time=1)

        self.wait(18.201)

        # TODO 3.697 secs케이상승 후 가격상승 또는 하락하는 경우를 보겠습니다
        # TODO 0:01:28.353  ~  0:01:32.050
        # TODO 1.0secs pause
        # TODO 0:01:32.050  ~  0:01:33.050

        # TODO 7.611 secs케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        # TODO 0:01:33.050  ~  0:01:40.661
        # TODO 1.0secs pause
        # TODO 0:01:40.661  ~  0:01:41.661

        self.wait(5)
        k_up_px_dn = MathTex(r'K \  \Uparrow', r'Price\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])
        k_up_px_up = MathTex(r'K \  \Uparrow', r'Price\  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        self.play(Write(k_up_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(5.308)

        # K 상승 가격 하락#####################################################################################

        # TODO 5.581 secs아까 300테더에서 3개를 매도할 때는 프라이스 임팩트가 23퍼센트 발생했지만
        # TODO 0:01:55.102  ~  0:02:00.683
        # TODO 1.0secs pause
        # TODO 0:02:00.683  ~  0:02:01.683

        # TODO 5.932 secs지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 19퍼센트만 발생했습니다
        # TODO 0:02:01.683  ~  0:02:07.615
        # TODO 1.0secs pause
        # TODO 0:02:07.615  ~  0:02:08.615
        share_change_1 = MathTex(r'30\% \\ $\Downarrow$ \\ 23\%', tex_environment='center')
        k_up_px_dn_text_1 = MathTex(r'23\% \\ $\downarrow$ \\ 19\%', tex_environment='center').arrange(D).next_to(k_up_px_dn, D)
        k_up_px_up_text_1 = MathTex(r'43\% \\ $\downarrow$ \\ 30\%', tex_environment='center').arrange(D).next_to(k_up_px_dn, D)

        self.play(Write(k_up_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_up_px_dn_text_1))
        self.wait(4)
        self.play(Uncreate(k_up_px_dn_text_1))

        self.play(Unwrite(k_up_px_dn[ 1 ]))

        self.wait(0.513)
        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(C0193).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # TODO 5.69 secs아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만
        # TODO 0:01:41.661  ~  0:01:47.351
        # TODO 1.0secs pause
        # TODO 0:01:47.351  ~  0:01:48.351

        # TODO 5.751 secs지금은 유동성으 풍부하고 3개 매수할 때  프라이스 임팩트가 30퍼센트 발생했습니다
        # TODO 0:01:48.351  ~  0:01:54.102
        # TODO 1.0secs pause
        # TODO 0:01:54.102  ~  0:01:55.102
        self.play(Write(k_up_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_up_px_up_text_1))
        self.wait(4)
        self.play(Uncreate(k_up_px_up_text_1))

        self.play(Unwrite(k_up_px_up[ 1 ]), Unwrite(k_up_px_dn[ 0 ]))
        self.wait(0.441)

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

        # TODO 3.636 secs같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        # TODO 0:02:08.615  ~  0:02:12.251
        # TODO 1.0secs pause
        # TODO 0:02:12.251  ~  0:02:13.251

        # TODO 6.113 secs아까는 10분에 3 지금은 13분에 3, 퍼센트로 따지면 33퍼와 23퍼센트입니다
        # TODO 0:02:13.251  ~  0:02:19.364
        # TODO 1.0secs pause
        # TODO 0:02:19.364  ~  0:02:20.364

        self.wait(2)

        self.play(Create(share_change_1))
        self.wait(5)
        self.play(Uncreate(share_change_1))

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(C1193).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.749)

        # TODO 3.66 secs케이하락 후 가격상승 또는 하락하는 경우를 보겠습니다
        # TODO 0:02:20.364  ~  0:02:24.024
        # TODO 1.0secs pause
        # TODO 0:02:24.024  ~  0:02:25.024

        # TODO 7.14 secs케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다
        # TODO 0:02:25.024  ~  0:02:32.164
        # TODO 1.0secs pause
        # TODO 0:02:32.164  ~  0:02:33.164

        k_dn_px_dn = MathTex(r'K\  \Downarrow', r'Price \  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])
        k_dn_px_up = MathTex(r'K\  \Downarrow', r'Price \  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])

        share_change_2 = MathTex(r'30\% \\ $\Downarrow$ \\ 42\%', tex_environment='center')

        k_dn_px_dn_text_1 = MathTex(r'23\% \\ $\downarrow$ \\ 30\%', tex_environment='center').arrange(D).next_to(k_dn_px_dn, D)
        k_dn_px_up_text_1 = MathTex(r'43\% \\ $\downarrow$ \\ 75\%', tex_environment='center').arrange(D).next_to(k_dn_px_dn, D)

        self.play(Write(k_dn_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        # 그말은 유동성이 줄었다는 거하고
        # 아까 유동성이 늘었서 슬리피지가 덜 발행하던 것과 달리
        # 지금부터는 슬리피지가 더 발생합니다
        #

        self.wait(9.8)
        # TODO 5.581 secs아까 300데터에서 3개를 매도할 때는 프라이스 임팩트가  23퍼센트 발생했지만
        # TODO 0:02:33.164  ~  0:02:38.745
        # TODO 1.0secs pause
        # TODO 0:02:38.745  ~  0:02:39.745

        # TODO 5.727 secs지금은 유동성으 적어졌고 3개 매도할 때 프라이스 임팩트가 30퍼센트 발생했습니다
        # TODO 0:02:39.745  ~  0:02:45.472
        # TODO 1.0secs pause
        # TODO 0:02:45.472  ~  0:02:46.472

        self.play(Write(k_dn_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_dn_px_dn_text_1))
        self.wait(4)
        self.play(Uncreate(k_dn_px_dn_text_1))

        self.play(Unwrite(k_dn_px_dn[ 1 ]), run_time=1)
        self.wait(1.308)

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        # TODO 5.69 secs아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만
        # TODO 0:02:46.472  ~  0:02:52.162
        # TODO 1.0secs pause
        # TODO 0:02:52.162  ~  0:02:53.162

        # TODO 5.932 secs지금은 유동성으 적어졌고 3개 매수할 때 프라이스 임팩트가 75퍼센트 발생했습니다
        # TODO 0:02:53.162  ~  0:02:59.094
        # TODO 1.0secs pause
        # TODO 0:02:59.094  ~  0:03:00.094
        self.play(Write(k_dn_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_dn_px_up_text_1))
        self.wait(4)
        self.play(Uncreate(k_dn_px_up_text_1))

        self.play(Unwrite(k_dn_px_up[ 1 ]),
                  Unwrite(k_dn_px_dn[ 0 ]))

        self.wait(0.417)

        # TODO 3.721 secs같은 3비티씨지만 풀에서 차지하는 비율이 커졌습니다
        # TODO 0:03:00.118  ~  0:03:03.839
        # TODO 1.0secs pause
        # TODO 0:03:03.839  ~  0:03:04.839

        # TODO 6.113 secs아까는 10분에 3 지금은 7 분에 3, 퍼센트로 따지면 33퍼와 42퍼센트입니다
        # TODO 0:03:04.839  ~  0:03:10.952
        # TODO 1.0secs pause
        # TODO 0:03:10.952  ~  0:03:11.952

        self.wait(2)
        self.play(Create(share_change_2))
        self.wait(5)
        self.play(Uncreate(share_change_2))

        # self.wait(2.834)
        # self.wait(2)

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)
        self.wait(0.334)

        # TODO 4.277 secs이번에는 가격이 먼저 상승하고 케이상승 또 하락하는 상황입니다
        # TODO 0:03:11.928  ~  0:03:16.205
        # TODO 1.0secs pause
        # TODO 0:03:16.205  ~  0:03:17.205

        # TODO 5.738 secs아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        # TODO 0:03:17.205  ~  0:03:22.943
        # TODO 1.0secs pause
        # TODO 0:03:22.943  ~  0:03:23.943

        px_up_k_up = MathTex(r'Price \  \Uparrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        px_up_k_dn = MathTex(r'Price \  \Uparrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])

        self.play(Write(px_up_k_up[ 0 ]), run_time=1)

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(9.06)
        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다

        # TODO 6.959 secs아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 올라버린 가격인 612 테더를 넣어줘야합니다
        # TODO 0:03:23.943  ~  0:03:30.902
        # TODO 1.0secs pause
        # TODO 0:03:30.902  ~  0:03:31.902
        # TODO 4.591 secs그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됐습니다
        # TODO 0:03:31.902  ~  0:03:36.493
        # TODO 1.0secs pause
        # TODO 0:03:36.493  ~  0:03:37.493

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

        self.wait(3)
        self.play(Unwrite(px_up_k_up[ 1 ]))
        self.wait(0.868)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################

        # TODO 9.737 secs만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 올라가있는 현재 가격대로 비티씨 한 개당 612테더를 돌려받게 됩니다
        # TODO 0:03:37.493  ~  0:03:47.230
        # TODO 1.0secs pause
        # TODO 0:03:47.230  ~  0:03:48.230

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

        self.wait(3)
        self.play(Unwrite(px_up_k_dn[ 1 ]),
                  Uncreate(px_up_k_up[ 0 ]))
        self.wait(0.737)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################

        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)
        # self.wait(2)

        # TODO 4.059 secs이번에는 가격이 먼저 하락하고 케이상승 및 하락하는 상황입니다
        # TODO 0:03:48.230  ~  0:03:52.289
        # TODO 1.0secs pause
        # TODO 0:03:52.289  ~  0:03:53.289

        # TODO 3.564 secs어번에도 현재가격에 맞게 같은 가치를 넣어줘야합니다
        # TODO 0:03:53.289  ~  0:03:56.853
        # TODO 1.0secs pause
        # TODO 0:03:56.853  ~  0:03:57.853

        px_dn_k_up = MathTex(r'Price \  \Downarrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])

        self.play(Write(px_dn_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        # self.wait(2)
        self.wait(6.623)

        # 가격 하락에서 K상승#####################################################################################

        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다

        # TODO 7.103 secs아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 내려버린 가격인 177 테더를 넣어줘야합니다

        # TODO 0:03:57.853  ~  0:04:04.956

        # TODO 1.0secs pause

        # TODO 0:04:04.956  ~  0:04:05.956

        # TODO 4.615 secs그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다

        # TODO 0:04:05.956  ~  0:04:10.571

        # TODO 1.0secs pause

        # TODO 0:04:10.571  ~  0:04:11.571
        self.play(Write(px_dn_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(3)
        self.play(Unwrite(px_dn_k_up[ 1 ]))
        self.wait(3.718)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # TODO 9.918 secs만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 내려가있는 현재 가격대로 비티씨 한 개당 177테더를 돌려받게 됩니다
        # TODO 0:04:11.571  ~  0:04:21.489
        # TODO 1.0secs pause
        # TODO 0:04:21.489  ~  0:04:22.489

        self.play(Write(px_dn_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 10),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        self.wait(3)
        self.play(Unwrite(px_dn_k_dn[ 1 ]),
                  Unwrite(px_dn_k_up[ 0 ]))
        self.wait(1)

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        # 가격 원점#####################################################################################
        px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(px_origin), run_time=0.5)

        # TODO 3.322 secs각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        # TODO 0:04:22.489  ~  0:04:25.811
        # TODO 1.0secs pause
        # TODO 0:04:25.811  ~  0:04:26.811
        # TODO 4.12 secs동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다
        # TODO 0:04:26.811  ~  0:04:30.931
        # TODO 1.0secs pause
        # TODO 0:04:30.931  ~  0:04:31.931

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


class working1(Scene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '아비트라지를 설명하고 마치겠습니다#1'
        '수익이라는 것은 기본적으로 시장의 비효율성이나 에러를 이용하는 것입니다#1'
        '그리고 시장이 많으면 많을수록 그런 기회가 많아지기에 덱스를 마다할 이유는 없습니다#1'
        '아비트라지란 한국어로 재정거래라고 불리고 두 개의 시장 사이이서 가격차가 발생하면 그 차익을 노리고 거래하는 것입니다#1'
        '싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다#1'
        '지금 덱스 에이에서 비트코인이 500테더, 덱스 비에서 470테더인 상황을 가정합니다#1'
        '덱스비에서 사서 바로 덱스 에이에 팔면 이득을 얻을 수 있습니다#1'

        '그러나 고려할 것들이 있습니다#1'
        '덱스 비에서 비트코인을 구매하면 수수료를 내고 비티씨 가격변동에 노출이 됩니다#1'
        '혹시나 다른 중앙화 거래소로 옮긴다면 비싼 전송수수료도 들 것이고, 블록체인 처리시간과 중앙화 거래소의 자체 서버 처리시간에 거래수수료도 지불합니다#1'
        '다른 덱스로 옮긴다면 전송수수료와 블록체인 상 처리시간 비싼 거래수수료도 지불합니다#1'
        '다른 블록체인으로 브릿지를 해도 비싼 브릿지 수수료가 들것이고 시간도 더 걸립니다#1'
        '각거래마다 슬리피지도 발생할 수도 있습니다#1'
        '성공할지 안 할지 보장도 없구요 이 모든 것을 계산하고도 남는 장사라고 생각하면 아비트라지를 하는 것입니다#1'
        '보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고, 얼핏보면 하는 거 없이 돈 버는 것 같지만 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서 보통 컴퓨터로 봇을 만들어 돌리게 됩니다#1'

        '아비트라지가 중요한 이유는 코인 가격을 맞춰주고 안정화 하기 때문입니다#1'
        '여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다#1'
        '수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.#1'
        '마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 만든다는 상상을 할 수도 있습니다#1'
        '내가 비트코인이 비싸지길 바라면서 10비트와 5000테더를 넣으면 그 순간 1비트의 가격은 500테더입니다#1'
        '곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.덱스도 중앙화거래소에 영향을 주고 중앙화 거래소도 덱스에 영향을 줍니다#1'
        '모든 거래소가 아비트라지 봇으로 묶여있어 서로가 서로에게 영향을 줍니다#1'
        '아비트라지도 금융 생태계를 이루는 중요한 요소 중 하나이므로 잘 이해하고 있어야합니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        # TODO 3.165 secs다음으로 넘어가기 전에 수수료예 대해 알아보겠습니다
        # TODO 0:00:00.000  ~  0:00:03.165
        # TODO 1.0secs pause
        # TODO 0:00:03.165  ~  0:00:04.165
        inefficiency_profit = MathTex(r'Inefficiency \  \Rightarrow\  Profit')

        ##### 아비트라지를 설명하고 마치겠습니다
        # 아비트라지 제목

        # TODO 2.151 secs아비트라지를 설명하고 마치겠습니다
        # TODO 0:00:00.000  ~  0:00:02.151
        # TODO 1.0secs pause
        # TODO 0:00:02.151  ~  0:00:03.151

        arb = Tex('Arbitrage').scale(2)
        self.play(Create(arb))
        self.wait(1)

        self.play(Uncreate(arb), run_time=1.151)

        dex_1_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_1_text = Tex('DEX A').next_to(dex_1_rect, UP)
        dex_1 = VGroup(dex_1_rect, dex_1_text).to_edge(L)

        dex_2_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_2_text = Tex('DEX B').next_to(dex_2_rect, UP)
        dex_2 = VGroup(dex_2_rect, dex_2_text).to_edge(R)

        dex_1_px = Variable(500, 'BTC', var_type=Integer)
        dex_1_px_tracker = dex_1_px.tracker
        dex_1_px_unit = Tex(r'USDT').next_to(dex_1_px, R)
        dex_1_px.add(dex_1_px_unit).scale(0.65).move_to(dex_1_rect)

        dex_2_px = Variable(470, 'BTC', var_type=Integer)
        dex_2_px_tracker = dex_2_px.tracker
        dex_2_px_unit = Tex(r'USDT').next_to(dex_2_px, R, buff=0.1)
        dex_2_px.add(dex_2_px_unit).scale(0.65).move_to(dex_2_rect)
        # TODO 4.687 secs수익이라는 것은 기본적으로 시장의 비효율성이나 에러를 이용하는 것입니다
        # TODO 0:00:03.151  ~  0:00:07.838
        # TODO 1.0secs pause
        # TODO 0:00:07.838  ~  0:00:08.838

        profit = Tex('Profit').scale(2.5)
        inefficiency = Tex('Inefficiency').scale(2.5)
        inefficiency_1 = inefficiency.copy().scale(0.8).to_edge(UL, buff=1)
        inefficiency_2 = inefficiency.copy().scale(0.7).to_edge(DL, buff=1)
        inefficiency_3 = inefficiency.copy().scale(0.6).to_edge(UR, buff=1)
        inefficiency_4 = inefficiency.copy().scale(0.5).to_edge(DR, buff=1)
        profit_1 = profit.copy().scale(0.8).move_to(inefficiency_1)
        profit_2 = profit.copy().scale(0.7).move_to(inefficiency_2)
        profit_3 = profit.copy().scale(0.6).move_to(inefficiency_3)
        profit_4 = profit.copy().scale(0.5).move_to(inefficiency_4)

        self.play(Create(inefficiency))

        self.play(Transform(inefficiency, profit))
        self.wait(3.687)

        # TODO 5.001 secs그리고 시장이 많으면 많을수록 그런 기회가 많아지기에 덱스를 마다할 이유는 없습니다
        # TODO 0:00:08.838  ~  0:00:13.839
        # TODO 1.0secs pause
        # TODO 0:00:13.839  ~  0:00:14.839

        self.play(Create(inefficiency_1), run_time=0.5)
        self.play(Transform(inefficiency_1, profit_1), run_time=0.5)
        self.play(Create(inefficiency_2), run_time=0.5)
        self.play(Transform(inefficiency_2, profit_2), run_time=0.5)
        self.play(Create(inefficiency_3), run_time=0.5)
        self.play(Transform(inefficiency_3, profit_3), run_time=0.5)
        self.play(Create(inefficiency_4), run_time=0.5)
        self.play(Transform(inefficiency_4, profit_4), run_time=0.5)

        self.play(Uncreate(VGroup(inefficiency, inefficiency_1, inefficiency_2, inefficiency_3, inefficiency_4), run_time=2.001))

        # TODO 5.28 secs아비트라지란 한국어로 재정거래라고 불리고 두 개의 시장 사이이서 가격차가 발쌩하면
        # TODO 0:00:14.839  ~  0:00:20.119
        # TODO 1.0secs pause
        # TODO 0:00:20.119  ~  0:00:21.119
        # TODO 2.308 secs그 차익을 노리고 거래하는 것입니다
        # TODO 0:00:21.119  ~  0:00:23.427
        # TODO 1.0secs pause
        # TODO 0:00:23.427  ~  0:00:24.427
        # TODO 3.564 secs싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다
        # TODO 0:00:24.427  ~  0:00:27.991
        # TODO 1.0secs pause
        # TODO 0:00:27.991  ~  0:00:28.991

        arbitrage_text = Tex('Arbitrage').scale(2)
        arbitrage_text_kor = Tex('재정거래').scale(2)
        boddari = Tex('보따리장사').scale(2)

        self.play(Create(arbitrage_text))
        self.wait(0.5)
        self.play(ReplacementTransform(arbitrage_text, arbitrage_text_kor))
        self.wait(5.5)
        self.play(ReplacementTransform(arbitrage_text_kor, boddari))
        self.wait(5.152)

        # TODO 6.222 secs지금 덱스 에이에서 비트코인이 500테더, 덱스 비에서 470테더인 상황을 가정합니다
        # TODO 0:00:28.991  ~  0:00:35.213
        # TODO 1.0secs pause
        # TODO 0:00:35.213  ~  0:00:36.213
        # TODO 3.939 secs덱스비에서 사서 바로 덱스 에이에 팔면 이득을 얻을 수 있습니다
        # TODO 0:00:36.213  ~  0:00:40.152
        # TODO 1.0secs pause
        # TODO 0:00:40.152  ~  0:00:41.152
        # TODO 1.861 secs그러나 고려할 것들이 있습니다
        # TODO 0:00:41.152  ~  0:00:43.013
        # TODO 1.0secs pause
        # TODO 0:00:43.013  ~  0:00:44.013

        self.play(Create(dex_1),
                  Create(dex_2), run_time=1)
        self.wait(1)
        self.play(Create(dex_1_px),
                  Create(dex_2_px), run_time=1)
        self.wait(4)
        self.play(Uncreate(boddari), run_time=1)
        self.wait(4.022)

        blist = BulletedList("Exposure to BTC fluctuation",
                             "Fees, time from DEX B",
                             r"In case of CEX, time, \\trade fees and high tx fees",
                             r"In case of DEX, time, \\high trade fees and tx fees",
                             r"In case of another blockchain,\\time and bridging fees",
                             "Slippage risk from every trade", height=7, width=7)

        # TODO 5.315 secs덱스 비에서 비트코인을 구매하면 수수료를 내고 비티씨 가격변동에 노출이 됩니다

        # TODO 0:00:44.013  ~  0:00:49.328

        # TODO 1.0secs pause

        # TODO 0:00:49.328  ~  0:00:50.328

        self.play(Create(blist[ 0 ]), run_time=1)
        self.wait(2)

        self.play(Create(blist[ 1 ]), run_time=1)
        self.wait(2.315)

        # TODO 9.809 secs혹시나 다른 중앙화 거래소로 옮긴다면 비싼 전송수수료도 들 것이고, 블록체인 처리시간과 중앙화 거래소의 자체 서버 처리시간에 거래수수료도 지불합니다

        # TODO 0:00:50.328  ~  0:01:00.137

        # TODO 1.0secs pause

        # TODO 0:01:00.137  ~  0:01:01.137

        self.play(Create(blist[ 2 ]), run_time=1)
        self.wait(9.809)

        # TODO 5.618 secs다른 덱스로 옮긴다면 전송수수료와 블록체인 상 처리시간 비싼 거래수수료도 지불합니다

        # TODO 0:01:01.137  ~  0:01:06.755

        # TODO 1.0secs pause

        # TODO 0:01:06.755  ~  0:01:07.755

        self.play(Create(blist[ 3 ]), run_time=1)
        self.wait(5.618)

        # TODO 5.424 secs다른 블록체인으로 브릿지를 해도 비싼 브릿지 수수료가 들것이고 시간도 더 걸립니다

        # TODO 0:01:07.755  ~  0:01:13.179

        # TODO 1.0secs pause

        # TODO 0:01:13.179  ~  0:01:14.179

        self.play(Create(blist[ 4 ]), run_time=1)
        self.wait(5.424)
        # TODO 2.888 secs각거래마다 슬리피지도 발생할 수도 있습니다

        # TODO 0:01:14.179  ~  0:01:17.067

        # TODO 1.0secs pause

        # TODO 0:01:17.067  ~  0:01:18.067

        self.play(Create(blist[ 5 ]), run_time=1)
        self.wait(2.888)

        ##### 지금 덱스 에이에서 비트코인이 500달러 덱스 비에서 470달러면
        ##### 덱스 비에서 비트코인을 구매하고 비트코인 가격변동에 대한 노출
        ##### 덱스 비에서 구매하는 거래수수료
        ##### 혹시나 다른 중앙화 거래소로 옮긴다면 전송수수료도 들고 시간 소요
        ##### 다른 블록체인으로 브릿지를 해도 브릿지 비용이 들것이고 시간 소요
        ##### 거래소 에이에서 비로 도착해서 다시 팔때도 거래 수수료가 발생합니다
        ##### 각거래마다 슬리피지
        ##### 그리고 성공할지 안 할지 보장도 없구요
        ##### 그런데도 가격이 매력적이라면 아비트라지를 하는 것입니다
        # 다 지우고
        # 스틸 낫 슈어 텍스트 좀 더 크게 제일 밑에
        # TODO 6.512 secs성공할지 안 할지 보장도 없구요 이 모든 것을 계산하고도 남는 장사라고 생각하면 아비트라지를 하는 것입니다

        # TODO 0:01:18.067  ~  0:01:24.579

        # TODO 1.0secs pause

        # TODO 0:01:24.579  ~  0:01:25.579

        still_not_sure = Tex('Still not sure...').scale(1.5)

        self.play(ReplacementTransform(blist, still_not_sure), run_time=1)
        self.wait(3)

        self.play(Uncreate(still_not_sure), run_time=1)
        self.wait(2.512)

        ##### 싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다.
        ##### 얼핏보면 하는 거 없이 돈 버는 것 같지만
        ##### 보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고
        ##### 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서
        ##### 보통 컴퓨터로 봇을 만ㄷ르어 돌리게 됩니다.
        # 불릿 더 라저 더 베터
        # 왓치 24 앤 패스트 핸드
        # 보통 컴퓨터 프로그램 오토메이티드
        # TODO 14.449 secs보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고, 얼핏보면 하는 거 없이 돈 버는 것 같지만 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서 보통 컴퓨터로 봇을 만들어 돌리게 됩니다

        # TODO 0:01:25.579  ~  0:01:40.028

        # TODO 1.0secs pause

        # TODO 0:01:40.028  ~  0:01:41.028
        blist_2 = BulletedList("The Larger, The Better",
                               "Watch 24/7, Act Fast",
                               r"Normally automated\\with programming", height=7, width=7)

        self.wait(1)
        self.play(Create(blist_2[ 0 ]), run_time=1)
        self.wait(7)
        self.play(Create(blist_2[ 1 ]), run_time=1)
        self.wait(3)
        self.play(Create(blist_2[ 2 ]), run_time=1)
        self.wait(1.449)

        ##### 그리고 결정적으로 아비트라지는 가격 안정에 매우 중요한 역할을 합니다
        ##### 여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면
        ##### 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다
        # 가격 전부 다르게 해놓고 똑같이 맞춰짐
        # 3번정도 반복
        # TODO 4.349 secs아비트라지가 중요한 이유는 코인 가격을 맞춰주고 안정화 하기 때문입니다

        # TODO 0:01:41.028  ~  0:01:45.377

        # TODO 1.0secs pause

        # TODO 0:01:45.377  ~  0:01:46.377

        # TODO 12.105 secs여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다

        # TODO 0:01:46.377  ~  0:01:58.482

        # TODO 1.0secs pause

        # TODO 0:01:58.482  ~  0:01:59.482

        # TODO 9.218 secs수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.

        # TODO 0:01:59.482  ~  0:02:08.700

        # TODO 1.0secs pause

        # TODO 0:02:08.700  ~  0:02:09.700

        dex_3_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_3_text = Tex('DEX C').next_to(dex_3_rect, UP)
        dex_3 = VGroup(dex_3_rect, dex_3_text)

        dex_3_px = Variable(500, 'BTC', var_type=Integer)
        dex_3_px_tracker = dex_3_px.tracker
        dex_3_px_unit = Tex(r'USDT').next_to(dex_3_px, R)
        dex_3_px.add(dex_3_px_unit).scale(0.65).move_to(dex_3_rect)

        self.play(ReplacementTransform(blist_2, dex_3),
                  Create(dex_3_px), run_time=2)
        self.wait(2)

        ##### 수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고
        ##### 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.
        self.play(dex_1_px_tracker.animate.set_value(510),
                  dex_2_px_tracker.animate.set_value(550),
                  dex_3_px_tracker.animate.set_value(540), run_time=2)
        self.wait(2)
        self.play(dex_1_px_tracker.animate.set_value(530),
                  dex_2_px_tracker.animate.set_value(530),
                  dex_3_px_tracker.animate.set_value(530), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(420),
                  dex_2_px_tracker.animate.set_value(480),
                  dex_3_px_tracker.animate.set_value(450), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(455),
                  dex_2_px_tracker.animate.set_value(455),
                  dex_3_px_tracker.animate.set_value(455), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(755),
                  dex_2_px_tracker.animate.set_value(741),
                  dex_3_px_tracker.animate.set_value(787), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(751),
                  dex_2_px_tracker.animate.set_value(751),
                  dex_3_px_tracker.animate.set_value(751), run_time=2)
        self.wait(2)

        ##### 마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 공급해도
        ##### 곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.
        # 다 없애고 덱스에 최초로 코인 상장해서 비트를 올릴 때 올라가는데 내가 뉴코인 10개와 5000달러를 넣어 개당 500달러로 만들어놓으면
        # 전부 없어짐 아비트라지로 민주화 당함

        self.play(Uncreate(VGroup(dex_1, dex_1_px, dex_2, dex_2_px, dex_3, dex_3_px)), run_time=0.672)
        self.wait(t)
        # TODO 6.27 secs마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 만든다는 상상을 할 수도 있습니다

        # TODO 0:02:09.700  ~  0:02:15.970

        # TODO 1.0secs pause

        # TODO 0:02:15.970  ~  0:02:16.970
        # TODO 6.693 secs내가 비트코인이 비싸지길 바라면서 10비트와 5000테더를 넣으면 그 순간 1비트의 가격은 500테더입니다

        # TODO 0:02:16.970  ~  0:02:23.663

        # TODO 1.0secs pause

        # TODO 0:02:23.663  ~  0:02:24.663

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        pool_btc_px = Variable(500, 'BTC', var_type=Integer)
        px_unit = Tex(r'USDT').next_to(pool_btc_px, R)
        pool_btc_px.add(px_unit).scale(1.5).next_to(pool_rect, D)

        self.play(Create(pool_rect_text),
                  Create(pool_rect), run_time=3)
        self.wait(1)

        usdt_lump_tracker = ValueTracker(5000)
        btc_lump_tracker = ValueTracker(10)

        btc_lump = create_circle_asset(Tex(rf'\textbf{{{int(btc_lump_tracker.get_value())}}} \\ \textbf{{BTC}}', color=WHITE, font_size=25),
                                       fill_color=C_BTC).scale_to_fit_height(2).shift(L * 1.5)
        usdt_lump = create_circle_asset(
            Tex(rf'\textbf{{{int(usdt_lump_tracker.get_value())}}} \\ \textbf{{USDT}}', color=WHITE, font_size=25),
            fill_color=C_USDT).scale_to_fit_height(2).shift(R * 1.5)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3, asset_text_color=WHITE).shift(R * 5)
        btc_asset_liq_prov = liq_provider[ 1 ]
        usdt_asset_liq_prov = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(
            liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset_liq_prov)
        arbitrager = create_entity(Tex(r' \emph{Arbitrager}', color=BLACK).scale(0.7), 1, WHITE, "2.9 BTC", ORANGE, 1.4,
                                   0.3, asset_text_color=WHITE).shift(L * 5)
        btc_asset_arbitrager = arbitrager[ 1 ]
        usdt_asset_arbitrager = create_entity("A", 0.5, WHITE, "1127 USDT", GREEN, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].move_to(
            btc_asset_arbitrager)

        self.play(FadeIn(liq_provider, target_position=R * 10), run_time=2)
        self.wait(1.27)

        self.play(ReplacementTransform(liq_provider[ 1 ], btc_lump),
                  ReplacementTransform(liq_provider[ 2 ], usdt_lump), run_time=3)
        self.wait(2)

        self.play(Create(pool_btc_px), run_time=1)
        self.wait(0.693)
        # TODO 8.13 secs곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.덱스도 중앙화거래소에 영향을 주고 중앙화 거래소도 덱스에 영향을 줍니다

        # TODO 0:02:24.663  ~  0:02:32.793

        # TODO 1.0secs pause

        # TODO 0:02:32.793  ~  0:02:33.793

        self.play(FadeIn(arbitrager, target_position=L * 10), run_time=1)
        self.wait(1)

        btc_lump.add_updater(lambda x: x.become(
            create_circle_asset(Tex(rf'\textbf{{{round(btc_lump_tracker.get_value(), 1)}}} \\ \textbf{{BTC}}', color=WHITE, font_size=25),
                                fill_color=C_BTC).scale_to_fit_height(2).shift(L * 1.5)))
        usdt_lump.add_updater(lambda x: x.become(
            create_circle_asset(Tex(rf'\textbf{{{int(usdt_lump_tracker.get_value())}}} \\ \textbf{{USDT}}', color=WHITE, font_size=25),
                                fill_color=C_USDT).scale_to_fit_height(2).shift(R * 1.5)))
        self.play(pool_btc_px.tracker.animate.set_value(300),
                  usdt_lump_tracker.animate.set_value(3873),
                  btc_lump_tracker.animate.set_value(12.9),
                  FadeOut(btc_asset_arbitrager, target_position=btc_lump),
                  FadeIn(usdt_asset_arbitrager, target_position=usdt_lump), run_time=5)
        self.wait(1.13)

        btc_lump.clear_updaters()
        usdt_lump.clear_updaters()
        self.play(FadeOut(VGroup(
            pool_btc_px, pool_rect, pool_rect_text, btc_lump, usdt_lump, arbitrager, usdt_asset_arbitrager, liq_provider[ 0 ])), run_time=1)

        # TODO 4.615 secs모든 거래소가 아비트라지 봇으로 묶여있어 서로가 서로에게 영향을 줍니다

        # TODO 0:02:33.793  ~  0:02:38.408

        # TODO 1.0secs pause

        # TODO 0:02:38.408  ~  0:02:39.408

        # TODO 5.134 secs아비트라지도 금융 생태계를 이루는 중요한 요소 중 하나이므로 잘 이해하고 있어야합니다

        # TODO 0:02:39.408  ~  0:02:44.542

        # TODO 1.0secs pause

        # TODO 0:02:44.542  ~  0:02:45.542

        arbigrager_circle = LabeledDot(Tex(rf'Arbitrager', color=BLACK, font_size=30), radius=1, color=ORANGE).set_z_index(1)

        dex_1 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=RED).set_z_index(1)
        dex_2 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=GREEN).set_z_index(0.5)
        dex_3 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=BLUE).set_z_index(1)
        dex_4 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=TEAL).set_z_index(1)
        dex_5 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=YELLOW).set_z_index(1)
        dex_6 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=MAROON).set_z_index(1)
        dex_7 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=PURPLE).set_z_index(1)
        cex_1 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=RED).set_z_index(1)
        cex_2 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=GREEN).set_z_index(1)
        cex_3 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=BLUE).set_z_index(1)
        cex_4 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=TEAL).set_z_index(1)
        cex_5 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=YELLOW).set_z_index(1)
        cex_6 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=MAROON).set_z_index(1)
        cex_7 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=PURPLE).set_z_index(1)

        dex_line_1 = Line(dex_1.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_2 = Line(dex_2.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_3 = Line(dex_3.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_4 = Line(dex_4.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_5 = Line(dex_5.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_6 = Line(dex_6.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_7 = Line(dex_7.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_1 = Line(cex_1.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_2 = Line(cex_2.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_3 = Line(cex_3.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_4 = Line(cex_4.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_5 = Line(cex_5.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_6 = Line(cex_6.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_7 = Line(cex_7.get_center(), arbigrager_circle.get_center(), color=WHITE)

        ex_group = VGroup(dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7, cex_1, cex_2, cex_3, cex_4, cex_5, cex_6, cex_7)
        line_group = VGroup(dex_line_1, dex_line_2, dex_line_3, dex_line_4, dex_line_5, dex_line_6, dex_line_7, cex_line_1, cex_line_2,
                            cex_line_3, cex_line_4, cex_line_5, cex_line_6, cex_line_7)
        ex_list = [ dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7, cex_1, cex_2, cex_3, cex_4, cex_5, cex_6, cex_7 ]

        rotation_val_tracker = ValueTracker(1)

        dist_dict = {0: 3.66, 1: 3.2, 2: 3.21, 3: 3.12, 4: 3.42, 5: 3.37, 6: 3.34, 7: 3.04, 8: 3.24, 9: 3.43, 10: 3.4, 11: 3.26, 12: 3.1,
                     13: 3.24}
        dist_dict = {0: 3.76, 1: 2.6, 2: 3.24, 3: 3.29, 4: 3.46, 5: 2.83, 6: 2.74, 7: 2.82, 8: 2.63, 9: 2.85, 10: 2.85, 11: 3.47, 12: 3.38,
                     13: 3.07}
        dist_dict = {0: 2.8, 1: 3.6, 2: 2.99, 3: 3.71, 4: 2.83, 5: 3.89, 6: 2.82, 7: 3.82, 8: 2.8, 9: 3.8, 10: 2.8, 11: 3.6, 12: 3.54,
                     13: 3.7}

        # dist_dict = {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 3,
        #              13: 3}
        dir_dict = {0: 0.4488, 1: 0.8976, 2: 1.3464, 3: 1.7952, 4: 2.24399, 5: 2.69279, 6: 3.14159, 7: 3.59039, 8: 4.03919, 9: 4.48799,
                    10: 4.93679, 11: 5.38559, 12: 5.83439, 13: 6.28319}

        ex_group[ 0 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * dist_dict[ 0 ],
              sin(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * dist_dict[ 0 ], 0 ])))
        ex_group[ 1 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * dist_dict[ 1 ],
              sin(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * dist_dict[ 1 ], 0 ])))
        ex_group[ 2 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * dist_dict[ 2 ],
              sin(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * dist_dict[ 2 ], 0 ])))
        ex_group[ 3 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * dist_dict[ 3 ],
              sin(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * dist_dict[ 3 ], 0 ])))
        ex_group[ 4 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * dist_dict[ 4 ],
              sin(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * dist_dict[ 4 ], 0 ])))
        ex_group[ 5 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * dist_dict[ 5 ],
              sin(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * dist_dict[ 5 ], 0 ])))
        ex_group[ 6 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * dist_dict[ 6 ],
              sin(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * dist_dict[ 6 ], 0 ])))
        ex_group[ 7 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 7 ] + rotation_val_tracker.get_value()) * dist_dict[ 7 ],
              sin(dir_dict[ 7 ] + rotation_val_tracker.get_value()) * dist_dict[ 7 ], 0 ])))
        ex_group[ 8 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 8 ] + rotation_val_tracker.get_value()) * dist_dict[ 8 ],
              sin(dir_dict[ 8 ] + rotation_val_tracker.get_value()) * dist_dict[ 8 ], 0 ])))
        ex_group[ 9 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 9 ] + rotation_val_tracker.get_value()) * dist_dict[ 9 ],
              sin(dir_dict[ 9 ] + rotation_val_tracker.get_value()) * dist_dict[ 9 ], 0 ])))
        ex_group[ 10 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 10 ] + rotation_val_tracker.get_value()) * dist_dict[ 10 ],
              sin(dir_dict[ 10 ] + rotation_val_tracker.get_value()) * dist_dict[ 10 ], 0 ])))
        ex_group[ 11 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 11 ] + rotation_val_tracker.get_value()) * dist_dict[ 11 ],
              sin(dir_dict[ 11 ] + rotation_val_tracker.get_value()) * dist_dict[ 11 ], 0 ])))
        ex_group[ 12 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 12 ] + rotation_val_tracker.get_value()) * dist_dict[ 12 ],
              sin(dir_dict[ 12 ] + rotation_val_tracker.get_value()) * dist_dict[ 12 ], 0 ])))
        ex_group[ 13 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 13 ] + rotation_val_tracker.get_value()) * dist_dict[ 13 ],
              sin(dir_dict[ 13 ] + rotation_val_tracker.get_value()) * dist_dict[ 13 ], 0 ])))

        dex_line_1.add_updater(lambda x: x.become(Line(dex_1.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_2.add_updater(lambda x: x.become(Line(dex_2.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_3.add_updater(lambda x: x.become(Line(dex_3.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_4.add_updater(lambda x: x.become(Line(dex_4.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_5.add_updater(lambda x: x.become(Line(dex_5.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_6.add_updater(lambda x: x.become(Line(dex_6.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_7.add_updater(lambda x: x.become(Line(dex_7.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_1.add_updater(lambda x: x.become(Line(cex_1.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_2.add_updater(lambda x: x.become(Line(cex_2.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_3.add_updater(lambda x: x.become(Line(cex_3.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_4.add_updater(lambda x: x.become(Line(cex_4.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_5.add_updater(lambda x: x.become(Line(cex_5.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_6.add_updater(lambda x: x.become(Line(cex_6.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_7.add_updater(lambda x: x.become(Line(cex_7.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))

        self.play(Create(ex_group), run_time=0.5)

        self.play(Create(arbigrager_circle), run_time=0.5)

        self.play(Create(line_group), run_time=0.5)

        self.play(rotation_val_tracker.animate.set_value(3), run_time=2, rate_functions=exponential_decay)
        self.wait(0.5)

        cex_line_5.set_color(RED_E)
        self.wait(0.25)
        cex_line_2.set_color(RED_E)
        self.wait(0.25)
        cex_line_5.set_color(WHITE)
        cex_line_2.set_color(WHITE)
        self.wait(0.25)

        dex_line_5.set_color(RED_E)
        self.wait(0.25)
        cex_line_3.set_color(RED_E)
        self.wait(0.25)
        dex_line_5.set_color(WHITE)
        cex_line_3.set_color(WHITE)
        self.wait(0.25)

        dex_line_1.set_color(RED_E)
        self.wait(0.25)
        cex_line_1.set_color(RED_E)
        self.wait(0.25)
        dex_line_1.set_color(WHITE)
        cex_line_1.set_color(WHITE)
        self.wait(0.25)

        dex_line_2.set_color(RED_E)
        self.wait(0.25)
        cex_line_7.set_color(RED_E)
        self.wait(0.25)
        dex_line_2.set_color(WHITE)
        cex_line_7.set_color(WHITE)
        self.wait(0.25)

        dex_line_3.set_color(RED_E)
        self.wait(0.25)
        dex_line_4.set_color(RED_E)
        self.wait(0.25)
        dex_line_3.set_color(WHITE)
        dex_line_4.set_color(WHITE)
        self.wait(0.25)
        self.wait(5)


class working3(Scene):

    def construct(self):
        self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '아비트라지를 설명하고 마치겠습니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        a = 555

        circle_1 = Circle().shift(L * 4 + U * 2)
        circle_2 = Circle().shift(R * 4 + D * 2)
        self.play(Create(circle_1),
                  Create(circle_2))

        dot = Dot().move_to(get_halfway(circle_1.get_right(), circle_2.get_left()))

        self.play(Create(dot))
        self.wait(5)


class working(Scene):
    def construct(self):
        p1 = np.array([ -4, -2, 0 ])
        p2 = np.array([ 4, -2, 0 ])
        p3 = [ 1, 1, 0 ]
        p4 = [ -1, 1, 0 ]
        # a = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        a = Line(start=p1, end=p2, buff=0.1)
        # point_start= a.get_start()
        # point_end  = a.get_end()
        # point_center = a.get_center()

        # self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        # self.add(Dot(a.get_end()).set_color(RED).scale(2))
        # self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        # self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        # self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        # self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[ Dot(x) for x in a.points ])
        self.add(a)


class working1(MovingCameraScene):
    def construct(self):
        self.add(NumberPlane().set_z_inex(1))

        speak(self, title='Scene2', txt=
        '#9'
        '#9'
        '#9'
        '#9'
        '#1'
        '잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다#1'
        '케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게, 가격이 내려가는 것은 빨간색 올라가는 것은 초록색으로 표시했습니다. 원점은 회색입니다#1'

        '비티씨 매수로 가격이 상승하는 상황입니다#1'
        '비티씨 매도로 가격이 하락하는 상황입니다#3'
        '유동성 공급으로 케이가 상승하는 상황입니다#1'
        '유동성 제거로 케이가 하락하는 상황입니다#1'
        '다시 한번 명심할 것은 유동성 공급, 제거는 가격과 관계가 없습니다#1'
        '그냥 지금 가격에 맞게 풀 사이즈만 변화시키기에 가격을 움직이는 행위가 아닙니다#1'
        '그러므로 거래자 활동과 달리 프라이스 임팩트와 관계가 전혀 없습니다#1'

        '기본적인 상황들을 복습해봤습니다#1'

        '케이상승 후 가격상승 또는 하락하는 경우를 보겠습니다#1'
        '케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다#1'
        '아까 300테더에서 3개를 매도할 때는 프라이스 임팩트가 23퍼센트 발생했지만#1'
        '지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 19퍼센트만 발생했습니다#1'
        '아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만#1'
        '지금은 유동성이 풍부하고 3개 매수할 때  프라이스 임팩트가 30퍼센트 발생했습니다#1'
        '같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다#1'
        '아까는 10분에 3 지금은 13분에 3, 퍼센트로 따지면 33퍼와 23퍼센트입니다#1'

        '케이하락 후 가격상승 또는 하락하는 경우를 보겠습니다#1'
        '케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다#1'
        '아까 300데터에서 3개를 매도할 때는 프라이스 임팩트가  23퍼센트 발생했지만 #1'
        '지금은 유동성으 적어졌고 3개 매도할 때 프라이스 임팩트가 30퍼센트 발생했습니다#1'
        '아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만#1'
        '지금은 유동성으 적어졌고 3개 매수할 때 프라이스 임팩트가 75퍼센트 발생했습니다#1'
        '같은 3비티씨지만 풀에서 차지하는 비율이 커졌습니다#1'
        '아까는 10분에 3 지금은 7 분에 3, 퍼센트로 따지면 33퍼와 42퍼센트입니다#1'

        '이번에는 가격이 먼저 상승하고 케이상승 또는 하락하는 상황입니다#1'
        '아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다#1'
        '아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 올라버린 가격인 612 테더를 넣어줘야합니다#1'
        '그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됐습니다#1'
        '만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 올라가있는 현재 가격대로 비티씨 한 개당 612테더를 돌려받게 됩니다#3'

        '이번에는 가격이 먼저 하락하고 케이상승 및 하락하는 상황입니다#1'
        '어번에도 현재가격에 맞게 같은 가치를 넣어줘야합니다#1'
        '아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 내려버린 가격인 177 테더를 넣어줘야합니다#1'
        '그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다#1'
        '만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 내려가있는 현재 가격대로 비티씨 한 개당 177테더를 돌려받게 됩니다#3'

        '각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다#1'
        '동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3, asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN,
                                                                                                                        buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Create(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.play(Uncreate(liq_provider), run_time=0.5)
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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)

        # E##############################################

        # TODO 3.479 secs잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다
        # TODO 0:00:37.000  ~  0:00:40.479
        # TODO 1.0secs pause
        # TODO 0:00:40.479  ~  0:00:41.479

        # TODO 10.16 secs케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게, 가격이 내려가는 것은 빨간색 올라가는 것은
        #  초록색으로 표시했습니다. 원점은 회색입니다
        # TODO 0:00:41.479  ~  0:00:51.639
        # TODO 1.0secs pause
        # TODO 0:00:51.639  ~  0:00:52.639

        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))
        self.wait(14.639)

        # 가격 상승#####################################################################################
        # TODO 2.899 secs비티씨 매수로 가격이 상승하는 상황입니다
        # TODO 0:00:52.639  ~  0:00:55.538
        # TODO 1.0secs pause
        # TODO 0:00:55.538  ~  0:00:56.538

        def get_halfway(point_A, point_B, z=0):
            x_dist = (abs(point_A[ 0 ]) + abs(point_B[ 0 ])) / 2
            y_dist = (abs(point_A[ 1 ]) + abs(point_B[ 1 ])) / 2

            if point_A[ 0 ] < point_B[ 0 ]:
                x = point_A[ 0 ] + x_dist
            else:
                x = point_A[ 0 ] + x_dist

            if point_A[ 1 ] < point_B[ 1 ]:
                y = point_A[ 1 ] + y_dist
            else:
                y = point_A[ 1 ] + y_dist

            return np.array([ x, y, z ])

        position = get_halfway(np.array([ liq_pool_rect.get_right()[ 0 ], liq_pool_rect.get_right()[ 1 ], 0 ]),
                               np.array([ ax.get_left()[ 0 ], liq_pool_rect.get_right()[ 1 ], 0 ]))
        position[ 1 ] = position[ 1 ] + 1
        px_up = MathTex(r'Price \  \Uparrow').move_to(position)
        self.play(Write(px_up))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)
        self.play(Unwrite(px_up), run_time=0.899)
        # self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################

        # TODO 2.875 secs비티씨 매도로 가격이 하락하는 상황입니다

        # TODO 0:00:56.538  ~  0:00:59.413

        # TODO 1.0secs pause

        # TODO 0:00:59.413  ~  0:01:00.413
        px_dn = MathTex(r'Price \  \Downarrow').move_to(position)
        self.play(Write(px_dn))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)
        self.play(Unwrite(px_dn), run_time=0.875)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)

        # K 하락#####################################################################################
        # TODO 2.851 secs유동성 제거로 케이가 하락하는 상황입니다

        # TODO 0:01:04.301  ~  0:01:07.152
        # TODO 1.0secs pause
        # TODO 0:01:07.152  ~  0:01:08.152
        k_dn = MathTex(r'K \  \Downarrow').move_to(position)
        self.play(Write(k_dn), run_time=1)

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 하락한다는 건 풀에서 누군가 유동성을 빼간 것입니다.
        # 명심할 것은 케이의 변동은 가격과 관계가 없음
        # 내가 유동성 풀에 제거하고 싶으면
        # 그냥 지금 가격에 맞게 빼가면 됨
        # 스왑처럼 내가 가격을 움직이며 하는 행위가 아님
        # 왜냐하면 가격이란 풀 내부의 비율인데
        # 지금 비율(1개에 300달러) 그대로 빼기 때문에
        # 가격은 움직이지 않고 그로인해 슬리피지등이 발생하지 않는다
        # 착각 금지

        self.wait(1)
        self.play(Unwrite(k_dn), run_time=0.851)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################

        # TODO 2.888 secs유동성 공급으로 케이가 상승하는 상황입니다
        # TODO 0:01:00.413  ~  0:01:03.301
        # TODO 1.0secs pause
        # TODO 0:01:03.301  ~  0:01:04.301

        k_up = MathTex(r'K \  \Uparrow').move_to(position)
        self.play(Write(k_up), run_time=1)

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(1)
        self.play(Unwrite(k_up), run_time=0.888)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # TODO 4.7 secs다시 한번 명심할 것은 유동성 공급, 제거는 가격과 관계가 없습니다
        # TODO 0:01:08.152  ~  0:01:12.852
        # TODO 1.0secs pause
        # TODO 0:01:12.852  ~  0:01:13.852
        # TODO 4.977 secs그냥 지금 가격에 맞게 풀 사이즈만 변화시키기에 가격을 움직이는 행위가 아닙니다
        # TODO 0:01:13.852  ~  0:01:18.829
        # TODO 1.0secs pause
        # TODO 0:01:18.829  ~  0:01:19.829
        # TODO 4.349 secs그러므로 거래자 활동과 달리 프라이스 임팩트와 관계가 전혀 없습니다
        # TODO 0:01:19.829  ~  0:01:24.178
        # TODO 1.0secs pause
        # TODO 0:01:24.178  ~  0:01:25.178
        # TODO 2.175 secs기본적인 상황들을 복습해봤습니다
        # TODO 0:01:25.178  ~  0:01:27.353
        # TODO 1.0secs pause
        # TODO 0:01:27.353  ~  0:01:28.353

        # K 원점#####################################################################################
        k_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin), run_time=1)

        self.wait(18.201)

        # TODO 3.697 secs케이상승 후 가격상승 또는 하락하는 경우를 보겠습니다
        # TODO 0:01:28.353  ~  0:01:32.050
        # TODO 1.0secs pause
        # TODO 0:01:32.050  ~  0:01:33.050

        # TODO 7.611 secs케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        # TODO 0:01:33.050  ~  0:01:40.661
        # TODO 1.0secs pause
        # TODO 0:01:40.661  ~  0:01:41.661

        self.wait(5)
        k_up_px_dn = MathTex(r'K \  \Uparrow', r'Price\  \Downarrow').arrange(D).move_to(position)
        k_up_px_up = MathTex(r'K \  \Uparrow', r'Price\  \Uparrow').arrange(D).move_to(position)
        self.play(Write(k_up_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(5.308)

        # K 상승 가격 하락#####################################################################################

        # TODO 5.581 secs아까 300테더에서 3개를 매도할 때는 프라이스 임팩트가 23퍼센트 발생했지만
        # TODO 0:01:55.102  ~  0:02:00.683
        # TODO 1.0secs pause
        # TODO 0:02:00.683  ~  0:02:01.683

        # TODO 5.932 secs지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 19퍼센트만 발생했습니다
        # TODO 0:02:01.683  ~  0:02:07.615
        # TODO 1.0secs pause
        # TODO 0:02:07.615  ~  0:02:08.615
        share_change_1 = MathTex(r'Moving\\ 30\% $\rightarrow$ 23\% \\of\  the\  pool', tex_environment='center').move_to(position)
        k_up_px_dn_text_1 = MathTex(r'Price Impact\\23\% \\ $\downarrow$ \\ 19\%', tex_environment='center').arrange(D).next_to(k_up_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)
        k_up_px_up_text_1 = MathTex(r'Price Impact\\43\% \\ $\downarrow$ \\ 30\%', tex_environment='center').arrange(D).next_to(k_up_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)

        self.play(Write(k_up_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_up_px_dn_text_1))
        self.wait(4)
        self.play(Uncreate(k_up_px_dn_text_1))

        self.play(Unwrite(k_up_px_dn[ 1 ]))

        self.wait(0.513)
        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(C0193).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # TODO 5.69 secs아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만
        # TODO 0:01:41.661  ~  0:01:47.351
        # TODO 1.0secs pause
        # TODO 0:01:47.351  ~  0:01:48.351

        # TODO 5.751 secs지금은 유동성으 풍부하고 3개 매수할 때  프라이스 임팩트가 30퍼센트 발생했습니다
        # TODO 0:01:48.351  ~  0:01:54.102
        # TODO 1.0secs pause
        # TODO 0:01:54.102  ~  0:01:55.102
        self.play(Write(k_up_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_up_px_up_text_1))
        self.wait(4)
        self.play(Uncreate(k_up_px_up_text_1))

        self.play(Unwrite(k_up_px_up[ 1 ]), Unwrite(k_up_px_dn[ 0 ]))
        self.wait(0.441)

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

        # TODO 3.636 secs같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        # TODO 0:02:08.615  ~  0:02:12.251
        # TODO 1.0secs pause
        # TODO 0:02:12.251  ~  0:02:13.251

        # TODO 6.113 secs아까는 10분에 3 지금은 13분에 3, 퍼센트로 따지면 33퍼와 23퍼센트입니다
        # TODO 0:02:13.251  ~  0:02:19.364
        # TODO 1.0secs pause
        # TODO 0:02:19.364  ~  0:02:20.364

        self.wait(2)

        self.play(Create(share_change_1))
        self.wait(5)
        self.play(Uncreate(share_change_1))

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(C1193).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.749)

        k_dn_px_dn = MathTex(r'K\  \Downarrow', r'Price \  \Downarrow').arrange(D).move_to(position)
        k_dn_px_up = MathTex(r'K\  \Downarrow', r'Price \  \Uparrow').arrange(D).move_to(position)

        share_change_2 = MathTex(r'Moving\\ 30\%$\rightarrow$42\% \\of\  the\  pool', tex_environment='center').move_to(position)

        k_dn_px_dn_text_1 = MathTex(r'Price Impact\\23\% \\ $\downarrow$ \\ 30\%', tex_environment='center').arrange(D).next_to(k_dn_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)
        k_dn_px_up_text_1 = MathTex(r'Price Impact\\43\% \\ $\downarrow$ \\ 75\%', tex_environment='center').arrange(D).next_to(k_dn_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)

        self.play(Write(k_dn_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(9.8)

        self.play(Write(k_dn_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_dn_px_dn_text_1))
        self.wait(4)
        self.play(Uncreate(k_dn_px_dn_text_1))

        self.play(Unwrite(k_dn_px_dn[ 1 ]), run_time=1)
        self.wait(1.308)

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        self.play(Write(k_dn_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_dn_px_up_text_1))
        self.wait(4)
        self.play(Uncreate(k_dn_px_up_text_1))

        self.play(Unwrite(k_dn_px_up[ 1 ]),
                  Unwrite(k_dn_px_dn[ 0 ]))

        self.wait(0.417)

        self.wait(2)
        self.play(Create(share_change_2))
        self.wait(5)
        self.play(Uncreate(share_change_2))

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)
        self.wait(0.334)

        # TODO 4.277 secs이번에는 가격이 먼저 상승하고 케이상승 또 하락하는 상황입니다
        # TODO 0:03:11.928  ~  0:03:16.205
        # TODO 1.0secs pause
        # TODO 0:03:16.205  ~  0:03:17.205

        # TODO 5.738 secs아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        # TODO 0:03:17.205  ~  0:03:22.943
        # TODO 1.0secs pause
        # TODO 0:03:22.943  ~  0:03:23.943

        px_up_k_up = MathTex(r'Price \  \Uparrow', r'K\  \Uparrow').arrange(D).move_to(position)
        px_up_k_dn = MathTex(r'Price \  \Uparrow', r'K\  \Downarrow').arrange(D).move_to(position)

        self.play(Write(px_up_k_up[ 0 ]), run_time=1)

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(9.06)
        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다

        # TODO 6.959 secs아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 올라버린 가격인 612 테더를 넣어줘야합니다
        # TODO 0:03:23.943  ~  0:03:30.902
        # TODO 1.0secs pause
        # TODO 0:03:30.902  ~  0:03:31.902
        # TODO 4.591 secs그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됐습니다
        # TODO 0:03:31.902  ~  0:03:36.493
        # TODO 1.0secs pause
        # TODO 0:03:36.493  ~  0:03:37.493

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

        self.wait(3)
        self.play(Unwrite(px_up_k_up[ 1 ]))
        self.wait(0.868)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################

        # TODO 9.737 secs만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 올라가있는 현재 가격대로 비티씨 한 개당 612테더를 돌려받게 됩니다
        # TODO 0:03:37.493  ~  0:03:47.230
        # TODO 1.0secs pause
        # TODO 0:03:47.230  ~  0:03:48.230

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

        self.wait(3)
        self.play(Unwrite(px_up_k_dn[ 1 ]),
                  Uncreate(px_up_k_up[ 0 ]))
        self.wait(0.737)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################

        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)
        # self.wait(2)

        # TODO 4.059 secs이번에는 가격이 먼저 하락하고 케이상승 및 하락하는 상황입니다
        # TODO 0:03:48.230  ~  0:03:52.289
        # TODO 1.0secs pause
        # TODO 0:03:52.289  ~  0:03:53.289

        # TODO 3.564 secs어번에도 현재가격에 맞게 같은 가치를 넣어줘야합니다
        # TODO 0:03:53.289  ~  0:03:56.853
        # TODO 1.0secs pause
        # TODO 0:03:56.853  ~  0:03:57.853

        px_dn_k_up = MathTex(r'Price \  \Downarrow', r'K\  \Uparrow').arrange(D).move_to(position)
        px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(position)

        self.play(Write(px_dn_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        # self.wait(2)
        self.wait(6.623)

        # 가격 하락에서 K상승#####################################################################################

        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다

        # TODO 7.103 secs아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 내려버린 가격인 177 테더를 넣어줘야합니다

        # TODO 0:03:57.853  ~  0:04:04.956

        # TODO 1.0secs pause

        # TODO 0:04:04.956  ~  0:04:05.956

        # TODO 4.615 secs그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다

        # TODO 0:04:05.956  ~  0:04:10.571

        # TODO 1.0secs pause

        # TODO 0:04:10.571  ~  0:04:11.571
        self.play(Write(px_dn_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(3)
        self.play(Unwrite(px_dn_k_up[ 1 ]))
        self.wait(3.718)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # TODO 9.918 secs만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 내려가있는 현재 가격대로 비티씨 한 개당 177테더를 돌려받게 됩니다
        # TODO 0:04:11.571  ~  0:04:21.489
        # TODO 1.0secs pause
        # TODO 0:04:21.489  ~  0:04:22.489

        self.play(Write(px_dn_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 10),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        self.wait(3)
        self.play(Unwrite(px_dn_k_dn[ 1 ]),
                  Unwrite(px_dn_k_up[ 0 ]))
        self.wait(1)

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        # 가격 원점#####################################################################################
        px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(px_origin), run_time=0.5)

        # TODO 3.322 secs각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        # TODO 0:04:22.489  ~  0:04:25.811
        # TODO 1.0secs pause
        # TODO 0:04:25.811  ~  0:04:26.811
        # TODO 4.12 secs동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다
        # TODO 0:04:26.811  ~  0:04:30.931
        # TODO 1.0secs pause
        # TODO 0:04:30.931  ~  0:04:31.931

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


class working1(MovingCameraScene):
    def construct(self):
        # mtex_1 = MathTex(r'{{a^2}} + {{b^2}} = {{c^2}}').scale(2).shift(U * 2)
        # mtex_2 = MathTex(r'{{a^2}} + {{4^2}} = {{c^2}}').scale(2).shift(D * 2)

        line = Line(D,U,stroke_width=120)
        rect = Rectangle(width=2,height = 3,fill_color=RED).to_edge(U)
        tex_1 = Tex(r'I am S\\ddk').arrange(D,aligned_edge= L).scale(1.5).shift(D * 2.5)

        # texts = VGroup(mtex_1, tex_1)

        self.play(Create(line))
        self.play(Create(Dot(line.get_left()[],color=RED)))
        self.play(Create(rect))




        # self.add(index_labels(tex_1))

        # self.play(mtex_1.animate.set_color(RED),run_time=5)
        # self.play(Create(texts))

        self.wait(5)
