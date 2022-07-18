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
              , keep_pitch=True, update=0, speed=1.4)
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
        x = u
        y = v
        k = ((1 + x) / (1 + y)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + x) + 0.5 * (1 + y)
        curr_val = hold_val * (1 + z) - 1

        return np.array([ x, y, curr_val ])

    def construct(self):
        resolution_fa = 20
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0, zoom=1)
        axes = ThreeDAxes(x_range=(-0.99, 3, 0.11), y_range=(-0.99, 3, 0.11), z_range=(-1, 3, 0.1),
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

        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=50
            # checkerboard_colors=[C0177, C0134]
        )

        val_graph.set_style(fill_opacity=0.8)
        val_graph.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

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

        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, labs)
        # self.add(imp_loss_graph)
        # self.play(Create(val_graph),run_time=5)
        self.add(val_graph)
        # self.play(Create(my_graph))
        # self.play(my_graph.animate.set_color_by_gradient([RED,BLUE,GREEN]),run_time=3)
        # self.play(my_graph.animate.set_color(RED),run_time=3)
        # self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 5)
        # self.begin_ambient_camera_rotation(rate=0.2, about="theta",run_time=1)
        # self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        # self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES,gamma=0)

        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(phi=45 * DEGREES, about="phi", run_time=1)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(phi=90 * DEGREES, about="phi", run_time=1)
        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(phi=135 * DEGREES, about="phi", run_time=1)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=PI / 2, about="theta", run_time=2)


class working1(MovingCameraScene):
    # config.background_color = GRAY

    def construct(self):
        axes = Axes(x_range=[ 0, 10 ], y_range=[ 0, 20 ], x_length=14, y_length=7, )

        def my_func(x):
            if x < 5:
                y = np.log(x)
            elif 5 <= x <= 7:
                y = x
            else:
                y = -2 * x + 20
            return y

        graph = axes.plot(my_func, discontinuities=[ 5, 7 ], x_range=[ 0.1, 8 ], color=BLUE, dt=0.01)

        def my_rate(t: float, pause_ratio: float = 0.2) -> float:
            a = 1.0 / pause_ratio
            if t < 0.5 - pause_ratio / 2:
                return smooth(a * t)
            elif t < 0.5 + pause_ratio / 2:
                return 1
            else:
                return smooth(a - a * t)

        circle = Circle(radius=3)
        self.play(Create(circle), rate_func=there_and_back, run_time=8)
        # self.add(axes, graph)

        # x_tracker = ValueTracker(5)
        # z_tracker = ValueTracker(5.5)
        # a = 3
        # b = 7
        #
        # a_line = axes.get_lines_to_point(axes.c2p(a, graph.underlying_function(a)), color=RED)[ 1 ].set_stroke(width=5).set_z_index(2)
        # x_line = axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())), color=RED)[
        #     1 ].set_stroke(width=5).set_z_index(2)
        # b_line = axes.get_lines_to_point(axes.c2p(b, graph.underlying_function(b)), color=RED)[ 1 ].set_stroke(width=5).set_z_index(2)
        # z_line = axes.get_lines_to_point(axes.c2p(z_tracker.get_value(), graph.underlying_function(z_tracker.get_value())), color=RED)[
        #     1 ].set_stroke(width=5).set_z_index(2)
        #
        # x_line.add_updater(lambda mob: mob.become(
        #     axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())), color=RED)[
        #         1 ].set_stroke(width=5).set_z_index(2)))
        # z_line.add_updater(lambda mob: mob.become(
        #     axes.get_lines_to_point(axes.c2p(z_tracker.get_value(), graph.underlying_function(z_tracker.get_value())), color=RED)[
        #         1 ].set_stroke(width=5).set_z_index(2)))
        #
        # a2x_area = axes.get_area(graph, x_range=[ a, x_tracker.get_value() ], color=[ BLUE, WHITE ], opacity=0.5,
        #                          stroke_opacity=0).set_sheen_direction(R)
        # x2z_area = axes.get_area(graph, x_range=[ x_tracker.get_value(), z_tracker.get_value() ], color=YELLOW, opacity=1)
        # z2b_area = axes.get_area(graph, x_range=[ x_tracker.get_value(), b ], color=GRAY, stroke_opacity=0).set_sheen(10, R)
        #
        # a2x_area.add_updater(lambda mob: mob.become(
        #     axes.get_area(graph, x_range=[ a, x_tracker.get_value() ], color=[ BLUE, WHITE ], opacity=0.5).set_sheen_direction(R)))
        # x2z_area.add_updater(
        #     lambda mob: mob.become(axes.get_area(graph, x_range=[ x_tracker.get_value(), z_tracker.get_value() ], color=YELLOW, opacity=1)))
        # z2b_area.add_updater(lambda mob: mob.become(
        #     axes.get_area(graph, x_range=[ x_tracker.get_value(), b ], color=GRAY, stroke_opacity=0).set_sheen(10, R)))
        #
        # a2x_area_label = MathTex('F(x)').move_to(a2x_area)
        # a2x_area_label.add_updater(lambda mob: mob.move_to(a2x_area))
        #
        # a_label = Tex(rf'a\\{a:.1f}').scale(0.7).next_to(a_line, D)
        # x_label = Tex(rf'a\\{x_tracker.get_value():.1f}').scale(0.7).next_to(x_line, D)
        # z_label = Tex(rf'a\\{z_tracker.get_value():.1f}').scale(0.7).next_to(z_line, D)
        # b_label = Tex(rf'a\\{b:.1f}').scale(0.7).next_to(b_line, D)
        #
        # a_label.add_updater(lambda mob: mob.become(Tex(rf'a\\{a:.1f}').scale(0.7).next_to(a_line, D)))
        # x_label.add_updater(lambda mob: mob.become(Tex(rf'x\\{x_tracker.get_value():.1f}').scale(0.7).next_to(x_line, D)))
        # z_label.add_updater(lambda mob: mob.become(Tex(rf'z\\{z_tracker.get_value():.1f}').scale(0.7).next_to(z_line, D)))
        # b_label.add_updater(lambda mob: mob.become(Tex(rf'b\\{b:.1f}').scale(0.7).next_to(b_line, D)))
        #
        # self.add(axes[ 0 ], graph, a_line, x_line, z_line, b_line, a2x_area, x2z_area, z2b_area, a2x_area_label, a_label, x_label, z_label,
        #          b_label
        #          )
        #
        # self.play(x_tracker.animate.set_value(4))
        # self.play(x_tracker.animate.set_value(5))
        # self.play(z_tracker.animate.set_value(6))
        # self.play(x_tracker.animate.set_value(5.5))
        #


# class working1(MovingCameraScene):
#     # config.background_color = GRAY
#     def construct(self):
#         axes = Axes(x_range=[ -5, 5 ], y_range=[ -8, 8 ], x_length=6, y_length=9, tips=False, axis_config={'include_numbers': 1})
#         graph_1 = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ -3, 5 ]).set_z_index(3)
#         graph_2 = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=RED, x_range=[ -3, 5 ]).set_z_index(3)
#
#         x_tracker = ValueTracker(2)
#         a = 1
#         b = 3
#
#         graph_2_a_dot = Dot(axes.c2p(a, graph_2.underlying_function(a)), color=RED_E).set_z_index(2)
#         graph_2_x_dot = Dot(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
#                             color=RED_E).set_z_index(2)
#         graph_2_b_dot = Dot(axes.c2p(b, graph_2.underlying_function(b)), color=RED_E).set_z_index(2)
#         graph_1_a_dot = Dot(axes.c2p(a, graph_1.underlying_function(a)), color=BLUE_E).set_z_index(2)
#         graph_1_x_dot = Dot(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
#                             color=BLUE_E).set_z_index(2)
#         graph_1_b_dot = Dot(axes.c2p(b, graph_1.underlying_function(b)), color=BLUE_E).set_z_index(2)
#
#         graph_2_x_dot.add_updater(
#             lambda mob: mob.become(Dot(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
#                                        color=RED_E).set_z_index(2)))
#         graph_1_x_dot.add_updater(
#             lambda mob: mob.become(Dot(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
#                                        color=BLUE_E).set_z_index(2)))
#
#         graph_1_x_dot_label = Tex(rf'({x_tracker.get_value():.1f},{graph_1.underlying_function(x_tracker.get_value()):.1f})').next_to(
#             graph_1_x_dot, UL)
#         graph_2_x_dot_label = Tex(rf'({x_tracker.get_value():.1f},{graph_2.underlying_function(x_tracker.get_value()):.1f})').next_to(
#             graph_2_x_dot, DL)
#         graph_1_x_dot_label.add_updater(
#             lambda mob: mob.become(
#                 Tex(rf'({x_tracker.get_value():.1f},{graph_1.underlying_function(x_tracker.get_value()):.1f})').scale(0.7).next_to(
#                     graph_1_x_dot, UL, buff=0.05)))
#         graph_2_x_dot_label.add_updater(
#             lambda mob: mob.become(
#                 Tex(rf'({x_tracker.get_value():.1f},{graph_2.underlying_function(x_tracker.get_value()):.1f})').scale(0.7).next_to(
#                     graph_2_x_dot, DL, buff=0.05)
#             ))
#
#         graph_2_a_line = axes.get_lines_to_point(axes.c2p(a, graph_2.underlying_function(a)), color=RED).set_stroke(width=5).set_z_index(2)
#         graph_2_x_line = axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
#                                                  color=RED).set_stroke(width=5).set_z_index(2)
#         graph_2_b_line = axes.get_lines_to_point(axes.c2p(b, graph_2.underlying_function(b)), color=RED).set_stroke(width=5).set_z_index(2)
#
#         graph_1_a_line = axes.get_lines_to_point(axes.c2p(a, graph_1.underlying_function(a)), color=BLUE).set_stroke(width=5).set_z_index(2)
#         graph_1_x_line = axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
#                                                  color=BLUE).set_stroke(width=5).set_z_index(2)
#         graph_1_b_line = axes.get_lines_to_point(axes.c2p(b, graph_1.underlying_function(b)), color=BLUE).set_stroke(width=5).set_z_index(2)
#
#         graph_2_x_line.add_updater(lambda mob: mob.become(
#             axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
#                                     color=RED).set_stroke(width=5).set_z_index(2)))
#         graph_1_x_line.add_updater(lambda mob: mob.become(
#             axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
#                                     color=BLUE).set_stroke(width=5).set_z_index(2)))
#
#         graph_2_a2x_area = axes.get_area(graph_2, x_range=[ a, x_tracker.get_value() ], color=RED_A, opacity=0.3).set_sheen_direction(U)
#         graph_1_x2b_area = axes.get_area(graph_1, x_range=[ x_tracker.get_value(), b ], color=BLUE_A, opacity=0.3).set_sheen_direction(D)
#
#         graph_1_x2b_area.add_updater(lambda mob: mob.become(
#             axes.get_area(graph_1, x_range=[ x_tracker.get_value(), b ], color=BLUE_A, opacity=0.3).set_sheen_direction(D)))
#         graph_2_a2x_area.add_updater(lambda mob: mob.become(
#             axes.get_area(graph_2, x_range=[ a, x_tracker.get_value() ], color=RED_A, opacity=0.3).set_sheen_direction(U)))
#
#         graph_1_label = axes.get_graph_label(graph_1, label=MathTex(r'y=(x-1)^2+1'), x_val=b, direction=np.array([ 1., 0., 0. ]), buff=0.25,
#                                              color=BLUE_E, dot=False, dot_config=None)
#         graph_2_label = axes.get_graph_label(graph_2, label=MathTex(r'y=-(x-1)^2-1'), x_val=b, direction=np.array([ 1., 0., 0. ]),
#                                              buff=0.25, color=RED_E, dot=False, dot_config=None)
#         self.add(axes,
#                  graph_1,
#                  graph_2,
#                  graph_1_label,
#                  graph_2_label,
#                  graph_2_a_line,
#                  graph_2_x_line,
#                  graph_2_b_line,
#                  graph_1_a_line,
#                  graph_1_x_line,
#                  graph_1_b_line,
#                  graph_2_a_dot,
#                  graph_2_x_dot,
#                  graph_2_b_dot,
#                  graph_1_a_dot,
#                  graph_1_x_dot,
#                  graph_1_b_dot,
#                  graph_1_x2b_area,
#                  graph_2_a2x_area,
#                  graph_2_x_dot_label,
#                  graph_1_x_dot_label
#                  )
#
#         self.play(x_tracker.animate.set_value(2.5), run_time=3)
#         self.play(x_tracker.animate.set_value(1.5), run_time=3)
#         self.play(x_tracker.animate.set_value(2), run_time=3)
#
#         self.camera.frame.save_state()
#
#         path = VMobject()
#         graph_1_subpath = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
#         graph_1_subpath.reverse_points()
#         path.add_subpath(graph_1_subpath.get_all_points())
#         graph_2_subpath = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
#         dot_for_path = Dot(radius=0.3, color=GREEN).move_to(graph_1_b_dot)
#         path.add_points_as_corners([ axes.c2p(1, 1), axes.c2p(1, -1) ])
#         path.add_points_as_corners(graph_2_subpath.get_all_points())
#
#         self.play(self.camera.frame.animate.scale(0.5).move_to(dot_for_path))
#
#         self.play(MoveAlongPath(self.camera.frame, path), run_time=5)
#
#         self.play(Restore(self.camera.frame))
#
#         self.wait(10)
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

        self.play(new_tri.animate.move_to(get_moved_coor_based_submob(new_tri, new_tri.get_end_anchors()[ -1 ], [ -6, 4, 0 ])))
        self.play(new_tri.animate.move_to(get_moved_coor_based_submob(new_tri, new_tri.get_end_anchors()[ -2 ], fuck_line.get_end())))

        # new_fucking_temp_line = Line(start=midpoint(new_tri.get_end_anchors()[ -1 ],new_tri.get_end_anchors()[ -2 ], end=fuck_line.e)
        # self.play(MoveAlongPath(new_tri, fuck_line))

        self.wait(5)


class working1(MovingCameraScene):
    # config.background_color = GRAY

    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)

        # start_dot = Dot(color=RED).move_to([ -2, 2, 0 ])

        # line = Line(start=[ 3, -1, 0 ], end=[ 2, 2, 0 ])
        # line = Arrow(start=[ 2, 2, 0 ], end=[ 3, -1, 0 ])

        # tri_base_line = Arrow(color=BLUE, buff=0, start=[ 2, -1, 0 ], end=[ -2, -1, 0 ])
        # tri_base_line = Line(color=BLUE, buff=0, start=[ -2, -1, 0 ], end=[ 2, -1, 0 ])
        #
        # unit_v = line.get_unit_vector()
        # print(is_on_left(tri_base_line, np.array([0,-5,0])))

        tri = Triangle().scale(2.5)
        print(tri.get_end_anchors())

        dot = Dot(color=RED).move_to(center_of_mass(tri.get_end_anchors()))

        perp_line_left = get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 2 ] ]).set_stroke(
            color=YELLOW).set_z_index(3)
        perp_line_right = get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 1 ], tri.get_end_anchors()[ 2 ] ]).set_stroke(
            color=PINK).set_z_index(3)
        perp_line_bottom = get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 1 ] ]).set_stroke(
            color=GREEN).set_z_index(3)
        perp_line_left.add_updater(lambda line: line.become(
            get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 2 ] ]).set_stroke(
                color=YELLOW).set_z_index(3)))
        perp_line_right.add_updater(lambda line: line.become(
            get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 1 ], tri.get_end_anchors()[ 2 ] ]).set_stroke(
                color=PINK).set_z_index(3)))
        perp_line_bottom.add_updater(lambda line: line.become(
            get_perpendicular_line(dot.get_center(), [ tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 1 ] ]).set_stroke(
                color=GREEN).set_z_index(3)))

        vertical_green = Line(stroke_width=13, start=[ 4, -4, 0 ], end=[ 4, -4, 0 ] + U * get_line_length(perp_line_bottom))
        vertical_pink = Line(stroke_width=13, start=vertical_green.get_end(),
                             end=vertical_green.get_end() + U * get_line_length(perp_line_right))
        vertical_yellow = Line(stroke_width=13, start=vertical_green.get_end(), end=vertical_green.get_end() + U * perp_line_left.get_end())

        my_scaler = 2
        vertical_green.add_updater(lambda x: x.become(
            Line(color=GREEN, stroke_width=13, start=O, end=U * get_line_length(perp_line_bottom) * my_scaler).next_to([ 4, -4, 0 ], U,
                                                                                                                       buff=0)))
        vertical_pink.add_updater(
            lambda x: x.become(Line(color=PINK, stroke_width=13, start=O,
                                    end=U * get_line_length(perp_line_right) * my_scaler).next_to(vertical_green, U, buff=-0.1)))
        vertical_yellow.add_updater(
            lambda x: x.become(Line(color=YELLOW, stroke_width=13, start=O,
                                    end=U * get_line_length(perp_line_left) * my_scaler).next_to(vertical_pink, U, buff=-0.2)))

        self.add(tri, dot, perp_line_left, perp_line_right, perp_line_bottom, vertical_green, vertical_yellow, vertical_pink)

        self.play(dot.animate.shift(L * 1))
        self.play(dot.animate.shift(R * 1))
        self.play(dot.animate.shift(U * 1))
        self.play(dot.animate.shift(D * 1))
        self.play(dot.animate.shift(D * 0.5 + R * 0.5))

        yellow_tri = Polygon(dot.get_center(), dot.get_center() + L * get_line_length(perp_line_left) / np.cos(30 * DEGREES),
                             move_point_with_angle_and_length(dot.get_center(), 120 * DEGREES,
                                                              get_line_length(perp_line_left) / np.cos(30 * DEGREES)), color=BLUE,
                             fill_opacity=1).set_z_index(0.5)

        pink_tri = Polygon(dot.get_center(), dot.get_center() + R * get_line_length(perp_line_right) / np.cos(30 * DEGREES),
                           move_point_with_angle_and_length(dot.get_center(), 60 * DEGREES,
                                                            get_line_length(perp_line_right) / np.cos(30 * DEGREES)), color=BLUE,
                           fill_opacity=1).set_z_index(0.5)
        green_tri = Polygon(dot.get_center(),
                            dot.get_center() + np.array([ np.cos(-60 * DEGREES), np.sin(-60 * DEGREES), 0 ]) * get_line_length(
                                perp_line_bottom) / np.cos(30 * DEGREES),
                            move_point_with_angle_and_length(dot.get_center(), -120 * DEGREES,
                                                             get_line_length(perp_line_bottom) / np.cos(30 * DEGREES)), color=BLUE,
                            fill_opacity=1).set_z_index(0.5)

        perp_line_left.clear_updaters()
        perp_line_right.clear_updaters()
        perp_line_bottom.clear_updaters()

        self.add(yellow_tri, green_tri, pink_tri)

        yellow_tri.add(perp_line_left)
        pink_tri.add(perp_line_right)
        green_tri.add(perp_line_bottom)

        print('pink tri anchors', pink_tri.get_end_anchors())
        print('yellow tri anchors', yellow_tri.get_end_anchors())
        print('green tri anchors', green_tri.get_end_anchors())

        big_tri = Polygon(yellow_tri.get_end_anchors()[ 0 ], pink_tri.get_end_anchors()[ 0 ], tri.get_end_anchors()[ 2 ], color=GRAY,
                          fill_opacity=0.5, fill_color=GRAY).set_z_index(4)
        self.play(Rotate(yellow_tri, angle=-120 * DEGREES, about_point=center_of_mass(yellow_tri.get_end_anchors())))

        self.play(Create(big_tri))

        big_tri.add(yellow_tri, pink_tri)
        # self.play(Rotate(VGroup(big_tri, yellow_tri,pink_tri), angle=-120 * DEGREES, about_point=center_of_mass(big_tri.get_end_anchors())))
        self.play(Rotate(big_tri, angle=-120 * DEGREES, about_point=center_of_mass(big_tri.get_end_anchors())))

        self.wait(10)

        # poly = Polygon([ -2, 2, 0 ], [ 2, 2, 0 ], [ 2, -2, 0 ], [ -2, -2, 0 ], color=GREEN, fill_opacity=0.5)

        # print(poly.get_end_anchors())
