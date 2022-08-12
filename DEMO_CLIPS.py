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
        # test_mob.set_fill_by_checkerboard(BLUE)
        self.play(Create(axes))
        self.play(Create(test_mob), run_time=5)
        self.move_camera(phi=45 * DG, about="phi", run_time=2)
        self.move_camera(theta=2 * PI, about="theta", run_time=5)


class Helix_3D(ThreeDScene):
    """3D 스피어 생성과 카메라 회전"""

    def construct(self):
        axes = ThreeDAxes()
        test_mob = OpenGLThreeDVMobjectFromPLY('helix.ply',
                                               fill_color=RED, fill_opacity=0.5,
                                               stroke_width=1, stroke_opacity=0.5, scaler=3).scale_to_fit_width(4).move_to(
            axes.c2p(0, 0, 0))
        # test_mob.set_fill_by_checkerboard(BLUE)
        self.play(Create(axes))
        self.play(Create(test_mob), run_time=1)
        self.move_camera(phi=45 * DG, about="phi", run_time=2)
        self.move_camera(theta=2 * PI, about="theta", run_time=5)


class King_3D(ThreeDScene):
    """3D 스피어 생성과 카메라 회전"""

    def construct(self):
        axes = ThreeDAxes()
        test_mob = OpenGLThreeDVMobjectFromPLY('king.ply',
                                               fill_color=DARK_BROWN, fill_opacity=1,
                                               stroke_width=0.5, stroke_opacity=0.2, scaler=3).scale_to_fit_width(4).move_to(
            axes.c2p(0, 0, 0))
        # test_mob.set_fill_by_checkerboard(BLUE)
        self.play(Create(axes))
        self.play(Create(test_mob), run_time=1)
        self.move_camera(phi=45 * DG, about="phi", run_time=2)
        self.move_camera(theta=2 * PI, about="theta", run_time=5)


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
                                      axes.get_lines_to_point(curr_p_projected[ 0 ].get_center())[ 0 ].set_color(GREEN)))
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

        lab_x = axes.get_x_axis_label(Tex("$x$-label"), direction=DR, buff=0.5)
        lab_y = axes.get_y_axis_label(Tex("$y$-label"), direction=UL, buff=0.5)
        lab_z = axes.get_z_axis_label(Tex("$z$-label"), direction=OUT, buff=0.5).rotate(270 * DG, axis=X)
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
            u_range=[ -0.99, 3 ],
            resolution=30
        )
        # val_graph_2.set_style(fill_opacity=1,fill_color =RED)
        val_graph_2.set_style(fill_opacity=0.5, fill_color=RED)
        # val_graph_2.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        self.move_camera(theta=80 * DG, about="theta", run_time=1)
        circle_cut = Circle().scale_to_fit_width(radius * 2 * get_dist_btwn_points(axes.c2p(0, 0), axes.c2p(1, 0))).move_to(
            axes.c2p(x_shift, y_shift, 0)).set_fill(opacity=0.2, color=RED)

        text = MathTex(rf'(x-{x_shift})^2+(y-{y_shift})^2<{radius}^2').move_to(axes.c2p(x_shift, y_shift, -1)).scale(0.7)
        text_dashed_line = DashedLine(start=axes.c2p(x_shift, y_shift, -0.8), end=axes.c2p(x_shift, y_shift, 0), stroke_color=RED)

        self.play(Create(val_graph))
        self.add_fixed_orientation_mobjects(text)
        self.play(Create(text_dashed_line))
        self.play(Create(circle_cut))
        self.play(circle_cut.copy().animate.shift(OUT * 5.5))
        self.play(Transform(val_graph, val_graph_2))

        self.move_camera(phi=80 * DG, about="phi", run_time=1)
        self.move_camera(theta=10 * DG, about="theta", run_time=5)
        # self.move_camera(theta=0 * DG, about="theta", run_time=1)
        # self.begin_ambient_camera_rotation(-0.2, about='theta')
        # self.stop_ambient_camera_rotation()

        self.wait(3)


class ElectricField(Scene):
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
        self.play(charge1.animate.shift(R * 1), run_time=1)
        self.play(charge1.animate.shift(U * 1), run_time=1)
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

        x_axis = Line(start=D * 3 + L * 15, end=D * 3 + R * 15, stroke_width=10, stroke_color=WHITE)
        b_radius_tracker = ValueTracker(1)
        a_radius = 2

        a_line = Line(start=D * 3, end=D * 3 + U * a_radius * 2, color=BLUE).shift(L * a_radius)
        b_line = Line(start=D * 3, color=GREEN, end=D * 3 + U * b_radius_tracker.get_value() * 2).shift(
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
            [ a_circle.get_x() + np.sqrt(a_radius * 2 * b_radius_tracker.get_value() * 2), b_radius_tracker.get_value() - 3, 0 ])))
        self.wait(1)
        self.add(a_dia_line, b_dia_line)
        self.remove(a_line, b_line)

        hypotenuse_label = MathTex(r'\frac{a+b}{2}')
        hypotenuse_label.add_updater(lambda x: x.next_to(a2b_line.get_midpoint(), U))
        vert_label = MathTex(r'\frac{|a+b|}{2}')
        vert_label.add_updater(lambda x: x.move_to(
            [ a_circle.get_x() - 1.5, a_dia_line.get_center()[ 1 ] + (get_line_length(b_dia_line) - get_line_length(a_dia_line)) / 4, 0 ]))
        horz_label = MathTex(r'\sqrt{ab}')
        horz_label.add_updater(lambda x: x.next_to(a_horz_brace, D))

        self.play(Create(VGroup(a2b_line, a2b_line_horz, a_vert_brace, a_horz_brace, hypotenuse_label, vert_label, horz_label)))

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
            get_compensated_coor(a_union_b_inter_c_form, a_union_b_inter_c_form[ 0 ][ 5 ].get_center(),
                                 [ equal_sign_x, equal_sign_y - 3, 0 ]))
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
        graph_1_subpath = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        graph_1_subpath.reverse_points()
        path.add_subpath(graph_1_subpath.get_all_points())
        graph_2_subpath = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
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

        math = Tex('Math').scale(2).shift(UP + L * 4).rotate(30 * DG)

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
        self.make_rigid_body(rect, elasticity=0.8, )  # Mobjects will move with gravity
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
class ElectricField2(Scene):

    def construct(self):
        class Charge(OpenGLVGroup):
            def __init__(
                    self,
                    magnitude: float = 1,
                    point: np.ndarray = ORIGIN,
                    add_glow: bool = True,
                    **kwargs,
            ) -> None:
                OpenGLVGroup.__init__(self, **kwargs)

                self.magnitude = magnitude
                self.point = point
                self.radius = (abs(magnitude) * 0.4 if abs(magnitude) < 2 else 0.8) * 0.3
                # print(self.magnitude)

                if magnitude > 0:
                    label = OpenGLVGroup(
                        Rectangle(width=0.32 * 1.1, height=0.006 * 1.1),
                        Rectangle(width=0.006 * 1.1, height=0.32 * 1.1),
                    )
                    color = RED
                    layer_colors = [ RED_D, RED_A ]
                    layer_radius = 4
                else:
                    label = Rectangle(width=0.27, height=0.003)
                    color = BLUE
                    layer_colors = [ "#3399FF", "#66B2FF" ]
                    layer_radius = 2

                if add_glow:  # use many arcs to simulate glowing
                    layer_num = 40
                    color_list = color_gradient(layer_colors, layer_num)
                    opacity_func = lambda t: 1500 * (1 - abs(t - 0.009) ** 0.0001)
                    rate_func = lambda t: t ** 2

                    for i in range(layer_num):
                        self.add(
                            Arc(
                                radius=layer_radius * rate_func((0.5 + i) / layer_num),
                                angle=TAU,
                                color=color_list[ i ],
                                stroke_width=101
                                             * (rate_func((i + 1) / layer_num) - rate_func(i / layer_num))
                                             * layer_radius,
                                stroke_opacity=opacity_func(rate_func(i / layer_num)),
                            ).shift(self.point)
                        )

                self.add(Dot(point=self.point, radius=self.radius, color=color))
                self.add(label.scale(self.radius / 0.3).shift(point))
                for mob in self:
                    mob

            def set_magnitude(self, mag):
                self.magnitude = mag
                print(self.magnitude)

                return self

        C1_x_tkr = ValueTracker(2)
        C1_y_tkr = ValueTracker(0)
        C1_mag_tkr = ValueTracker(1)
        C2_x_tkr = ValueTracker(-2)
        C2_y_tkr = ValueTracker(0)
        C2_mag_tkr = ValueTracker(-1)

        charge1 = redraw(lambda: Charge(magnitude=C1_mag_tkr.get_value(), point=[ C1_x_tkr.get_value(), C1_y_tkr.get_value(), 0 ]))
        charge2 = redraw(lambda: Charge(magnitude=C2_mag_tkr.get_value(), point=[ C2_x_tkr.get_value(), C2_y_tkr.get_value(), 0 ]))

        field = redraw(
            lambda: ElectricField(Charge(magnitude=C1_mag_tkr.get_value(), point=[ C1_x_tkr.get_value(), C1_y_tkr.get_value(), 0 ]),
                                  Charge(magnitude=C2_mag_tkr.get_value(), point=[ C2_x_tkr.get_value(), C2_y_tkr.get_value(), 0 ])))
        self.add(field, charge1, charge2)
        #
        self.play(C1_x_tkr.animate.set_value(2),
                  C1_y_tkr.animate.set_value(3),
                  C1_mag_tkr.animate.set_value(10),
                  run_time=5)
        self.play(C2_x_tkr.animate.set_value(-4),
                  C2_y_tkr.animate.set_value(-3),
                  C2_mag_tkr.animate.set_value(-10),
                  run_time=3)

        self.wait(1)


class RiemannRectangles(Scene):

    def construct(self):
        ax = Axes(y_range=[ -2, 10 ])
        quadratic = ax.plot(lambda x: 0.5 * x ** 2 - 0.5)

        rects_right_dt_var = Variable(0.3, 'dt')
        rects_right_dt_tkr = rects_right_dt_var.tracker

        rects_right = redraw(
            lambda: ax.get_riemann_rectangles(quadratic, x_range=[ -5, -2 ], dx=rects_right_dt_tkr.get_value(),
                                              color=(TEAL, BLUE_B, DARK_BLUE),
                                              input_sample_type="right", ))
        rects_right_area = ax.get_area(quadratic, x_range=[ -5, -2 ], color=(TEAL, BLUE_B, DARK_BLUE)).set_fill(opacity=1)

        rects_right_dt_var.next_to(rects_right_area, L)

        bounding_line = ax.plot(lambda x: 0.5 * x, color=BLUE_B, x_range=[ -6, 6 ])

        bounded_rects_dt_var = Variable(0.3, 'dt')
        bounded_rects_dt_tkr = bounded_rects_dt_var.tracker

        bounded_rects = redraw(
            lambda: ax.get_riemann_rectangles(bounding_line, bounded_graph=quadratic, dx=bounded_rects_dt_tkr.get_value(), x_range=[ 4, 5 ],
                                              show_signed_area=False,
                                              color=(MAROON_A, RED_B, PURPLE_D), ))
        #
        bounded_rects_area = ax.get_area(quadratic, x_range=[ 4, 5 ], color=(MAROON_A, RED_B, PURPLE_D),
                                         bounded_graph=bounding_line).set_fill(
            opacity=1)
        bounded_rects_dt_var.next_to(bounded_rects_area, R)

        rects_bounding_dt_var = Variable(0.5, 'dt')
        rects_bounding_dt_tkr = rects_bounding_dt_var.tracker
        rects_bounding = redraw(
            lambda: ax.get_riemann_rectangles(bounding_line, x_range=[ -5, -2 ], dx=rects_bounding_dt_tkr.get_value(),
                                              color=[ ORANGE, BLUE ],
                                              input_sample_type="right", ))

        rects_bounding_area = ax.get_area(bounding_line, x_range=[ -5, -2 ], color=(RED, BLUE)).set_fill(opacity=1)
        rects_bounding_dt_var.next_to(rects_bounding_area, L)

        self.play(Create(ax))
        self.play(Create(quadratic))
        self.play(Create(bounding_line))

        self.wait(q)
        self.play(Create(rects_right))
        # self.play(Create(rects_right_dt_var))
        self.play(rects_right_dt_tkr.animate.set_value(0.02), run_time=5, rate_func=rush_into)
        rects_right.clear_updaters()
        self.play(Transform(rects_right, rects_right_area))

        self.wait(q)
        self.play(Create(rects_bounding))
        self.play(Create(rects_bounding_dt_var))
        self.play(rects_bounding_dt_tkr.animate.set_value(0.02), run_time=5, rate_func=rush_into)
        rects_bounding.clear_updaters()
        # self.play(Transform(rects_bounding, rects_bounding_area))

        self.wait(q)

        self.play(Create(bounded_rects))
        self.play(Create(bounded_rects_dt_var))
        self.play(bounded_rects_dt_tkr.animate.set_value(0.02), run_time=5, rate_func=rush_into)
        self.play(bounded_rects_dt_tkr.animate.set_value(0.3), run_time=5, rate_func=rush_into)

        self.wait(1)


# cairo
class Derivative(Scene):

    def construct(self):
        ax = Axes(y_range=[ -2, 10 ])
        x_tkr = ValueTracker(-3)

        quadratic = ax.plot(lambda x: 0.5 * x ** 2 + 1)
        quadratic_deri = ax.plot(lambda x: x).set_color(GRAY)
        quadratic_dot = redraw(lambda: Dot(color=RED).move_to(ax.c2p(x_tkr.get_value(), quadratic.underlying_function(x_tkr.get_value()))))

        def quadratic_deri_line():
            if x_tkr.get_value() > 0:
                return ax.get_lines_to_point(ax.c2p(x_tkr.get_value(), quadratic_deri.underlying_function(x_tkr.get_value())))

            else:
                return VMobject()

        quadratic_deri_line = redraw(quadratic_deri_line)
        quadratic_deri_dot = redraw(
            lambda: Dot(color=GREEN).move_to(ax.c2p(x_tkr.get_value(), quadratic_deri.underlying_function(x_tkr.get_value()))))

        q2d_line = redraw(lambda: DashedLine(start=quadratic_dot.get_center(), end=quadratic_deri_dot.get_center()))
        tangent_line = redraw(lambda: get_tangent_line(ax, quadratic, x_point=x_tkr.get_value(), line_length=6).set_color(RED))

        label = MathTex(r'y=0.5x^2+1').to_edge(L)
        tan_angle_equal_text = MathTex(r'Angle=').shift(D).to_edge(L).set_color(GRAY)
        tan_angle_num = redraw(
            lambda: MathTex(rf'{ax.angle_of_tangent(x_tkr.get_value(), quadratic):.2f}').next_to(tan_angle_equal_text, R).set_color(GREEN))
        # tan_angle_num = redraw(
        # lambda: DecimalNumber(rf'{round(ax.angle_of_tangent(x_tkr.get_value(), quadratic), 3)}').next_to(tan_angle_equal_text, R).set_color(
        #     GREEN))
        # tan_angle= OpenGLVGroup(tan_angle_equal_text,tan_angle_num)
        self.play(Create(ax))
        self.play(Create(quadratic))
        self.play(Create(quadratic_deri))
        self.play(Create(label))
        self.play(Create(tan_angle_equal_text))
        self.play(Create(tan_angle_num))
        self.play(Create(quadratic_dot))
        self.play(Create(tangent_line))

        self.play(Create(quadratic_deri_dot))
        self.play(Create(quadratic_deri_line))
        self.play(Create(q2d_line))
        self.play(x_tkr.animate.set_value(4), run_time=6, rate_func=linear)

        self.wait(3)
#
class SphereSlice(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[ -5, 5, 1 ],
                          y_range=[ -5, 5, 1 ],
                          z_range=[ -5, 5, 1 ],
                          x_length=9,
                          y_length=5.5,
                          z_length=5.5,
                          )

        def elip(t):
            print(np.array([ -1.41 * np.cos(t) + 0.82 * np.sin(t), 1.41 * np.cos(t) + 0.82 * np.sin(t), -1.63 * np.sin(t) ]))

            # return axes.c2p(-1.41*np.cos(t) + 0.82*np.sin(t), 1.41*np.cos(t) + 0.82*np.sin(t), -1.63*np.sin(t))
            return (-1.41 * np.cos(t) + 0.82 * np.sin(t), 1.41 * np.cos(t) + 0.82 * np.sin(t), -1.63 * np.sin(t))

        elip = ParametricFunction(elip, t_range=[ 0.01, 3.148 ], color=YELLOW, stroke_width=10)

        plane = OpenGLSurface(lambda u, v: (u, v, -u - v),
                              u_range=[ -2, 2 ],
                              v_range=[ -2, 2 ], shade_in_3d=True).set_color(color=RED, opacity=0.5)

        def elip(t):

            # return axes.c2p(-1.41*np.cos(t) + 0.82*np.sin(t), 1.41*np.cos(t) + 0.82*np.sin(t), -1.63*np.sin(t))
            return (-0.71 * np.cos(t) + 0.41 * np.sin(t), 0.71 * np.cos(t) + 0.41 * np.sin(t), -0.82 * np.sin(t))

        elip = ParametricFunction(elip, t_range=[ 0, TAU ], color=YELLOW, stroke_width=10)

        sphere = Sphere(radius=1, shade_in_3d=True, color=BLUE)
        self.move_camera(phi=90 * DG)
        self.play(Create(sphere))
        # self.add(sphere)
        self.play(Create(plane))
        self.play(Create(elip))
        self.move_camera(theta=180 * DG,run_time=5)
class LATEX(ThreeDScene):
    def construct(self):

        math_text = MathTex(r'\sum_{n=1}^{\infty} 2^{-n} = 1').scale(2.5)

        self.play(Create(math_text))

        self.wait(1)

        angle_step= TAU/ len(math_text[0])
        angle= 0
        animations=[]
        radius=4

        math_text.save_state()

        angle_norm_step=1/len(math_text[0])
        angle_norm=1/len(math_text[0])
        for letter in math_text[0]:
            # letter.save_state()

            # letter)
            animations.append(letter.animate.move_to([np.cos(angle)*radius, np.sin(angle)*radius, 0]).set_color(Color(hsl=(angle_norm, 0.9, 0.7))))

            angle+=angle_step
            angle_norm+=angle_norm_step

        self.play(AnimationGroup(*animations, lag_ratio=0.3),run_time=5)

        self.play(math_text[0][5].animate.scale(2))
        self.play(math_text[0][1].animate.scale(0.5))
        self.play(Rotate(math_text[0][-1]))

        self.play(CyclicReplace(math_text[0][6],math_text[0][1],math_text[0][3]))
        self.play(Swap(math_text[0][6],math_text[0][4]))

        self.play(Restore(math_text))

        self.wait(1)
class SVGIcons(ThreeDScene):
    def construct(self):

        btc = coin('btc')
        link = coin('link')
        # dot = coin('dot')
        mana = coin('aave')
        usdt = coin('usdt')
        eth = coin('eth')
        bnb = coin('bnb')
        etc = coin('etc')
        sol = coin('sol')
        icp = coin('icp')
        avax = coin('crv')

        air = SVGMobject('svgs/airbnb.svg')
        coca = SVGMobject('svgs/coca-cola.svg')
        fb = SVGMobject('svgs/facebook.svg')
        kakao = SVGMobject('svgs/kakaotalk.svg')
        mc = SVGMobject('svgs/mcdonald.svg')
        adobe = SVGMobject('svgs/adobexd.svg')

        coins=VGroup(btc,link,mana,usdt,bnb,eth,etc,sol,icp,avax).arrange_in_grid(2,5).scale(0.7)

        self.play(Create(coins))
        self.play(FadeOut(coins, shift=U), rate_func=rush_from)

        self.play(Create(air))
        self.play(air.animate.to_edge(UR), rate_func=rush_from)
        self.play(Create(coca))
        self.play(coca.animate.to_edge(DR), rate_func=rush_from)

        self.play(Create(fb))

        self.play(fb.animate.to_edge(DL), rate_func=rush_from)

        self.play(Create(kakao))

        self.play(kakao.animate.to_edge(UL), rate_func=rush_from)
        self.play(Create(mc))

        self.play(mc.animate.to_edge(U), rate_func=rush_from)


        self.play(mc.animate.set_color(BLUE))
        self.play(fb[1].animate.shift(U*2+R*2), rate_func=rush_from)
        self.play(kakao[2].animate.shift(D*2), rate_func=rush_from)
        self.play(coca[0].animate.shift(L*2), rate_func=rush_from)
        self.play(coca[1].animate.shift(U*2+L*1.4), rate_func=rush_from)
        self.play(coca[2].animate.shift(U*2), rate_func=rush_from)
        # self.play(coca[0][0].animate.shift(L*2), rate_func=rush_from)

        self.play(coca[0].animate.set_color(YELLOW))
        self.play(coca[1].animate.set_color(GREEN))
        self.play(coca[2].animate.set_color(WHITE))

        self.wait(3)

class LorenzAttractor(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-3.5,3.5],y_range=[-3.5,3.5],z_range=[0,6],
                          x_length=7,y_length=7,z_length=6,axis_config={"include_tip": True,"include_ticks":True,"stroke_width":1})


        dot = Sphere(radius=0.05,fill_color=BLUE).move_to(0*RIGHT + 0.1*UP + 0.105*OUT)

        self.move_camera(phi=30 * DEGREES,zoom=0.9)
        self.begin_ambient_camera_rotation(rate=0.08)            #Start move camera

        dtime = 0.01
        numsteps = 30
        self.add(axes,dot)


        def lorenz(x, y, z, s=10, r=28, b=2.667):
            x_dot = s*(y - x)
            y_dot = r*x - y - x*z
            z_dot = x*y - b*z
            return x_dot, y_dot, z_dot

        def update_trajectory_V(self, dt):
            new_point = dot.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)
        def update_trajectory_Open(self, dt):
            new_point = dot.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_line_to(new_point)
        which= 0

        if which ==0:
            traj = OpenGLVMobject()
            traj.start_new_path(dot.get_center())
            traj.set_stroke(BLUE, 1.5, opacity=0.8)

            traj.add_updater(update_trajectory_Open)

        else:
            traj = VMobject()
            traj.start_new_path(dot.get_center())
            traj.set_stroke(BLUE, 1.5, opacity=0.8)
            traj.add_updater(update_trajectory_V)

        self.add(traj)

        def update_position(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot.get_center()[0]*10, dot.get_center()[1]*10, dot.get_center()[2]*10)
            x = x_dot * dt/10
            y = y_dot * dt/10
            z = z_dot * dt/10
            self.shift(x/10*RIGHT + y/10*UP + z/10*OUT)

        dot.add_updater(update_position)
        self.wait(600)

class Aizawa1(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[ -3.5, 3.5 ], y_range=[ -3.5, 3.5 ], z_range=[ -3.5, 3.5 ],
                          x_length=7, y_length=7, z_length=7, axis_config={"include_tip": True, "include_ticks": True, "stroke_width": 1})

        dot_1 = Sphere(radius=0.02, color=Color(hsl=(0, 1, 0.5),)).move_to([0.1,0,0])
        dot_2 = Sphere(radius=0.02, color=Color(hsl=(1/5, 1, 0.5))).move_to([0.2,0,0])
        dot_3 = Sphere(radius=0.02, color=Color(hsl=(2/5, 1, 0.5))).move_to([0.3,0,0])
        dot_4 = Sphere(radius=0.02, color=Color(hsl=(3/5, 1, 0.5))).move_to([0.4,0,0])
        dot_5 = Sphere(radius=0.02, color=Color(hsl=(4/5, 1, 0.5))).move_to([0.5,0,0])

        self.move_camera(phi=60 * DEGREES, zoom=2)
        self.begin_ambient_camera_rotation(rate=0.08)  # Start move camera

        dt = 0.01
        self.add( dot_1,dot_2,dot_3,dot_4,dot_5)


        def aizawa(x, y, z, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
            x_dot = (z - b) * x - d * y
            y_dot = d * x + (z - b) * y
            z_dot = c + a * z - z ** 3 / 3 - (x ** 2 + y ** 2) * (1 + e * z) + f * z * x ** 3
            return x_dot, y_dot, z_dot

        def update_trajectory_V(self):
            new_point = self.get_center()
            if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
                self.add_smooth_curve_to(new_point)
        def update_trajectory_Open_dot_1(self):
            new_point = dot_1.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)

        def update_trajectory_Open_dot_2(self):
            new_point = dot_2.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_3(self):
            new_point = dot_3.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_4(self):
            new_point = dot_4.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_5(self):
            new_point = dot_5.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)

        which = 0
        traj_opacity=0.5
        if which == 0:
            traj_1 = OpenGLVMobject()
            traj_1.start_new_path(dot_1.get_center())
            traj_1.set_stroke(Color(hsl=(0, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_2 = OpenGLVMobject()
            traj_2.start_new_path(dot_2.get_center())
            traj_2.set_stroke(Color(hsl=(1/5, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_3 = OpenGLVMobject()
            traj_3.start_new_path(dot_3.get_center())
            traj_3.set_stroke(Color(hsl=(2/5, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_4 = OpenGLVMobject()
            traj_4.start_new_path(dot_4.get_center())
            traj_4.set_stroke(Color(hsl=(3/5, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_5 = OpenGLVMobject()
            traj_5.start_new_path(dot_5.get_center())
            traj_5.set_stroke(Color(hsl=(4/5, 1, 0.5)), 1.5, opacity=traj_opacity)

            traj_1.add_updater(update_trajectory_Open_dot_1)
            traj_2.add_updater(update_trajectory_Open_dot_2)
            traj_3.add_updater(update_trajectory_Open_dot_3)
            traj_4.add_updater(update_trajectory_Open_dot_4)
            traj_5.add_updater(update_trajectory_Open_dot_5)
            # traj_1.add_updater(update_trajectory_Open_dot_1)
            # traj_1.add_updater(update_trajectory_Open_dot_2)
            # traj_1.add_updater(update_trajectory_Open_dot_3)
            # traj_1.add_updater(update_trajectory_Open_dot_4)
            # traj_1.add_updater(update_trajectory_Open_dot_5)

        else:
            traj = VMobject()
            traj.set_stroke(BLUE, 1.5, opacity=0.8)
            traj.add_updater(update_trajectory_V)

        self.add(traj_1,traj_2,traj_3,traj_4,traj_5)

        def update_position_dot(self,dt):
            x_dot, y_dot, z_dot = aizawa(self.get_center()[ 0 ], self.get_center()[ 1 ], self.get_center()[ 2 ])
            x = x_dot * dt
            y = y_dot * dt
            z = z_dot * dt
            # self.move_to((self.get_x()+x,self.get_y()+y,self.get_z()+z))
            self.shift(x * RIGHT + y * UP + z * OUT)

        dot_1.add_updater(update_position_dot)
        dot_2.add_updater(update_position_dot)
        dot_3.add_updater(update_position_dot)
        dot_4.add_updater(update_position_dot)
        dot_5.add_updater(update_position_dot)

        self.wait(300)

class Aizawa2(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[ -3.5, 3.5 ], y_range=[ -3.5, 3.5 ], z_range=[ -3.5, 3.5 ],
                          x_length=7, y_length=7, z_length=7, axis_config={"include_tip": True, "include_ticks": True, "stroke_width": 1})

        dot_1 = Sphere(radius=0.02, color=Color(hsl=(0, 1, 0.5),)).move_to([0.1,0,0])
        dot_2 = Sphere(radius=0.02, color=Color(hsl=(1/5, 1, 0.5))).move_to([0.2,0,0])
        dot_3 = Sphere(radius=0.02, color=Color(hsl=(2/5, 1, 0.5))).move_to([0.3,0,0])
        dot_4 = Sphere(radius=0.02, color=Color(hsl=(3/5, 1, 0.5))).move_to([0.4,0,0])
        dot_5 = Sphere(radius=0.02, color=Color(hsl=(4/5, 1, 0.5))).move_to([0.5,0,0])

        self.move_camera(phi=60 * DEGREES, zoom=2)
        self.begin_ambient_camera_rotation(rate=0.08)  # Start move camera

        dt = 0.01
        # self.add( dot_1,dot_2,dot_3,dot_4,dot_5)
        self.add(dot_4,dot_5)


        def aizawa(x, y, z, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
            x_dot = (z - b) * x - d * y
            y_dot = d * x + (z - b) * y
            z_dot = c + a * z - z ** 3 / 3 - (x ** 2 + y ** 2) * (1 + e * z) + f * z * x ** 3
            return x_dot, y_dot, z_dot

        def update_trajectory_V(self):
            new_point = self.get_center()
            if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
                self.add_smooth_curve_to(new_point)
        def update_trajectory_Open_dot_1(self):
            new_point = dot_1.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)

        def update_trajectory_Open_dot_2(self):
            new_point = dot_2.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_3(self):
            new_point = dot_3.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_4(self):
            new_point = dot_4.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_5(self):
            new_point = dot_5.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)

        which = 0
        traj_opacity=0.5
        if which == 0:
            traj_1 = OpenGLVMobject()
            traj_1.start_new_path(dot_1.get_center())
            traj_1.set_stroke(Color(hsl=(0, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_2 = OpenGLVMobject()
            traj_2.start_new_path(dot_2.get_center())
            traj_2.set_stroke(Color(hsl=(1/5, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_3 = OpenGLVMobject()
            traj_3.start_new_path(dot_3.get_center())
            traj_3.set_stroke(Color(hsl=(2/5, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_4 = OpenGLVMobject()
            traj_4.start_new_path(dot_4.get_center())
            traj_4.set_stroke(Color(hsl=(3/5, 1, 0.5)), 1.5, opacity=traj_opacity)
            traj_5 = OpenGLVMobject()
            traj_5.start_new_path(dot_5.get_center())
            traj_5.set_stroke(Color(hsl=(4/5, 1, 0.5)), 1.5, opacity=traj_opacity)

            # traj_1.add_updater(update_trajectory_Open_dot_1)
            # traj_2.add_updater(update_trajectory_Open_dot_2)
            # traj_3.add_updater(update_trajectory_Open_dot_3)
            # traj_4.add_updater(update_trajectory_Open_dot_4)
            # traj_5.add_updater(update_trajectory_Open_dot_5)
            # traj_1.add_updater(update_trajectory_Open_dot_1)
            # traj_1.add_updater(update_trajectory_Open_dot_2)
            # traj_1.add_updater(update_trajectory_Open_dot_3)
            traj_5.add_updater(update_trajectory_Open_dot_4)
            traj_5.add_updater(update_trajectory_Open_dot_5)

        else:
            traj = VMobject()
            traj.set_stroke(BLUE, 1.5, opacity=0.8)
            traj.add_updater(update_trajectory_V)

        self.add(traj_1,traj_2,traj_3,traj_4,traj_5)

        def update_position_dot(self,dt):
            x_dot, y_dot, z_dot = aizawa(self.get_center()[ 0 ], self.get_center()[ 1 ], self.get_center()[ 2 ])
            x = x_dot * dt
            y = y_dot * dt
            z = z_dot * dt
            # self.move_to((self.get_x()+x,self.get_y()+y,self.get_z()+z))
            self.shift(x * RIGHT + y * UP + z * OUT)

        dot_1.add_updater(update_position_dot)
        dot_2.add_updater(update_position_dot)
        dot_3.add_updater(update_position_dot)
        dot_4.add_updater(update_position_dot)
        dot_5.add_updater(update_position_dot)

        self.wait(30)


class NoseHoover(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[ -3.5, 3.5 ], y_range=[ -3.5, 3.5 ], z_range=[ -3.5, 3.5 ],
                          x_length=7, y_length=7, z_length=7, axis_config={"include_tip": True, "include_ticks": True, "stroke_width": 1})

        # dot = Sphere(radius=0.05,fill_color=BLUE).move_to(0*RIGHT + 0.1*UP + 0.105*OUT)
        dot_1 = Sphere(radius=0.02, color=Color(hsl=(0, 1, 0.5),)).move_to([1,0,0])
        dot_2 = Sphere(radius=0.02, color=Color(hsl=(1/5, 1, 0.5))).move_to([0.8,0,0])
        dot_3 = Sphere(radius=0.02, color=Color(hsl=(2/5, 1, 0.5))).move_to([0.6,0,0])
        dot_4 = Sphere(radius=0.02, color=Color(hsl=(3/5, 1, 0.5))).move_to([0.4,0,0])
        dot_5 = Sphere(radius=0.02, color=Color(hsl=(4/5, 1, 0.5))).move_to([0.2,0,0])
        # dot_1 = Sphere(radius=0.02, color=Color(hsl=(0, 1, 0.5),)).move_to([1,0,0])
        # dot_2 = Sphere(radius=0.02, color=Color(hsl=(1/5, 1, 0.5))).move_to([0.2,0,0])
        # dot_3 = Sphere(radius=0.02, color=Color(hsl=(2/5, 1, 0.5))).move_to([0.3,0,0])
        # dot_4 = Sphere(radius=0.02, color=Color(hsl=(3/5, 1, 0.5))).move_to([0.4,0,0])
        # dot_5 = Sphere(radius=0.02, color=Color(hsl=(4/5, 1, 0.5))).move_to([0.5,0,0])

        # self.set_camera_orientation(phi=45 * DEGREES,theta=30*DEGREES,gamma = 90*DEGREES)
        self.move_camera(phi=60 * DEGREES, zoom=1.2)
        self.begin_ambient_camera_rotation(rate=0.08)  # Start move camera

        dt = 0.1
        self.add( dot_1)


        def hoover(x, y, z, a=1.5):
            x_dot = y
            y_dot = -x+y*z
            z_dot = a-y**2
            return x_dot, y_dot, z_dot

        def update_trajectory_V(self):
            new_point = self.get_center()
            if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
                self.add_smooth_curve_to(new_point)
        def update_trajectory_Open_dot_1(self):
            new_point = dot_1.get_center()
            if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
                self.add_line_to(new_point)
        which = 0
        traj_opacity=0.8
        if which == 0:
            traj_1 = OpenGLVMobject()
            traj_1.start_new_path(dot_1.get_center())
            traj_1.set_stroke(Color(hsl=(0, 1, 0.5)), 1.5, opacity=traj_opacity)

            traj_1.add_updater(update_trajectory_Open_dot_1)

        else:
            traj = VMobject()
            # traj.start_new_path(dot.get_center())
            traj.set_stroke(BLUE, 1.5, opacity=0.8)
            traj.add_updater(update_trajectory_V)

        self.add(traj_1)
        def update_position_dot(self,dt):
            x_dot, y_dot, z_dot = hoover(self.get_center()[ 0 ], self.get_center()[ 1 ], self.get_center()[ 2 ])
            x = x_dot * 0.01
            y = y_dot * 0.01
            z = z_dot * 0.01
            # self.move_to((self.get_x()+x,self.get_y()+y,self.get_z()+z))
            self.shift(x * RIGHT + y * UP + z * OUT)

        dot_1.add_updater(update_position_dot)
        self.wait(120)

#cairo
class Helicoid(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[ -1.5, 1.5, 0.5 ],
                          y_range=[ -1.5, 1.5, 0.5 ],
                          z_range=[ 0, TAU + PI / 2, PI / 2 ],
                          x_length=6,
                          y_length=6,
                          z_length=6,
                          ).move_to(O)
        #
        # surface = OpenGLSurface(lambda u, v: ((2 + np.cos(3 * u)) * np.cos(2 * u), (2 + np.cos(3 * u)) * np.sin(2 * u), np.sin(3 * u)),
        #                         u_range=[ 0, TAU ], shade_in_3d=True).set_color(color=RED, opacity=0.5)
        # surface = OpenGLSurface(lambda u, v: ((2 + 0.5 * np.cos(v)) * np.cos(u), (2 + 0.5 * np.cos(v)) * np.sin(u), 0.5 * np.sin(v)),
        #                         u_range=[ 0, TAU ], v_range=[ 0, TAU ], shade_in_3d=True).set_color(color=RED, opacity=1)
        # heli = OpenGLSurface(lambda u, v: axes.c2p(u * np.cos(v), u * np.sin(v), v),
        #                      u_range=[ 0, 1 ], v_range=[ 0, TAU ], shade_in_3d=True).set_opacity(0.5)
        # heli = Surface(lambda u, v: axes.c2p(u * np.cos(v), u * np.sin(v), v),
        #                u_range=[ 0, 1 ], v_range=[ 0, TAU ], shade_in_3d=True,stroke_opacity=0.5,fill_opacity=0.5,checkerboard_colors=[ORANGE,ORANGE])
        heli = OpenGLSurface(lambda u, v: axes.c2p(u * np.cos(v), u * np.sin(v), v),
                       u_range=[ 0, 1 ], v_range=[ 0, TAU ], shade_in_3d=True,stroke_opacity=0).set_opacity(0.5)
        graph = ParametricFunction(lambda t: ((2 + np.cos(3 * t)) * np.cos(2 * t), (2 + np.cos(3 * t)) * np.sin(2 * t), np.sin(3 * t)),
                                   t_range=[ 0, TAU ], shade_in_3d=True).set_color(color=RED)


        u_tkr = ValueTracker(0)
        v_tkr = ValueTracker(0)

        # u_var = redraw(lambda: manim.Text(f"u={u_tkr.get_value():.3f} ").shift(L * 4 + U * 3).scale(0.5))
        # v_var = redraw(lambda: manim.Text(f"v={v_tkr.get_value():.3f} ").scale(0.5).next_to(u_var, D))
        # u_var = DecimalNumber(u_tkr.get_value()).shift(L * 4 + U * 3).scale(0.5)
        # u_var.add_updater(lambda num :num.set_value(u_tkr.get_value()))
        # v_var = DecimalNumber(v_tkr.get_value()).scale(0.5).next_to(u_var, D)
        # v_var.add_updater(lambda num :num.set_value(v_tkr.get_value()))


        # self.add_fixed_in_frame_mobjects(u_var)
        # self.add_fixed_in_frame_mobjects(v_var)

        y_vals = [ r'\ang{0}', r"\ang{90}", r"\ang{180}", r"\ang{270}", r'\ang{360}' ]
        # y_vals = [ '0', "0", "0", "0", '0' ]
        y_pos = [ 0, PI / 2, PI, 3 * PI / 2, TAU ]
        y_dict = dict(zip(y_pos, y_vals))

        uv_plane = Axes(y_range=[ 0, 2 * PI, PI / 2 ],
                        x_range=[ 0, 1, 0.2 ],
                        x_length=3,
                        y_length=6,
                        axis_config={
                            "include_tip": False
                        }
                        ).add_coordinates(None, y_dict).shift(L * 4.5)

        def func(u, v):
            return axes.c2p(u * np.cos(v), u * np.sin(v), v)

        def u_var_func(x):

            x.become(Tex(f"u={u_tkr.get_value():.3f} ").scale(0.5).shift(L * 4 + U * 3))
            self.add_fixed_in_frame_mobjects(x)
        def v_var_func(x):

            x.become(Tex(f"v={v_tkr.get_value():.3f} ").scale(0.5).next_to(u_var, D))
            self.add_fixed_in_frame_mobjects(x)

        u_var = Tex(f"u={u_tkr.get_value():.1f} ").scale(0.5).shift(L * 4 + U * 3)
        u_var.add_updater(u_var_func)

        v_var = Tex(f"v={v_tkr.get_value():.3f} ").scale(0.5).next_to(u_var, D)
        v_var.add_updater(v_var_func)


        self.add_fixed_in_frame_mobjects(u_var,v_var)

        self.add(u_var, v_var)

        # dot_2d = redraw(lambda: Dot(color=BLUE).move_to(uv_plane.c2p(u_tkr.get_value(), v_tkr.get_value())))
        dot_2d = Dot(color=BLUE).move_to(uv_plane.c2p(u_tkr.get_value(), v_tkr.get_value()))
        dot_2d.add_updater(lambda x: x.move_to(uv_plane.c2p(u_tkr.get_value(), v_tkr.get_value())))

        dot = redraw(lambda: Sphere(radius=0.1, color=BLUE, shade_in_3d=True, stroke_opacity=0, checkerboard_colors=[BLUE,BLUE]).move_to(func(u_tkr.get_value(), v_tkr.get_value())))
        def uv_line_func(x):

            x.become(uv_plane.get_lines_to_point(dot_2d.get_center()))
            self.add_fixed_in_frame_mobjects(x)

        uv_line=uv_plane.get_lines_to_point(dot_2d.get_center())
        uv_line.add_updater(uv_line_func)
        # heli_and_axes=VGroup(heli, axes, dot)

        self.add(uv_line)

        self.add_fixed_in_frame_mobjects(uv_plane)
        self.add_fixed_in_frame_mobjects(dot_2d)

        self.add(uv_plane)

        self.move_camera(phi=45 * DG, theta=45 * DG)

        # heli.rotate(-45*DG, axis=X).rotate(45*DG, axis=Z)
        # axes
        # axes.rotate(-90*DG, axis=Z)
        # axes.rotate(-135 * DG).rotate(-45 * DG, axis=X)
        self.add(dot)
        self.wait(q)
        self.add(axes)
        self.wait(q)
        self.add(heli)
        #
        # self.add_fixed_in_frame_mobjects(axes)

        # self.add(axes)
        # self.play(Create(axes))
        # self.play(Create(heli))
        # self.play(Create(dot_2d))
        # self.play(Create(dot))

        # self.begin_ambient_camera_rotation(rate=0.08)  # Start move camera

        self.play(u_tkr.animate.set_value(1))
        self.play(v_tkr.animate.set_value(PI))
        self.play(u_tkr.animate.set_value(0.5))
        self.play(v_tkr.animate.set_value(3 * PI / 2))
        # self.stop_ambient_camera_rotation()

        self.move_camera(theta=180 * DG, run_time=3)
        #
        self.wait(5)

        # self.interactive_embed()


