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

config.frame_width = 16
config.frame_height = 9
background_color = W02
from pprint import pprint

class working1(ThreeDScene):

    def scene_1(self):
        def dollar_val_surface(u, v):
            x = u
            y = v
            k = ((1 + x) / (1 + y)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + x) + 0.5 * (1 + y)
            curr_val = hold_val * (1 + z) - 1

            return np.array([ x, y, curr_val ])

        scene_1_axes = ThreeDAxes(x_range=(-0.99, 3, 0.11), y_range=(-0.99, 3, 0.11), z_range=(-1, 3, 0.1),
                                  x_length=5, y_length=5, z_length=5) \
            .rotate(axis=X_AXIS, angle=-90 * DEGREES) \
            .rotate(axis=Y_AXIS, angle=0 * DEGREES) \
            .rotate(axis=X_AXIS, angle=0 * DEGREES)
        lab_x = scene_1_axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = scene_1_axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = scene_1_axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x, lab_y, lab_z)

        scene_1_val_graph = Surface(
            lambda u, v: scene_1_axes.c2p(*dollar_val_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=30
        )

        scene_1_val_graph.set_style(fill_opacity=0.8)
        scene_1_val_graph.set_fill_by_value(axes=scene_1_axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ],
                                            axis=2)

        # VGroup(scene_1_val_graph, scene_1_axes).rotate(axis = X_AXIS, angle = 45*DEGREES)
        # VGroup(scene_1_val_graph, scene_1_axes) \
        #     .rotate(axis=X_AXIS, angle=-60 * DEGREES) \
        #     .rotate(axis=Y_AXIS, angle=-60 * DEGREES) \
        #     .rotate(axis=Z_AXIS, angle=45 * DEGREES)

        return VGroup(scene_1_val_graph, scene_1_axes)

    def scene_2(self):
        mag_tracker = ValueTracker(2)
        current1 = Current(LEFT * 4)
        current2 = Current(RIGHT * 4, direction=IN, magnitude=mag_tracker.get_value())
        field = MagneticField(current1, current2)

        magnet = BarMagnet().rotate(PI/4)
        field = MagneticField(current1, current2,magnet)
        # self.add(field, current1, current2, magnet)
        return VGroup(field, current1, current2, magnet)

    # def scene_2(self):
    #     ax = Axes(
    #         x_range=[ 0, 8.0, 1 ],
    #         y_range=[ -1, 1, 0.2 ],
    #         axis_config={"font_size": 24},
    #     ).add_coordinates()
    #
    #     curve = ax.plot(lambda x: np.sin(x) / np.e ** 2 * x, stroke_width=1.2)
    #
    #     lines = ax.get_vertical_lines_to_graph(
    #         curve, x_range=[ 0, 4 ], num_lines=30, color=BLUE
    #     )
    #
    #     # self.add()
    #
    #     return VGroup(ax, curve, lines)
    #
    def scene_3(self):
        plane = PolarPlane(radius_max=3)
        r = lambda theta: 2 * np.sin(theta * 5)
        graph = plane.plot_polar_graph(r, [ 0, 2 * PI ], color=ORANGE, stroke_width=1.5)
        # self.add(plane, graph)

        return VGroup(plane, graph)

    def scene_4(self):
        charge1 = Charge(-4, LEFT*3.5 )
        charge2 = Charge(2, RIGHT*4+ DOWN*2)
        charge3 = Charge(8, UP * 3)
        charge4 = Charge(-1, RIGHT*7+ U*3.5)
        charge5= Charge(-1,  DOWN*3.5)
        charge6 = Charge(-1, RIGHT*7+ DOWN*2)
        charge7 = Charge(-1, L*7+ DOWN*3)
        field = ElectricField(charge1, charge2, charge3,charge4,charge5, charge6,charge7)
        # self.add(field,charge1, charge2, charge3,charge4,charge5, charge6,charge7)
        return VGroup(field,charge1, charge2, charge3,charge4,charge5, charge6,charge7)
    # def scene_4(self):
    #     scene_4_ax = Axes()
    #     scene_4_a = scene_4_ax.plot_implicit_curve(
    #         lambda x, y: y * (x - y) ** 2 - 4 * x - 8, color=BLUE, stroke_width=1.2
    #     )
    #     # self.add(scene_4_ax, scene_4_a)
    #     return VGroup(scene_4_ax, scene_4_a)

    def scene_5(self):
        scene_4_ax = Axes()
        scene_4_a = scene_4_ax.plot_implicit_curve(
            lambda x, y: y * (x - y) ** 2 - 4 * x - 8, color=BLUE, stroke_width=1.2
        )
        # self.add(scene_4_ax, scene_4_a)
        return VGroup(scene_4_ax, scene_4_a)

    # def scene_5(self):
    #     func = lambda pos: np.sin(pos[ 0 ] / 2) * UR + np.cos(pos[ 1 ] / 2) * LEFT
    #     vf = ArrowVectorField(func, x_range=[ -7, 7, 1 ], stroke_width=2)
    #
    #     length_func = lambda x: x / 3
    #     vf2 = ArrowVectorField(func, x_range=[ -7, 7, 1 ], length_func=length_func)
    #     return VGroup(vf)

    def scene_6(self):
        resolution_fa = 10

        # self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [ 0.0, 0.0 ]
            d = np.linalg.norm(np.array([ x - mu[ 0 ], y - mu[ 1 ] ]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([ x, y, z ])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[ -2, +2 ],
            u_range=[ -2, +2 ]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1, stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        axes = ThreeDAxes(x_range=[ -4, 4 ],
                          y_range=[ -4, 4 ],
                          z_range=[ -4, 4 ]
                          )
        VGroup(axes, gauss_plane).rotate(axis=X_AXIS, angle=-45 * DEGREES)
        return VGroup(axes, gauss_plane)

    def scene_7(self):
        ax = Axes(
            x_range=[ 0, 5 ],
            y_range=[ 0, 6 ],
            x_axis_config={"numbers_to_include": [ 2, 3 ]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[ 0, 4.2 ], color=BLUE_C, stroke_width=1.2)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[ 0, 4.2 ],
            color=GREEN_B, stroke_width=1.2
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[ 0.3, 0.6 ], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [ 2, 3 ], bounded_graph=curve_1, color=GREY, opacity=0.5)

        # self.add(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)
        return VGroup(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)

    def scene_8(self):
        # self.set_camera_orientation(phi=80 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(x_range=[ -6 * PI, +6 * PI, PI / 2 ],
                          y_range=[ -PI, PI, PI / 2 ],
                          z_range=[ -6 * PI, +6 * PI, PI / 2 ],
                          x_length=14,
                          y_length=8,
                          z_length=8
                          ).rotate(axis=X_AXIS, angle=-110 * DEGREES)
        sin_1 = axes.plot(lambda x: np.sin(x - PI), x_range=[ -5 * PI, +5 * PI ], stroke_width=1, stroke_color=RED)
        sin_2 = axes.plot(lambda x: np.sin(x), x_range=[ -5 * PI, +5 * PI ], stroke_width=1, stroke_color=BLUE)

        area_1 = axes.get_area(sin_1, x_range=[ -5 * PI, +5 * PI ], color=[ RED ], opacity=0.3, bounded_graph=None)
        area_2 = axes.get_area(sin_2, x_range=[ -5 * PI, +5 * PI ], color=[ BLUE ], opacity=0.3, bounded_graph=None)
        VGroup(sin_1, area_1).rotate(axis=X_AXIS, angle=PI / 2)

        # VGroup(axes, sin_1, sin_2, area_1, area_2)

        return VGroup(axes, sin_1, sin_2, area_1, area_2)

    def scene_9(self):
        num_plane = NumberPlane()

        vec_1 = Arrow(start=O, end=R * 2 + U * 1, buff=0, color=BLUE_E, stroke_width=1)
        vec_2 = Arrow(start=O, end=R * 2 + D * 3, buff=0, color=RED_E, stroke_width=1)
        vec_3 = Arrow(start=R * 2 + U * 1, end=R * 4 + D * (2), buff=0, color=PURPLE, stroke_width=1)
        vec_4 = Arrow(start=R * 2 + D * 3, end=R * 4 + D * (2), buff=0, color=PINK, stroke_width=1)

        area = Polygram([ O, R * 2 + U * 1, R * 4 + D * (2), R * 2 + D * 3 ], fill_color=GREEN, fill_opacity=0.5, stroke_opacity=0)

        # self.add(num_plane, vec_1, vec_2, vec_3, vec_4, area)

        return VGroup(num_plane, vec_1, vec_2, vec_3, vec_4, area)

    def scene_10(self):
        cw = CurvedArrow(start_point=2 * RIGHT, end_point=2 * UP, stroke_width=1.4).rotate(about_point=O, angle=PI / 4).flip(axis=Y_AXIS)
        cw.add(Tex('CW').next_to(cw, U))
        m0 = Matrix([ [ r"x'" ],
                      [ r"y'" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        equal_1 = MathTex('=')
        m1 = Matrix([ [ r'cos\theta', r'sin\theta', 0 ],
                      [ r'-sin\theta', r'cos\theta', 0 ],
                      [ 0, 0, 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        m1.add(SurroundingRectangle(m1.get_rows()[ 2 ], stroke_width=1.2))
        m1.add(SurroundingRectangle(m1.get_columns()[ 2 ], color=RED, stroke_width=1.2))

        m2 = Matrix([ [ r"x" ],
                      [ r"y" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        ccw = CurvedArrow(start_point=2 * RIGHT, end_point=2 * UP, stroke_width=1.4).rotate(about_point=O, angle=PI / 4)
        ccw.add(Tex('CCW').next_to(ccw, U))

        n0 = Matrix([ [ r"x'" ],
                      [ r"y'" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        equal_2 = MathTex('=')
        n1 = Matrix([ [ r'cos\theta', r'-sin\theta', 0 ],
                      [ r'sin\theta', r'cos\theta', 0 ],
                      [ 0, 0, 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        n1.add(SurroundingRectangle(n1.get_rows()[ 2 ], color=GREEN, stroke_width=1.2))
        n1.add(SurroundingRectangle(n1.get_columns()[ 2 ], color=BLUE, stroke_width=1.2))

        n2 = Matrix([ [ r"x" ],
                      [ r"y" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))

        row1 = VGroup(cw, m0, equal_1, m1, m2).arrange(R)
        row2 = VGroup(ccw, n0, equal_2, n1, n2).arrange(R)

        VGroup(row1, row2).arrange(D)
        row2.move_to(get_moved_coor_based_submob(row2, equal_2.get_center(), [ equal_1.get_x(), row2.get_y(), 0 ]))
        # self.add(row1, row2)

        return VGroup(row1, row2)

    def scene_11(self):
        mtex_1 = MathTex(r'\Phi(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{\frac{(x-\mu)^2}{2\sigma^2}}').scale(3)
        mtex_1[ 0 ][ 12 ].set_color(RED)
        mtex_1[ 0 ][ 13: ].set_color(GREEN)
        mtex_1[ 0 ][ 5:12 ].set_color(BLUE)

        return VGroup(mtex_1)

    def scene_12(self):

        array = [ [ 1, 0.62, 0.6, 0.55 ],
                  [ 0.62, 1, 0.64, 0.76 ],
                  [ 0.6, 0.64, 1, 0.7 ],
                  [ 0.55, 0.76, 0.7, 1 ] ]
        sqs = VGroup()
        for row in array:
            for num in row:
                sq = Square(stroke_opacity=0, fill_opacity=1, fill_color=Color(hsl=(0.33, 0.9, (-0.8 / 0.45) * num + (0.1 + (0.8 / 0.45)))))
                if num < 1:
                    text = Tex(num, color=BLACK)
                else:
                    text = Tex(num)

                sq.add(text)
                sqs.add(sq)

        sqs.arrange_in_grid(4, 4, buff=0).scale(0.8)
        labels = VGroup()
        text_list = [ 'Acetic', 'H2S', 'Lactic', 'Taste' ]
        for num, label in zip([ 0, 4, 8, 12 ], text_list):
            labels.add(Tex(f'{label}').scale(0.85).rotate(PI / 2).next_to(sqs[ num ], L))

        for num, label in zip([ 12, 13, 14, 15 ], text_list):
            labels.add(Tex(f'{label}').scale(0.85).next_to(sqs[ num ], D))

        index_bar = Rectangle(stroke_opacity=0, width=0.5, height=sqs.height, fill_opacity=1, fill_color=[ Color(hsl=(0.33, 0.9, 0.1)),
                                                                                                           Color(hsl=(0.33, 0.9, 0.9)) ],
                              sheen_direction=D).next_to(sqs,
                                                         R)

        index_1 = Tex(1).next_to(index_bar, R).align_to(index_bar, U).scale(0.8)
        index_055 = Tex(0.55).next_to(index_bar, R).align_to(index_bar, D).scale(0.8)
        # self.add(sqs, labels, index_bar,index_1,index_055)
        return VGroup(sqs, labels, index_bar, index_1, index_055)

    def scene_13(self):
        func = lambda pos: np.sin(pos[ 0 ]) * UR + np.cos(pos[ 1 ]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[ -3, 3, 0.2 ], y_range=[ -2, 2, 0.2 ], padding=1
        )

        spawning_area = Rectangle(width=6, height=4, stroke_width=1)
        flowing_area = Rectangle(width=8, height=6, stroke_width=1)
        labels = [ Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5) ]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        # self.add(stream_lines, spawning_area, flowing_area, *labels)
        return VGroup(stream_lines, spawning_area, flowing_area, *labels)

    def scene_14(self):
        text = Tex(r'"Bitcoin is real money"').scale(2).to_edge(U)
        arrow = MathTex(r'\Downarrow').scale(2)
        mtex_1 = Tex(r'SHA256 Hash').scale(2).shift(U * 2)
        mtex_1.add(SurroundingRectangle(mtex_1, stroke_width=1.2).scale(1.5))
        hash = Tex(r'060a3201f182042b\\'
                   r'837357d8732eceec\\'
                   r'35fa0b3d2889f9bc\\'
                   r'ad13399d3653298f').scale(2).to_edge(D)

        VGroup(text, arrow, mtex_1, hash).arrange(D)
        return VGroup(text, arrow, mtex_1, hash)

    def scene_15(self):
        torus = Torus().shift(U * 0.5)
        obj1 = Dodecahedron(graph_config={"edge_config": {'stroke_opacity': 0}},
                            faces_config={'stroke_width': 0.5, 'fill_color': RED, 'fill_opacity': 0.5}).to_edge(UR).shift(U * 0.5 + R * 0.3)
        # obj1 = Dodecahedron({'edge_config':{'stroke_width':1}}).to_edge(UR).shift(U*0.5)
        obj2 = Icosahedron(graph_config={"edge_config": {'stroke_width': 0.5}},
                           faces_config={'stroke_width': 0.5, 'fill_color': GREEN, 'fill_opacity': 0.5}).scale(1.6).to_edge(UL).shift(
            U * 0.5)
        obj3 = Octahedron(graph_config={"edge_config": {'stroke_width': 0.5}},
                          faces_config={'stroke_width': 0.5, 'fill_color': PURPLE, 'fill_opacity': 0.5}).scale(1.8).to_edge(DL).shift(
            R * 0.2)
        obj4 = Tetrahedron(graph_config={"edge_config": {'stroke_width': 0.5}},
                           faces_config={'stroke_width': 0.5, 'fill_color': YELLOW, 'fill_opacity': 0.5}).scale(2).to_edge(DR,
                                                                                                                           buff=0.8).shift(
            L * 0.5)

        VGroup(torus, obj1, obj2, obj3, obj4).rotate(axis=X_AXIS, angle=-45 * DEGREES)

        # self.add(torus,obj1, obj2,obj3,obj4)
        return VGroup(torus, obj1, obj2, obj3, obj4)

    def scene_16(self):
        plane = ComplexPlane().add_coordinates()
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW).scale(2)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW).scale(2)
        label1 = MathTex("2+i").scale(2).next_to(d1, UR, 0.1).set_z_index(1.5)
        label1.add(BackgroundRectangle(label1))
        label2 = MathTex("-3-2i").scale(2).next_to(d2, UL, 0.1).set_z_index(1.5)
        label2.add(BackgroundRectangle(label2))

        return VGroup(plane, d1, label1, d2, label2)

    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        sq_center = Rectangle(width=2, height=15, stroke_opacity=0, fill_opacity=1, fill_color=[ W02, WHITE, W02 ]).shift(
            L * 4.5).set_z_index(
            0.1)
        sq_left = Rectangle(width=7, height=15, stroke_opacity=0, fill_opacity=1, fill_color=[ W02 ]).set_z_index(0.1).next_to(
            sq_center, L, buff=-0.01)
        sq_right = Rectangle(width=6.5, height=15, stroke_opacity=0, fill_opacity=1, fill_color=[ W02 ]).set_z_index(
            0.1).next_to(sq_center, R, buff=-0.01)
        sq_center.set_sheen_direction(R)
        sqs = VGroup(sq_center, sq_left, sq_right).shift(D * 3)

        slide_svg = SVGMobject('slide.svg', fill_color='#787878', fill_opacity=1).scale(2).set_z_index(0.2).shift(D * 3)
        VGroup(slide_svg, sqs).shift(R * 0.7)
        stem_cutout = SVGMobject('stem_updated.svg', fill_color=BLACK, fill_opacity=1, stroke_opacity=0).scale(3).set_z_index(0.2).shift(U * 1.2)
        stem_cutout.save_state()

        slider_circle = Circle(0.88, fill_color='#E6E8EB', fill_opacity=1, stroke_opacity=0).set_z_index(0.5).shift(D * 3)
        slider_arrow = VMobject(stroke_color='#8A929B').set_points_as_corners(
            [ [ -0.5, 0.5, 0 ], [ 0, 0, 0 ], [ -0.5, -0.5, 0 ] ]).set_z_index(5).scale(0.8).move_to(slider_circle).set_z_index(0.5)
        slider_flim = Circle(1, fill_color='#787878', fill_opacity=1, stroke_opacity=0).set_z_index(0.3).move_to(slider_circle)
        slider = VGroup(slider_circle, slider_arrow, slider_flim).shift(L * 3.5)

        stem_box = Rectangle(width=stem_cutout.width - 0.1, height=stem_cutout.height - 0.1, fill_color='#787878', fill_opacity=1,
                             stroke_opacity=0).move_to(stem_cutout)
        slide_box = RoundedRectangle(width=9, height=2, corner_radius=1, stroke_opacity=0).shift(D * 3).set_z_index(0.4)

        slide_box.add_updater(lambda slide_box: slide_box.become(
            RoundedRectangle(width=3.5 - (slider.get_x()) + 2, height=2, corner_radius=1, stroke_opacity=0).shift(
                R * (0.5 * slider.get_x() + 3.5 * 0.5)).set_z_index(0.4).shift(D * 3)))
        cutout = Cutout(Square(20, stroke_opacity=0, fill_opacity=1, fill_color=BLACK), slide_box, stem_box, stroke_opacity=0,
                        fill_opacity=1,
                        fill_color=BLACK).set_z_index(0.4)

        cutout.add_updater(lambda cutout: cutout.become(
            Cutout(Square(20, stroke_opacity=0, fill_opacity=1, fill_color=RED), slide_box, stem_box, stroke_opacity=0, fill_opacity=1,
                   fill_color=BLACK).set_z_index(0.4)))

        slide_stuff = VGroup(slide_svg, sqs, slide_box, slider, cutout)
        slide_stuff.save_state()

        stem_film = Square(fill_opacity=1, fill_color=WHITE)

        self.add(slide_svg, sqs, slide_box, cutout, slider, stem_cutout)

        sqs.save_state()
        self.play(sqs.animate.shift(R * 8), run_time=1.5)
        sqs.restore()
        self.play(sqs.animate.shift(R * 8), run_time=1.5)
        self.play(slider.animate(rate_func=rush_into).shift(R * 7), run_time=0.4)
        self.remove(slide_svg, sqs, cutout, stem_cutout)
        # self.wait(q)
        self.play(AnimationGroup(FadeOut(slider_circle),
                                 FadeOut(slider_flim),
                                 FadeOut(slider_arrow), run_time=0.1)
                  )

        # self.play(Flash(Dot(fill_opacity=0).shift(R*3.5),color='#787878', line_length=1,
        #     num_lines=30,flash_radius=1+SMALL_BUFF,
        #     time_width=0.3),run_time=2)

        stem_svg = SVGMobject('stem.svg', fill_color=RED, fill_opacity=0.5)

        frames = VGroup(
            *[ RoundedRectangle(width=16 / 4 * 0.9, height=9 / 4 * 0.9, corner_radius=0.3, stroke_width=1.5) for i in
               range(16) ]).arrange_in_grid(4, 4, buff=18)
        frames.save_state()
        frame_pos = [ ]
        for frame in frames:
            frame_pos.append(frame.get_center())
        # self.play(Create(frames))
        self.add(frames)
        self.play(frames.animate.arrange_in_grid(4, 4))
        #
        scene_1_mobs = self.scene_1().scale(0.325).move_to(frames[ 0 ])
        scene_2_mobs = self.scene_2().scale(0.18).move_to(frames[ 1 ])
        scene_3_mobs = self.scene_3().scale(0.3).move_to(frames[ 2 ])
        scene_4_mobs = self.scene_4().scale(0.17).move_to(frames[ 3 ]).shift(U*0.05)
        scene_5_mobs = self.scene_5().scale(0.225).move_to(frames[ 4 ])
        scene_6_mobs = self.scene_6().scale(0.225).move_to(frames[ 5 ])
        scene_7_mobs = self.scene_7().scale(0.225).move_to(frames[ 6 ])
        scene_8_mobs = self.scene_8().scale(0.225).move_to(frames[ 7 ])
        scene_9_mobs = self.scene_9().scale(0.21).move_to(frames[ 8 ])
        scene_10_mobs = self.scene_10().scale(0.32).move_to(frames[ 9 ])
        scene_11_mobs = self.scene_11().scale(0.225).move_to(frames[ 10 ])
        scene_12_mobs = self.scene_12().scale(0.27).move_to(frames[ 11 ])
        scene_13_mobs = self.scene_13().scale(0.3).move_to(frames[ 12 ])
        scene_14_mobs = self.scene_14().scale(0.225).move_to(frames[ 13 ])
        scene_15_mobs = self.scene_15().scale(0.225).move_to(frames[ 14 ])
        scene_16_mobs = self.scene_16().scale(0.21).move_to(frames[ 15 ])

        self.play(Create(scene_1_mobs),
                  Create(scene_2_mobs),
                  Create(scene_3_mobs),
                  Create(scene_4_mobs),
                  Create(scene_5_mobs),
                  Create(scene_6_mobs),
                  Create(scene_7_mobs),
                  Create(scene_8_mobs),
                  Create(scene_9_mobs),
                  Create(scene_10_mobs),
                  Create(scene_11_mobs),
                  Create(scene_12_mobs),
                  Create(scene_13_mobs),
                  Create(scene_14_mobs),
                  Create(scene_15_mobs),
                  Create(scene_16_mobs),
                  run_time=7, rate_func=exponential_decay)
        self.wait(0.5)
        self.play(FadeOut(scene_1_mobs, target_position=frame_pos[ 0 ]),
                  FadeOut(scene_2_mobs, target_position=frame_pos[ 1 ]),
                  FadeOut(scene_3_mobs, target_position=frame_pos[ 2 ]),
                  FadeOut(scene_4_mobs, target_position=frame_pos[ 3 ]),
                  FadeOut(scene_5_mobs, target_position=frame_pos[ 4 ]),
                  FadeOut(scene_6_mobs, target_position=frame_pos[ 5 ]),
                  FadeOut(scene_7_mobs, target_position=frame_pos[ 6 ]),
                  FadeOut(scene_8_mobs, target_position=frame_pos[ 7 ]),
                  FadeOut(scene_9_mobs, target_position=frame_pos[ 8 ]),
                  FadeOut(scene_10_mobs, target_position=frame_pos[ 9 ]),
                  FadeOut(scene_11_mobs, target_position=frame_pos[ 10 ]),
                  FadeOut(scene_12_mobs, target_position=frame_pos[ 11 ]),
                  FadeOut(scene_13_mobs, target_position=frame_pos[ 12 ]),
                  FadeOut(scene_14_mobs, target_position=frame_pos[ 13 ]),
                  FadeOut(scene_15_mobs, target_position=frame_pos[ 14 ]),
                  FadeOut(scene_16_mobs, target_position=frame_pos[ 15 ]),
                  Restore(frames),
                  run_time=1)
        self.play(Restore(frames), run_time=0.5)

        title_1 = Tex('Visual').scale(3).set_z_index(1).shift(U * 1.5 + L * 2)
        title_2 = Tex('STEM').scale(2.8).set_z_index(1).shift(R * 1)
        VGroup(title_1, title_2).move_to(O).shift(U * 0.7)

        eyelid_up = ArcBetweenPoints(L * 2 + D * 0.1, R * 2 + D * 0.1, radius=-2.5, stroke_width=3)
        eyelid_dn = ArcBetweenPoints(L * 2 + U * 0.1, R * 2 + U * 0.1, radius=2.5, stroke_width=3)
        iris = Annulus(inner_radius=0.5, outer_radius=0.9, stroke_opacity=0, fill_color=WHITE, fill_opacity=1)

        eyelash_1 = Line(start=eyelid_up.point_from_proportion(0.2), end=L * 1.7 + U * 1.1, stroke_width=2)
        eyelash_2 = Line(start=eyelid_up.point_from_proportion(0.5),
                         end=eyelid_up.point_from_proportion(0.5) + U * (eyelash_1.get_length()), stroke_width=2)
        eyelash_3 = Line(start=eyelid_up.point_from_proportion(0.8), end=R * 1.7 + U * 1.1, stroke_width=2)

        eye = VGroup(eyelid_up, eyelid_dn, iris, eyelash_1, eyelash_2, eyelash_3).scale(0.15).next_to(title_1[ 0 ][ 0 ], U, buff=0.15).set_z_index(1)

        slide_stuff.restore()
        slide_svg = SVGMobject('slide_start.svg', fill_color='#787878', fill_opacity=1).scale(2).set_z_index(0.2).shift(D * 3).shift(
            R * 1.2)

        cutout.clear_updaters()
        cutout.add_updater(lambda cutout: cutout.become(
            Cutout(Square(20, stroke_opacity=0, fill_opacity=1, fill_color=RED), slide_box, stroke_opacity=0, fill_opacity=1,
                   fill_color=BLACK).set_z_index(0.4)))

        self.add(slide_svg, sqs, slide_box, slider, cutout)
        self.play(Write(VGroup(eye, title_1, title_2)),
                  sqs.animate.shift(R * 7),
                  run_time=1)
        self.play(slider.animate(rate_func=rush_into).shift(R * 7), run_time=0.4)
        self.remove(slide_svg, sqs, cutout)
        # self.wait(q)
        self.play(AnimationGroup(FadeOut(slider_circle),
                                 FadeOut(slider_flim),
                                 FadeOut(slider_arrow),
                                 run_time=0.1)
                  )
        self.play(FadeOut(VGroup(eye, title_1, title_2), scale=3), run_time=0.7)
        self.add(scene_1_mobs,
                 scene_2_mobs,
                 scene_3_mobs,
                 scene_4_mobs,
                 scene_5_mobs,
                 scene_6_mobs,
                 scene_7_mobs,
                 scene_8_mobs,
                 scene_9_mobs,
                 scene_10_mobs,
                 scene_11_mobs,
                 scene_12_mobs,
                 scene_13_mobs,
                 scene_14_mobs,
                 scene_15_mobs,
                 scene_16_mobs,
                 )
        #
        self.wait(10)


class test(ThreeDScene):

    def scene_1(self):
        def dollar_val_surface(u, v):
            x = u
            y = v
            k = ((1 + x) / (1 + y)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + x) + 0.5 * (1 + y)
            curr_val = hold_val * (1 + z) - 1

            return np.array([ x, y, curr_val ])

        scene_1_axes = ThreeDAxes(x_range=(-0.99, 3, 0.11), y_range=(-0.99, 3, 0.11), z_range=(-1, 3, 0.1),
                                  x_length=5, y_length=5, z_length=5) \
            .rotate(axis=X_AXIS, angle=-90 * DEGREES) \
            .rotate(axis=Y_AXIS, angle=0 * DEGREES) \
            .rotate(axis=X_AXIS, angle=0 * DEGREES)
        lab_x = scene_1_axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = scene_1_axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = scene_1_axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x, lab_y, lab_z)

        scene_1_val_graph = Surface(
            lambda u, v: scene_1_axes.c2p(*dollar_val_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=30
        )

        scene_1_val_graph.set_style(fill_opacity=0.8)
        scene_1_val_graph.set_fill_by_value(axes=scene_1_axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ],
                                            axis=2)

        # VGroup(scene_1_val_graph, scene_1_axes).rotate(axis = X_AXIS, angle = 45*DEGREES)
        # VGroup(scene_1_val_graph, scene_1_axes) \
        #     .rotate(axis=X_AXIS, angle=-60 * DEGREES) \
        #     .rotate(axis=Y_AXIS, angle=-60 * DEGREES) \
        #     .rotate(axis=Z_AXIS, angle=45 * DEGREES)

        return VGroup(scene_1_val_graph, scene_1_axes)

    def scene_2(self):
        mag_tracker = ValueTracker(2)
        current1 = Current(LEFT * 4)
        current2 = Current(RIGHT * 4, direction=IN, magnitude=mag_tracker.get_value())
        field = MagneticField(current1, current2)

        magnet = BarMagnet().rotate(PI/4)
        field = MagneticField(current1, current2,magnet)
        # self.add(field, current1, current2, magnet)
        return VGroup(field, current1, current2, magnet)

    # def scene_2(self):
    #     ax = Axes(
    #         x_range=[ 0, 8.0, 1 ],
    #         y_range=[ -1, 1, 0.2 ],
    #         axis_config={"font_size": 24},
    #     ).add_coordinates()
    #
    #     curve = ax.plot(lambda x: np.sin(x) / np.e ** 2 * x, stroke_width=1.2)
    #
    #     lines = ax.get_vertical_lines_to_graph(
    #         curve, x_range=[ 0, 4 ], num_lines=30, color=BLUE
    #     )
    #
    #     # self.add()
    #
    #     return VGroup(ax, curve, lines)
    #
    def scene_3(self):
        plane = PolarPlane(radius_max=3)
        r = lambda theta: 2 * np.sin(theta * 5)
        graph = plane.plot_polar_graph(r, [ 0, 2 * PI ], color=ORANGE, stroke_width=1.5)
        # self.add(plane, graph)

        return VGroup(plane, graph)

    def scene_4(self):
        charge1 = Charge(-4, LEFT*3.5 )
        charge2 = Charge(2, RIGHT*4+ DOWN*2)
        charge3 = Charge(8, UP * 3)
        charge4 = Charge(-1, RIGHT*7+ U*3.5)
        charge5= Charge(-1,  DOWN*3.5)
        charge6 = Charge(-1, RIGHT*7+ DOWN*2)
        charge7 = Charge(-1, L*7+ DOWN*3)
        field = redraw(lambda: ElectricField(charge1, charge2, charge3,charge4,charge5, charge6,charge7))
        # self.add(field,charge1, charge2, charge3,charge4,charge5, charge6,charge7)
        return VGroup(field,charge1, charge2, charge3,charge4,charge5, charge6,charge7)
    # def scene_4(self):
    #     scene_4_ax = Axes()
    #     scene_4_a = scene_4_ax.plot_implicit_curve(
    #         lambda x, y: y * (x - y) ** 2 - 4 * x - 8, color=BLUE, stroke_width=1.2
    #     )
    #     # self.add(scene_4_ax, scene_4_a)
    #     return VGroup(scene_4_ax, scene_4_a)

    def scene_5(self):
        scene_4_ax = Axes()
        scene_4_a = scene_4_ax.plot_implicit_curve(
            lambda x, y: y * (x - y) ** 2 - 4 * x - 8, color=BLUE, stroke_width=1.2
        )
        # self.add(scene_4_ax, scene_4_a)
        return VGroup(scene_4_ax, scene_4_a)
    # def scene_5(self):
    #     func = lambda pos: np.sin(pos[ 0 ] / 2) * UR + np.cos(pos[ 1 ] / 2) * LEFT
    #     vf = ArrowVectorField(func, x_range=[ -7, 7, 1 ], stroke_width=2)
    #
    #     length_func = lambda x: x / 3
    #     vf2 = ArrowVectorField(func, x_range=[ -7, 7, 1 ], length_func=length_func)
    #     return VGroup(vf)

    def scene_6(self):
        resolution_fa = 10

        # self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [ 0.0, 0.0 ]
            d = np.linalg.norm(np.array([ x - mu[ 0 ], y - mu[ 1 ] ]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([ x, y, z ])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[ -2, +2 ],
            u_range=[ -2, +2 ]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1, stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        axes = ThreeDAxes(x_range=[ -4, 4 ],
                          y_range=[ -4, 4 ],
                          z_range=[ -4, 4 ]
                          )
        VGroup(axes, gauss_plane).rotate(axis=X_AXIS, angle=-45 * DEGREES)
        return VGroup(axes, gauss_plane)

    def scene_7(self):
        ax = Axes(
            x_range=[ 0, 5 ],
            y_range=[ 0, 6 ],
            x_axis_config={"numbers_to_include": [ 2, 3 ]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[ 0, 4.2 ], color=BLUE_C, stroke_width=1.2)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[ 0, 4.2 ],
            color=GREEN_B, stroke_width=1.2
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[ 0.3, 0.6 ], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [ 2, 3 ], bounded_graph=curve_1, color=GREY, opacity=0.5)

        # self.add(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)
        return VGroup(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)

    def scene_8(self):
        # self.set_camera_orientation(phi=80 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(x_range=[ -6 * PI, +6 * PI, PI / 2 ],
                          y_range=[ -PI, PI, PI / 2 ],
                          z_range=[ -6 * PI, +6 * PI, PI / 2 ],
                          x_length=14,
                          y_length=8,
                          z_length=8
                          ).rotate(axis=X_AXIS, angle=-110 * DEGREES)
        sin_1 = axes.plot(lambda x: np.sin(x - PI), x_range=[ -5 * PI, +5 * PI ], stroke_width=1, stroke_color=RED)
        sin_2 = axes.plot(lambda x: np.sin(x), x_range=[ -5 * PI, +5 * PI ], stroke_width=1, stroke_color=BLUE)

        area_1 = axes.get_area(sin_1, x_range=[ -5 * PI, +5 * PI ], color=[ RED ], opacity=0.3, bounded_graph=None)
        area_2 = axes.get_area(sin_2, x_range=[ -5 * PI, +5 * PI ], color=[ BLUE ], opacity=0.3, bounded_graph=None)
        VGroup(sin_1, area_1).rotate(axis=X_AXIS, angle=PI / 2)

        # VGroup(axes, sin_1, sin_2, area_1, area_2)

        return VGroup(axes, sin_1, sin_2, area_1, area_2)

    def scene_9(self):
        num_plane = NumberPlane()

        vec_1 = Arrow(start=O, end=R * 2 + U * 1, buff=0, color=BLUE_E, stroke_width=1)
        vec_2 = Arrow(start=O, end=R * 2 + D * 3, buff=0, color=RED_E, stroke_width=1)
        vec_3 = Arrow(start=R * 2 + U * 1, end=R * 4 + D * (2), buff=0, color=PURPLE, stroke_width=1)
        vec_4 = Arrow(start=R * 2 + D * 3, end=R * 4 + D * (2), buff=0, color=PINK, stroke_width=1)

        area = Polygram([ O, R * 2 + U * 1, R * 4 + D * (2), R * 2 + D * 3 ], fill_color=GREEN, fill_opacity=0.5, stroke_opacity=0)

        # self.add(num_plane, vec_1, vec_2, vec_3, vec_4, area)

        return VGroup(num_plane, vec_1, vec_2, vec_3, vec_4, area)

    def scene_10(self):
        cw = CurvedArrow(start_point=2 * RIGHT, end_point=2 * UP, stroke_width=1.4).rotate(about_point=O, angle=PI / 4).flip(axis=Y_AXIS)
        cw.add(Tex('CW').next_to(cw, U))
        m0 = Matrix([ [ r"x'" ],
                      [ r"y'" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        equal_1 = MathTex('=')
        m1 = Matrix([ [ r'cos\theta', r'sin\theta', 0 ],
                      [ r'-sin\theta', r'cos\theta', 0 ],
                      [ 0, 0, 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        m1.add(SurroundingRectangle(m1.get_rows()[ 2 ], stroke_width=1.2))
        m1.add(SurroundingRectangle(m1.get_columns()[ 2 ], color=RED, stroke_width=1.2))

        m2 = Matrix([ [ r"x" ],
                      [ r"y" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        ccw = CurvedArrow(start_point=2 * RIGHT, end_point=2 * UP, stroke_width=1.4).rotate(about_point=O, angle=PI / 4)
        ccw.add(Tex('CCW').next_to(ccw, U))

        n0 = Matrix([ [ r"x'" ],
                      [ r"y'" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        equal_2 = MathTex('=')
        n1 = Matrix([ [ r'cos\theta', r'-sin\theta', 0 ],
                      [ r'sin\theta', r'cos\theta', 0 ],
                      [ 0, 0, 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))
        n1.add(SurroundingRectangle(n1.get_rows()[ 2 ], color=GREEN, stroke_width=1.2))
        n1.add(SurroundingRectangle(n1.get_columns()[ 2 ], color=BLUE, stroke_width=1.2))

        n2 = Matrix([ [ r"x" ],
                      [ r"y" ],
                      [ 1 ] ], element_alignment_corner=np.array([ 0., 0., 0. ]))

        row1 = VGroup(cw, m0, equal_1, m1, m2).arrange(R)
        row2 = VGroup(ccw, n0, equal_2, n1, n2).arrange(R)

        VGroup(row1, row2).arrange(D)
        row2.move_to(get_moved_coor_based_submob(row2, equal_2.get_center(), [ equal_1.get_x(), row2.get_y(), 0 ]))
        # self.add(row1, row2)

        return VGroup(row1, row2)

    def scene_11(self):
        mtex_1 = MathTex(r'\Phi(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{\frac{(x-\mu)^2}{2\sigma^2}}').scale(3)
        mtex_1[ 0 ][ 12 ].set_color(RED)
        mtex_1[ 0 ][ 13: ].set_color(GREEN)
        mtex_1[ 0 ][ 5:12 ].set_color(BLUE)

        return VGroup(mtex_1)

    def scene_12(self):

        array = [ [ 1, 0.62, 0.6, 0.55 ],
                  [ 0.62, 1, 0.64, 0.76 ],
                  [ 0.6, 0.64, 1, 0.7 ],
                  [ 0.55, 0.76, 0.7, 1 ] ]
        sqs = VGroup()
        for row in array:
            for num in row:
                sq = Square(stroke_opacity=0, fill_opacity=1, fill_color=Color(hsl=(0.33, 0.9, (-0.8 / 0.45) * num + (0.1 + (0.8 / 0.45)))))
                if num < 1:
                    text = Tex(num, color=BLACK)
                else:
                    text = Tex(num)

                sq.add(text)
                sqs.add(sq)

        sqs.arrange_in_grid(4, 4, buff=0).scale(0.8)
        labels = VGroup()
        text_list = [ 'Acetic', 'H2S', 'Lactic', 'Taste' ]
        for num, label in zip([ 0, 4, 8, 12 ], text_list):
            labels.add(Tex(f'{label}').scale(0.85).rotate(PI / 2).next_to(sqs[ num ], L))

        for num, label in zip([ 12, 13, 14, 15 ], text_list):
            labels.add(Tex(f'{label}').scale(0.85).next_to(sqs[ num ], D))

        index_bar = Rectangle(stroke_opacity=0, width=0.5, height=sqs.height, fill_opacity=1, fill_color=[ Color(hsl=(0.33, 0.9, 0.1)),
                                                                                                           Color(hsl=(0.33, 0.9, 0.9)) ],
                              sheen_direction=D).next_to(sqs,
                                                         R)

        index_1 = Tex(1).next_to(index_bar, R).align_to(index_bar, U).scale(0.8)
        index_055 = Tex(0.55).next_to(index_bar, R).align_to(index_bar, D).scale(0.8)
        # self.add(sqs, labels, index_bar,index_1,index_055)
        return VGroup(sqs, labels, index_bar, index_1, index_055)

    def scene_13(self):
        func = lambda pos: np.sin(pos[ 0 ]) * UR + np.cos(pos[ 1 ]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[ -3, 3, 0.2 ], y_range=[ -2, 2, 0.2 ], padding=1
        )

        spawning_area = Rectangle(width=6, height=4, stroke_width=1)
        flowing_area = Rectangle(width=8, height=6, stroke_width=1)
        labels = [ Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5) ]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        # self.add(stream_lines, spawning_area, flowing_area, *labels)
        return VGroup(stream_lines, spawning_area, flowing_area, *labels)

    def scene_14(self):
        text = Tex(r'"Bitcoin is real money"').scale(2).to_edge(U)
        arrow = MathTex(r'\Downarrow').scale(2)
        mtex_1 = Tex(r'SHA256 Hash').scale(2).shift(U * 2)
        mtex_1.add(SurroundingRectangle(mtex_1, stroke_width=1.2).scale(1.5))
        hash = Tex(r'060a3201f182042b\\'
                   r'837357d8732eceec\\'
                   r'35fa0b3d2889f9bc\\'
                   r'ad13399d3653298f').scale(2).to_edge(D)

        VGroup(text, arrow, mtex_1, hash).arrange(D)
        return VGroup(text, arrow, mtex_1, hash)

    def scene_15(self):
        torus = Torus().shift(U * 0.5)
        obj1 = Dodecahedron(graph_config={"edge_config": {'stroke_opacity': 0}},
                            faces_config={'stroke_width': 0.5, 'fill_color': RED, 'fill_opacity': 0.5}).to_edge(UR).shift(U * 0.5 + R * 0.3)
        # obj1 = Dodecahedron({'edge_config':{'stroke_width':1}}).to_edge(UR).shift(U*0.5)
        obj2 = Icosahedron(graph_config={"edge_config": {'stroke_width': 0.5}},
                           faces_config={'stroke_width': 0.5, 'fill_color': GREEN, 'fill_opacity': 0.5}).scale(1.6).to_edge(UL).shift(
            U * 0.5)
        obj3 = Octahedron(graph_config={"edge_config": {'stroke_width': 0.5}},
                          faces_config={'stroke_width': 0.5, 'fill_color': PURPLE, 'fill_opacity': 0.5}).scale(1.8).to_edge(DL).shift(
            R * 0.2)
        obj4 = Tetrahedron(graph_config={"edge_config": {'stroke_width': 0.5}},
                           faces_config={'stroke_width': 0.5, 'fill_color': YELLOW, 'fill_opacity': 0.5}).scale(2).to_edge(DR,
                                                                                                                           buff=0.8).shift(
            L * 0.5)

        VGroup(torus, obj1, obj2, obj3, obj4).rotate(axis=X_AXIS, angle=-45 * DEGREES)

        # self.add(torus,obj1, obj2,obj3,obj4)
        return VGroup(torus, obj1, obj2, obj3, obj4)

    def scene_16(self):
        plane = ComplexPlane().add_coordinates()
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW).scale(2)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW).scale(2)
        label1 = MathTex("2+i").scale(2).next_to(d1, UR, 0.1).set_z_index(1.5)
        label1.add(BackgroundRectangle(label1))
        label2 = MathTex("-3-2i").scale(2).next_to(d2, UL, 0.1).set_z_index(1.5)
        label2.add(BackgroundRectangle(label2))

        return VGroup(plane, d1, label1, d2, label2)

    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        sq_center = Rectangle(width=2, height=15, stroke_opacity=0, fill_opacity=1, fill_color=[ W02, WHITE, W02 ]).shift(
            L * 4.5).set_z_index(
            0.1)
        sq_left = Rectangle(width=7, height=15, stroke_opacity=0, fill_opacity=1, fill_color=[ W02 ]).set_z_index(0.1).next_to(
            sq_center, L, buff=-0.01)
        sq_right = Rectangle(width=6.5, height=15, stroke_opacity=0, fill_opacity=1, fill_color=[ W02 ]).set_z_index(
            0.1).next_to(sq_center, R, buff=-0.01)
        sq_center.set_sheen_direction(R)
        sqs = VGroup(sq_center, sq_left, sq_right).shift(D * 3)

        slide_svg = SVGMobject('slide.svg', fill_color='#787878', fill_opacity=1).scale(2).set_z_index(0.2).shift(D * 3)
        VGroup(slide_svg, sqs).shift(R * 0.7)
        stem_cutout = SVGMobject('stem_updated.svg', fill_color=BLACK, fill_opacity=1, stroke_opacity=0).scale(3).set_z_index(0.2).shift(U * 1.2)
        stem_cutout.save_state()

        slider_circle = Circle(0.88, fill_color='#E6E8EB', fill_opacity=1, stroke_opacity=0).set_z_index(0.5).shift(D * 3)
        slider_arrow = VMobject(stroke_color='#8A929B').set_points_as_corners(
            [ [ -0.5, 0.5, 0 ], [ 0, 0, 0 ], [ -0.5, -0.5, 0 ] ]).set_z_index(5).scale(0.8).move_to(slider_circle).set_z_index(0.5)
        slider_flim = Circle(1, fill_color='#787878', fill_opacity=1, stroke_opacity=0).set_z_index(0.3).move_to(slider_circle)
        slider = VGroup(slider_circle, slider_arrow, slider_flim).shift(L * 3.5)

        stem_box = Rectangle(width=stem_cutout.width - 0.1, height=stem_cutout.height - 0.1, fill_color='#787878', fill_opacity=1,
                             stroke_opacity=0).move_to(stem_cutout)
        slide_box = RoundedRectangle(width=9, height=2, corner_radius=1, stroke_opacity=0).shift(D * 3).set_z_index(0.4)

        slide_box.add_updater(lambda slide_box: slide_box.become(
            RoundedRectangle(width=3.5 - (slider.get_x()) + 2, height=2, corner_radius=1, stroke_opacity=0).shift(
                R * (0.5 * slider.get_x() + 3.5 * 0.5)).set_z_index(0.4).shift(D * 3)))
        cutout = Cutout(Square(20, stroke_opacity=0, fill_opacity=1, fill_color=BLACK), slide_box, stem_box, stroke_opacity=0,
                        fill_opacity=1,
                        fill_color=BLACK).set_z_index(0.4)

        cutout.add_updater(lambda cutout: cutout.become(
            Cutout(Square(20, stroke_opacity=0, fill_opacity=1, fill_color=RED), slide_box, stem_box, stroke_opacity=0, fill_opacity=1,
                   fill_color=BLACK).set_z_index(0.4)))

        slide_stuff = VGroup(slide_svg, sqs, slide_box, slider, cutout)
        slide_stuff.save_state()

        stem_film = Square(fill_opacity=1, fill_color=WHITE)

        # self.add(slide_svg, sqs, slide_box, cutout, slider, stem_cutout)
        #
        # sqs.save_state()
        # self.play(sqs.animate.shift(R * 8), run_time=1.5)
        # sqs.restore()
        # self.play(sqs.animate.shift(R * 8), run_time=1.5)
        # self.play(slider.animate(rate_func=rush_into).shift(R * 7), run_time=0.4)
        # self.remove(slide_svg, sqs, cutout, stem_cutout)
        # # self.wait(q)
        # self.play(AnimationGroup(FadeOut(slider_circle),
        #                          FadeOut(slider_flim),
        #                          FadeOut(slider_arrow), run_time=0.1)
        #           )

        # self.play(Flash(Dot(fill_opacity=0).shift(R*3.5),color='#787878', line_length=1,
        #     num_lines=30,flash_radius=1+SMALL_BUFF,
        #     time_width=0.3),run_time=2)

        stem_svg = SVGMobject('stem.svg', fill_color=RED, fill_opacity=0.5)

        frames = VGroup(
            *[ RoundedRectangle(width=16 / 4 * 0.9, height=9 / 4 * 0.9, corner_radius=0.3, stroke_width=1.5) for i in
               range(16) ]).arrange_in_grid(4, 4, buff=18)
        frames.save_state()
        frame_pos = [ ]
        for frame in frames:
            frame_pos.append(frame.get_center())
        # self.play(Create(frames))
        self.add(frames.arrange_in_grid(4, 4))
        # self.play(frames.animate.arrange_in_grid(4, 4))
        #
        scene_1_mobs = self.scene_1().scale(0.325).move_to(frames[ 0 ])
        scene_2_mobs = self.scene_2().scale(0.18).move_to(frames[ 1 ])
        scene_3_mobs = self.scene_3().scale(0.3).move_to(frames[ 2 ])
        scene_4_mobs = self.scene_4().scale(0.17).move_to(frames[ 3 ]).shift(U*0.05)
        scene_5_mobs = self.scene_5().scale(0.225).move_to(frames[ 4 ])
        scene_6_mobs = self.scene_6().scale(0.225).move_to(frames[ 5 ])
        scene_7_mobs = self.scene_7().scale(0.225).move_to(frames[ 6 ])
        scene_8_mobs = self.scene_8().scale(0.225).move_to(frames[ 7 ])
        scene_9_mobs = self.scene_9().scale(0.21).move_to(frames[ 8 ])
        scene_10_mobs = self.scene_10().scale(0.32).move_to(frames[ 9 ])
        scene_11_mobs = self.scene_11().scale(0.225).move_to(frames[ 10 ])
        scene_12_mobs = self.scene_12().scale(0.27).move_to(frames[ 11 ])
        scene_13_mobs = self.scene_13().scale(0.3).move_to(frames[ 12 ])
        scene_14_mobs = self.scene_14().scale(0.225).move_to(frames[ 13 ])
        scene_15_mobs = self.scene_15().scale(0.225).move_to(frames[ 14 ])
        scene_16_mobs = self.scene_16().scale(0.21).move_to(frames[ 15 ])

        # self.play(Create(scene_1_mobs),
        #           Create(scene_2_mobs),
        #           Create(scene_3_mobs),
        #           Create(scene_4_mobs),
        #           Create(scene_5_mobs),
        #           Create(scene_6_mobs),
        #           Create(scene_7_mobs),
        #           Create(scene_8_mobs),
        #           Create(scene_9_mobs),
        #           Create(scene_10_mobs),
        #           Create(scene_11_mobs),
        #           Create(scene_12_mobs),
        #           Create(scene_13_mobs),
        #           Create(scene_14_mobs),
        #           Create(scene_15_mobs),
        #           Create(scene_16_mobs),
        #           run_time=7, rate_func=exponential_decay)
        # self.wait(0.5)
        # self.play(FadeOut(scene_1_mobs, target_position=frame_pos[ 0 ]),
        #           FadeOut(scene_2_mobs, target_position=frame_pos[ 1 ]),
        #           FadeOut(scene_3_mobs, target_position=frame_pos[ 2 ]),
        #           FadeOut(scene_4_mobs, target_position=frame_pos[ 3 ]),
        #           FadeOut(scene_5_mobs, target_position=frame_pos[ 4 ]),
        #           FadeOut(scene_6_mobs, target_position=frame_pos[ 5 ]),
        #           FadeOut(scene_7_mobs, target_position=frame_pos[ 6 ]),
        #           FadeOut(scene_8_mobs, target_position=frame_pos[ 7 ]),
        #           FadeOut(scene_9_mobs, target_position=frame_pos[ 8 ]),
        #           FadeOut(scene_10_mobs, target_position=frame_pos[ 9 ]),
        #           FadeOut(scene_11_mobs, target_position=frame_pos[ 10 ]),
        #           FadeOut(scene_12_mobs, target_position=frame_pos[ 11 ]),
        #           FadeOut(scene_13_mobs, target_position=frame_pos[ 12 ]),
        #           FadeOut(scene_14_mobs, target_position=frame_pos[ 13 ]),
        #           FadeOut(scene_15_mobs, target_position=frame_pos[ 14 ]),
        #           FadeOut(scene_16_mobs, target_position=frame_pos[ 15 ]),
        #           Restore(frames),
        #           run_time=1)
        # self.play(Restore(frames), run_time=0.5)

        title_1 = Tex('Visual').scale(3).set_z_index(1).shift(U * 1.5 + L * 2)
        title_2 = Tex('STEM').scale(2.8).set_z_index(1).shift(R * 1)
        VGroup(title_1, title_2).move_to(O).shift(U * 0.7)

        eyelid_up = ArcBetweenPoints(L * 2 + D * 0.1, R * 2 + D * 0.1, radius=-2.5, stroke_width=3)
        eyelid_dn = ArcBetweenPoints(L * 2 + U * 0.1, R * 2 + U * 0.1, radius=2.5, stroke_width=3)
        iris = Annulus(inner_radius=0.5, outer_radius=0.9, stroke_opacity=0, fill_color=WHITE, fill_opacity=1)

        eyelash_1 = Line(start=eyelid_up.point_from_proportion(0.2), end=L * 1.7 + U * 1.1, stroke_width=2)
        eyelash_2 = Line(start=eyelid_up.point_from_proportion(0.5),
                         end=eyelid_up.point_from_proportion(0.5) + U * (eyelash_1.get_length()), stroke_width=2)
        eyelash_3 = Line(start=eyelid_up.point_from_proportion(0.8), end=R * 1.7 + U * 1.1, stroke_width=2)

        eye = VGroup(eyelid_up, eyelid_dn, iris, eyelash_1, eyelash_2, eyelash_3).scale(0.15).next_to(title_1[ 0 ][ 0 ], U, buff=0.15).set_z_index(1)

        slide_stuff.restore()
        slide_svg = SVGMobject('slide_start.svg', fill_color='#787878', fill_opacity=1).scale(2).set_z_index(0.2).shift(D * 3).shift(
            R * 1.2)

        cutout.clear_updaters()
        cutout.add_updater(lambda cutout: cutout.become(
            Cutout(Square(20, stroke_opacity=0, fill_opacity=1, fill_color=RED), slide_box, stroke_opacity=0, fill_opacity=1,
                   fill_color=BLACK).set_z_index(0.4)))

        # self.add(slide_svg, sqs, slide_box, slider, cutout)
        # self.play(Write(VGroup(eye, title_1, title_2)),
        #           sqs.animate.shift(R * 7),
        #           run_time=1)
        # self.play(slider.animate(rate_func=rush_into).shift(R * 7), run_time=0.4)
        # self.remove(slide_svg, sqs, cutout)
        # # self.wait(q)
        # self.play(AnimationGroup(FadeOut(slider_circle),
        #                          FadeOut(slider_flim),
        #                          FadeOut(slider_arrow),
        #                          run_time=0.1)
        #           )
        # self.play(FadeOut(VGroup(eye, title_1, title_2), scale=3), run_time=0.7)
        self.add(scene_1_mobs,
                 scene_2_mobs,
                 scene_3_mobs,
                 scene_4_mobs,
                 scene_5_mobs,
                 scene_6_mobs,
                 scene_7_mobs,
                 scene_8_mobs,
                 scene_9_mobs,
                 scene_10_mobs,
                 scene_11_mobs,
                 scene_12_mobs,
                 scene_13_mobs,
                 scene_14_mobs,
                 scene_15_mobs,
                 scene_16_mobs,
                 )
        #
        # self.wait(10)
