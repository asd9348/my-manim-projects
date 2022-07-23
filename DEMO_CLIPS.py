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

