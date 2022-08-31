from manim.opengl import *

from custom_manim_utils.custom_mobs import *
# import manim.utils.space_ops
from manim import *
# from manimlib.imports import *

import random as rd
import numpy as np
# from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
# from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_mobs import *
from custom_manim_utils.custom_mobs import *
from manim_physics import *
from manim_gearbox import *
from pathlib import Path

from pprint import pprint

config.frame_width = 16
config.frame_height = 9


# background_color = W02


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

        price_of_usdt = Tex(r'Price of 1 ``USDT" is \\normally 1.01 \textasciitilde \  0.99 ``USD"').scale(1.5)

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
        icon = SVGMobject('svgs/coin/color/usdt.svg')
        icon.add_updater(
            lambda mob: mob.become(
                SVGMobject('svgs/coin/color/usdt.svg').scale(0.65).next_to(self.camera.frame.get_center(), DR, buff=0.5)))

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

        self.play(Uncreate(VGroup(supply_graph, demand_graph, ax, axis_labels, cross_dot, cross_dot_text, lines)))

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
                                 run_time=5))
        cant_wait_text = Tex("Can't wait!").rotate(-30 * DG).next_to(clock, UR, buff=-0.5)

        self.play(FadeIn(cant_wait_text),
                  run_time=1)

        self.play(FadeOut(VGroup(clock, cant_wait_text)), run_time=0.874)

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

        pair_rect = RoundedRectangle(corner_radius=0.5, height=7, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text)

        self.play(Create(pair, run_time=1))

        self.wait(1)

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

        # TODO 2.332 secs지금 보시는 건 마켓 주문입니다
        # TODO 0:00:56.854  ~  0:00:59.186
        # TODO 1.0secs pause
        # TODO 0:00:59.186  ~  0:01:00.186

        # TODO 6.717 secs매수 시장가 주문이면 빨간색 칸 중 가장 아래에 있는 유리한 가격 즉 싸게 팔아줄 판매자에게 구매를 합니다
        # TODO 0:01:00.186  ~  0:01:06.903
        # TODO 1.0secs pause
        # TODO 0:01:06.903  ~  0:01:07.903

        # TODO 6.693 secs매도 시장가 주문이면 초록색 칸 중 가장 위에 있는 유리한 가격 즉 비싸게 사줄 구매자에게 판매를 합니다
        # TODO 0:01:07.903  ~  0:01:14.596
        # TODO 1.0secs pause
        # TODO 0:01:14.596  ~  0:01:15.596

        negative_nums = rd.sample(range(-40, -25, 1), k=8)
        negative_nums.sort(reverse=True)
        # trade_occurred = Tex('A trade has occurred!').scale(0.8).to_corner(UR)
        market_occurred = Tex('Market order!').scale(1.8).next_to(pair_rect, R)

        # self.play(Write(trade_occurred))
        # self.play(Write(market_occurred), run_time=2.332)
        # self.wait(1)
        repetition = 8
        each_100_101 = [ 1, 1, 1, 1, 0, 0, 0, 0 ]
        each_change = [ -10, -20, -30, -40, -50, -60, -70, -75 ]

        order_book_runtime = 0.2
        # for i in range(repetition):
        #
        #     if_100_or_101 = each_100_101[ i ]
        #     change = each_change[ i ]
        #
        #     if if_100_or_101 == 0:
        #         # self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
        #         self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=0.6)
        #         curr_px_rect.set_color(RED)
        #         self.play(
        #             change_waiting_order_by_perc(self, order_book_long_table, 1, 2, change, order_book_runtime),
        #             run_time=order_book_runtime)
        #         # self.play(FadeIn(curr_px_number_100), FadeOut(curr_px_number_101), run_time=0.1)
        #         self.add(curr_px_number_100)
        #         self.remove(curr_px_number_101)
        #
        #         # self.remove(curr_px_number_101)
        #
        #         self.wait(1.1)
        #
        #         # self.play(Uncreate(trade_occurred), run_time=0.01)
        #
        #         # if i != 7:
        #         #     self.remove(curr_px_number_100)
        #         # else:
        #         curr_px_number = curr_px_number_100
        #
        #
        #     else:
        #         # self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
        #         self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=0.6)
        #
        #         # self.play(Uncreate(curr_px_number_100),Uncreate(curr_px_number_101),Create)
        #         curr_px_rect.set_color(GREEN)
        #         self.play(
        #             change_waiting_order_by_perc(self, order_book_shrt_table, 5, 2, change, order_book_runtime),
        #             run_time=order_book_runtime)
        #
        #         self.add(curr_px_number_101)
        #         self.remove(curr_px_number_100)
        #
        #         # self.play(Uncreate(trade_occurred), run_time=0.01)
        #         # self.play(Uncreate(curr_px_number_101))
        #         self.wait(1.1)
        #
        #         # if i != 7:
        #         #     self.remove(curr_px_number_101)
        #         # else:
        #         curr_px_number = curr_px_number_101

        # self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
        # self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=1)
        # self.play(Unwrite(market_occurred), run_time=2)

        # TODO 2.271 secs지금 보시는 건 리밋 주문입니다
        # TODO 0:01:15.596  ~  0:01:17.867
        # TODO 1.0secs pause
        # TODO 0:01:17.867  ~  0:01:18.867

        # TODO 7.55 secs매수 지정가 주문이면 초록색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 싼 가격에 구매하려고 대기합니다
        # TODO 0:01:18.867  ~  0:01:26.417
        # TODO 1.0secs pause
        # TODO 0:01:26.417  ~  0:01:27.417

        # TODO 7.683 secs매도 지정가 주문이면 빨간색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 비싼 가격에 판매하려고 대기합니다
        # TODO 0:01:27.417  ~  0:01:35.100
        # TODO 1.0secs pause
        # TODO 0:01:35.100  ~  0:01:36.100
        negative_nums = rd.sample(range(-40, -25, 1), k=8)
        negative_nums.sort(reverse=True)
        limit_occured = Tex('Limit order!').scale(1.8).next_to(pair_rect, R)

        self.play(Write(limit_occured), run_time=2.271)
        self.wait(1)

        order_book_runtime = 0.6

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_long_table, 5, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_long_table, 4, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_long_table, 3, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_long_table, 2, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_shrt_table, 1, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_shrt_table, 2, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_shrt_table, 3, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  change_waiting_order_by_perc(self, order_book_shrt_table, 4, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(0.4)

        px_not_moving = Tex(r'Price \\is not moving').scale(1.8).next_to(pair_rect, L)

        self.play(Create(px_not_moving))
        self.wait(9.614)

        # TODO 8.106 secs그러다가 누군가 기다림을 참지 못하고 시장가로 구매를 하면 호가창에 쌓여있던 물량이 시장가로 소화되면서 가격은 움직입니다
        # TODO 0:00:43.099  ~  0:00:51.205
        # TODO 1.0secs pause
        # TODO 0:00:51.205  ~  0:00:52.205

        curr_px_rect.set_color(GREEN)
        self.play(Transform(limit_occured, market_occurred),
                  FadeOut(px_not_moving),
                  change_waiting_order_by_perc(self, order_book_shrt_table, 5, 2, -30, order_book_runtime),
                  run_time=2)

        self.add(curr_px_number_101)
        self.remove(curr_px_number_100)

        self.wait(7.106)

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


class working2(MovingCameraScene):
    def construct(self):

        map = Rectangle(width=12, height=8)

        dot = Dot().move_to(map.point_from_proportion(0.33))

        UL_pos = map.get_corner(UL)
        DR_pos = map.get_corner(DR)

        velocity = 0.05

        x_range = [ UL_pos[ 0 ], DR_pos[ 0 ], DR_pos[ 0 ] - UL_pos[ 0 ] ]  # [min, max, len]
        y_range = [ DR_pos[ 1 ], UL_pos[ 1 ], UL_pos[ 1 ] - DR_pos[ 1 ] ]

        dots = VGroup()

        def get_pos_on_map(x_pos, y_pos, x_range, y_range):
            new_x_pos = x_range[ 2 ] * x_pos + x_range[ 0 ]
            new_y_pos = y_range[ 2 ] * y_pos + y_range[ 0 ]

            return [ new_x_pos, new_y_pos, 0 ]

        get_unit_v_by_angle(rd.uniform(0, TAU))
        for i in range(100):
            dots.add(Dot().move_to(get_pos_on_map(rd.random(), rd.random(), x_range, y_range)))

        self.play(Create(map))
        self.play(Create(dots))

        self.play(Flash(dots[ 0 ].get_center()))

        for i in range(50):
            anims = [ ]
            for dot in dots:
                anims.append(dot.animate.shift(get_unit_v_by_angle(rd.uniform(0, TAU)) * velocity))

            # self.play(*anims, rate_func=linear)

        self.wait(2)


class working2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # surface = OpenGLSurface(lambda u, v : (u,v, -1), u_range=[0,1], v_range=[0,1], resolution= (5,5)).set_opacity(opacity=0.5)
        # surface =Sphere(radius=1.5, opacity=0.5,resolution=(8,10))

        u_tkr = ValueTracker(4)
        v_tkr = ValueTracker(4)
        surface = redraw(
            lambda: Surface(lambda u, v: (u, v, -1), u_range=[ 0, u_tkr.get_value() ], v_range=[ 0, v_tkr.get_value() ], resolution=(5, 5)))
        self.add(*[ Dot3D().move_to(point) for point in surface.points ])
        self.add(axes)
        self.add(surface)

        self.add(index_labels(surface).shift(OUT * 1))

        self.move_camera(phi=30 * DG)

        torus = Torus(major_radius=3, minor_radius=1, u_range=(0, TAU), v_range=(0, TAU), resolution=(5, 5)).set_opacity(opacity=0.5)
        # self.play()
        # self.add(torus)
        surface.clear_updaters()

        surface[ 0 ].set_color(RED)
        torus[ 8 ].set_color(RED)

        # self.play(u_tkr.animate.set_value(1))
        self.play(Transform(surface[ 0 ], torus[ 8 ]))

        self.wait(5)


class working2(ThreeDScene):
    def construct(self):
        # nxm의 사각형이라면 일단 5x3이라고 하고

        point_list = np.array(
            [ [ [ 0, 0, 0 ], [ 1, 0, 0 ] ],
              [ [ 0, 1, 0 ], [ 1, 1, 0 ] ],
              [ [ 0, 2, 0 ], [ 1, 2, 0 ] ] ]
        )

        print(point_list.shape)

        n = point_list.shape[ 1 ]
        m = point_list.shape[ 0 ]

        # n cols
        # m rows
        for row in range(0, m):
            for col in range(0, n):
                point_list[ row, col ]

                sqDL = point_list[ row, col ]
                sqDR = point_list[ row, col + 1 ]
                sqUR = point_list[ row + 1, col + 1 ]
                sqUL = point_list[ row + 1, col ]

        #

        #
        # self.add(NumberPlane())
        # surface = Surface(lambda u, v :(u,v,0), u_range=[-2,2],v_range=[-2,2], resolution=(10,10))
        #
        # torus = Torus(resolution=(10,10))
        #
        # self.play(DrawBorderThenFill(surface[0]))
        # # self.add(index_labels(torus))
        # # self.play(DrawBorderThenFill(torus[0]))
        #
        # self.add(index_labels(surface[0]))
        # print(surface[0].get_start_anchors())

        class MySurfaceByPoints(VGroup, metaclass=ConvertToOpenGL):

            def __init__(
                    self,
                    vertex_list: Sequence = [ [ 0, 0 ],
                                              [ 1, 0 ],
                                              [ 1, 1 ],
                                              [ 0, 1 ] ],
                    u_range: Sequence[ float ] = [ 0, 1 ],
                    v_range: Sequence[ float ] = [ 0, 1 ],
                    resolution: Sequence[ int ] = 32,
                    surface_piece_config: dict = {},
                    fill_color: Color = BLUE_D,
                    fill_opacity: float = 1.0,
                    checkerboard_colors: Sequence[ Color ] = [ BLUE_D, BLUE_E ],
                    stroke_color: Color = LIGHT_GREY,
                    stroke_width: float = 0.5,
                    should_make_jagged: bool = False,
                    pre_function_handle_to_anchor_scale_factor: float = 0.00001,
                    **kwargs,
            ) -> None:
                self.u_range = u_range
                self.v_range = v_range
                super().__init__(**kwargs)
                self.resolution = resolution
                self.surface_piece_config = surface_piece_config
                self.fill_color = fill_color
                self.fill_opacity = fill_opacity
                self.checkerboard_colors = checkerboard_colors
                self.stroke_color = stroke_color
                self.stroke_width = stroke_width
                self.should_make_jagged = should_make_jagged
                self.pre_function_handle_to_anchor_scale_factor = (
                    pre_function_handle_to_anchor_scale_factor
                )
                # self.func = func
                self._setup_in_uv_space()
                # self.apply_function(lambda p: func(p[ 0 ], p[ 1 ]))
                if self.should_make_jagged:
                    self.make_jagged()

            def _get_u_values_and_v_values(self):
                res = tuplify(self.resolution)
                if len(res) == 1:
                    u_res = v_res = res[ 0 ]
                else:
                    u_res, v_res = res

                u_values = np.linspace(*self.u_range, u_res + 1)
                v_values = np.linspace(*self.v_range, v_res + 1)

                return u_values, v_values

            def _setup_in_uv_space(self):
                u_values, v_values = self._get_u_values_and_v_values()
                faces = VGroup()
                for i in range(len(u_values) - 1):
                    for j in range(len(v_values) - 1):
                        u1, u2 = u_values[ i: i + 2 ]
                        v1, v2 = v_values[ j: j + 2 ]
                        face = ThreeDVMobject()
                        face.set_points_as_corners(
                            [
                                [ u1, v1, 0 ],
                                [ u2, v1, 0 ],
                                [ u2, v2, 0 ],
                                [ u1, v2, 0 ],
                                [ u1, v1, 0 ],
                            ],
                        )
                        faces.add(face)
                        face.u_index = i
                        face.v_index = j
                        face.u1 = u1
                        face.u2 = u2
                        face.v1 = v1
                        face.v2 = v2
                faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)
                faces.set_stroke(
                    color=self.stroke_color,
                    width=self.stroke_width,
                    opacity=self.stroke_opacity,
                )
                self.add(*faces)
                if self.checkerboard_colors:
                    self.set_fill_by_checkerboard(*self.checkerboard_colors)

            def set_fill_by_checkerboard(self, *colors, opacity=None):
                n_colors = len(colors)
                for face in self:
                    c_index = (face.u_index + face.v_index) % n_colors
                    face.set_fill(colors[ c_index ], opacity=opacity)
                return self

        self.wait(3)

        # self.play(Transform(surface[0], torus[4].set_opacity(opacity=0.5)))

        # self.interactive_embed()


class working2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        axes[ 0 ].set_color(RED)
        axes[ 1 ].set_color(GREEN)
        axes[ 2 ].set_color(BLUE)

        # self.add(axes)

        # self.set_camera_orientation(phi =45*DG,theta=-80*DG, )
        # self.set_camera_orientation(zoom=0.6 )
        self.set_camera_orientation(phi=45 * DG, theta=-80 * DG, zoom=0.6)
        # self.move_camera(theta=45*DG)

        array = [ ]

        u_min = -10
        u_max = 10
        v_min = -4
        v_max = 4
        for v in np.linspace(v_min, v_max, 10):
            row = [ ]
            for u in np.linspace(u_min, u_max, 20):
                row.append([ u, v, 0 ])
            array.append(row)

        point_list = np.array(array)
        # print(point_list)

        n = point_list.shape[ 1 ]
        m = point_list.shape[ 0 ]

        points = VGroup()
        points_without_rc = VGroup()
        faces = VGroup()
        faces_without_rc = VGroup()

        for row in range(0, m):
            row_group = VGroup()
            for col in range(0, n):
                coor = point_list[ row, col ]

                dot = Dot().move_to(coor)
                dot.r = row
                dot.c = col
                row_group.add(dot)
                points_without_rc.add(dot)

            points.add(row_group)
            # points.add(Dot3D().move_to(coor))

        # self.add(points)

        for row in range(0, m - 1):
            row_group = VGroup()
            for col in range(0, n - 1):
                sqDL = points[ row ][ col ]
                sqDR = points[ row ][ col + 1 ]
                sqUR = points[ row + 1 ][ col + 1 ]
                sqUL = points[ row + 1 ][ col ]

                globals()[ f'{row}_{col}' ] = points[ row ][ col ]
                globals()[ f'{row}_{col + 1}' ] = points[ row ][ col + 1 ]
                globals()[ f'{row + 1}_{col + 1}' ] = points[ row + 1 ][ col + 1 ]
                globals()[ f'{row + 1}_{col}' ] = points[ row + 1 ][ col ]

                face = ThreeDVMobject().set_points_as_corners([ sqDL.get_center(), sqDR.get_center(), sqUR.get_center(),
                                                                sqUL.get_center(),
                                                                sqDL.get_center() ]).set_style(fill_color=RED, fill_opacity=0.4,
                                                                                               stroke_width=0.5, stroke_color=GRAY,
                                                                                               stroke_opacity=0.5)

                face.sqDL = points[ row ][ col ]
                face.sqDR = points[ row ][ col + 1 ]
                face.sqUR = points[ row + 1 ][ col + 1 ]
                face.sqUL = points[ row + 1 ][ col ]

                face.r = row
                face.c = col

                row_group.add(face)

                # print(face.sqDL)

                def face_func(mob):
                    updated_mob = mob.set_points_as_corners(
                        [ mob.sqDL.get_center(), mob.sqDR.get_center(), mob.sqUR.get_center(), mob.sqUL.get_center(),
                          mob.sqDL.get_center() ])

                    return updated_mob

                face.add_updater(face_func)
                faces_without_rc.add(face)
            faces.add(row_group)

        self.add(faces)
        # self.add(index_labels(faces))
        # self.add(index_labels(faces[0]))
        self.wait(1)

        coloring_anims = [ ]
        for i in range(len(faces)):
            coloring_anims.append(
                faces[ i ].animate.set_color(Color(hue=i / len(faces), saturation=1, luminance=0.6)))

        faces[ 0 ].set_style(fill_color=BLUE, fill_opacity=0.7)
        faces[ -1 ].set_style(fill_color=GREEN, fill_opacity=0.7)

        for face in faces_without_rc:
            if face.c == 0:
                face.set_style(fill_color=YELLOW, fill_opacity=0.7)
            if face.c == 18:
                face.set_style(fill_color=ORANGE, fill_opacity=0.7)

        points_without_rc.set_opacity(opacity=0)

        roll_up_anims = [ ]
        for point in points_without_rc:
            x = point.get_center()[ 0 ]
            y = point.get_center()[ 1 ]
            z = point.get_center()[ 2 ]

            new_x = x
            new_y = np.cos(270 * DG + 90 / ((v_max - v_min) / 4) * y * DG) * (v_max - v_min) / 2 / PI
            new_z = np.sin(270 * DG + 90 / ((v_max - v_min) / 4) * y * DG) * (v_max - v_min) / 2 / PI

            new_coor = np.array([ new_x, new_y, new_z ])

            roll_up_anims.append(point.animate.move_to(new_coor))

            # for opengl
            # point.move_to(new_coor)

        self.play(*roll_up_anims, run_time=3)
        print(points_without_rc[ 0 ].get_center())

        round_up_anims = [ ]

        for point in points_without_rc:
            x = point.get_center()[ 0 ]
            y = point.get_center()[ 1 ]
            z = point.get_center()[ 2 ]

            new_x = np.cos(270 * DG + 90 / ((u_max - u_min) / 4) * x * DG) * (-2 / PI * y + 6 / PI)
            new_y = np.sin(270 * DG + 90 / ((u_max - u_min) / 4) * x * DG) * (-2 / PI * y + 6 / PI)
            new_z = z

            new_coor = np.array([ new_x, new_y, new_z ])

            round_up_anims.append(point.animate.move_to(new_coor))
            # for opengl
            # point.move_to(new_coor)

        self.play(*round_up_anims, run_time=3)

        self.wait(1)

        self.move_camera(phi=90 * DG, theta=-80 * DG, zoom=1.2)
        self.wait(1)
        # self.set_camera_orientation(phi =90*DG,theta=-80*DG)

        self.begin_ambient_camera_rotation(rate=0.3)
        self.move_camera(phi=0, run_time=10, rate_func=linear)

        self.wait(5)


class working2(ThreeDScene):
    def construct(self):
        self.add(NumberPlane())
        func = lambda pos: (pos[ 0 ] * UR + pos[ 1 ] * LEFT) - pos

        self.set_camera_orientation(phi=45*DG, theta=45*DG)
        plane = VMobject().set_points_as_corners(
            [ (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 0) ]).set_style(fill_opacity=0.5, fill_color=RED)
        self.add(plane)
        def stream_func(pos):
            x = pos[ 0 ]
            y = pos[ 1 ]
            z = pos[ 2 ]
            if x > 0:
                return (pos[ 0 ] * UR + pos[ 1 ] * LEFT) - pos

            else:
                return np.sin(pos[ 0 ] / 2) * UR + np.cos(pos[ 1 ] / 2) * LEFT

        def DE(pos):
            v = 2
            c = 3

            p=pos[0]
            q=pos[1]
            r=pos[2]
            D = p
            H = q
            R = 1 - p - q

            D_avg_payoff = v * (1 - q) / 2
            H_avg_payoff = p * v + (1 - p) * (v - c) / 2
            R_avg_payoff = (q * (v - c) + (1 - q) * v) / 2
            avg_payoff = p * D_avg_payoff + q * H_avg_payoff + (1 - p - q) * R_avg_payoff

            delta_D = D * (D_avg_payoff - avg_payoff)
            delta_H = H * (H_avg_payoff - avg_payoff)
            delta_R = R * (R_avg_payoff - avg_payoff)

            new_D = D + delta_D
            new_H = H + delta_H
            new_R = R + delta_R

            return np.array([new_D, new_H, new_R])

        stream_lines = StreamLines(
            stream_func, stroke_width=1, max_anchors_per_line=5, virtual_time=1, color=BLUE,
            x_range=[0,1],
            y_range=[0,1],
            z_range=[0,1],
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=0.5, time_width=10)
        self.wait(1)
        self.play(stream_lines.end_animation())

#
#
class working2(ThreeDScene):
    # config.background_color = '#090A3B'
    def construct(self):
        sat=1
        lum=0.5
        plus= 0.05

        circle_1 =Circle(stroke_opacity=0,fill_opacity = 1, fill_color =Color(hsl=(0+plus,sat,lum)))
        circle_2 =Circle(stroke_opacity=0,fill_opacity = 1, fill_color =Color(hsl=(1/3+plus,sat,lum)))
        circle_3 =Circle(stroke_opacity=0,fill_opacity = 1, fill_color =Color(hsl=(1/6+plus,sat,lum)))
        circle_4 =Circle(stroke_opacity=0,fill_opacity = 1, fill_color =Color(hsl=(2/3+plus,sat,lum)))

        circles = VGroup(circle_1,circle_2,circle_3,circle_4).arrange_in_grid(2,2)

        self.add(circles)
class working2(ThreeDScene):

    def construct(self):
        wind = SVGMobject('svg/wind.svg')

        self.play(FadeIn(wind, shift=DL), rate_func=smooth,run_time=0.5)
        self.play(FadeOut(wind, shift=DL), rate_func=smooth,run_time=1.5)




        self.wait(5)

        # self.wait(5)
# from manimlib.imports import *
