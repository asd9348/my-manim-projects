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

        speak(self, title='Scene2', txt=
        '페어를 표시할 때는 보통 슬래시나 대시를 사용하거나 그냥 티커를 붙여서 표시하기도 합니다#1'
              , keep_pitch=True, update=True, speed=1.4)





class working2(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=

        '이제 에이와 비는 본격적으로 주문을 넣기 시작합니다#1'
        '거래소에서 주문을 넣는 것에 대해서도 알고 가야할 게 있습니다#1'
        '거래소에서 넣는 주문은 주문가격에 따라 크게 두 가지가 있습니다#1'
        '리밋 주문과 마켓 주문이고 한국어로는 지정가 주문 시장가 주문이라고 부릅니다#1'
        '이전에 들어본 스톱오더 트레일링오더 같은 것은 이 주문 종류에 추가 기능을 넣은 것입니다#1'
        '지정가 주문은 말그대로 주문가격을 지정해놓는 주문이고 시장가 주문은 우리가 회를 먹을 때 싯가라고 부르듯이 그냥 그 자리에서 구할 수 있는대로 현재가격으로 즉시 체결하는 주문입니다#1'

        '리밋 주문은 일반적으로 알고 있듯이 가격을 지정해서 그 가격에 거래하고 싶은 상대측이 나타나면 거래가 체결되는 주문입니다#1'
        '마켓 주문은 원하는 주문량을 입력하면 현재 나와있는 매물 중 가장 유리한 가격대로 주문량이 모두 충족될 때까지 거래를 합니다#1'
        '마켓 주문은 주문을 넣는 순간 돌이킬 수 없이 바로 체결되고 리밋 주문은 일반적으로 현재가격보다 더 유리한 가격에 걸어놓기에 기다려야 합니다#1'
        '지금 보시는 건 마켓 주문입니다#1'
        '매수 시장가 주문이면 빨간색 칸 중 가장 아래에 있는 유리한 가격 즉 싸게 팔아줄 판매자에게 구매를 합니다#1'
        '매도 시장가 주문이면 초록색 칸 중 가장 위에 있는 유리한 가격 즉 비싸게 사줄 구매자에게 판매를 합니다#1'
        '지금 보시는 건 마켓 주문입니다#1'
        '매수 지정가 주문이면 초록색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 싼 가격에 구매하려고 대기합니다#1'
        '매도 지정가 주문이면 빨간색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 비싼 가격에 판매하려고 대기합니다#1'
              , keep_pitch=True, update=0, speed=1.4)

        order = Tex('Order').scale(2)
        self.play(Create(order))

        self.wait(3)
        # self.play(Uncreate(order))

        limit_order_text = Tex(r'Limit Order\\지정가 주문').shift(L * 4)
        market_order_text = Tex(r'Market Order\\시장가 주문').shift(R * 4)

        order_type = VGroup(limit_order_text, market_order_text)
        self.play(ReplacementTransform(order, order_type))

        self.wait(1)





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
        graph = axes.plot(lambda x: (x - 5) ** 3 - 4 * (x - 5) + 15, color=BLUE, x_range=[ 2.5, 7.5 ]).set_z_index(3)

        x_tracker = ValueTracker(5)
        z_tracker = ValueTracker(5.5)
        a = 3
        b = 7

        a_line = axes.get_lines_to_point(axes.c2p(a, graph.underlying_function(a)), color=RED)[ 1 ].set_stroke(width=5).set_z_index(2)
        x_line = axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())), color=RED)[
            1 ].set_stroke(width=5).set_z_index(2)
        b_line = axes.get_lines_to_point(axes.c2p(b, graph.underlying_function(b)), color=RED)[ 1 ].set_stroke(width=5).set_z_index(2)
        z_line = axes.get_lines_to_point(axes.c2p(z_tracker.get_value(), graph.underlying_function(z_tracker.get_value())), color=RED)[
            1 ].set_stroke(width=5).set_z_index(2)

        x_line.add_updater(lambda mob: mob.become(
            axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())), color=RED)[
                1 ].set_stroke(width=5).set_z_index(2)))
        z_line.add_updater(lambda mob: mob.become(
            axes.get_lines_to_point(axes.c2p(z_tracker.get_value(), graph.underlying_function(z_tracker.get_value())), color=RED)[
                1 ].set_stroke(width=5).set_z_index(2)))

        a2x_area = axes.get_area(graph, x_range=[ a, x_tracker.get_value() ], color=[ BLUE, WHITE ], opacity=0.5,
                                 stroke_opacity=0).set_sheen_direction(R)
        x2z_area = axes.get_area(graph, x_range=[ x_tracker.get_value(), z_tracker.get_value() ], color=YELLOW, opacity=1)
        z2b_area = axes.get_area(graph, x_range=[ x_tracker.get_value(), b ], color=GRAY, stroke_opacity=0).set_sheen(10, R)

        a2x_area.add_updater(lambda mob: mob.become(
            axes.get_area(graph, x_range=[ a, x_tracker.get_value() ], color=[ BLUE, WHITE ], opacity=0.5).set_sheen_direction(R)))
        x2z_area.add_updater(
            lambda mob: mob.become(axes.get_area(graph, x_range=[ x_tracker.get_value(), z_tracker.get_value() ], color=YELLOW, opacity=1)))
        z2b_area.add_updater(lambda mob: mob.become(
            axes.get_area(graph, x_range=[ x_tracker.get_value(), b ], color=GRAY, stroke_opacity=0).set_sheen(10, R)))

        a2x_area_label = MathTex('F(x)').move_to(a2x_area)
        a2x_area_label.add_updater(lambda mob: mob.move_to(a2x_area))

        a_label = Tex(rf'a\\{a:.1f}').scale(0.7).next_to(a_line, D)
        x_label = Tex(rf'a\\{x_tracker.get_value():.1f}').scale(0.7).next_to(x_line, D)
        z_label = Tex(rf'a\\{z_tracker.get_value():.1f}').scale(0.7).next_to(z_line, D)
        b_label = Tex(rf'a\\{b:.1f}').scale(0.7).next_to(b_line, D)

        a_label.add_updater(lambda mob: mob.become(Tex(rf'a\\{a:.1f}').scale(0.7).next_to(a_line, D)))
        x_label.add_updater(lambda mob: mob.become(Tex(rf'x\\{x_tracker.get_value():.1f}').scale(0.7).next_to(x_line, D)))
        z_label.add_updater(lambda mob: mob.become(Tex(rf'z\\{z_tracker.get_value():.1f}').scale(0.7).next_to(z_line, D)))
        b_label.add_updater(lambda mob: mob.become(Tex(rf'b\\{b:.1f}').scale(0.7).next_to(b_line, D)))

        self.add(axes[ 0 ], graph, a_line, x_line, z_line, b_line, a2x_area, x2z_area, z2b_area, a2x_area_label, a_label, x_label, z_label,
                 b_label
                 )

        self.play(x_tracker.animate.set_value(4))
        self.play(x_tracker.animate.set_value(5))
        self.play(z_tracker.animate.set_value(6))
        self.play(x_tracker.animate.set_value(5.5))

        self.wait(10)


class working1(MovingCameraScene):
    # config.background_color = GRAY
    def construct(self):
        axes = Axes(x_range=[ -5, 5 ], y_range=[ -8, 8 ], x_length=6, y_length=9, tips=False, axis_config={'include_numbers': 1})
        graph_1 = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ -3, 5 ]).set_z_index(3)
        graph_2 = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=RED, x_range=[ -3, 5 ]).set_z_index(3)

        x_tracker = ValueTracker(2)
        a = 1
        b = 3

        graph_2_a_dot = Dot(axes.c2p(a, graph_2.underlying_function(a)), color=RED_E).set_z_index(2)
        graph_2_x_dot = Dot(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
                            color=RED_E).set_z_index(2)
        graph_2_b_dot = Dot(axes.c2p(b, graph_2.underlying_function(b)), color=RED_E).set_z_index(2)
        graph_1_a_dot = Dot(axes.c2p(a, graph_1.underlying_function(a)), color=BLUE_E).set_z_index(2)
        graph_1_x_dot = Dot(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
                            color=BLUE_E).set_z_index(2)
        graph_1_b_dot = Dot(axes.c2p(b, graph_1.underlying_function(b)), color=BLUE_E).set_z_index(2)

        graph_2_x_dot.add_updater(
            lambda mob: mob.become(Dot(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
                                       color=RED_E).set_z_index(2)))
        graph_1_x_dot.add_updater(
            lambda mob: mob.become(Dot(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
                                       color=BLUE_E).set_z_index(2)))

        graph_1_x_dot_label = Tex(rf'({x_tracker.get_value():.1f},{graph_1.underlying_function(x_tracker.get_value()):.1f})').next_to(
            graph_1_x_dot, UL)
        graph_2_x_dot_label = Tex(rf'({x_tracker.get_value():.1f},{graph_2.underlying_function(x_tracker.get_value()):.1f})').next_to(
            graph_2_x_dot, DL)
        graph_1_x_dot_label.add_updater(
            lambda mob: mob.become(
                Tex(rf'({x_tracker.get_value():.1f},{graph_1.underlying_function(x_tracker.get_value()):.1f})').scale(0.7).next_to(
                    graph_1_x_dot, UL, buff=0.05)))
        graph_2_x_dot_label.add_updater(
            lambda mob: mob.become(
                Tex(rf'({x_tracker.get_value():.1f},{graph_2.underlying_function(x_tracker.get_value()):.1f})').scale(0.7).next_to(
                    graph_2_x_dot, DL, buff=0.05)
            ))

        graph_2_a_line = axes.get_lines_to_point(axes.c2p(a, graph_2.underlying_function(a)), color=RED).set_stroke(width=5).set_z_index(2)
        graph_2_x_line = axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
                                                 color=RED).set_stroke(width=5).set_z_index(2)
        graph_2_b_line = axes.get_lines_to_point(axes.c2p(b, graph_2.underlying_function(b)), color=RED).set_stroke(width=5).set_z_index(2)

        graph_1_a_line = axes.get_lines_to_point(axes.c2p(a, graph_1.underlying_function(a)), color=BLUE).set_stroke(width=5).set_z_index(2)
        graph_1_x_line = axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
                                                 color=BLUE).set_stroke(width=5).set_z_index(2)
        graph_1_b_line = axes.get_lines_to_point(axes.c2p(b, graph_1.underlying_function(b)), color=BLUE).set_stroke(width=5).set_z_index(2)

        graph_2_x_line.add_updater(lambda mob: mob.become(
            axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_2.underlying_function(x_tracker.get_value())),
                                    color=RED).set_stroke(width=5).set_z_index(2)))
        graph_1_x_line.add_updater(lambda mob: mob.become(
            axes.get_lines_to_point(axes.c2p(x_tracker.get_value(), graph_1.underlying_function(x_tracker.get_value())),
                                    color=BLUE).set_stroke(width=5).set_z_index(2)))

        graph_2_a2x_area = axes.get_area(graph_2, x_range=[ a, x_tracker.get_value() ], color=RED_A, opacity=0.3).set_sheen_direction(U)
        graph_1_x2b_area = axes.get_area(graph_1, x_range=[ x_tracker.get_value(), b ], color=BLUE_A, opacity=0.3).set_sheen_direction(D)

        graph_1_x2b_area.add_updater(lambda mob: mob.become(
            axes.get_area(graph_1, x_range=[ x_tracker.get_value(), b ], color=BLUE_A, opacity=0.3).set_sheen_direction(D)))
        graph_2_a2x_area.add_updater(lambda mob: mob.become(
            axes.get_area(graph_2, x_range=[ a, x_tracker.get_value() ], color=RED_A, opacity=0.3).set_sheen_direction(U)))

        graph_1_label = axes.get_graph_label(graph_1, label=MathTex(r'y=(x-1)^2+1'), x_val=b, direction=np.array([ 1., 0., 0. ]), buff=0.25,
                                             color=BLUE_E, dot=False, dot_config=None)
        graph_2_label = axes.get_graph_label(graph_2, label=MathTex(r'y=-(x-1)^2-1'), x_val=b, direction=np.array([ 1., 0., 0. ]),
                                             buff=0.25, color=RED_E, dot=False, dot_config=None)
        self.add(axes,
                 graph_1,
                 graph_2,
                 graph_1_label,
                 graph_2_label,
                 graph_2_a_line,
                 graph_2_x_line,
                 graph_2_b_line,
                 graph_1_a_line,
                 graph_1_x_line,
                 graph_1_b_line,
                 graph_2_a_dot,
                 graph_2_x_dot,
                 graph_2_b_dot,
                 graph_1_a_dot,
                 graph_1_x_dot,
                 graph_1_b_dot,
                 graph_1_x2b_area,
                 graph_2_a2x_area,
                 graph_2_x_dot_label,
                 graph_1_x_dot_label
                 )

        # self.play(x_tracker.animate.set_value(2.5), run_time=3)
        # self.play(x_tracker.animate.set_value(1.5), run_time=3)
        # self.play(x_tracker.animate.set_value(2), run_time=3)
        #
        self.camera.frame.save_state()

        path = VMobject()
        graph_1_subpath = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        graph_1_subpath.reverse_points()
        path.add_subpath(graph_1_subpath.get_all_points())
        graph_2_subpath = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        dot_for_path = Dot(radius=0.3, color=GREEN).move_to(graph_1_b_dot)
        path.add_points_as_corners([ axes.c2p(1, 1), axes.c2p(1, -1) ])
        path.add_points_as_corners(graph_2_subpath.get_all_points())


        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_for_path))

        self.play(MoveAlongPath(self.camera.frame, path), run_time=5)

        self.play(Restore(self.camera.frame))

        self.wait(10)
