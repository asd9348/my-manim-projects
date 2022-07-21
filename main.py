import manim.utils.space_ops
from manim import *

import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_mobs import *
from custom_manim_utils.custom_mobs import *
from manim_physics import *
from manim_gearbox import *
from manim_fontawesome import regular
from pathlib import Path

config.frame_width = 16
config.frame_height = 9
# background_color = W02
from pprint import pprint


class final(Scene):
    def construct(self):
        self.add(NumberPlane())
        # lec1_s1.construct(self)


class working4(MovingCameraScene):
    def construct(self):
        #     self.add(NumberPlane())
        self.camera.frame.save_state()
        #     self.add(NumberPlane())
        self.camera.frame.save_state()

        speak(self, title='Scene2', txt=

        '가격이라는 것에 대해 정확하게 정의하고 가겠습니다#1'
        '가격은 경제,비즈니스면에서 물건,용역,자산의 금전적 수적가치를 따지는 것으로, 한 제품 및 서비스의 가격이란 소비자가 그 제품이나 서비스를 한 단위로 구매하기 위해 지불해야 하는 화폐의 양을 말한다#1'
        '비티씨 테더 페어에서 38000테더라고 적혀있다면 있다면 우리는 비티씨의 가격이 얼마라고 얘기합니까#1'
        '38000달러라고 부릅니다. 그러나 이는 엄밀하게 보면 틀린 표현입니다#1'
        '비티씨의 가격은 38000테더입니다. 테더와 달러는 다른 것입니다 #1'
        '달러는 달러 그자체이고 테더는 이 달러를 담보로 발행했기에 테더 회사가 지급불능이 된다면 테더는 디지털 쓰레기가 됩니다#1'
        '달러를 옹호하는 건 아닙니다. 미국정부가 망하면 달러는 종이 쓰레기가 됩니다#1'
        '그리고 국민이 없다면 정부는 존재할 수 없습니다#1'
        '테더는 실제로 거래해보면 보통 0.999에서 1.001 달러 사이를 움직이며 거래됩니다#1'
        '금본위제 시절에 달러가 금하고 바꿀 수 있는 종이였지 금이 아니듯 테더는 달러가 아니고 가치가 미세하지만 어쨌든 변동하는 자산입니다#1'
        '지금까지의 얘기는 무의식적으로 달러와 테더가 같다고 여겨지는 생각을 없애기 위함이고 이것은 나중에 논스테이블 페어를 이해하는데 도움이 됩니다#1'

        '가격은 어떻게 움직일까요#1'
        '우리가 배우기로는 수요와 공급이 교차하는 지점에서 결정된다고 배웁니다#1'
        '그러나 거래소에서의 가격은 그 말보다는 인내심이 더 부족한 쪽에 의해 결정된다고 하는게 이해하기 쉬울겁니다#1'
        '누구나 더 높은 가격에 팔고 더 낮은 가격에 사고 싶기 때문에 호가창에는 지정가 주문들이 쌓이기 시작합니다#1'
        '그렇게 지정가 주문들이 현재가 위 아래로 계속 쌓이기만 하면 가격은 움직이지 않습니다 #1'
        '실제로 호가창에 100달러와 101달러가 맞닿아 있고 아무도 시장가 주문을 넣지 않으면 가격은 마지막 거래가 100원에서 매수였으면 100원, 101원에서 매도였으면 101원에 정지해있습니다#1'
        '그러다가 누군가 기다림을 참지 못하고 시장가로 구매를 하면 호가창에 쌓여있던 물량이 시장가로 소화되면서 가격은 움직입니다 #1'
        '잘 생각해보면 모든 사람이 지정가 주문만 넣으면 아무 일도 일어나지 않고 모두 기다리기만 합니다#1'

              , keep_pitch=True, update=1, speed=1.4)
        # TODO 3.117 secs가격이라는 것에 대해 정확하게 정의하고 가겠습니다
        # TODO 0:00:00.000  ~  0:00:03.117
        # TODO 1.0secs pause
        # TODO 0:00:03.117  ~  0:00:04.117

        # TODO 13.845 secs가격은 경제,비즈니스면에서 물건,용역,자산의 금전적 수적가치를 따지는 것으로,
        #  한 제품 및 서비스의 가격이란 소비자가 그 제품이나 서비스를 한 단위로 구매하기 위해 지불해야하는 화폐의양을말한다
        # TODO 0:00:04.117  ~  0:00:17.962
        # TODO 1.0secs pause
        # TODO 0:00:17.962  ~  0:00:18.962
        price = Tex('Price').scale(2)

        self.play(Create(price), run_time=3.117)

        price_text = Tex(
            r'A price is the (usually not negative) quantity of payment \\'
            r'or compensation given by one party to another\\in return for goods or services.').next_to(
            price, D)
        self.play(Create(price_text), run_time=10)
        self.wait(3)

        self.play(Uncreate(price),
                  Uncreate(price_text), run_time=2.845)

        # TODO 6.584 secs비티씨 테더 페어에서 38000테더라고 적혀있다면 있다면 우리는 비티씨의 가격이 얼마라고 얘기합니까
        # TODO 0:00:18.962  ~  0:00:25.546
        # TODO 1.0secs pause
        # TODO 0:00:25.546  ~  0:00:26.546

        # TODO 4.591 secs38000달러라고 부릅니다. 그러나 이는 엄밀하게 보면 틀린 표현입니다
        # TODO 0:00:26.546  ~  0:00:31.137
        # TODO 1.0secs pause
        # TODO 0:00:31.137  ~  0:00:32.137

        # TODO 4.639 secs비티씨의 가격은 38000테더입니다. 테더와 달러는 다른 것입니다
        # TODO 0:00:32.137  ~  0:00:36.776
        # TODO 1.0secs pause
        # TODO 0:00:36.776  ~  0:00:37.776

        pair_rect = RoundedRectangle(corner_radius=0.5, height=7, width=4)
        pair_rect_text = Tex("BTCUSDT").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text)

        self.play(Create(pair),
                  run_time=2)

        curr_px_usdt = Tex('38000 USDT').move_to(pair_rect)
        curr_px = Tex('38000').move_to(pair_rect)
        curr_px_usd = Tex('38000 USD?').next_to(pair_rect, R)

        self.play(Create(curr_px_usdt),
                  run_time=2)
        self.wait(2)

        self.play(Create(curr_px_usd),
                  run_time=2)

        curr_px_usd_cross = Cross(curr_px_usd)
        self.wait(1)

        self.play(Create(curr_px_usd_cross),
                  run_time=1)

        circle_curr_px = Circle(color=GREEN, radius=1, stroke_width=25).rotate(PI / 2).move_to(curr_px_usdt)
        self.wait(2)

        usdt_1 = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 2, 1, asset_text_color=WHITE, scaler=0.8)[ 1 ]
        usd_1 = create_entity("A", 0.5, WHITE, "USD", '#9DC87B', 2, 1, asset_text_color='#2A5A25', scaler=0.8)[ 1 ]
        equal = MathTex(r'\neq').scale(2)

        n_eq_form = VGroup(usd_1, equal, usdt_1).arrange(RIGHT, buff=0.5)
        # self.play(Create(n_eq_form))
        #
        #
        # not_equal= Tex(r'USD \neq USDT')
        self.play(ReplacementTransform(VGroup(pair, curr_px_usdt, curr_px_usd_cross, curr_px_usd, circle_curr_px), n_eq_form),
                  run_time=3)
        # self.wait(q)
        #
        # self.play(Uncreate(not_equal))
        #
        #
        n_eq_form = VGroup(usd_1, equal, usdt_1).arrange(RIGHT, buff=0.5).scale(2)
        # usg = LabeledDot(Tex(r'\emph{US\\Gov}',color=BLACK ), radius=1)[ 0].to_edge(D, buff=0.5)
        # us_people = LabeledDot(Tex(r'\emph{US\\People}',color=BLACK), radius=1)[ 0].to_edge(DR, buff=0.5)
        #
        # backed_by_1 = Tex('Backed by').move_to(np.array([usdt.get_x(),0,0]))
        # backed_by_2 = Tex('Backed by')
        # backed_by_3 = Tex('Backed by').move_to(np.array([usg.get_x(),0,0]))

        self.wait(2)
        self.play(Uncreate(n_eq_form),
                  run_time=1.814)

        # btc_equal_38000 = Tex('1 BTC = 38000')
        # cross = Cross(stroke_width=25).scale(3)
        # btc_equal_38000dollars = Tex('1 BTC = 38000 USD')
        # circle = Circle(color=GREEN, radius=3, stroke_width=25).rotate(PI / 2)
        # self.play(Create(btc_equal_38000))
        #
        # self.play(Create(cross))
        #
        # self.play(FadeOut(cross))
        # self.play(TransformMatchingShapes(btc_equal_38000, btc_equal_38000dollars))
        #
        # self.play(Create(circle))
        #
        # self.play(FadeOut(circle),
        #           Uncreate(btc_equal_38000dollars))
        #
        # self.wait(q)

        # TODO 7.55 secs달러는 달러 그자체이고 테더는 이 달러를 담보로 발행했기에 테더 회사가 지급불능이 된다면 테더는 디지털 쓰레기가 됩니다
        # TODO 0:00:37.776  ~  0:00:45.326
        # TODO 1.0secs pause
        # TODO 0:00:45.326  ~  0:00:46.326

        usdt = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 2, 1, asset_text_color=WHITE, scaler=0.8)[ 1 ].to_edge(UL, buff=1)
        usd = create_entity("A", 0.5, WHITE, "USD", '#9DC87B', 2, 1, asset_text_color='#2A5A25', scaler=0.8)[ 1 ].to_edge(DL, buff=1)
        usg = SVGMobject('svgs/government.svg', fill_color=WHITE).scale(0.85).to_edge(D, buff=0.7)
        us_people = SVGMobject('svgs/people.svg', fill_color=WHITE).scale(0.85).to_edge(D, buff=0.7).to_edge(R, buff=1)

        usd_copy = usd.copy().move_to(ORIGIN).to_edge(U, buff=1)

        usg_copy = usg.copy().move_to(ORIGIN).to_edge(U, buff=0.5).to_edge(R, buff=1)
        us_people.move_to([ usg_copy.get_x(), us_people.get_y(), 0 ])

        backed_by_1 = Tex('Backed by').move_to(np.array([ usdt.get_x(), 0, 0 ]))
        backed_by_2 = Tex('Backed by')
        backed_by_3 = Tex('Backed by').move_to(np.array([ us_people.get_x(), 0, 0 ]))

        self.play(Create(usdt), run_time=0.5)
        self.play(Create(backed_by_1), run_time=0.5)
        self.play(Create(usd), run_time=0.5)
        self.play(TransformFromCopy(usd, usd_copy), run_time=0.5)
        self.play(Create(backed_by_2), run_time=0.5)
        self.play(Create(usg), run_time=0.5)
        self.play(TransformFromCopy(usg, usg_copy), run_time=0.5)
        self.play(Create(backed_by_3), run_time=0.5)
        self.play(Create(us_people), run_time=0.5)

        self.wait(2)

        self.play(FadeOut(VGroup(usd, backed_by_1)), run_time=0.5)
        self.wait(1)
        self.play(Uncreate(usdt), run_time=0.55)

        # TODO 4.881 secs달러를 옹호하는 건 아닙니다. 미국정부가 망하면 달러는 종이 쓰레기가 됩니다
        # TODO 0:00:46.326  ~  0:00:51.207
        # TODO 1.0secs pause
        # TODO 0:00:51.207  ~  0:00:52.207
        self.play(FadeOut(VGroup(usg, backed_by_2)),
                  run_time=1.881)
        self.wait(1.5)
        self.play(Uncreate(usd_copy),
                  run_time=1)
        self.wait(1.5)

        # TODO 3.165 secs그리고 국민이 없다면 정부는 존재할 수 없습니다
        # TODO 0:00:52.207  ~  0:00:55.372
        # TODO 1.0secs pause
        # TODO 0:00:55.372  ~  0:00:56.37
        self.play(FadeOut(VGroup(us_people, backed_by_3)),
                  run_time=1)
        self.wait(1)
        self.play(Uncreate(usg_copy),
                  run_time=1.165)
        self.wait(1)

        # TODO 5.98 secs테더는 실제로 거래해보면 보통 0.999에서 1.001 달러 사이를 움직이며 거래됩니다
        # TODO 0:00:56.372  ~  0:01:02.352
        # TODO 1.0secs pause
        # TODO 0:01:02.352  ~  0:01:03.352

        price_of_usdt = Tex(r'Price of 1 "USDT" is \\normally 1.01 \textasciitilde \  0.99 "USD"').scale(1.5)

        self.play(Create(price_of_usdt), run_time=2)
        self.wait(2)
        self.play(Uncreate(price_of_usdt), run_time=2.98)

        # TODO 8.263 secs금본위제 시절에 달러가 금하고 바꿀 수 있는 종이였지 금이 아니듯 테더는 달러가 아니고 가치가 미세하지만 어쨌든 변동하는 자산입니다
        # TODO 0:01:03.352  ~  0:01:11.615
        # TODO 1.0secs pause
        # TODO 0:01:11.615  ~  0:01:12.615

        plane = Axes(
            x_range=(0, 20),
            y_range=(0, 12),
            x_length=15,
            y_length=8,
            axis_config={"include_numbers": False,
                         'include_ticks': False},
        )
        x_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ]
        y_list = [ 5.5, 5, 6, 4, 5, 7, 5, 6, 5, 4, 5, 6, 5, 6, 7, 6, 5, 6, 7, 6.2 ]
        # plane.center()
        line_graph = plane.plot_line_graph(
            x_values=x_list,
            y_values=y_list,
            line_color=C_USDT,
            add_vertex_dots=0,
            # vertex_dot_style=dict(stroke_width=1, fill_color=PURPLE),
            stroke_width=10,
        )

        path = VMobject()
        print(plane.c2p(1, 5), plane.c2p(1, 7))

        print([ plane.c2p(x, y) for x, y in zip(x_list, y_list) ])
        path.set_points_as_corners([ plane.c2p(x, y) for x, y in zip(x_list, y_list) ])
        px = ValueTracker(1)
        px.add_updater(lambda mob: mob.become(ValueTracker(self.camera.frame.get_y())))

        label = Tex(rf'Price of USDT : {px.get_value()}')
        label.add_updater(lambda mob: mob.become(
            Tex(rf'Price of USDT\\{(1.015 - 0.985) * (self.camera.frame.get_y() - (-1 / 3)) / (1 / 3 - (-1 / 3)) + 0.985:.03f} USD').next_to(
                self.camera.frame.get_center(), UR, buff=0.5)))
        icon = SVGMobject('svgs/svg/color/usdt.svg')
        icon.add_updater(
            lambda mob: mob.become(SVGMobject('svgs/svg/color/usdt.svg').scale(0.65).next_to(self.camera.frame.get_center(), DR, buff=0.5)))

        self.play(Create(plane),
                  self.camera.frame.animate.scale(0.7).move_to(path.get_start()),
                  run_time=4)

        self.play(Create(label),
                  Create(icon), run_time=2)
        self.play(Create(line_graph),
                  MoveAlongPath(self.camera.frame, path),
                  run_time=6)

        label.clear_updaters()
        icon.clear_updaters()

        self.wait(2)

        self.play(Restore(self.camera.frame),
                  label.animate.scale(1 / 0.7).move_to([ 2, 2.5, 0 ]),
                  icon.animate.scale(1 / 0.7).move_to([ 2 - label.width / 2, 2.5, 0 ]).shift(L * 2),
                  run_time=4)

        # TODO 8.686 secs지금까지의 얘기는 무의식적으로 달러와 테더가 같다고 여겨지는 생각을 없애기 위함이고 이것은 나중에 논스테이블 페어를 이해하는데 도움이 됩니다
        # TODO 0:01:12.615  ~  0:01:21.301
        # TODO 1.0secs pause
        # TODO 0:01:21.301  ~  0:01:22.301

        self.play(Uncreate(VGroup(icon, label, line_graph, plane), run_time=0.949))

        # TODO 1.752 secs가격은 어떻게 움직일까요
        # TODO 0:00:00.000  ~  0:00:01.752
        # TODO 1.0secs pause
        # TODO 0:00:01.752  ~  0:00:02.752

        # TODO 4.578 secs우리가 배우기로는 수요와 공급이 교차하는 지점에서 결정된다고 배웁니다
        # TODO 0:00:02.752  ~  0:00:07.330
        # TODO 1.0secs pause
        # TODO 0:00:07.330  ~  0:00:08.330
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

        self.wait(1.278)

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

        self.play(Uncreate(VGroup(supply_graph, demand_graph, ax, axis_labels, cross_dot, cross_dot_text)))

        # new_dot = Dot(0.5, color=RED).move_to(ax.c2p(5, supply_graph.underlying_function(5)))
        #
        # self.play(Create(new_dot))
        #

        # self.play(FadeOut(self.mobjects, shift=UP))

        # TODO 6.874 secs그러나 거래소에서의 가격은 그 말보다는 인내심이 더 부족한 쪽에 의해 결정된다고 하는게 이해하기 쉬울겁니다
        # TODO 0:00:08.330  ~  0:00:15.204
        # TODO 1.0secs pause
        # TODO 0:00:15.204  ~  0:00:16.204

        clock_min_angle = ValueTracker(PI / 2)
        clock_hour_angle = ValueTracker(PI / 2)
        clock_circle = Circle(color=WHITE).scale(2)
        clock_center_dot = Dot(color=WHITE)
        clock_min_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=3, buff=0,
                                 max_stroke_width_to_length_ratio=100)
        clock_hour_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                  max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)
        clock_min_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=5, buff=0,
                                                              max_stroke_width_to_length_ratio=100)))
        clock_hour_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                                               max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)))
        clock = VGroup(clock_circle, clock_center_dot, clock_min_handle, clock_hour_handle)

        self.play(Create(clock))

        self.play(AnimationGroup(AnimationGroup(clock_min_angle.animate.set_value(PI / 2 - 4 * 2 * PI),
                                                clock_hour_angle.animate.set_value(PI / 2 - 4 * 2 * PI / 12)), rate_func=linear,
                                 run_time=6))

        self.play(FadeOut(clock), run_time=0.874)

        # TODO 6.693 secs누구나 더 높은 가격에 팔고 더 낮은 가격에 사고 싶기 때문에 호가창에는 지정가 주문들이 쌓이기 시작합니다
        # TODO 0:00:16.204  ~  0:00:22.897
        # TODO 1.0secs pause
        # TODO 0:00:22.897  ~  0:00:23.897

        # TODO 5.629 secs그렇게 지정가 주문들이 현재가 위 아래로 계속 쌓이기만 하면 가격은 움직이지 않습니다
        # TODO 0:00:23.897  ~  0:00:29.526
        # TODO 1.0secs pause
        # TODO 0:00:29.526  ~  0:00:30.526

        # TODO 11.573 secs실제로 호가창에 100달러와 101달러가 맞닿아 있고 아무도 시장가 주문을 넣지 않으면 가격은 마지막 거래가 100원에서 매수였으면 100원, 101원에서 매도였으면 101원에 정지해있습니다
        # TODO 0:00:30.526  ~  0:00:42.099
        # TODO 1.0secs pause
        # TODO 0:00:42.099  ~  0:00:43.099

        # TODO 8.106 secs그러다가 누군가 기다림을 참지 못하고 시장가로 구매를 하면 호가창에 쌓여있던 물량이 시장가로 소화되면서 가격은 움직입니다
        # TODO 0:00:43.099  ~  0:00:51.205
        # TODO 1.0secs pause
        # TODO 0:00:51.205  ~  0:00:52.205

        # TODO 6.233 secs잘 생각해보면 모든 사람이 지정가 주문만 넣으면 아무 일도 일어나지 않고 모두 기다리기만 합니다
        # TODO 0:00:52.205  ~  0:00:58.438
        # TODO 1.0secs pause
        # TODO 0:00:58.438  ~  0:00:59.438

        self.wait(10)


class working2(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=

        '주문의 종류에 대해서 간단히 알아보겠습니다#1'
        '거래소에서 넣는 주문은 주문가격에 따라 크게 두 가지가 있습니다#1'
        '리밋 주문과 마켓 주문이고 한국어로는 지정가 주문 시장가 주문이라고 부릅니다#1'
        '지정가 주문은 말그대로 주문가격을 지정해놓는 주문이고 시장가 주문은 우리가 회를 먹을 때 싯가라고 부르듯이 그냥 그 자리에서 구할 수 있는대로 현재가격으로 즉시 체결하는 주문입니다#1'
        '이전에 들어본 스톱리밋오더, 스톱마켓오더, 트레일링스탑오더 같은 것은 이 가장 기본이 되는 두 종류에 부가적인 기능을 넣은 것입니다#1'


        '리밋 주문은 일반적으로 알고 있듯이 가격을 지정해서 그 가격에 거래하고 싶은 상대측이 나타나면 거래가 체결되는 주문입니다#1'
        '마켓 주문은 원하는 주문량을 입력하면 현재 나와있는 매물 중 가장 유리한 가격대로 주문량이 모두 충족될 때까지 거래를 합니다#1'
        '오더북에서 살펴보겠습니다#1'
        '지금 보시는 건 마켓 주문입니다#1'
        '매수 시장가 주문이면 빨간색 칸 중 가장 아래에 있는 유리한 가격 즉 싸게 팔아줄 판매자에게 구매를 합니다#1'
        '매도 시장가 주문이면 초록색 칸 중 가장 위에 있는 유리한 가격 즉 비싸게 사줄 구매자에게 판매를 합니다#1'
        '지금 보시는 건 리밋 주문입니다#1'
        '매수 지정가 주문이면 초록색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 싼 가격에 구매하려고 대기합니다#1'
        '매도 지정가 주문이면 빨간색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 비싼 가격에 판매하려고 대기합니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        plane = NumberPlane(
            x_range=(0, 20),
            y_range=(0, 10),
            x_length=16,
            y_length=9,
            axis_config={"include_numbers": False},
        )
        x_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ]
        y_list = [ 0, 1, 4, 2, 3, 7, 2, 6, 8, 6, 3, 2, 1, 2, 14, 7, 2, 6, 8, 6 ]
        # plane.center()
        line_graph = plane.plot_line_graph(
            x_values=x_list,
            y_values=y_list,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
            stroke_width=4,
        )

        path = VMobject()
        # graph_1_subpath = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        # graph_1_subpath.reverse_points()
        # path.add_subpath(graph_1_subpath.get_all_points())
        # graph_2_subpath = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        # dot_for_path = Dot(radius=0.3, color=GREEN).move_to(graph_1_b_dot)

        # print()
        # path.add_points_as_corners([ plane.c2p(x, y) for x, y in zip(x_list, y_list) ])
        # path.add_points_as_corners(graph_2_subpath.get_all_points())

        # self.play(MoveAlongPath(self.camera.frame, path), run_time=5)

        dot = Dot().move_to(plane.c2p(5, 5))
        self.play(Create(dot))
        #           MoveAlongPath(self.camera.frame, line_graph), run_time=5)
        # self.play(MoveAlongPath(self.camera.frame, path), run_time=5)

        # dot_for_path = Dot()

        # self.play(MoveAlongPath(dot_for_path, line_graph), run_time=5)

        # self.play(self.camera.frame.animate.scale(0.5).move_to(dot_for_path))


class working3(ThreeDScene):
    def imp_loss_surface(self, u, v):
        x = u
        y = v
        k = ((1 + x) / (1 + y)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        # hold_val = 0.5*x+0.5*y
        # z = np.sin(x) * np.cos(y)
        return np.array([ x, y, z ])

    def dollar_val_surface(self, u, v):
        if u + v > 3:
            v = v - (u + v - 3)

        # x = u
        # y = v
        k = ((1 + u) / (1 + v)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
        curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

    def dollar_val_surface_circle(self, u, v):
        if u ** 2 + v ** 2 < 0.5 ** 2:
            # v=np.sqrt(0.5 ** 2-u ** 2)
            # return np.array([ u, v, 0 ])
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1
        else:

            angle = angle_of_vector(np.array([ u, v, 0 ]))
            u = np.cos(angle) * 0.5
            v = np.sin(angle) * 0.5
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

        # x = u
        # y = v

    def construct(self):
        resolution_fa = 20
        # self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0, zoom=1)
        axes = ThreeDAxes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33), z_range=(-1, 3, 1 / 3),
                          x_length=5, y_length=5, z_length=5)

        lab_x = axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x, lab_y, lab_z)

        imp_loss_graph = Surface(
            lambda u, v: axes.c2p(*self.imp_loss_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            fill_color=PINK
        )

        # sub_axes = ThreeDAxes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33), z_range=(-1, 3, 1/3),
        #                   x_length=5, y_length=5, z_length=5).shift(IN*2)
        sub_axes = Axes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33),
                        x_length=5, y_length=5).shift(IN * 2)

        some_graph = axes.plot(lambda x: 2 * x, x_range=[ -0.99, 2 ]).set_stroke(width=10, color=RED).set_shade_in_3d(True)

        some_graph.set_z_index_by_z_coordinate()
        entropy1 = ParametricFunction(lambda t: axes.c2p(t, t, 0), color=BLUE, stroke_width=6, t_range=[ -0.99, 3 ]).set_shade_in_3d(True)
        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface_circle(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=30
            # checkerboard_colors=[C0177, C0134]
        )

        val_graph.set_style(fill_opacity=0.5)
        val_graph.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        # self.add(sub_axes[0:2],some_graph,entropy1)
        self.add(some_graph, entropy1)

        # imp_loss_surface = Surface(
        #     lambda u, v: axes.c2p(u, v, imp_loss_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[-0.9, 4],
        #     u_range=[-0.9, 4],
        #     color=PINK
        #     )
        # dollar_val_surface = Surface(
        #     lambda u, v: axes.c2p(u, v, dollar_val_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[-0.9, 4],
        #     u_range=[-0.9, 4],
        #     color=RED
        #     )
        #

        my_graph = axes.plot(lambda x: x, x_range=[ -1, 5 ])
        # my_graph.set_colors_by_gradient([RED,BLUE])
        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        # face = ThreeDVMobject()
        # face.set_points_as_corners([
        #     [ 1, 0, 0 ],
        #     [ 1, 0, 5 ],
        #     [ 0, 1, 5 ],
        #     [ 0, 1, 0 ],
        #     [ 1, 0, 0 ]
        # ])
        #
        # face.set_fill(color=RED, opacity=0.5)
        # face.set_stroke(color=RED_E,width=3,opacity=0.7)
        #
        three_d_wall = ThreeDVMobject().set_points_as_corners([ [ -0.5, -0.5, -0.5 ],
                                                                [ 2, -0.5, -0.5 ],
                                                                [ 2, -0.5, 1 ],
                                                                [ -0.5, -0.5, 1 ],
                                                                [ -0.5, -0.5, -0.5 ],
                                                                ]).set_fill(color=BLUE, opacity=1).set_shade_in_3d(True)

        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, labs)
        # self.add(imp_loss_graph)
        # self.play(Create(val_graph),run_time=5)
        self.add(val_graph, three_d_wall)
        # self.play(Create(my_graph))
        # self.play(my_graph.animate.set_color_by_gradient([RED,BLUE,GREEN]),run_time=3)
        # self.play(my_graph.animate.set_color(RED),run_time=3)
        # val_graph.get_z_index_reference_point()
        # some_graph.get_z_index_reference_point()

        # val_graph.set_z_index_by_z_coordinate()
        # some_graph.set_z_index_by_z_coordinate()
        # axes.set_z_index(5)
        # val_graph.set_z_index(1)
        # some_graph.set_z_index(3)
        # entropy1.set_z_index(3)
        # three_d_wall.set_z_index(8)
        # some_graph.set_z_index_by_z_coordinate()

        # some_graph.shift(IN * 3)

        # print(val_graph.get_z_index_reference_point())
        # print(some_graph.get_z_index_reference_point())
        # print(val_graph.get_z())
        # print(some_graph.get_z())
        self.set_camera_orientation(theta=-90 * DEGREES, phi=45 * DEGREES, zoom=1)

        # self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 5)
        # self.begin_ambient_camera_rotation(rate=0.2, about="theta",run_time=1)
        # self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        # self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES,gamma=0)

        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=45 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=90 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=135 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)


class working1(MovingCameraScene):
    # config.background_color = GRAY

    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        line = Line(start=[ -2, 2, 0 ], end=[ 3, 1, 0 ])
        # poly = Polygram([[-2,2,0],[2,2,0]],
        #                 [[2,2,0],[2,-2,0]],
        #                 [[2,-2,0],[-2,-2,0]],
        #                 [[-2,-2,0],[-2,2,0]],color = RED, fill_opacity=0.5)
        poly = Polygon([ -2, 2, 0 ], [ 2, 2, 0 ], [ 2, -2, 0 ], [ -2, -2, 0 ], color=GREEN, fill_opacity=0.5)

        print(poly.get_end_anchors())

        temp_line = Line(start=poly.get_end_anchors()[ 1 ], end=poly.get_end_anchors()[ 2 ])
        # self.add(index_labels(poly.get_subpaths()))
        print(line_intersection(([ -2, 2, 0 ], [ 3, -1, 0 ]), (poly.get_end_anchors()[ 0 ], poly.get_end_anchors()[ 1 ])))

        # alpha_half_base = line_intersection((A, alpha_half_point), (B, C))

        intersect = line_intersection(
            ([ -2, 2, 0 ], [ 3, 1, 0 ]),
            (poly.get_end_anchors()[ 0 ], poly.get_end_anchors()[ 1 ]))
        dot = Dot(radius=0.5).move_to(line_intersection(
            ([ -2, 2, 0 ], [ 3, 1, 0 ]),
            (poly.get_end_anchors()[ 0 ], poly.get_end_anchors()[ 1 ])))

        fuck_line = Line(start=[ -6, 4, 0 ], end=[ -3, -2, 0 ])
        print(f'getvector is {fuck_line.get_vector()}')
        fuck_vector = Arrow(start=O, end=fuck_line.get_vector(), buff=0)
        print(f'unutvector is {fuck_line.get_unit_vector()}')
        fuck_unit_vector = Arrow(start=O, end=fuck_line.get_unit_vector(), buff=0, color=RED)
        # new_tri = Polygon
        new_tri = Polygon([ -2, 2, 0 ], [ 2, 2, 0 ], intersect, color=BLUE, fill_opacity=1)

        # print(angle_of_vector([1,1,0]))
        # new_tri.align_to(O, UL)
        # print(new_tri.get_end_anchors())
        # print(angle_between_vectors([ 2, 2, 0 ],intersect))
        # print(angle_between_vectors([ 4, -0.5, 0 ],[ 4, 0, 0 ]))

        print('current angle is', angle_of_vector(fuck_line.get_unit_vector()))

        unit_vector_1 = Line(start=[ -2, 2, 0 ], end=[ 2, 2, 0 ]).get_unit_vector()
        unit_vector_2 = Line(start=[ -2, 2, 0 ], end=[ 2, 1.2, 0 ]).get_unit_vector()
        unit_vector_1_arrow = Arrow(start=O, end=unit_vector_1, buff=0, color=RED)
        unit_vector_2_arrow = Arrow(start=O, end=unit_vector_2, buff=0, color=BLUE)
        angle = angle_between_vectors(unit_vector_1, unit_vector_2)
        print(angle)

        fuck_angle = angle_of_vector(fuck_line.get_unit_vector()) - (-angle)

        new_tri_path = Line(start=new_tri.get_center(), end=new_tri.get_center() + R * new_tri.width + D * new_tri.height)
        # self.add( line,
        #          poly, dot,new_tri, new_rect,fuck_line,unit_vector_1_arrow,unit_vector_2_arrow
        #          )

        self.play(Create(poly))

        self.play(Create(new_tri))
        poly.become(Polygon([ -2, 2, 0 ], intersect, [ 2, -2, 0 ], [ -2, -2, 0 ], color=GREEN, fill_opacity=0.5))
        # self.play(Create(poly))
        # self.play(Create(poly))

        self.play(Rotate(new_tri, angle=fuck_angle, about_point=new_tri.get_end_anchors()[ -1 ]))

        self.play(new_tri.animate.move_to(get_compensated_coor(new_tri, new_tri.get_end_anchors()[ -1 ], [ -6, 4, 0 ])))
        self.play(new_tri.animate.move_to(get_compensated_coor(new_tri, new_tri.get_end_anchors()[ -2 ], fuck_line.get_end())))

        # new_fucking_temp_line = Line(start=midpoint(new_tri.get_end_anchors()[ -1 ],new_tri.get_end_anchors()[ -2 ], end=fuck_line.e)
        # self.play(MoveAlongPath(new_tri, fuck_line))

        self.wait(5)


class working1(MovingCameraScene):
    # config.background_color = GRAY

    def construct(self):
        numberplane = NumberPlane()
        # self.add(numberplane)

        # start_dot = Dot(color=RED).move_to([ -2, 2, 0 ])

        # line = Line(start=[ 3, -1, 0 ], end=[ 2, 2, 0 ])
        # line = Arrow(start=[ 2, 2, 0 ], end=[ 3, -1, 0 ])

        # tri_base_line = Arrow(color=BLUE, buff=0, start=[ 2, -1, 0 ], end=[ -2, -1, 0 ])
        # tri_base_line = Line(color=BLUE, buff=0, start=[ -2, -1, 0 ], end=[ 2, -1, 0 ])
        #
        # unit_v = line.get_unit_vector()
        # print(is_on_left(tri_base_line, np.array([0,-5,0])))

        tri = Triangle(fill_color=C2495, fill_opacity=1, stroke_color=C2498).scale(4)
        tri.move_to(get_compensated_coor(tri, tri.get_bottom(), [ 0, -3, 0 ]))
        print(tri.get_end_anchors())

        dot = Dot(color=RED).move_to(center_of_mass(tri.get_end_anchors())).set_z_index(3.5)

        perp_line_left = redraw(
            lambda: get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 2 ] ]).set_stroke(
                color=YELLOW, width=7).set_z_index(3))
        perp_line_right = redraw(
            lambda: get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 1 ], tri.get_end_anchors()[ 2 ] ]).set_stroke(
                color=PINK, width=7).set_z_index(3))
        perp_line_bottom = redraw(
            lambda: get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 1 ] ]).set_stroke(
                color=GREEN, width=7).set_z_index(3))

        my_scaler = 1

        vertical_green = Line(color=GREEN, stroke_width=13, start=[ 4, -4, 0 ],
                              end=[ 4, -4, 0 ] + U * get_line_length(perp_line_bottom)).set_z_index(4)
        vertical_pink = Line(color=PINK, stroke_width=13, start=vertical_green.get_end(),
                             end=vertical_green.get_end() + U * get_line_length(perp_line_right)).set_z_index(3)
        vertical_yellow = Line(color=YELLOW, stroke_width=13, start=vertical_green.get_end(),
                               end=vertical_green.get_end() + U * perp_line_left.get_end()).set_z_index(2)

        start = [ 4, -3, 0 ]

        vertical_green = redraw(
            lambda: Line(color=GREEN, stroke_width=13, start=start, end=start + + U * get_line_length(perp_line_bottom)).set_z_index(4))
        vertical_pink = redraw(lambda: Line(color=PINK, stroke_width=13, start=start, end=start + U * (
                get_line_length(perp_line_right) + get_line_length(perp_line_bottom)) * my_scaler).set_z_index(3))
        vertical_yellow = redraw(lambda: Line(color=YELLOW, stroke_width=13, start=start, end=start + U * (
                get_line_length(perp_line_left) + get_line_length(perp_line_bottom) + get_line_length(
            perp_line_right)) * my_scaler).set_z_index(2))

        yellow_var = Variable(0, 'YELLOW', DecimalNumber).to_edge(UL, buff=1.5)
        yellow_var[ 0 ][ 0 ].set_color(color=YELLOW)
        yellow_var[ 1 ].add_updater(lambda x: x.become(DecimalNumber(get_line_length(perp_line_left)).next_to(yellow_var[ 0 ], R)))

        pink_var = Variable(0, 'PINK', DecimalNumber)
        pink_var[ 0 ][ 0 ].set_color(color=YELLOW)
        pink_var.move_to(get_compensated_coor(pink_var, pink_var[ 0 ][ 1 ].get_center(), yellow_var[ 0 ][ 1 ].get_bottom() + D * 1))
        pink_var[ 1 ].add_updater(lambda x: x.become(DecimalNumber(get_line_length(perp_line_right)).next_to(pink_var[ 0 ], R)))

        green_var = Variable(0, 'GREEN', DecimalNumber)
        green_var[ 0 ][ 0 ].set_color(color=YELLOW)
        green_var.move_to(get_compensated_coor(green_var, green_var[ 0 ][ 1 ].get_center(), pink_var[ 0 ][ 1 ].get_bottom() + D * 1))
        green_var[ 1 ].add_updater(lambda x: x.become(DecimalNumber(get_line_length(perp_line_bottom)).next_to(green_var[ 0 ], R)))

        vertical_green_braces = redraw(lambda: BraceBetweenPoints(vertical_green.get_start(), vertical_green.get_end()))
        vertical_pink_braces = redraw(lambda: BraceBetweenPoints(vertical_green.get_end(), vertical_pink.get_end()))
        vertical_yellow_braces = redraw(lambda: BraceBetweenPoints(vertical_pink.get_end(), vertical_yellow.get_end()))

        vertical_green_braces_label = redraw(lambda: DecimalNumber(get_line_length(perp_line_bottom)).next_to(vertical_green_braces))
        vertical_pink_braces_label = redraw(lambda: DecimalNumber(get_line_length(perp_line_right)).next_to(vertical_pink_braces))
        vertical_yellow_braces_label = redraw(lambda: DecimalNumber(get_line_length(perp_line_left)).next_to(vertical_yellow_braces))

        self.play(Create(tri))
        self.play(Create(VGroup(yellow_var, pink_var, green_var)))
        self.play(Create(dot))
        self.play(Create(VGroup(perp_line_left, perp_line_right, perp_line_bottom)))
        self.play(Create(VGroup(vertical_green, vertical_pink, vertical_yellow)))
        self.play(Create(VGroup(vertical_green_braces, vertical_pink_braces, vertical_yellow_braces)))
        print(vertical_green_braces_label.get_center())
        self.play(Create(VGroup(vertical_green_braces_label, vertical_pink_braces_label, vertical_yellow_braces_label)))
        # self.play(Create(vertical_green_braces_label))

        self.play(dot.animate.shift(L * 1), run_time=1)
        self.play(dot.animate.shift(R * 1), run_time=1)
        self.play(dot.animate.shift(U * 1), run_time=1)
        self.play(dot.animate.shift(D * 1), run_time=1)

        tri_path = Triangle(fill_color=BLUE_E, fill_opacity=1).scale(2.5)
        tri_path.move_to(
            get_compensated_coor(tri_path, center_of_mass(tri_path.get_end_anchors()), center_of_mass(tri.get_end_anchors())))

        self.play(dot.animate.move_to(tri_path.get_end_anchors()[ 2 ]), run_time=1)
        self.play(MoveAlongPath(dot, tri_path), run_time=7)

        self.play(dot.animate.move_to(center_of_mass(tri.get_end_anchors())), run_time=3)
        self.play(dot.animate.shift(D * 0.5 + R * 0.5), run_time=3)

        yellow_tri = Polygon(dot.get_center(), dot.get_center() + L * get_line_length(perp_line_left) / np.cos(30 * DEGREES),
                             move_point_with_angle_and_length(dot.get_center(), 120 * DEGREES,
                                                              get_line_length(perp_line_left) / np.cos(30 * DEGREES)), color=C1995,
                             fill_opacity=1, stroke_color=C1998).set_z_index(2)

        pink_tri = Polygon(dot.get_center(), dot.get_center() + R * get_line_length(perp_line_right) / np.cos(30 * DEGREES),
                           move_point_with_angle_and_length(dot.get_center(), 60 * DEGREES,
                                                            get_line_length(perp_line_right) / np.cos(30 * DEGREES)), color=C1995,
                           fill_opacity=1, stroke_color=C1998).set_z_index(2)
        green_tri = Polygon(dot.get_center(),
                            dot.get_center() + np.array([ np.cos(-60 * DEGREES), np.sin(-60 * DEGREES), 0 ]) * get_line_length(
                                perp_line_bottom) / np.cos(30 * DEGREES),
                            move_point_with_angle_and_length(dot.get_center(), -120 * DEGREES,
                                                             get_line_length(perp_line_bottom) / np.cos(30 * DEGREES)), color=C1995,
                            fill_opacity=1, stroke_color=C1998).set_z_index(2)

        perp_line_left.clear_updaters()
        perp_line_right.clear_updaters()
        perp_line_bottom.clear_updaters()

        self.play(Create(VGroup(yellow_tri, green_tri, pink_tri)),
                  FadeOut(dot))

        yellow_tri.add(perp_line_left)
        pink_tri.add(perp_line_right)
        green_tri.add(perp_line_bottom)

        big_tri = Polygon(yellow_tri.get_end_anchors()[ 0 ], pink_tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 2 ], color=C2298,
                          fill_opacity=1, fill_color=C2295).set_z_index(1.5)

        self.play(Rotate(yellow_tri, angle=-120 * DEGREES, about_point=center_of_mass(yellow_tri.get_end_anchors())))

        self.play(Create(big_tri))

        big_tri.add(yellow_tri, pink_tri)

        self.play(Rotate(big_tri, angle=-120 * DEGREES, about_point=center_of_mass(big_tri.get_end_anchors())))

        self.play(pink_tri.animate.move_to([ 0, pink_tri.get_y(), 0 ]),
                  green_tri.animate.move_to([ 0, green_tri.get_y(), 0 ]))

        self.wait(10)


class working1(ThreeDScene):
    # config.background_color = GRAY

    def construct(self):
        # self.add(coin('mana', type='color'))

        # def _setup_faces(self):
        # u_values, v_values = self._get_u_values_and_v_values()

        axes = ThreeDAxes()

        vertex_list = [ [ 0.0, 0.0, 0.0 ], [ 0.0, 0.1111111111111111, 0.1975308641975309 ], [ 0.0, 0.2222222222222222, 0.345679012345679 ],
                        [ 0.0, 0.3333333333333333, 0.4444444444444444 ], [ 0.0, 0.4444444444444444, 0.49382716049382713 ],
                        [ 0.0, 0.5555555555555556, 0.49382716049382713 ], [ 0.0, 0.6666666666666666, 0.4444444444444445 ],
                        [ 0.0, 0.7777777777777777, 0.3456790123456791 ], [ 0.0, 0.8888888888888888, 0.19753086419753094 ],
                        [ 0.0, 1.0, 0.0 ], [ 0.1111111111111111, 0.0, 0.1975308641975309 ],
                        [ 0.1111111111111111, 0.1111111111111111, 0.3703703703703704 ],
                        [ 0.1111111111111111, 0.2222222222222222, 0.49382716049382713 ],
                        [ 0.1111111111111111, 0.3333333333333333, 0.5679012345679012 ],
                        [ 0.1111111111111111, 0.4444444444444444, 0.5925925925925926 ],
                        [ 0.1111111111111111, 0.5555555555555556, 0.5679012345679012 ],
                        [ 0.1111111111111111, 0.6666666666666666, 0.49382716049382713 ],
                        [ 0.1111111111111111, 0.7777777777777777, 0.37037037037037046 ],
                        [ 0.1111111111111111, 0.8888888888888888, 0.1975308641975309 ],
                        [ 0.1111111111111111, 0.8888888888888888, 0.1975308641975309 ], [ 0.2222222222222222, 0.0, 0.345679012345679 ],
                        [ 0.2222222222222222, 0.1111111111111111, 0.49382716049382713 ],
                        [ 0.2222222222222222, 0.2222222222222222, 0.5925925925925926 ],
                        [ 0.2222222222222222, 0.3333333333333333, 0.6419753086419753 ],
                        [ 0.2222222222222222, 0.4444444444444444, 0.6419753086419753 ],
                        [ 0.2222222222222222, 0.5555555555555556, 0.5925925925925926 ],
                        [ 0.2222222222222222, 0.6666666666666666, 0.4938271604938272 ],
                        [ 0.2222222222222222, 0.7777777777777777, 0.34567901234567916 ],
                        [ 0.2222222222222222, 0.7777777777777777, 0.34567901234567916 ],
                        [ 0.2222222222222222, 0.7777777777777777, 0.34567901234567916 ], [ 0.3333333333333333, 0.0, 0.4444444444444444 ],
                        [ 0.3333333333333333, 0.1111111111111111, 0.5679012345679012 ],
                        [ 0.3333333333333333, 0.2222222222222222, 0.6419753086419753 ],
                        [ 0.3333333333333333, 0.3333333333333333, 0.6666666666666667 ],
                        [ 0.3333333333333333, 0.4444444444444444, 0.6419753086419753 ],
                        [ 0.3333333333333333, 0.5555555555555556, 0.5679012345679012 ],
                        [ 0.3333333333333333, 0.6666666666666666, 0.4444444444444446 ],
                        [ 0.3333333333333333, 0.6666666666666667, 0.4444444444444444 ],
                        [ 0.3333333333333333, 0.6666666666666667, 0.4444444444444444 ],
                        [ 0.3333333333333333, 0.6666666666666667, 0.4444444444444444 ], [ 0.4444444444444444, 0.0, 0.49382716049382713 ],
                        [ 0.4444444444444444, 0.1111111111111111, 0.5925925925925926 ],
                        [ 0.4444444444444444, 0.2222222222222222, 0.6419753086419753 ],
                        [ 0.4444444444444444, 0.3333333333333333, 0.6419753086419753 ],
                        [ 0.4444444444444444, 0.4444444444444444, 0.5925925925925926 ],
                        [ 0.4444444444444444, 0.5555555555555556, 0.49382716049382713 ],
                        [ 0.4444444444444444, 0.5555555555555555, 0.49382716049382724 ],
                        [ 0.4444444444444444, 0.5555555555555556, 0.49382716049382713 ],
                        [ 0.4444444444444444, 0.5555555555555556, 0.49382716049382713 ],
                        [ 0.4444444444444444, 0.5555555555555556, 0.49382716049382713 ], [ 0.5555555555555556, 0.0, 0.49382716049382713 ],
                        [ 0.5555555555555556, 0.1111111111111111, 0.5679012345679012 ],
                        [ 0.5555555555555556, 0.2222222222222222, 0.5925925925925926 ],
                        [ 0.5555555555555556, 0.3333333333333333, 0.5679012345679012 ],
                        [ 0.5555555555555556, 0.4444444444444444, 0.49382716049382713 ],
                        [ 0.5555555555555556, 0.4444444444444444, 0.49382716049382713 ],
                        [ 0.5555555555555556, 0.4444444444444443, 0.49382716049382724 ],
                        [ 0.5555555555555556, 0.4444444444444444, 0.49382716049382713 ],
                        [ 0.5555555555555556, 0.4444444444444444, 0.49382716049382713 ],
                        [ 0.5555555555555556, 0.4444444444444444, 0.49382716049382713 ], [ 0.6666666666666666, 0.0, 0.4444444444444445 ],
                        [ 0.6666666666666666, 0.1111111111111111, 0.49382716049382713 ],
                        [ 0.6666666666666666, 0.2222222222222222, 0.4938271604938272 ],
                        [ 0.6666666666666666, 0.3333333333333333, 0.44444444444444453 ],
                        [ 0.6666666666666666, 0.33333333333333326, 0.44444444444444453 ],
                        [ 0.6666666666666666, 0.33333333333333326, 0.44444444444444453 ],
                        [ 0.6666666666666666, 0.33333333333333337, 0.4444444444444445 ],
                        [ 0.6666666666666666, 0.3333333333333335, 0.4444444444444444 ],
                        [ 0.6666666666666666, 0.3333333333333335, 0.4444444444444444 ],
                        [ 0.6666666666666666, 0.3333333333333335, 0.4444444444444444 ], [ 0.7777777777777777, 0.0, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.1111111111111111, 0.3703703703703705 ],
                        [ 0.7777777777777777, 0.2222222222222222, 0.34567901234567916 ],
                        [ 0.7777777777777777, 0.22222222222222238, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.22222222222222232, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.22222222222222232, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.22222222222222243, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.22222222222222232, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.22222222222222232, 0.3456790123456791 ],
                        [ 0.7777777777777777, 0.22222222222222232, 0.3456790123456791 ], [ 0.8888888888888888, 0.0, 0.19753086419753094 ],
                        [ 0.8888888888888888, 0.1111111111111111, 0.19753086419753096 ],
                        [ 0.8888888888888888, 0.11111111111111105, 0.19753086419753096 ],
                        [ 0.8888888888888888, 0.11111111111111122, 0.19753086419753094 ],
                        [ 0.8888888888888888, 0.11111111111111116, 0.19753086419753094 ],
                        [ 0.8888888888888888, 0.11111111111111116, 0.19753086419753094 ],
                        [ 0.8888888888888888, 0.11111111111111127, 0.1975308641975309 ],
                        [ 0.8888888888888888, 0.11111111111111116, 0.19753086419753094 ],
                        [ 0.8888888888888888, 0.11111111111111116, 0.19753086419753094 ],
                        [ 0.8888888888888888, 0.11111111111111116, 0.19753086419753094 ], [ 1.0, 0.0, 0.0 ],
                        [ 1.0, -5.551115123125783e-17, 0.0 ], [ 1.0, -1.1102230246251565e-16, -1.232595164407831e-32 ],
                        [ 1.0, 5.551115123125783e-17, 0.0 ], [ 1.0, 0.0, 0.0 ], [ 1.0, 0.0, 0.0 ],
                        [ 1.0, 1.1102230246251565e-16, -1.232595164407831e-32 ], [ 1.0, 0.0, 0.0 ], [ 1.0, 0.0, 0.0 ], [ 1.0, 0.0, 0.0 ] ]

        test_mob = PointCloudFromCustom(vertex_list,
                                        fill_color=RED, fill_opacity=0.5,
                                        stroke_width=1, stroke_opacity=0.5, scaler=3).scale_to_fit_width(4)
        # .move_to(axes.c2p(0, 0, 0))
        test_mob.set_fill_by_checkerboard(BLUE)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.add(axes, test_mob)

        # for i in range(len(u_values) - 1):
        #     for j in range(len(v_values) - 1):
        #         u1, u2 = u_values[ i: i + 2 ]
        #         v1, v2 = v_values[ j: j + 2 ]
        #         face = ThreeDVMobject()
        #         face.set_points_as_corners(
        #             [
        #                 [ u1, v1, 0 ],
        #                 [ u2, v1, 0 ],
        #                 [ u2, v2, 0 ],
        #                 [ u1, v2, 0 ],
        #                 [ u1, v1, 0 ],
        #             ],
        #         )
        #         faces.add(face)
        #         face.u_index = i
        #         face.v_index = j
        #         face.u1 = u1
        #         face.u2 = u2
        #         face.v1 = v1
        #         face.v2 = v2
        # faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)
        # faces.set_stroke(
        #     color=self.stroke_color,
        #     width=self.stroke_width,
        #     opacity=self.stroke_opacity,
        # )
        # self.add(*faces)
        # if self.checkerboard_colors:
        #     self.set_fill_by_checkerboard(*self.checkerboard_colors)

        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=45 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=90 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=135 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)


class ParaSurface(ThreeDScene):
    def func(self, p1, p2):
        if p1 + p2 > 1:
            p2 = p2 - (p1 + p2 - 1)
        p3 = 1 - p1 - p2
        z = p1 * (1 - p1) + p2 * (1 - p2) + p3 * (1 - p3)
        return np.array([ p1, p2, z ])

    def dot_text(self, color, tracker):
        dot = Dot(radius=0.15, color=color)
        percent_text = Tex("\% = ", color=color).next_to(dot, RIGHT * 0.6)
        static_group = VGroup(dot, percent_text).scale(0.65)
        if isinstance(tracker, list):
            percent_changer = Integer(number=int((1 - tracker[ 0 ].get_value() - tracker[ 1 ].get_value()) * 100)).scale(0.65).set_color(
                color)
            percent_changer.add_updater(lambda perc: self.renderer.camera.add_fixed_in_frame_mobjects(
                perc.set_value(int((1 - tracker[ 0 ].get_value() - tracker[ 1 ].get_value()) * 100)).set_color(color).next_to(static_group,
                                                                                                                              RIGHT * 0.6)))
        else:
            percent_changer = Integer(number=int(tracker.get_value() * 100)).scale(0.65).set_color(color)
            percent_changer.add_updater(lambda perc: self.renderer.camera.add_fixed_in_frame_mobjects(
                perc.set_value(tracker.get_value() * 100).set_color(color).next_to(static_group, RIGHT * 0.6)))
        percent_changer.next_to(static_group, RIGHT * 0.6)
        text_group = VGroup(static_group, percent_changer)
        self.renderer.camera.add_fixed_in_frame_mobjects(static_group)
        return text_group

    def construct(self):
        x = ValueTracker(0.0)
        y = ValueTracker(0.0)

        blue_dot_tracker = self.dot_text(BLUE, x)
        red_dot_tracker = self.dot_text(RED, y).next_to(blue_dot_tracker, RIGHT * 2)
        green_dot_tracker = self.dot_text(GREEN, [ x, y ]).next_to(red_dot_tracker, RIGHT * 2)

        dot_updater_text = VGroup(blue_dot_tracker, red_dot_tracker, green_dot_tracker).scale(1.5).shift(DOWN * 3 + LEFT * 2)

        x_vals = [ "0\%", "33\%", "66\%", "100\%" ]
        x_pos = [ 0, 0.3333, 0.6666, 0.9999 ]
        x_dict = dict(zip(x_pos, x_vals))
        x_label_dot = Sphere(radius=.15).set_color(BLUE)
        x_label_perc = Tex("\%", color=BLUE).next_to(x_label_dot, RIGHT * 0.6)
        x_label = VGroup(x_label_dot, x_label_perc)

        # y_vals = [Tex("0\%").rotate(PI/2,axis=IN).rotate(p),Tex("33\%").rotate(PI/2,axis=IN).rotate(p),Tex("66\%").rotate(PI/2,axis=IN).rotate(p),Tex("100\%").rotate(PI/2,axis=IN).rotate(p)]
        y_vals = [ "0\%", "33\%", "66\%", "100\%" ]
        y_pos = [ 0, 0.3333, 0.6666, 0.9999 ]
        y_dict = dict(zip(y_pos, y_vals))
        y_label_dot = Sphere(radius=.15).set_color(RED)
        y_label_perc = Tex("\%", color=RED).next_to(y_label_dot, RIGHT * 0.6)
        y_label = VGroup(y_label_dot, y_label_perc)

        axes = ThreeDAxes(
            x_range=[ 0, 1, .3333 ],
            y_range=[ 0, 1, .3333 ],
            z_range=[ 0, 1, .2 ],
            axis_config={
                "include_tip": False
            }
        ).add_coordinates(x_dict, y_dict)

        cost_label = axes.get_z_axis_label('Gini')

        axes.background_line_style = {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 1,
        }

        labels = axes.get_axis_labels(
            x_label=x_label,
            y_label=y_label
        )
        axes.axis_labels[ 0 ].rotate(PI / 2, axis=RIGHT)
        axes.axis_labels[ 0 ].shift(RIGHT)
        axes.axis_labels[ 1 ].rotate(PI / 2, axis=RIGHT)
        axes.axis_labels[ 1 ].rotate(PI / 2, axis=IN)
        axes.axis_labels[ 1 ].shift(UP * 3)

        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[ 0, 1 ],
            v_range=[ 0, 1 ],
            fill_opacity=0.5
        )

        line1 = Line(axes.c2p(1, 0, 0), axes.c2p(0, 0, 0), stroke_width=2).set_color(color=YELLOW)
        line2 = Line(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), stroke_width=2).set_color(color=YELLOW)
        line3 = Line(axes.c2p(0, 1, 0), axes.c2p(1, 0, 0), stroke_width=2).set_color(color=YELLOW)
        triangle_perimeter = VGroup(line1, line2, line3)

        def triangular_grid(x_min, x_max, dx, y_min, y_max, dy):
            def get_line(s, e):
                return Line(s, e, color=BLUE_D, stroke_width=1)

            ctp = axes.coords_to_point
            v_lines = VGroup(*[ get_line(ctp(x, y_min), ctp(x, y_max - x)) for x in np.arange(x_min, x_max + dx, dx) ])
            h_lines = VGroup(*[ get_line(ctp(x_min, y), ctp(x_max - y, y)) for y in np.arange(y_min, y_max + dy, dy) ])

            return VGroup(v_lines, h_lines)

        plane = triangular_grid(0, 1, .05, 0, 1, 0.05).next_to(line1, UP, buff=0)

        initial_point = [ axes.coords_to_point(*self.func(x.get_value(), y.get_value())) ]
        sphere = Sphere(center=initial_point, radius=.08).set_color(YELLOW)
        xysphere = Sphere(center=initial_point, radius=.08).set_color(YELLOW)
        sphere.add_updater(lambda s: s.move_to(axes.coords_to_point(*self.func(x.get_value(), y.get_value()))))
        xysphere.add_updater(lambda s: s.move_to(axes.coords_to_point(x.get_value(), y.get_value(), 0)))

        entropy1 = ParametricFunction(lambda t: axes.c2p(t, 0, 2 * t * (1 - t)), color=YELLOW, stroke_width=6)
        entropy2 = ParametricFunction(lambda t: axes.c2p(0, t, 2 * t * (1 - t)), color=YELLOW, stroke_width=6)
        entropy3 = ParametricFunction(lambda t: axes.c2p(t, 1 - t, 2 * t * (1 - t)), color=YELLOW, stroke_width=6)

        self.set_camera_orientation(theta=-90 * DEGREES, phi=60 * DEGREES, zoom=0.5)
        self.play(Create(axes), FadeIn(labels), FadeIn(cost_label))
        # self.wait(0.3)
        self.play(Create(triangle_perimeter))
        self.play(Create(plane))
        self.bring_to_back(plane)
        self.play(triangle_perimeter.animate.set_color(BLUE_D))
        self.bring_to_back(triangle_perimeter)
        self.wait()
        # self.move_camera(theta=-90 * DEGREES, phi=75 * DEGREES, zoom=0.8, run_time=4)
        # self.play(Create(entropy1), run_time=1.5)
        # self.wait()
        # self.renderer.camera.add_fixed_in_frame_mobjects(dot_updater_text)
        # self.play(FadeIn(dot_updater_text))
        # self.add_fixed_in_frame_mobjects(dot_updater_text)
        # self.play(Create(xysphere))
        # self.wait(0.3)
        # self.play(x.animate.set_value(1.0), y.animate.set_value(0.0), run_time=2)
        # self.wait(0.3)
        # self.play(x.animate.set_value(0.0), y.animate.set_value(0.0), run_time=2)
        # self.wait()
        # self.move_camera(theta=-180 * DEGREES, phi=75 * DEGREES, zoom=0.8, run_time=3)
        # self.wait()
        # self.play(Create(entropy2), run_time=1.5)
        # self.wait(0.3)
        # self.play(x.animate.set_value(0.0), y.animate.set_value(1.0), run_time=2)
        # self.wait(0.3)
        # self.play(x.animate.set_value(0.0), y.animate.set_value(0.0), run_time=2)
        # self.move_camera(theta=-315 * DEGREES, phi=75 * DEGREES, zoom=0.8, run_time=3)
        # self.wait(0.3)
        # self.play(
        #     Create(entropy3),
        #     x.animate.set_value(1.0),
        #     y.animate.set_value(0.0),
        #     run_time=1.5
        # )
        # self.wait(0.3)
        # self.play(x.animate.set_value(0.0), y.animate.set_value(1.0), run_time=2)
        # self.wait(0.3)
        # self.play(x.animate.set_value(1.0), y.animate.set_value(0.0), run_time=2)
        # self.wait()
        # self.move_camera(theta=-420 * DEGREES, phi=75 * DEGREES, zoom=0.6, run_time=4)
        # self.begin_ambient_camera_rotation(rate=-0.1)
        # self.wait()
        self.play(Create(surface))
        self.play(
            Uncreate(entropy1),
            Uncreate(entropy2),
            Uncreate(entropy3)
        )
        # self.wait(0.3)
        # self.play(x.animate.set_value(0.3), y.animate.set_value(0.3), run_time=1)
        #
        # x_line = DashedLine(axes.c2p(x.get_value(), 0, 0), axes.c2p(x.get_value(), y.get_value(), 0), color=YELLOW)
        # y_line = DashedLine(axes.c2p(0, y.get_value(), 0), axes.c2p(x.get_value(), y.get_value(), 0), color=YELLOW)
        # z_line = DashedLine(axes.c2p(x.get_value(), y.get_value(), 0), axes.c2p(*self.func(x.get_value(), y.get_value())), color=YELLOW)
        #
        # x_line.add_updater(lambda l: l.put_start_and_end_on(
        #     axes.c2p(x.get_value(), 0, 0),
        #     axes.c2p(x.get_value(), y.get_value(), 0)
        # )
        #                    )
        #
        # y_line.add_updater(lambda l: l.put_start_and_end_on(
        #     axes.c2p(0, y.get_value(), 0),
        #     axes.c2p(x.get_value(), y.get_value(), 0)
        # )
        #                    )
        #
        # z_line.add_updater(lambda l: l.put_start_and_end_on(
        #     axes.c2p(x.get_value(), y.get_value(), 0),
        #     axes.coords_to_point(*self.func(x.get_value(), y.get_value()))
        # )
        #                    )
        #
        # self.play(Create(x_line), Create(y_line), FadeOut(xysphere))
        # self.play(Create(z_line))
        # self.play(Create(sphere))
        # self.wait(0.3)
        # self.play(x.animate.set_value(0.1), y.animate.set_value(0.1), run_time=1.5)
        # self.wait()
        # self.play(x.animate.set_value(0.6), y.animate.set_value(0.3), run_time=1.5)
        # self.wait()
        # self.play(x.animate.set_value(0.4), y.animate.set_value(0.5), run_time=1.5)
        # self.wait()


class working3(ThreeDScene):
    def imp_loss_surface(self, u, v):
        x = u
        y = v
        k = ((1 + x) / (1 + y)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        # hold_val = 0.5*x+0.5*y
        # z = np.sin(x) * np.cos(y)
        return np.array([ x, y, z ])

    def dollar_val_surface(self, u, v):
        if u + v > 3:
            v = v - (u + v - 3)

        # x = u
        # y = v
        k = ((1 + u) / (1 + v)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
        curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

    def dollar_val_surface_circle(self, u, v):
        if u ** 2 + v ** 2 < 0.5 ** 2:
            # v=np.sqrt(0.5 ** 2-u ** 2)
            # return np.array([ u, v, 0 ])
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1
        else:

            angle = angle_of_vector(np.array([ u, v, 0 ]))
            u = np.cos(angle) * 0.5
            v = np.sin(angle) * 0.5
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1
        return np.array([ u, v, curr_val ])

    def construct(self):
        resolution_fa = 20
        # self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0, zoom=1)
        axes = ThreeDAxes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33), z_range=(-1, 3, 1 / 3),
                          x_length=5, y_length=5, z_length=5)

        lab_x = axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x, lab_y, lab_z)

        # some_graph = axes.plot(lambda x: 2 * x, x_range=[ -0.99, 2 ]).set_stroke(width=10, color=RED).set_shade_in_3d(True)

        # some_graph.set_z_index_by_z_coordinate()
        # entropy1 = ParametricFunction(lambda t: axes.c2p(t, t, 0), color=BLUE, stroke_width=6, t_range=[ -0.99, 3 ]).set_shade_in_3d(True)

        def is_in_triangle(point, A, B, C, contain_border=False):
            COM = center_of_mass(A, B, C)
            if is_on_left_by_points(A, B, COM) and \
                    is_on_left_by_points(B, C, COM) and \
                    is_on_left_by_points(C, A, COM):
                if is_on_left_by_points(A, B, point, contain_border=contain_border) and \
                        is_on_left_by_points(B, C, point, contain_border=contain_border) and \
                        is_on_left_by_points(C, A, point, contain_border=contain_border):

                    return True
                else:
                    return False

            else:
                if is_on_right_by_points(A, B, point, contain_border=contain_border) and \
                        is_on_right_by_points(B, C, point, contain_border=contain_border) and \
                        is_on_right_by_points(C, A, point, contain_border=contain_border):
                    return True

                else:
                    return False

        a = [ 1, 1, 0 ]
        b = [ 2, 1.5, 0 ]
        c = [ 1, 2, 0 ]

        def dollar_val_surface_triangle(self, u, v):
            if is_in_triangle([ u, v, 0 ], a, b, c):
                k = ((1 + u) / (1 + v)) - 1
                z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
                hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
                curr_val = hold_val * (1 + z) - 1
            else:
                pass
            #
            #     # if
            #     angle = angle_of_vector(np.array([ u, v, 0 ]))
            #     u = np.cos(angle) * 0.5
            #     v = np.sin(angle) * 0.5
            #     k = ((1 + u) / (1 + v)) - 1
            #     z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            #     hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            #     curr_val = hold_val * (1 + z) - 1
            # return np.array([ u, v, curr_val ])

        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface_circle(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=30
        )

        val_graph.set_style(fill_opacity=0.5)
        val_graph.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        # self.add(some_graph, entropy1)

        my_graph = axes.plot(lambda x: x, x_range=[ -1, 5 ])
        three_d_wall = ThreeDVMobject().set_points_as_corners([ [ -0.5, -0.5, -0.5 ],
                                                                [ 2, -0.5, -0.5 ],
                                                                [ 2, -0.5, 1 ],
                                                                [ -0.5, -0.5, 1 ],
                                                                [ -0.5, -0.5, -0.5 ],
                                                                ]).set_fill(color=BLUE, opacity=1).set_shade_in_3d(True)

        self.add(axes, labs)
        self.add(val_graph, three_d_wall)
        self.set_camera_orientation(theta=-90 * DEGREES, phi=45 * DEGREES, zoom=1)

        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)


# with tempconfig({"quality": "low_quality", "preview": True, 'fps': 7}):
#     scene = working3()
#     #     # scene = working2()
#     #     # scene = working3()
#     #     # scene = working4()
#     #     # scene = working5()
#     scene.render()

