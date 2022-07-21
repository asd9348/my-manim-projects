
class working3(Scene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(5))

        speak(self, title='Scene2', txt=
        '원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        my_svg = SVGMobject('ethereum-eth-logo.svg').set_z_index(4).shift(U * 2)
        my_svg[ 1 ].set_color('#F2F2F2')
        my_svg[ 3 ].set_color('#F2F2F2')
        my_svg[ 0 ].set_color('#B7C2E9')
        my_svg[ 2 ].set_color('#B7C2E9')
        my_svg[ 5 ].set_color('#B7C2E9')
        my_svg[ 4 ].set_color('#7A90E2')

        eth_circle = Circle(color='#5D78DE', fill_color='#5D78DE', fill_opacity=1, radius=1.5).set_z_index(3).shift(U * 2)

        eco_element_1 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=RED).set_z_index(1)
        eco_element_2 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=GREEN).set_z_index(0.5)
        eco_element_3 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=BLUE).set_z_index(1)
        eco_element_4 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=TEAL).set_z_index(1)
        eco_element_5 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=YELLOW).set_z_index(1)
        eco_element_6 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=MAROON).set_z_index(1)
        eco_element_7 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=PURPLE).set_z_index(1)

        rotation_val_tracker = ValueTracker(1)

        elem_group = VGroup(eco_element_1, eco_element_2, eco_element_3, eco_element_4, eco_element_5, eco_element_6, eco_element_7)
        dir_dict = {0: 0.8975979010256552, 1: 1.7951958020513104, 2: 2.6927937030769655, 3: 3.5903916041026207, 4: 4.487989505128276,
                    5: 5.385587406153931, 6: 6.283185307179586}

        elem_group[ 0 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 1 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 2 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 3 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 4 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 5 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 6 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * 3, 0 ])))

        eco_element_line_1 = Line(eco_element_1.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        eco_element_line_2 = Line(eco_element_2.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        eco_element_line_3 = Line(eco_element_3.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        eco_element_line_4 = Line(eco_element_4.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        eco_element_line_5 = Line(eco_element_5.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        eco_element_line_6 = Line(eco_element_6.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        eco_element_line_7 = Line(eco_element_7.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)
        line_group = VGroup(eco_element_line_1, eco_element_line_2, eco_element_line_3, eco_element_line_4, eco_element_line_5,
                            eco_element_line_6, eco_element_line_7)
        line_group = VGroup(eco_element_line_1, eco_element_line_2, eco_element_line_3, eco_element_line_4, eco_element_line_5,
                            eco_element_line_6, eco_element_line_7)

        eco_element_line_1.add_updater(
            lambda x: x.become(Line(eco_element_1.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_2.add_updater(
            lambda x: x.become(Line(eco_element_2.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_3.add_updater(
            lambda x: x.become(Line(eco_element_3.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_4.add_updater(
            lambda x: x.become(Line(eco_element_4.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_5.add_updater(
            lambda x: x.become(Line(eco_element_5.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_6.add_updater(
            lambda x: x.become(Line(eco_element_6.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_7.add_updater(
            lambda x: x.become(Line(eco_element_7.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))

        # self.play(AnimationGroup(Create(elem_group, rate_func=smooth), rotation_val_tracker.animate(rate_func=smooth).set_value(6)),
        #           rate_func=linear, run_time=5)
        # self.play(rotation_val_tracker.animate.set_value(6),run_time=3)
        # self.play(Create(line_group, rate_func=rush_into), run_time=2)

        self.play(AnimationGroup(DrawBorderThenFill(my_svg), DrawBorderThenFill(eth_circle), run_time=1.5))

        dex = LabeledDot('DEX', color=WHITE, radius=1).set_z_index(0.5).move_to(eth_circle)
        self.play(dex.animate.move_to(D * 1),run_time=1)

        clock_min_angle = ValueTracker(PI / 2)
        clock_hour_angle = ValueTracker(PI / 2)
        clock_circle = Circle(color=WHITE)
        clock_center_dot = Dot(color=WHITE)
        clock_min_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=3, buff=0,
                                 max_stroke_width_to_length_ratio=100)
        clock_hour_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                  max_stroke_width_to_length_ratio=100)
        clock_min_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=5, buff=0,
                                                              max_stroke_width_to_length_ratio=100)))
        clock_hour_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                                               max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)))
        clock = VGroup(clock_circle, clock_center_dot, clock_min_handle, clock_hour_handle)

        self.wait(0.5)
        self.play(dex.animate.shift(L * 3),
                  Create(clock.shift(D * 1)))

        wbtc_coin = create_circle_asset(Tex(r'\textbf{WBTC}', color=WHITE, font_size=40), radius=0.97, stroke_width=20,
                                        stroke_opacity=1,
                                        stroke_color=C_ETH, fill_color=C_BTC).shift(D * 1 + R * 3)
        self.play(AnimationGroup(AnimationGroup(clock_min_angle.animate.set_value(PI / 2 - 4 * 2 * PI),
                                                clock_hour_angle.animate.set_value(PI / 2 - 4 * 2 * PI / 12)),
                                 FadeIn(wbtc_coin,target_position=clock),lag_ratio= 0.7, run_time=4))

        self.wait(5)
        self.wait(2)


class working2(Scene):
    def construct(self):

        my_svg = SVGMobject('ethereum-eth-logo.svg').set_z_index(4)
        my_svg[ 1 ].set_color('#F2F2F2')
        my_svg[ 3 ].set_color('#F2F2F2')
        my_svg[ 0 ].set_color('#B7C2E9')
        my_svg[ 2 ].set_color('#B7C2E9')
        my_svg[ 5 ].set_color('#B7C2E9')
        my_svg[ 4 ].set_color('#7A90E2')

        eth_circle = Circle(color='#5D78DE', fill_color='#5D78DE', fill_opacity=1, radius=1.5).set_z_index(3)
        self.play(AnimationGroup(DrawBorderThenFill(my_svg), DrawBorderThenFill(eth_circle), run_time=3))

        eco_element_1 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=RED).set_z_index(1)
        eco_element_2 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=GREEN).set_z_index(0.5)
        eco_element_3 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=BLUE).set_z_index(1)
        eco_element_4 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=TEAL).set_z_index(1)
        eco_element_5 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=YELLOW).set_z_index(1)
        eco_element_6 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=MAROON).set_z_index(1)
        eco_element_7 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=PURPLE).set_z_index(1)

        rotation_val_tracker = ValueTracker(1)

        elem_group = VGroup(eco_element_1, eco_element_2, eco_element_3, eco_element_4, eco_element_5, eco_element_6, eco_element_7)
        dir_dict = {0: 0.8975979010256552, 1: 1.7951958020513104, 2: 2.6927937030769655, 3: 3.5903916041026207, 4: 4.487989505128276,
                    5: 5.385587406153931, 6: 6.283185307179586}

        elem_group[ 0 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 1 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 2 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 3 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 4 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 5 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * 3, 0 ])))
        elem_group[ 6 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * 3,
              sin(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * 3, 0 ])))

        eco_element_line_1 = Line(eco_element_1.get_center(), eth_circle.get_center(), color=WHITE)
        eco_element_line_2 = Line(eco_element_2.get_center(), eth_circle.get_center(), color=WHITE)
        eco_element_line_3 = Line(eco_element_3.get_center(), eth_circle.get_center(), color=WHITE)
        eco_element_line_4 = Line(eco_element_4.get_center(), eth_circle.get_center(), color=WHITE)
        eco_element_line_5 = Line(eco_element_5.get_center(), eth_circle.get_center(), color=WHITE)
        eco_element_line_6 = Line(eco_element_6.get_center(), eth_circle.get_center(), color=WHITE)
        eco_element_line_7 = Line(eco_element_7.get_center(), eth_circle.get_center(), color=WHITE)
        line_group = VGroup(eco_element_line_1, eco_element_line_2, eco_element_line_3, eco_element_line_4, eco_element_line_5,
                            eco_element_line_6, eco_element_line_7)

        eco_element_line_1.add_updater(
            lambda x: x.become(Line(eco_element_1.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_2.add_updater(
            lambda x: x.become(Line(eco_element_2.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_3.add_updater(
            lambda x: x.become(Line(eco_element_3.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_4.add_updater(
            lambda x: x.become(Line(eco_element_4.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_5.add_updater(
            lambda x: x.become(Line(eco_element_5.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_6.add_updater(
            lambda x: x.become(Line(eco_element_6.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))
        eco_element_line_7.add_updater(
            lambda x: x.become(Line(eco_element_7.get_center(), eth_circle.get_center(), color=WHITE).set_z_index(0)))

        self.play(AnimationGroup(Create(elem_group, rate_func=smooth), rotation_val_tracker.animate(rate_func=smooth).set_value(6)),
                  rate_func=linear, run_time=5)
        # self.play(rotation_val_tracker.animate.set_value(6),run_time=3)
        self.play(Create(line_group, rate_func=rush_into), run_time=2)
        self.wait(5)



class working3(Scene):
    config.frame_width = 16 * 4
    config.frame_height = 9 * 4

    def construct(self):

        self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '아#1'
              , keep_pitch=True, update=True, speed=1.4)


        item_list = [ 'Mathmatical Physics',
                      'Fluid Dynamics',
                      'Numerical Analysis',
                      'Optimization',
                      'Probability Theory',
                      'Statistics',
                      'Financial Mathmatics',
                      'Game Theory',
                      ]

        def bezier_branch_creater(item_list=[ ], font_size=20, str8_start_width=1, str8_end_width=1, branch=5, branch_width=2,
                                  branch_height=7, direction=np.array((-1.0, 0.0, 0.0))):
            start_line = Line(ORIGIN, direction)
            clearance = branch_height / (branch - 1)
            branches = VGroup()

            for i in range(branch):
                curve = CubicBezier(direction,
                                    direction + direction * (branch_width / 2),
                                    direction + direction * (branch_width / 2) + U * ((branch_height / 2) - clearance * i),
                                    direction + direction * (branch_width) + U * ((branch_height / 2) - clearance * i))

                end_line = Line(curve.get_end(), curve.get_end() + direction * str8_end_width)
                bezier = VGroup(start_line.copy(), curve, end_line)
                if len(item_list) != 0:
                    text = Tex(item_list[ i ], font_size=font_size).next_to(end_line, U + direction).align_to(end_line, direction * (-1))
                    bezier.add(text)

                branches.add(bezier)

            return branches

        my_br = bezier_branch_creater(item_list=item_list,
                                      str8_start_width=2,
                                      str8_end_width=2,
                                      branch=8,
                                      branch_width=1,
                                      branch_height=6,
                                      direction=L)

        self.play(Create(my_br))

        self.wait(5)


class working3(Scene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '아#1'
              , keep_pitch=True, update=True, speed=1.4)

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
        self.play(a_intersection_b.animate.to_edge(UR, buff=1))

        a_difference_b_form = MathTex(r'A-B=').shift(R * 1)

        a_difference_b_shape = Difference(set_1, set_2, fill_color=RED_D, fill_opacity=0.8)

        self.play(Create(a_difference_b_form))
        self.play(Create(a_difference_b_shape))
        self.play(a_difference_b_shape.animate.scale(0.3).rotate(-PI / 3).next_to(a_difference_b_form, R))

        a_difference_b = VGroup(a_difference_b_form, a_difference_b_shape)
        self.play(a_difference_b.animate.next_to(a_intersection_b, D, buff=0.5, aligned_edge=L))

        a_union_b_inter_c_form = MathTex(r'A\cup B\cap C=').shift(R * 1)

        a_union_b_inter_c_shape = Intersection(Union(set_1, set_2), set_3, fill_color=PURPLE_D, fill_opacity=0.8)
        self.play(Create(a_union_b_inter_c_form))
        self.play(Create(a_union_b_inter_c_shape))
        self.play(a_union_b_inter_c_shape.animate.scale(0.3).rotate(PI / 3).next_to(a_union_b_inter_c_form, R))

        a_union_b_inter_c = VGroup(a_union_b_inter_c_form, a_union_b_inter_c_shape)
        self.play(a_union_b_inter_c.animate.next_to(a_difference_b, D, buff=0.5, aligned_edge=L))

        self.wait(5)



class working3(ThreeDScene):
    def func(self, u, v):
        line = Line(ORIGIN, L)

        r = 0.5
        height = 2
        x = u
        y = v

        z = (2 * x + 3 * y - 12) / 4
        return np.array([ (12 - 3 * y - 4 * z) / 2, (-2 * x - 4 * z + 12) / 3, (2 * x + 3 * y - 12) / 4 ])

    def construct(self):
        # self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES,gamma=45*DEGREES)

        # self.add(Square().shift(np.array([ 0, 0, 4 ])).rotate(PI / 2, axis=X_AXIS))
        # axes = ThreeDAxes()
        # cylinder = Cylinder(radius=2, height=3)
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, cylinder)

        # self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        # prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        # prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        # self.add(prismSmall, prismLarge)

        axes = ThreeDAxes(x_range=[ -4, 4 ], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[ -3, 3 ],
            v_range=[ 0, 2 * PI ],
            resolution=(32, 32)
        )
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(axes, surface)

        self.wait(5)


class working3(ThreeDScene):
    def construct(self):
        resolution_fa = 45
        self.set_camera_orientation(phi=75 * DEGREES, theta=-75 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        # def param_surface(u, v):
        #     x = u
        #     y = v
        #     z = np.sin(x) * np.cos(y)
        #     return z
        # surface_plane = Surface(
        #     lambda u, v: axes.c2p(u, v, param_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[0, 5],
        #     u_range=[0, 5],
        #     )
        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        face = ThreeDVMobject()
        face.set_points_as_corners([
            [ 1, 0, 0 ],
            [ 1, 0, 5 ],
            [ 0, 1, 5 ],
            [ 0, 1, 0 ],
            [ 1, 0, 0 ]
        ])

        face.set_fill(color=RED, opacity=0.5)
        face.set_stroke(color=RED_E,width=3,opacity=0.7)


        self.add(axes, face)

class working3(ThreeDScene):
    def imp_loss_surface(self, u, v):
        x = u
        y = v
        k = ((1 + x) / (1 + y)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        # hold_val = 0.5*x+0.5*y
        # z = np.sin(x) * np.cos(y)
        return np.array([x, y, z])

    def dollar_val_surface(self, u, v):
        x = u
        y = v
        k = ((1 + x) / (1 + y)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + x) + 0.5 * (1 + y)-1
        curr_val = hold_val*(1+z)

        return np.array([x, y, curr_val])

    def construct(self):
        resolution_fa = 15
        self.set_camera_orientation(phi=90*DEGREES, theta=0,gamma=0)
        axes = ThreeDAxes(x_range=(-1, 3, 1), y_range=(-1, 3, 1), z_range=(-1, 2, 0.5),
                          x_length=5,y_length=5,z_length=5)


        lab_x = axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x,lab_y,lab_z)


        imp_loss_graph = Surface(
            lambda u, v: axes.c2p(*self.imp_loss_surface(u, v)),
            v_range=[-0.99, 2],
            u_range=[-0.99, 2],
            color=PINK
            )

        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface(u, v)),
            v_range=[-0.99, 2],
            u_range=[-0.99, 2],
            color=BLUE
            )

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

        my_graph = axes.plot(lambda x : x, x_range=[-1,5])
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
        self.add(axes,labs)
        # self.play(Create(val_graph),run_time=5)
        self.add(val_graph)
        # self.play(Create(my_graph))
        # self.play(my_graph.animate.set_color_by_gradient([RED,BLUE,GREEN]),run_time=3)
        # self.play(my_graph.animate.set_color(RED),run_time=3)
        # self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 5)
        # self.begin_ambient_camera_rotation(rate=0.2, about="theta",run_time=1)
        # self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        # self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES,gamma=0)

        self.move_camera(theta=PI/2, about="theta",run_time=5)
        self.move_camera(theta=2*PI/2, about="theta",run_time=5)
        self.move_camera(theta=3*PI/2, about="theta",run_time=5)
        self.move_camera(theta=4*PI/2, about="theta",run_time=5)
        self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        self.move_camera(theta=PI/2, about="theta",run_time=5)
        self.move_camera(theta=2*PI/2, about="theta",run_time=5)
        self.move_camera(theta=3*PI/2, about="theta",run_time=5)
        self.move_camera(theta=4*PI/2, about="theta",run_time=5)
        self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        self.move_camera(theta=PI/2, about="theta",run_time=5)
        self.move_camera(theta=2*PI/2, about="theta",run_time=5)
        self.move_camera(theta=3*PI/2, about="theta",run_time=5)
        self.move_camera(theta=4*PI/2, about="theta",run_time=5)



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

class working3(MovingCameraScene):

    def construct(self):

        self.camera.frame.save_state()

        numberline = NumberLine(x_range=[ 0, 5.5, 1 ],
                                length=14,
                                include_numbers=True,
                                include_tip=True,
                                stroke_color=RED,
                                stroke_width=6,
                                longer_tick_multiple=3,
                                )

        self.add(index_labels(numberline[ 3 ]).shift(D * 1))

        self.add(numberline)

        i = 0
        for tick in numberline[ 2 ]:
            if i == 0:
                self.play(self.camera.frame.animate(rate_func=linear).scale(0.5).move_to(tick))
                i = i + 1
            else:
                self.play(self.camera.frame.animate(rate_func=linear).move_to(tick))

        self.play(Restore(self.camera.frame, rate_func=linear))

        # self.play(Create(numberline))

class working4(Scene):
    def construct(self):
        screen_verticl_pixel = 100
        screen_horizontal_pixel = 100
        screen = VGroup()

        for l in np.linspace(0, 1, screen_horizontal_pixel):
            for h in np.linspace(0, 1, screen_verticl_pixel):
                pixel = Square(0.1, fill_color=Color(hsl=(h, 1, l)), fill_opacity=1, stroke_opacity=0)
                screen.add(pixel)

        screen.arrange_in_grid(screen_verticl_pixel, screen_horizontal_pixel, buff=0).scale(0.5)

        self.play(Create(screen))

        self.play(screen.animate.arrange_in_grid(screen_verticl_pixel, screen_horizontal_pixel, buff=0.05))
        self.play(screen.animate.arrange_in_grid(screen_verticl_pixel, screen_horizontal_pixel, buff=0))

        # self.add(screen)
class working1(MovingCameraScene):
    def construct(self):
        self.add(NumberPlane())
        circle = Circle().scale(0.7).shift(R * 4 + U * 2)
        circles = VGroup(*[ Circle() for i in range(4) ]).arrange_in_grid(rows=2, cols=2, buff=0)

        self.play(Create(circle),
                  Create(circles))
        self.add(index_labels(circles))
        self.play(circles.animate.move_to(get_moved_coor_based_submob(circles, circles[ 1 ].get_center(), circle.get_center())))

        self.wait(5)
class working1(MovingCameraScene):
    def construct(self):
        self.add(NumberPlane())
        # self.camera.frame.save_state()
        #
        # circle = Circle(radius=1)
        # x_label = DecimalNumber(33333).next_to(circle, D)
        # y_label = DecimalNumber(45645).next_to(circle, L)
        #
        # self.play(Create(circle),
        #           Create(x_label),
        #           Create(y_label))
        # self.wait(q)
        #
        # scaler = 0.3
        # # dist = np.sqrt(circle.get_x() ** 2 + circle.get_y() ** 2)
        #
        # circle.add_updater(
        #     lambda mob: mob.scale_to_fit_height(2 + np.sqrt(circle.get_x() ** 2 + circle.get_y() ** 2) * scaler).set_color(
        #         Color(hue=1, saturation=np.sqrt(circle.get_x() ** 2 + circle.get_y() ** 2) / 9.17, luminance=0.5)))
        # x_label.add_updater(lambda mob: mob.become(DecimalNumber(circle.get_x()).next_to(circle, D)))
        # y_label.add_updater(lambda mob: mob.become(DecimalNumber(circle.get_y()).next_to(circle, L)))
        #
        # self.play(circle.animate.shift(L * 3))
        # self.play(circle.animate.shift(D * 3))
        # self.play(circle.animate.shift(U * 3))
        # self.play(circle.animate.shift(R * 3))
        #
        # self.play(Uncreate(circle))
        # ax = Axes(
        #     x_range=[ 0, 10, 1 ],
        #     y_range=[ 0, 10, 1 ],
        #     x_length=8,
        #     y_length=8
        # )
        # tracker = ValueTracker(1)
        #
        # k_var = Variable(1, 'k', var_type=DecimalNumber, num_decimal_places=2).to_edge(U)
        # k_tracker = k_var.tracker
        # self.play(Create(k_var))
        #
        # x_var = Variable(1, 'x', var_type=DecimalNumber, num_decimal_places=2).to_edge(UR)
        # x_tracker = x_var.tracker
        # self.play(Create(x_var))
        #
        # graph = ax.plot(lambda x: k_tracker.get_value() / x, x_range=[ 0.0001, 10 ], use_smoothing=False)
        # graph.add_updater(lambda graph: graph.become(
        #     ax.plot(lambda x: k_tracker.get_value() / x, x_range=[ k_tracker.get_value() / 10, 10 ], use_smoothing=False)))
        # # x_range = [ k_tracker.get_value() / 6000, 16 ]
        # self.play(Create(ax),
        #           Create(graph))
        #
        # dot = Dot().move_to(ax.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())))
        # dot.add_updater(lambda dot: dot.move_to(ax.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value()))))
        # dot_label = Tex(rf'({x_tracker.get_value():.2f},{graph.underlying_function(x_tracker.get_value()):.2f})').next_to(dot, UR)
        # dot_label.add_updater(lambda jot: jot.become(
        #     Tex(rf'({x_tracker.get_value():.2f},{graph.underlying_function(x_tracker.get_value()):.2f})').next_to(dot, UR)))
        # dot_lines = ax.get_lines_to_point(ax.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())))
        # dot_lines.add_updater(lambda dot_line:dot_line.become(ax.get_lines_to_point(ax.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())))))
        #
        # self.play(Create(dot),
        #           Create(dot_label),
        #           Create(dot_lines))
        #
        # rectangle  = Rectangle(width=dot.get_x() - ax.get_origin()[ 0 ], height=dot.get_y() - ax.get_origin()[ 1 ], color =BLUE, fill_opacity=0.5, stroke_opacity=0).align_to(ax.get_origin(), DL)
        #
        # rectangle.add_updater(lambda x : x.become(Rectangle(width=dot.get_x() - ax.get_origin()[ 0 ], height=dot.get_y() - ax.get_origin()[ 1 ], color =BLUE, fill_opacity=0.5, stroke_opacity=0).align_to(ax.get_origin(), DL)))
        #
        # rect_text = Tex('Area').scale(0.7).move_to(rectangle)
        # rect_text.add_updater(lambda x:x.move_to(rectangle))
        # self.play(Create(rectangle))
        # self.play(Create(rect_text))

        # num_line = NumberLine(x_range=[0,10, 2],length=10, stroke_width=10,
        #                       longer_tick_multiple=5,
        #
        #                       include_numbers=False,
        #                       label_direction=U)
        #
        # num_line.add_labels({2:'2022-07-05',
        #                      4:'2022-07-06',
        #                      6:'2022-07-07',
        #                      8:'2022-07-08',
        #                      10:'2022-07-09',
        #                      })
        #
        # for label in num_line[2]:
        #     label.shift(R*(label.width/2)).rotate(45*DEGREES, about_point=label.get_left())
        # self.add(index_labels(num_line))
        # self.play(Create(num_line))

        ax = Axes()
        sin = ax.plot(lambda x: np.sin(x), stroke_color = [RED, GREEN])
        label = ax.get_graph_label(
            graph=sin,
            label=MathTex(r"\frac{\pi}{2}"),
            x_val=PI / 2,
            dot=True,
            direction=UR,
        )

        tangent_x_var = Variable(-4, 'tan x val', var_type=DecimalNumber).to_edge(U)
        tan_x_tracker = tangent_x_var.tracker

        tan_line_length = 3
        slope = ax.plot(
            lambda x: ax.slope_of_tangent(tan_x_tracker.get_value(), sin) * (x - tan_x_tracker.get_value()) + sin.underlying_function(
                tan_x_tracker.get_value()),
            x_range=[ tan_x_tracker.get_value() - tan_line_length / np.cos(ax.angle_of_tangent(tan_x_tracker.get_value(), sin)) / 2,
                      tan_x_tracker.get_value() + tan_line_length / np.cos(ax.angle_of_tangent(tan_x_tracker.get_value(), sin)) / 2 ])
        slope.add_updater(lambda slope: slope.become(ax.plot(
            lambda x: ax.slope_of_tangent(tan_x_tracker.get_value(), sin) * (x - tan_x_tracker.get_value()) + sin.underlying_function(
                tan_x_tracker.get_value()),
            x_range=[ tan_x_tracker.get_value() - tan_line_length * np.cos(ax.angle_of_tangent(tan_x_tracker.get_value(), sin)) / 2,
                      tan_x_tracker.get_value() + tan_line_length * np.cos(ax.angle_of_tangent(tan_x_tracker.get_value(), sin)) / 2 ])))
        # slope = TangentLine(sin,10*1/16,length=3)


        dashed_sin = DashedVMobject(sin, num_dashes=40, fill_color=[RED, GREEN]).shift(U*3)
        self.play(Create(dashed_sin))

        my_graph = ParametricFunction(lambda x: np.array([ x, np.sin(x), 0 ]), color=RED, t_range=np.array([ -9, 9, 0.01 ]))

        self.add(ax, sin, slope, label)
        self.play(Create(tangent_x_var))

        self.play(tan_x_tracker.animate.set_value(4))

        circle = Circle(fill_opacity=1, fill_color=RED, sheen_factor=-10, sheen_direction=DR)
        # circle = Circle(fill_opacity=1, fill_color=RED).set_sheen.set_color_by_gradient([RED, BLUE])
        self.play(Create(circle))

        # self.play(num_line[2].animate.set_color(RED).scale(2))

        # self.play(k_tracker.animate.set_value(3),
        #           x_tracker.animate.set_value(5))
        # self.play(k_tracker.animate.set_value(1))
        # # graph.clear_updaters()
        # self.play(k_tracker.animate.set_value(5))
        # self.play(k_tracker.animate.set_value(5))
        # self.play(k_tracker.animate.set_value(8)
        #
        # def update_curve(mob):
        #     mob.move_to(moving_dot.get_center())
        #
        # self.camera.frame.add_updater(update_curve)
        #

        # moving_dummy_tracker = ValueTracker(k_tracker.get_value() / 10)
        # # moving_dummy = Dot(color=RED).move_to(ax.c2p(0.5, graph.underlying_function(0.5)))
        # moving_dummy = Dot(color=RED).move_to(graph.get_start())
        # moving_dummy.add_updater(
        #     lambda dot: dot.move_to(ax.c2p(moving_dummy_tracker.get_value(), graph.underlying_function(moving_dummy_tracker.get_value()))))
        # self.play(Create(moving_dummy))
        #
        # # self.play(self.camera.frame.animate.move_to(ORIGIN))
        # # def update_curve(mob):
        # #     mob.move_to(moving_dummy.get_center())
        #
        # self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dummy),run_time=5)
        #
        # self.camera.frame.add_updater(lambda camera: camera.move_to(moving_dummy.get_center()))
        # # self.camera.frame.add_updater(update_curve)
        #
        # # self.play(MoveAlongPath(moving_dummy, graph, rate_func=linear),run_time=5)
        #
        #
        # self.play(moving_dummy_tracker.animate.set_value(10),run_time=8)
        # self.play(Restore(self.camera.frame))
        #

        # self.play(self.camera.frame.scale(0.5).move_to(tick))
        # circles = VGroup(*[ Circle() for i in range(4) ]).arrange_in_grid(rows=2, cols=2, buff=0)

        # self.play(Create(circle),
        #           Create(circles))
        # self.add(index_labels(circles))
        # self.play(circles.animate.move_to(get_moved_coor_based_submob(circles, circles[ 1 ].get_center(), circle.get_center())))
        self.wait(20)


class test_2(VectorScene):
    def construct(self):
        mag_tracker = ValueTracker(2)
        current1 = Current(LEFT * 2.5)

        # current2 = redraw(lambda: Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))
        current2 = Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value())
        # def mag_change(current):
        #     current.magnitude= mag_tracker.get_value()
        # current2.add_updater(mag_change)

        # field = redraw(lambda: MagneticField(current1, current2))
        field = MagneticField(current1, current2)

        sources=[current1, current2]
        def field_update(field):
            field.magnetic_sources = sources

        field.add_updater(field_update)

        # field = MagneticField(current1, current2)
        # field.add_updater(lambda field:field.become(MagneticField(current1, Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))))

        # current2.magnitude=15
        # print(current2.magnitude)

        # print(self.mobjects)

        # current(1)
        self.add(field, current1, current2, index_labels(current2))
        self.wait(1)

        # self.play(field.animate.shift(L*1))

        # self.wait(5)
class test_2(VectorScene):
    def construct(self):
        mag_tracker = ValueTracker(2)
        current1 = Current(LEFT * 4)

        # current2 = redraw(lambda: Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))
        current2 = Current(RIGHT * 4, direction=IN, magnitude=mag_tracker.get_value())
        # def mag_change(current):
        #     current.magnitude= mag_tracker.get_value()
        # current2.add_updater(mag_change)

        # field = redraw(lambda: MagneticField(current1, current2))
        field = MagneticField(current1, current2)

        # sources=[current1, current2]
        # def field_update(field):
        #     field.magnetic_sources = sources
        #
        # field.add_updater(field_update)
        magnet = BarMagnet().rotate(PI/4)
        field = MagneticField(current1, current2,magnet)
        field.add_updater(lambda x: x.become(MagneticField(current1, current2)))

        # def field_fun(field):
        #     updated_field = MagneticField(current1, current2)
        #
        #     return updated_field
        # field.add_updater(field_update)

        # def redraw(func):
        #     mob = func()
        #     mob.add_updater(lambda m: mob.become(func()))
        #     return mob

        # field = MagneticField(current1, current2)
        # field.add_updater(lambda field:field.become(MagneticField(current1, Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))))

        # current2.magnitude=15
        # print(current2.magnitude)

        # print(self.mobjects)

        # current(1)
        # self.add(field,  magnet)
        self.add(field, current1, current2, magnet)

        # field.add_updater()
        # self.wait(1)

        # self.play(field.animate.shift(L*1))

        # self.wait(5)

        # self.play(current1.animate.shift(L * 4))
        # self.play(current2.animate.become(Current(U * 2.5, direction=IN, magnitude=10)))

        # self.play(mag_tracker.animate.set_value(10),
        #           current2.animate.shift(L * 2))

        # self.play()
        # self.play(mag_tracker.animate.set_value(2))
        # self.wait(5)
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

class working1(ThreeDScene):

    def construct(self):
        self.add(NumberPlane(faded_line_ratio=1, x_length=16, y_length=9))

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
                         .scale(scaler).next_to([ -7, 4, 0 ], DR, buff=0)), run_time=5)

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

        self.wait(5)



class working1(ThreeDScene):

    def construct(self):
        ax = Axes(
            x_range=[-10, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},

        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x**3, x_range=[-10, 10], use_smoothing=False)
        self.add(ax, graph)

        x_tracker = ValueTracker(-10)

        def special_text():
            text= manim.Text('Fuck')
            dummy_dot =Dot(fill_opacity=0).next_to(text,D,buff=0.2)
            text.add(dummy_dot)
            text.rotate(ax.angle_of_tangent(x_tracker.get_value(),graph))
            return text.move_to(get_compensated_coor(text, dummy_dot.get_center(),ax.c2p(x_tracker.get_value(),graph.underlying_function(x_tracker.get_value()))))

        text = redraw(special_text)

        self.add(text)

        self.play(x_tracker.animate.set_value(10),run_time=10)

        self.wait(5)
