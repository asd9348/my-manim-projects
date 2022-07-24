from manim.opengl import *

from custom_manim_utils.custom_mobs import *
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
from pathlib import Path

from pprint import pprint

config.frame_width = 16
config.frame_height = 9


class Sphere_3D(ThreeDScene):
    """3D 스피어 생성과 카메라 회전"""
    def construct(self):
        axes = ThreeDAxes()
        test_mob = ThreeDVMobjectFromPLY('sphere.ply',
                                        fill_color=RED, fill_opacity=0.5,
                                        stroke_width=1, stroke_opacity=0.5, scaler=3).scale_to_fit_width(4).move_to(axes.c2p(0, 0, 0))
        test_mob.set_fill_by_checkerboard(BLUE)
        self.play(Create(axes))
        self.play(Create(test_mob),run_time=5)
        self.move_camera(phi=45*DG, about="phi", run_time=2)
        self.move_camera(theta=2*PI, about="theta", run_time=5)


class ImpLossMovingDot(ThreeDScene):
    """ 반영구 손실 공간에서 3차원으로 움직이는 점
    xyz 보조선 공간템플릿, 엑스와이가 뒤쪽으로 모임, 제트 축은 왼쪽 """

    def dollar_val_surface(self, u, v):
        if u + v > 3:
            v = v - (u + v - 3)

        k = ((1 + u) / (1 + v)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
        curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 3, 1 ],
                          y_range=[ 0, 3, 1 ],
                          z_range=[ 0, 3, 1 ],
                          x_length=8,
                          y_length=8,
                          z_length=8,
                          tips=False,
                          axis_config={'include_numbers': True, 'include_ticks': True, "line_to_number_buff": 0.7},
                          x_axis_config={"label_direction": D},
                          y_axis_config={"label_direction": L},
                          z_axis_config={"label_direction": U}
                          )

        # curr_val_text.to_edge(UR).shift(L*1)
        x_tkr = ValueTracker(0)
        y_tkr = ValueTracker(0)
        # self.add(profit,curr_profit, inv_text)

        # self.add(index_labels(curr_profit))
        # self.add_fixed_orientation_mobjects(profit,curr_profit, inv_text)

        # 실제로 사용하게될 ㅌ제트축을 카피해서 마지막 서브 모브젝트로 넣어놓고 원하는 위치로 이동시키기, 원래 제트축은 움직이지 않았음
        axes.add(axes[ 2 ].copy())
        VGroup(axes[ 3 ]).move_to(get_compensated_coor(axes[ 3 ], axes.c2p(0, 0, 0), axes[ 0 ].get_end()))

        # 보조선 작성 루틴 , 틱 위치 개수하고 잘 보기
        x_range, y_range, z_range = axes.x_range, axes.y_range, axes.z_range

        x_tick_pos = np.arange(x_range[ 0 ], x_range[ 1 ] + 0.01, x_range[ 2 ])
        y_tick_pos = np.arange(y_range[ 0 ], y_range[ 1 ] + 0.01, y_range[ 2 ])
        z_tick_pos = np.arange(z_range[ 0 ], z_range[ 1 ] + 0.01, z_range[ 2 ])

        x_axis_aux_line, y_axis_aux_line, z_axis_aux_line = VGroup(), VGroup(), VGroup()

        for x, y, z in zip(x_tick_pos[ 1: ], y_tick_pos[ 1: ], z_tick_pos[ 1: ], ):
            z_axis_aux_line.add(
                VMobject().set_points_as_corners(
                    [ axes.c2p(x_tick_pos[ -1 ], 0, z), axes.c2p(0, 0, z), axes.c2p(0, y_tick_pos[ -1 ], z) ])
                    .set_stroke(opacity=0.3,
                                width=2,
                                color=GRAY))
            y_axis_aux_line.add(
                VMobject().set_points_as_corners([ axes.c2p(x_tick_pos[ -1 ], y, 0), axes.c2p(0, y, 0), axes.c2p(0, y, z_tick_pos[ -1 ]) ])
                    .set_stroke(opacity=0.3,
                                width=2,
                                color=GRAY))
            x_axis_aux_line.add(
                VMobject().set_points_as_corners(
                    [ axes.c2p(x, y_tick_pos[ -1 ], 0), axes.c2p(x, 0, 0), axes.c2p(x, 0, z_tick_pos[ -1 ]) ])
                    .set_stroke(opacity=0.3,
                                width=2,
                                color=GRAY))

        origin_vertical_aux_line = VMobject().set_points_as_corners([ axes.c2p(0, 0, 0), axes.c2p(0, 0, z_tick_pos[ -1 ]) ]) \
            .set_stroke(opacity=0.3,
                        width=2,
                        color=GRAY)

        aux_lines = VGroup(x_axis_aux_line, y_axis_aux_line, z_axis_aux_line, origin_vertical_aux_line, )
        # 기존 좌표계가 틀어지지 않게 모두 이동은 같이 하되 제트 축은 보여주지 않을 것임
        VGroup(axes[ 0 ], axes[ 1 ], axes[ 2 ], axes[ 3 ], aux_lines).move_to(O)
        # 실제 쓸 축들만 뉴 엑시스로 정의
        new_axes = VGroup(axes[ 0 ], axes[ 1 ], axes[ 3 ], aux_lines)

        new_axes[ 0 ].set_color(RED)
        new_axes[ 1 ].set_color(GREEN)
        new_axes[ 2 ].set_color(BLUE)

        # 뉴엑시스는 클래스가 없이 그저 브이그룹이어서 기존의 메서드들을 사용 못 함 그래서 메서드 사용은 기존 엑시스
        axes.get_z_axis_label('z')
        axes.get_x_axis_label('x')
        axes.get_y_axis_label('y')

        self.camera.set_zoom(0.6)

        self.add(new_axes)

        # 제트축 넘버들을 픽ㅅ드 오리엔테이션 적용 전에 전부 위로 향하게 돌려줌
        for number in axes[ 3 ].numbers:
            number.rotate(90 * DG, axis=X).rotate(90 * DG)

        # numbers = VGroup(*axes[ 0 ].numbers, *axes[ 1 ].numbers, *axes[ 3 ].numbers)

        # if Zoom is applied, gotta change scale,
        # for number in numbers:
        #     number.scale(0.5)

        self.add_fixed_orientation_mobjects(*axes[ 0 ].numbers)
        self.add_fixed_orientation_mobjects(*axes[ 1 ].numbers)
        self.add_fixed_orientation_mobjects(*axes[ 3 ].numbers, use_static_center_func=False)

        entropy1 = ParametricFunction(lambda t: axes.c2p(*self.dollar_val_surface(t, 0)), t_range=[ 0, 3 ], color=YELLOW, stroke_width=6)
        entropy2 = ParametricFunction(lambda t: axes.c2p(*self.dollar_val_surface(0, t)), t_range=[ 0, 3 ], color=YELLOW, stroke_width=6)
        entropy3 = ParametricFunction(lambda t: axes.c2p(t, 3 - t, self.dollar_val_surface(t, 3 - t)[ 2 ]), t_range=[ 0, 3 ], color=YELLOW,
                                      stroke_width=6)
        self.play(Create(entropy1),
                  Create(entropy2),
                  Create(entropy3))

        # 서페이스 생성 하고 카메라 회전
        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface(u, v)),
            v_range=[ 0, 3 ],
            u_range=[ 0, 3 ],
            resolution=15)

        val_graph.set_style(fill_opacity=0.3)
        val_graph.set_fill_by_value(axes=axes, colors=[ (RED, 0), (GREEN, 2) ], axis=2)

        self.play(Create(val_graph))

        self.move_camera(theta=20 * DEGREES, about="theta", run_time=1)
        self.move_camera(phi=80 * DEGREES, about="phi", run_time=1)

        inv = 100
        inv_text = Tex(rf'Investment = {inv}\$').move_to(axes.c2p(1.5, 0, 2.5)).rotate(90 * DG, axis=X).rotate(180 * DG, axis=Z).scale(1.5)

        self.play(Create(inv_text))

        def curr_profit_with_IfOnTriangle():

            text = Tex(rf'Profit = {inv * (self.dollar_val_surface(x_tkr.get_value(), y_tkr.get_value())[ 2 ]):.2f}\$') \
                .move_to(axes.c2p(0, 1.5, 2.5)).rotate(90 * DG, axis=X).rotate(90 * DG, axis=Z).scale(1.8).set_color(GREEN)
            letter_len = len([ letter for letter in text ])
            if x_tkr.get_value() + y_tkr.get_value() > 3:
                text = Tex(rf'Profit = Out of range') \
                    .move_to(axes.c2p(0, 1.5, 2.5)).rotate(90 * DG, axis=X).rotate(90 * DG, axis=Z).scale(1.6).set_color(RED)


            return text

        curr_profit = redraw(curr_profit_with_IfOnTriangle)
        self.add(curr_profit)

        flat_tri = VMobject().set_points_as_corners([ axes.c2p(3, 0, 0), axes.c2p(0, 0, 0), axes.c2p(0, 3, 0), axes.c2p(3, 0, 0) ]) \
            .set_fill(opacity=0.3, color=PINK).set_stroke(opacity=0)

        self.play(Create(flat_tri))

        # 3디 공간상의점을 정의하고 평면에 투사된 위치를 표시할 점도 같이 리드로우 설정정
        def curr_p_projected_with_label():
            dot = Dot().move_to(axes.c2p(x_tkr.get_value(), y_tkr.get_value(), 0))
            label = Tex(f'({x_tkr.get_value():.2f}, {y_tkr.get_value():.2f})').next_to(dot, UR, buff=0.5)
            return VGroup(dot, label)

        def curr_p_with_IfOnSurface():
            dot = Dot3D(radius=0.2, color=GREEN).move_to(
                axes.c2p(x_tkr.get_value(), y_tkr.get_value(), self.dollar_val_surface(x_tkr.get_value(), y_tkr.get_value())[ 2 ]))

            if x_tkr.get_value() + y_tkr.get_value() > 3:
                dot.set_color(RED)

            return dot

        curr_p = redraw(curr_p_with_IfOnSurface)
        curr_p_projected = redraw(curr_p_projected_with_label)
        self.add_fixed_orientation_mobjects(curr_p_projected[ 1 ])
        self.play(Create(VGroup(curr_p_projected, curr_p)))

        lines = redraw(lambda: VGroup(axes.get_lines_to_point(curr_p_projected[ 0 ].get_center())[ 1 ].set_color(RED),
                                      axes.get_lines_to_point(curr_p_projected[ 0 ].get_center())[ 0].set_color(GREEN)))
        vertical_line = redraw(lambda: DashedLine(start=curr_p_projected[ 0 ].get_center(), end=curr_p.get_center()))
        self.play(Create(VGroup(lines, vertical_line)))

        self.play(x_tkr.animate.set_value(1))
        self.play(y_tkr.animate.set_value(1))

        self.play(x_tkr.animate.set_value(2))
        self.play(y_tkr.animate.set_value(2))

        self.play(x_tkr.animate.set_value(1))
        self.play(y_tkr.animate.set_value(1))


        self.move_camera(phi=45 * DEGREES, run_time=1)

        self.begin_ambient_camera_rotation(0.1, about='theta')

        self.wait(3)

class ImpLossCircleCut(ThreeDScene):
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

    def dollar_val_surface_circle(self, u, v, x_shift=1, y_shift=1, radius=0.5):
        if (u - x_shift) ** 2 + (v - y_shift) ** 2 < radius ** 2:
            # v=np.sqrt(0.5 ** 2-u ** 2)
            # return np.array([ u, v, 0 ])
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1
        else:

            angle = angle_of_vector(np.array([ u - x_shift, v - y_shift, 0 ]))
            u = np.cos(angle) * radius + x_shift
            v = np.sin(angle) * radius + y_shift
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1
        return np.array([ u, v, curr_val ])

    def construct(self):

        # self.add(NumberPlane())
        radius = 0.5
        x_shift = 1
        y_shift = 1

        axes = ThreeDAxes(x_range=(-0.99, 3, 1), y_range=(-0.99, 3, 1), z_range=(-1, 3, 1),
                          x_length=7, y_length=7, z_length=7).move_to(O)

        lab_x = axes.get_x_axis_label(Tex("$x$-label"),direction=DR,  buff=0.5)
        lab_y = axes.get_y_axis_label(Tex("$y$-label"),direction=UL, buff=0.5)
        lab_z = axes.get_z_axis_label(Tex("$z$-label"),direction=OUT, buff=0.5).rotate(270 * DG, axis=X)
        labs = VGroup(lab_x, lab_y, lab_z)
        self.play(Create(VGroup(axes, labs)))
        self.add_fixed_orientation_mobjects(*labs)


        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=30
        )
        val_graph.set_style(fill_opacity=0.5)
        val_graph.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        val_graph_2 = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface_circle(u, v, x_shift, y_shift, radius)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99,3 ],
            resolution=30
        )
        # val_graph_2.set_style(fill_opacity=1,fill_color =RED)
        val_graph_2.set_style(fill_opacity=0.5,fill_color =RED)
        # val_graph_2.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        self.move_camera(theta=80 * DG, about="theta", run_time=1)
        circle_cut = Circle().scale_to_fit_width(radius*2 * get_dist_btwn_points(axes.c2p(0, 0), axes.c2p(1, 0))).move_to(axes.c2p(x_shift, y_shift,0)).set_fill(opacity=0.2, color =RED)

        text = MathTex(rf'(x-{x_shift})^2+(y-{y_shift})^2<{radius}^2').move_to(axes.c2p(x_shift,y_shift, -1)).scale(0.7)
        text_dashed_line = DashedLine(start=axes.c2p(x_shift,y_shift, -0.8), end=axes.c2p(x_shift,y_shift, 0), stroke_color = RED)

        self.play(Create(val_graph))
        self.add_fixed_orientation_mobjects(text)
        self.play(Create(text_dashed_line))
        self.play(Create(circle_cut))
        self.play(circle_cut.copy().animate.shift(OUT*5.5))
        self.play(Transform(val_graph, val_graph_2))

        self.move_camera(phi=80 * DG, about="phi", run_time=1)
        self.move_camera(theta=10 * DG, about="theta", run_time=5)
        # self.move_camera(theta=0 * DG, about="theta", run_time=1)
        # self.begin_ambient_camera_rotation(-0.2, about='theta')
        # self.stop_ambient_camera_rotation()

        self.wait(3)


class ElectricalField(Scene):
    def construct(self):
        charge1 = Charge(-4, LEFT * 3.5)
        charge2 = Charge(2, RIGHT * 4 + DOWN * 2)
        charge3_mag_tkr = ValueTracker(8)
        charge3 = redraw(lambda: Charge(charge3_mag_tkr.get_value(), UP * 3))
        charge4 = Charge(-1, RIGHT * 7 + U * 3.5)
        charge5 = Charge(-1, DOWN * 3.5)
        charge6 = Charge(-1, RIGHT * 7 + DOWN * 2)
        charge7 = Charge(-1, L * 7 + DOWN * 3)
        field = redraw(lambda: ElectricField(charge1, charge2, charge3, charge4, charge5, charge6, charge7))
        self.add(field, charge1, charge2, charge3, charge4, charge5, charge6, charge7)
        # self.play(charge3.animate.shift(L * 4), run_time=2)

        self.play(charge1.animate.shift(D * 1 + L * 1), run_time=1)
        self.play(charge1.animate.shift(D * 1 + R * 1), run_time=1)
        self.play(charge1.animate.shift( R * 1), run_time=1)
        self.play(charge1.animate.shift( U * 1), run_time=1)
        self.wait(5)


class VivianiTheorem(MovingCameraScene):
    """비비아니 띠어럼. 삼각형 내부의 삼각형들의 높이는 전체 삼각형의 높이와 같음"""

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
        pink_var[ 0 ][ 0 ].set_color(color=PINK)
        pink_var.move_to(get_compensated_coor(pink_var, pink_var[ 0 ][ 1 ].get_center(), yellow_var[ 0 ][ 1 ].get_bottom() + D * 1))
        pink_var[ 1 ].add_updater(lambda x: x.become(DecimalNumber(get_line_length(perp_line_right)).next_to(pink_var[ 0 ], R)))

        green_var = Variable(0, 'GREEN', DecimalNumber)
        green_var[ 0 ][ 0 ].set_color(color=GREEN)
        green_var.move_to(get_compensated_coor(green_var, green_var[ 0 ][ 1 ].get_center(), pink_var[ 0 ][ 1 ].get_bottom() + D * 1))
        green_var[ 1 ].add_updater(lambda x: x.become(DecimalNumber(get_line_length(perp_line_bottom)).next_to(green_var[ 0 ], R)))

        vertical_green_braces = redraw(lambda: BraceBetweenPoints(vertical_green.get_start(), vertical_green.get_end()))
        vertical_pink_braces = redraw(lambda: BraceBetweenPoints(vertical_green.get_end(), vertical_pink.get_end()))
        vertical_yellow_braces = redraw(lambda: BraceBetweenPoints(vertical_pink.get_end(), vertical_yellow.get_end()))

        vertical_green_braces_label = redraw(lambda: DecimalNumber(get_line_length(perp_line_bottom)).next_to(vertical_green_braces))
        vertical_pink_braces_label = redraw(lambda: DecimalNumber(get_line_length(perp_line_right)).next_to(vertical_pink_braces))
        vertical_yellow_braces_label = redraw(lambda: DecimalNumber(get_line_length(perp_line_left)).next_to(vertical_yellow_braces))

        self.play(Create(tri))
        self.play(Create(dot))
        self.play(Create(VGroup(perp_line_left, perp_line_right, perp_line_bottom)))
        self.play(Create(VGroup(yellow_var, pink_var, green_var)))
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

        self.wait(3)
class SumOfCubes(ThreeDScene):

    def construct(self):
    #     self.add(NumberPlane(faded_line_ratio=1, x_length=16, y_length=9))

        sq_len_1 = Square(1, fill_color=BLUE, fill_opacity=1)
        sq_len_list = [ sq_len_1 ]

        for i in range(2, 7):
            locals()[ 'sq_len_' + str(i) ] = VGroup(*[ Square(i, fill_color=BLUE, fill_opacity=1) for j in range(i) ]) \
                .arrange(R, buff=0).next_to(locals()[ 'sq_len_' + str(i - 1) ].get_corner(DL), DR, buff=0)
            sq_len_list.append(locals()[ 'sq_len_' + str(i) ])

        scaler = 0.35
        sq_len_group = VGroup(*sq_len_list)
        self.play(Create(VGroup(*sq_len_list,
                                Line(start=sq_len_list[ 5 ][ 5 ].get_corner(DR), end=sq_len_list[ 5 ][ 5 ].get_corner(DR) + R * 6))
                         .scale(scaler).move_to(O)), run_time=5)

        line = Line(start=sq_len_1.get_corner(UL), end=sq_len_list[ 5 ][ 5 ].get_corner(DR) + R * 6 * scaler)
        angle = get_angle_ABC(line.get_end(), sq_len_1[ -1 ].get_corner(UL), sq_len_1[ -1 ].get_corner(UR))

        triangles = VGroup()
        last_rects = VGroup()
        rects = VGroup()
        triangle_ani_slide_list = [ ]

        for sq_len in sq_len_list:
            index = sq_len_list.index(sq_len)
            hypotenuse = (index + 1) * scaler / np.cos(angle)

            triangle = Polygon(sq_len[ -1 ].get_corner(UL),
                               sq_len[ -1 ].get_corner(UR),
                               sq_len[ -1 ].get_corner(UR) + D * np.sin(angle) * hypotenuse,
                               fill_color=RED, fill_opacity=1, stroke_color=WHITE)

            rect = Polygon(sq_len[ -1 ].get_corner(UL),

                           sq_len[ -1 ].get_corner(DL),
                           sq_len[ -1 ].get_corner(DR),
                           sq_len[ -1 ].get_corner(UR) + D * np.sin(angle) * hypotenuse,
                           fill_color=BLUE, fill_opacity=1, stroke_color=WHITE)

            rects.add(rect)
            triangles.add(triangle)
            triangle_ani_slide_list.append(triangle.animate.move_to(
                get_compensated_coor(triangle, triangle.get_start_anchors()[ 0 ], triangle.get_start_anchors()[ 2 ])))
            last_rects.add(sq_len[ -1 ])

        self.play(Create(line))
        self.play(Create(triangles))

        for rect, last_rect in zip(rects, last_rects):
            last_rect.become(rect)

        self.play(*triangle_ani_slide_list)

        tri_ani_rotate_list = [ ]
        for triangle in triangles:
            about_point = midpoint(triangle.get_start_anchors()[ 0 ], triangle.get_start_anchors()[ 2 ])
            tri_ani_rotate_list.append(Rotate(triangle, angle=-PI, about_point=about_point))

        self.play(*tri_ani_rotate_list)

class AMGMInequality(ThreeDScene):

    def construct(self):
        axes = Axes(x_range=[ 0, 16 ], y_range=[ 0, 9 ], x_length=16 * 0.9, y_length=9 * 0.9, )

        # circle = Circle(radius=3)
        # self.play(Create(circle), rate_func=there_and_back, run_time=8)

        numberplane = NumberPlane()
        # self.add(numberplane)

        x_axis = Line(start=D*3+L * 15, end=D*3+R * 15, stroke_width=10, stroke_color=WHITE)
        b_radius_tracker = ValueTracker(1)
        a_radius = 2

        a_line = Line(start=D*3, end=D*3+U * a_radius * 2, color=BLUE).shift(L * a_radius)
        b_line = Line(start=D*3, color=GREEN, end=D*3+U * b_radius_tracker.get_value() * 2).shift(
            L * a_radius + R * np.sqrt(a_radius * 2 * b_radius_tracker.get_value() * 2))

        a_l_arc = ArcBetweenPoints(color=BLUE, start=a_line.get_start(), end=a_line.get_end(), radius=a_radius)
        a_r_arc = ArcBetweenPoints(color=BLUE, start=a_line.get_end(), end=a_line.get_start(), radius=a_radius)
        b_l_arc = ArcBetweenPoints(start=b_line.get_start(), end=b_line.get_end(), radius=b_radius_tracker.get_value())
        b_r_arc = ArcBetweenPoints(start=b_line.get_end(), end=b_line.get_start(), radius=b_radius_tracker.get_value())

        b_line_start = b_line.get_start()
        b_line_end = b_line.get_end()

        b_r_arc.add_updater(lambda x: x.become(
            ArcBetweenPoints(color=GREEN, start=b_line_start, end=b_line.get_start(), radius=b_radius_tracker.get_value())))
        b_l_arc.add_updater(
            lambda x: x.become(ArcBetweenPoints(color=GREEN, start=b_line_end, end=b_line.get_end(), radius=1)))

        self.add(b_l_arc, b_r_arc)
        self.add(x_axis, a_line, b_line)

        self.play(Rotate(a_line, angle=PI),
                  Rotate(b_line, angle=PI),
                  Create(a_l_arc, angle=PI),
                  Create(a_r_arc, angle=PI),
                  rate_func=smooth,
                  run_time=1)

        a_circle = Circle(radius=a_radius, color=BLUE).move_to(a_line)
        b_circle = Circle(radius=b_radius_tracker.get_value(), color=GREEN).move_to(b_line)

        a = a_line.get_center()
        b = b_line.get_center()

        self.add(a_circle, b_circle)
        self.remove(b_r_arc, b_l_arc, a_l_arc, a_r_arc)

        a_dia_line = Line(start=a_circle.get_bottom(), end=a_circle.get_top(), color=BLUE)
        b_dia_line = Line(start=b_circle.get_bottom(), end=b_circle.get_top(), color=GREEN)
        a2b_line = Line(start=a_circle.get_center(), end=b_circle.get_center())
        a2b_line_horz = DashedLine(start=[ a_circle.get_x(), b_circle.get_y(), 0 ], end=b_line.get_center())
        a_vert_brace = BraceBetweenPoints(a_circle.get_center(), [ a_circle.get_x(), b_circle.get_y(), 0 ])
        a_horz_brace = BraceBetweenPoints(a_circle.get_bottom(), b_circle.get_bottom())

        a_dia_line.add_updater(lambda x: x.become(Line(start=a_circle.get_bottom(), end=a_circle.get_top(), color=BLUE)))
        b_dia_line.add_updater(lambda x: x.become(Line(start=b_circle.get_bottom(), end=b_circle.get_top(), color=GREEN)))
        a2b_line.add_updater(lambda x: x.become(Line(start=a_circle.get_center(), end=b_circle.get_center())))
        a2b_line_horz.add_updater(
            lambda x: x.become(DashedLine(start=[ a_circle.get_x(), b_circle.get_y(), 0 ], end=b_circle.get_center())))

        def vert_brace(x):
            if a_circle.get_y() > b_circle.get_y():
                x.become(BraceBetweenPoints(a_circle.get_center(), [ a_circle.get_x(), b_circle.get_y(), 0 ]))
            elif a_circle.get_y() == b_circle.get_y():
                x.become(BraceBetweenPoints([ a_circle.get_x(), a_circle.get_y(), 0 ], a_circle.get_center()))

            else:
                x.become(BraceBetweenPoints([ a_circle.get_x(), b_circle.get_y(), 0 ], a_circle.get_center()))

        a_vert_brace.add_updater(vert_brace)

        a_horz_brace.add_updater(lambda x: x.become(BraceBetweenPoints(a_circle.get_bottom(), b_circle.get_bottom())))

        b_circle.add_updater(lambda circle: circle.become(Circle(radius=b_radius_tracker.get_value(), color=GREEN)
            .move_to(
            [ a_circle.get_x() + np.sqrt(a_radius * 2 * b_radius_tracker.get_value() * 2), b_radius_tracker.get_value()-3, 0 ])))
        self.wait(1)
        self.add(a_dia_line, b_dia_line)
        self.remove(a_line, b_line)

        hypotenuse_label= MathTex(r'\frac{a+b}{2}')
        hypotenuse_label.add_updater(lambda x:x.next_to(a2b_line.get_midpoint(),U))
        vert_label= MathTex(r'\frac{|a+b|}{2}')
        vert_label.add_updater(lambda x:x.move_to([ a_circle.get_x()-1.5, a_dia_line.get_center()[1]+(get_line_length(b_dia_line)-get_line_length(a_dia_line))/4, 0 ]))
        horz_label= MathTex(r'\sqrt{ab}')
        horz_label.add_updater(lambda x:x.next_to(a_horz_brace,D))


        self.play(Create(VGroup(a2b_line, a2b_line_horz, a_vert_brace, a_horz_brace,hypotenuse_label,vert_label,horz_label )))

        self.play(b_radius_tracker.animate.set_value(5), run_time=3)
        self.wait(1)


class BooleanOps(ThreeDScene):

    def construct(self):
        # self.add(NumberPlane())
        set_1 = Circle(radius=2, color=RED_B, fill_opacity=0.5, fill_color=RED_B).shift(U * 1.732)
        set_1_label = MathTex('A').next_to(set_1, U)
        set_1.add(set_1_label)

        set_2 = Circle(radius=2, color=GREEN_B, fill_opacity=0.5, fill_color=GREEN_B).shift(L * 1)
        set_2_label = MathTex('B').next_to(set_2.get_center() + L * 1.414 + D * 1.414, DL)
        set_2.add(set_2_label)

        set_3 = Circle(radius=2, color=BLUE_B, fill_opacity=0.5, fill_color=BLUE_B).shift(R * 1)
        set_3_label = MathTex('C').next_to(set_3.get_center() + R * 1.414 + D * 1.414, DR)
        set_3.add(set_3_label)

        sets = VGroup(set_1, set_2, set_3).move_to(ORIGIN)

        self.play(DrawBorderThenFill(sets))

        self.play(sets.animate.to_edge(L, buff=1))

        a_intersection_b_form = MathTex(r'A\cap B=').shift(R * 1)
        a_intersection_b_shape = Intersection(set_1, set_2, fill_color=YELLOW_D, fill_opacity=0.8)
        self.play(Create(a_intersection_b_form))
        self.play(Create(a_intersection_b_shape))
        self.play(a_intersection_b_shape.animate.scale(0.3).rotate(-PI / 3).next_to(a_intersection_b_form, R))
        a_intersection_b = VGroup(a_intersection_b_form, a_intersection_b_shape)
        self.play(a_intersection_b.animate.move_to([ 4, 3, 0 ]))

        equal_sign_x = a_intersection_b_form[ 0 ][ 3 ].get_x()
        equal_sign_y = a_intersection_b_form[ 0 ][ 3 ].get_y()

        a_difference_b_form = MathTex(r'A-B=').shift(R * 1)
        a_difference_b_form.move_to(
            get_compensated_coor(a_difference_b_form, a_difference_b_form[ 0 ][ 3 ].get_center(), [ equal_sign_x, equal_sign_y - 1.5, 0 ]))
        a_difference_b_shape = Difference(set_1, set_2, fill_color=RED_D, fill_opacity=0.8)
        self.play(Create(a_difference_b_form))
        self.play(Create(a_difference_b_shape))
        self.play(a_difference_b_shape.animate.scale(0.3).rotate(-PI / 3).next_to(a_difference_b_form, R))
        a_difference_b = VGroup(a_difference_b_form, a_difference_b_shape)

        a_union_b_inter_c_form = MathTex(r'A\cup B\cap C=').shift(R * 1)
        a_union_b_inter_c_form.move_to(
            get_compensated_coor(a_union_b_inter_c_form, a_union_b_inter_c_form[ 0 ][ 5 ].get_center(), [ equal_sign_x, equal_sign_y - 3, 0 ]))
        a_union_b_inter_c_shape = Intersection(manim.Union(set_1, set_2), set_3, fill_color=PURPLE_D, fill_opacity=0.8)
        self.play(Create(a_union_b_inter_c_form))
        self.play(Create(a_union_b_inter_c_shape))
        self.play(a_union_b_inter_c_shape.animate.scale(0.3).rotate(PI / 3).next_to(a_union_b_inter_c_form, R))
        a_union_b_inter_c = VGroup(a_union_b_inter_c_form, a_union_b_inter_c_shape)

        a_inter_b_inter_c_form = MathTex(r'A\cap B\cap C=').shift(R * 1)
        a_inter_b_inter_c_form.move_to(get_compensated_coor(a_inter_b_inter_c_form, a_inter_b_inter_c_form[ 0 ][ 5 ].get_center(),
                                                                         [ equal_sign_x, equal_sign_y - 4.5, 0 ]))
        a_inter_b_inter_c_shape = Intersection(manim.Intersection(set_1, set_2), set_3, fill_color=TEAL, fill_opacity=0.8)
        self.play(Create(a_inter_b_inter_c_form))
        self.play(Create(a_inter_b_inter_c_shape))
        self.play(a_inter_b_inter_c_shape.animate.scale(0.3).rotate(PI / 3).next_to(a_inter_b_inter_c_form, R))
        a_inter_b_inter_c = VGroup(a_inter_b_inter_c_form, a_inter_b_inter_c_shape)

        a_inter_b_difference_c_form = MathTex(r'A\cap B- C=').shift(R * 1)
        a_inter_b_difference_c_form.move_to(
            get_compensated_coor(a_inter_b_difference_c_form, a_inter_b_difference_c_form[ 0 ][ 5 ].get_center(),
                                 [ equal_sign_x, equal_sign_y - 6, 0 ]))
        a_inter_b_difference_c_shape = Difference(manim.Intersection(set_1, set_2), set_3, fill_color=YELLOW_E, fill_opacity=0.8)
        self.play(Create(a_inter_b_difference_c_form))
        self.play(Create(a_inter_b_difference_c_shape))
        self.play(a_inter_b_difference_c_shape.animate.scale(0.3).next_to(a_inter_b_difference_c_form, R))
        a_inter_b_difference_c = VGroup(a_inter_b_difference_c_form, a_inter_b_difference_c_shape)

        self.wait(1)

class ParabolaMovingCam(MovingCameraScene):

    def construct(self):
        # self.add(NumberPlane())
        axes = Axes(x_range=[ -5, 5 ], y_range=[ -8, 8 ], x_length=6, y_length=9, tips=False, axis_config={'include_numbers': 1})
        graph_1 = axes.plot(lambda x: (x - 1)**2 + 1, color = BLUE, x_range = [ -3, 5 ]).set_z_index(3)
        graph_2 = axes.plot(lambda x: -(x - 1)**2 - 1, color = RED, x_range = [ -3, 5 ]).set_z_index(3)

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
        # axes = Axes(x_range=[ 0, 16 ], y_range=[ 0, 9 ], x_length=16 * 0.9, y_length=9 * 0.9, )

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

        self.play(x_tracker.animate.set_value(2.5), run_time=1)
        self.play(x_tracker.animate.set_value(1.5), run_time=1)
        self.play(x_tracker.animate.set_value(2), run_time=1)

        self.camera.frame.save_state()

        path = VMobject()
        graph_1_subpath = axes.plot(lambda x: (x - 1)**2 + 1, color = BLUE, x_range = [ 1, 3 ]).set_z_index(3)
        graph_1_subpath.reverse_points()
        path.add_subpath(graph_1_subpath.get_all_points())
        graph_2_subpath = axes.plot(lambda x: -(x - 1)**2 - 1, color = BLUE, x_range = [ 1, 3 ]).set_z_index(3)
        dot_for_path = Dot(radius=0.3, color=GREEN).move_to(graph_1_b_dot)
        path.add_points_as_corners([ axes.c2p(1, 1), axes.c2p(1, -1) ])
        path.add_points_as_corners(graph_2_subpath.get_all_points())

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_for_path))

        self.play(MoveAlongPath(self.camera.frame, path), run_time=6)

        self.play(Restore(self.camera.frame))
        self.wait(1)


class ParabolaArea(MovingCameraScene):

    def construct(self):
        axes = Axes(x_range=[ -10, 10 ], y_range=[ -8, 8 ], x_length=12, y_length=9, tips=False, axis_config={'include_numbers': 1})
        graph_1 = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ -3, 5 ]).set_z_index(3)

        x_tracker = ValueTracker(2)
        a = 1
        b = 3

        self.camera.frame.save_state()

        self.add(axes, graph_1)


        my_tan_1 = get_tangent_line(axes, graph_1, -1, line_length=30).set_stroke(color=GREEN)
        my_tan_2 = get_tangent_line(axes, graph_1, 3, line_length=30).set_stroke(color=RED)
        self.add(my_tan_1, my_tan_2)

        print(my_tan_1.get_function())


        path = VMobject()
        graph_1_subpath = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ -1, 3 ])
        path.add_subpath(graph_1_subpath.get_all_points())
        path.add_points_as_corners([ axes.c2p(3, 5), axes.c2p(1, -3) ])
        path.add_points_as_corners([ axes.c2p(1, -3), axes.c2p(-1, 5) ])

        path.set_stroke(width=4, color=WHITE).set_z_index(5).set_fill(color=YELLOW, opacity=0.5)
        self.play(DrawBorderThenFill(path), run_time=3)

        path_2 = VMobject()
        graph_1_subpath_2 = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ 0, 3 ])

        path_2.add_subpath(graph_1_subpath_2.get_all_points())
        path_2.add_points_as_corners([ axes.c2p(3, 5), axes.c2p(0, 2) ])
        path_2.set_fill(color=BLUE, opacity=0.5)

        self.play(DrawBorderThenFill(path_2), run_time=2)

        self.play(path.copy().animate.move_to([ 4, -2, 0 ]).scale(0.6))
        self.play(path_2.copy().animate.move_to([ 4, 2, 0 ]).scale(0.6))

        self.wait(2)


class GravityEngine(SpaceScene):

    def construct(self):
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        # tri = Triangle().shift(UP+L*4).rotate(30*DG)
        # tri.set_fill(BLUE, 1)
        # circle.shift(DOWN + RIGHT)

        math = Tex('Math').scale(2).shift(UP+L*4).rotate(30*DG)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)

        ground = Line([ -6, -4, 0 ], [ 6, -4, 0 ])
        wall1 = Line([ -6, -4, 0 ], [ -6, 4, 0 ])
        wall2 = Line([ 6, -4, 0 ], [ 6, 4, 0 ])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(rect),
            DrawBorderThenFill(math),
        )
        self.make_rigid_body(rect, elasticity=0.8,)  # Mobjects will move with gravity
        self.make_rigid_body(circle, elasticity=0.9)  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.make_rigid_body(*math, elasticity=0.4)  # Mobjects will move with gravity
        self.wait(10)

# with tempconfig({"quality": "medium_quality", "preview": True, 'fps': '10',
#                  'renderer': 'opengl', 'write_to_movie': True}):
#     scene = Sphere_3D()
#     #     #     # scene = working2()
#     #     #     # scene = working3()
#     #     #     # scene = working4()
#     #     #     # scene = working5()
#     scene.render()
