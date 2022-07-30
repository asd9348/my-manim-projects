
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
    """불리언 오퍼레이션 테스트"""
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
    """단순 면 생산해보기"""
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
    """반영구적 손실 3디 그래프 그리기"""

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

    """카메라 움직여보기"""
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
    """알지비 박스 반복문으로 만들어보기"""
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
    """compensated move 데모"""
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
    """접선이 사인그래프를 따라 실시간으로 움직이는 것"""

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
    """자기장 필드에서 전류가 흐르는 것"""

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
    """자기장 필드에서 전류가 흐르는 것"""
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
    """구간별로 단절된 그래프 그리기 """

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


class working1(MovingCameraScene):
    """간단한 미적분 애니메이션 """
    def construct(self):

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



class working1(MovingCameraScene):
    """이거는 포물선 그래프 두개, 대쉬라인 여러개 그리고 포물선 라인 따라서 카메라 움직이기 """
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

        self.play(x_tracker.animate.set_value(2.5), run_time=3)
        self.play(x_tracker.animate.set_value(1.5), run_time=3)
        self.play(x_tracker.animate.set_value(2), run_time=3)

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

class working1(ThreeDScene):
    """사각형들 줄줄이 세워놓고 직선으로 끄트머리 잘라서 삼각형 슬라이드 후 회전"""


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
    """텍스트가 곡면의 그래프를 따라 움직이는 것"""

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

class working1(MovingCameraScene):
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


class working1(MovingCameraScene):
    # config.background_color = GRAY
    """이거는 포물선 그래프와 접선 사이의 특이한 모양의 영역을 벡터모브젝트로 따는 것"""

    def construct(self):
        numberplane = NumberPlane()
        axes = Axes(x_range=[ -5, 5 ], y_range=[ -8, 8 ], x_length=6, y_length=9, tips=False, axis_config={'include_numbers': 1})
        graph_1 = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ -3, 5 ]).set_z_index(3)
        # graph_2 = axes.plot(lambda x: -(x - 1)**2 - 1, color = RED, x_range = [ -3, 5 ]).set_z_index(3)

        x_tracker = ValueTracker(2)
        a = 1
        b = 3

        self.camera.frame.save_state()

        self.add(axes, graph_1)

        # axes.slope_of_tangent()

        # x_trkr = ValueTracker(-2)

        my_tan_1 = get_tangent_line(axes, graph_1, -1,line_length=30).set_stroke(color =GREEN)
        my_tan_2 = get_tangent_line(axes, graph_1,3,line_length=30).set_stroke(color =RED)
        self.add(my_tan_1, my_tan_2)

        print(my_tan_1.get_function())

        # self.play(x_trkr.animate.set_value(2),run_time=10)

        path = VMobject()
        graph_1_subpath = axes.plot(lambda x: (x - 1)**2 + 1, color = BLUE, x_range = [ -1, 3 ])
        # graph_1_subpath.reverse_points()
        path.add_subpath(graph_1_subpath.get_all_points())
        # graph_2_subpath = axes.plot(lambda x: -(x - 1)**2 - 1, color = BLUE, x_range = [ 1, 3 ])
        # dot_for_path = Dot(radius=0.3, color=GREEN).move_to(graph_1_b_dot)
        path.add_points_as_corners([ axes.c2p(3, 5), axes.c2p(1, -3) ])
        path.add_points_as_corners([ axes.c2p(1, -3), axes.c2p(-1, 5) ])
        # path.add_points_as_corners(graph_2_subpath.get_all_points())

        path.set_stroke(width = 10, color = PINK).set_z_index(5).set_fill(color=RED, opacity=0.8)
        self.add(path)
        # self.play(Create(path.set_stroke(width =10, color = GREEN)),run_time=20,rate_func=linear)

        # self.play(self.camera.frame.animate.scale(0.5).move_to(dot_for_path))

        # self.play(MoveAlongPath(self.camera.frame, path), run_time=20,rate_func=linear)

        # self.play(Restore(self.camera.frame))

        self.wait(10)
        label_rotation_line = Line(start=[ 0, 0, 0 ], end=[ -1, 1, 0 ])
        label_rotation_line = Line(start=[ 0, 0, 0 ], end=[ np.cos((phi + 90) * DG), np.sin((phi + 90) * DG), 0 ])
        label_rotation_unit_v = label_rotation_line.get_unit_vector()
        z_label_rotation_line = Line(start=[ 0, 0, 0 ], end=[ 0, 0, 1 ], stroke_color=WHITE)
        z_label_rotation_unit_v = label_rotation_line.get_unit_vector()

class working1(ThreeDScene):
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
        # self.add(val_graph)

        self.move_camera(theta=20 * DEGREES, about="theta", run_time=1)
        # self.move_camera(phi=25 * DEGREES, about="phi", run_time=3)
        self.move_camera(phi=80 * DEGREES, about="phi", run_time=1)

        inv = 100
        inv_text = Tex(rf'Investment = {inv}\$').move_to(axes.c2p(1.5, 0, 2.5)).rotate(90 * DG, axis=X).rotate(180 * DG, axis=Z).scale(1.5)

        self.play(Create(inv_text))

        # self.add(inv_text)

        # profit = Tex('Profit = ').move_to(axes.c2p(0, 0.8, 2.5)).rotate(90 * DG, axis=X).rotate(90 * DG, axis=Z).scale(1.8)

        # self.play(Create(profit))

        def curr_profit_with_IfOnTriangle():

            text = Tex(rf'Profit = {inv * (self.dollar_val_surface(x_tkr.get_value(), y_tkr.get_value())[ 2 ]):.2f}\$') \
                .move_to(axes.c2p(0, 1.5, 2.5)).rotate(90 * DG, axis=X).rotate(90 * DG, axis=Z).scale(1.8).set_color(GREEN)
            # text = DecimalNumber(inv * (self.dollar_val_surface(x_tkr.get_value(), y_tkr.get_value())[ 2 ])).next_to(profit,R)
            letter_len = len([ letter for letter in text ])
            if x_tkr.get_value() + y_tkr.get_value() > 3:
                text = Tex(rf'Profit = Out of range') \
                    .move_to(axes.c2p(0, 1.5, 2.5)).rotate(90 * DG, axis=X).rotate(90 * DG, axis=Z).scale(1.6).set_color(RED)

            # self.add_fixed_in_frame_mobjects(*[text[i] for i in range(letter_len) ])

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
        # self.add(curr_p_projected, curr_p)

        lines = redraw(lambda: VGroup(axes.get_lines_to_point(curr_p_projected[ 0 ].get_center())[ 1 ].set_color(RED),
                                      axes.get_lines_to_point(curr_p_projected[ 0 ].get_center())[ 0].set_color(GREEN)))
        vertical_line = redraw(lambda: DashedLine(start=curr_p_projected[ 0 ].get_center(), end=curr_p.get_center()))
        self.play(Create(VGroup(lines, vertical_line)))
        # self.add(lines, vertical_line)

        self.play(x_tkr.animate.set_value(1))
        self.play(y_tkr.animate.set_value(1))

        # self.play(x_tkr.animate.set_value(2), y_tkr.animate.set_value(2))
        self.play(x_tkr.animate.set_value(2))
        self.play(y_tkr.animate.set_value(2))
        #           val_tkr.animate.set_value(self.dollar_val_surface(x_tkr.get_value(),2)[2]))

        # self.play(y_tkr.animate.set_value(2))
        # self.move_camera(theta=70 * DEGREES, about="theta", run_time=1)

        self.play(x_tkr.animate.set_value(1))
        self.play(y_tkr.animate.set_value(1))

        # self.move_camera(theta=45 * DEGREES, about="theta", run_time=1)

        self.move_camera(phi=45 * DEGREES, run_time=1)

        self.begin_ambient_camera_rotation(0.1, about='theta')

        self.wait(3)


# class working1(ThreeDScene):
#     def construct(self):
#         axes = ThreeDAxes(x_range=[ -4, 4, 2 ],
#                           y_range=[ -4, 4, 2 ],
#                           z_range=[ -4, 4, 2 ],
#                           x_length=8,
#                           y_length=8,
#                           z_length=8,
#                           tips=False,
#                           axis_config={'include_numbers': True, 'include_ticks': True,"line_to_number_buff":0.2},
#                           x_axis_config = {"label_direction":DR},
#                           y_axis_config = {"label_direction":UL},
#                           z_axis_config = {"label_direction":UR,"line_to_number_buff":0.2}
#
#                           )
#
#
#         circle= Circle()
#
#         self.play(TracedPath)
#         self.add(text,axes)
#
#         # self.wait(2)
#
#         self.wait(2)
#
#         self.wait(1)
class working1(MovingCameraScene):

    """사각형 자르고 움직여보는 연습습"""    def construct(self):
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



# self.add(z_label_rotation_line)

# def rearrange_labels(x_labels, y_labels, z_labels, phi=45, theta=60):
#
#
#     label_rotation_line = Line(start=[ 0, 0, 0 ], end=[ -1, 1, 0 ])
#     label_rotation_unit_v = label_rotation_line.get_unit_vector()
#     z_label_rotation_line = Line(start=[ 0, 0, 0 ], end=[ 0, 0, 1 ], stroke_color=WHITE)
#     z_label_rotation_unit_v = label_rotation_line.get_unit_vector()
#
#     # self.add(z_label_rotation_line)
#
#     for number in x_labels:
#         number.rotate(135 * DG).rotate(45 * DG, axis=label_rotation_unit_v)
#     for number in y_labels:
#         number.rotate(135 * DG).rotate(45 * DG, axis=label_rotation_unit_v)
#     for number in z_labels:
#         # number.rotate(45*DG).rotate(45*DG, axis=Y_AXIS)
#         number.rotate(45 * DG, axis=z_label_rotation_unit_v).rotate(-135 * DG, axis=Y)

# for number in axes[ 0 ].numbers:
#     number.rotate((90-theta)*DG).rotate(phi*DG, axis=label_rotation_unit_v)
# for number in axes[ 1 ].numbers:
#     number.rotate((90+theta)*DG).rotate(phi*DG, axis=label_rotation_unit_v)
# for number in axes[ 3].numbers:
#     number.rotate(phi*DG, axis=z_label_rotation_unit_v).rotate(-(90+(90-theta))*DG, axis=Y)
# for number in axes[ 0 ].numbers:
#     number.rotate(135*DG).rotate(45*DG, axis=label_rotation_unit_v)
# for number in axes[ 1 ].numbers:
#     number.rotate(135*DG).rotate(45*DG, axis=label_rotation_unit_v)
# self.add_fixed_orientation_mobjects(axes[0].numbers)

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
        # self.move_camera(theta=10 * DG, about="theta", run_time=1)
        # self.move_camera(theta=0 * DG, about="theta", run_time=1)
        self.begin_ambient_camera_rotation(-0.2, about='theta')

        self.wait(5)

        # self.interactive_embed()
class working2(ThreeDScene):
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
        # numsteps = 30
        # self.add(axes, dot)
        # self.add( dot_1,dot_2,dot_3,dot_4,dot_5)
        # self.add( dot_4,dot_5)
        self.add( dot_1)


        def lorenz(x, y, z, s=10, r=28, b=2.667):
            x_dot = s * (y - x)
            y_dot = r * x - y - x * z
            z_dot = x * y - b * z
            return x_dot, y_dot, z_dot

        def aizawa(x, y, z, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
            x_dot = (z - b) * x - d * y
            y_dot = d * x + (z - b) * y
            z_dot = c + a * z - z ** 3 / 3 - (x ** 2 + y ** 2) * (1 + e * z) + f * z * x ** 3
            return x_dot, y_dot, z_dot
        def hoover(x, y, z, a=1.5):
            x_dot = y
            y_dot = -x+y*z
            z_dot = a-y**2
            return x_dot, y_dot, z_dot
        def rayleigh(x, y, z, a=9, r=12,b=5):
            x_dot = -a*x+a*y
            y_dot = r*x-y-x*z
            z_dot = x*y-b*z
            return x_dot, y_dot, z_dot

        def halvorsen(x, y, z, a=1.4):
            x_dot = -a*x-4*y-4*z-y**2
            y_dot =-a*y-4*z-4*x-z**2
            z_dot =-a*z-4*x-4*y-x**2
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
        def update_trajectory_face_dot_45(self):
            new_point = dot_5.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)
        def update_trajectory_Open_dot_5(self):
            new_point = dot_5.get_center()
            # if np.linalg.norm(new_point - self.points[ -1 ]) > 0.01:
            self.add_line_to(new_point)

        #
        #
        #

        which = 0
        traj_opacity=0.8
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
            # traj_5.add_updater(update_trajectory_Open_dot_4)
            # traj_5.add_updater(update_trajectory_Open_dot_5)
            #
        else:
            traj = VMobject()
            # traj.start_new_path(dot.get_center())
            traj.set_stroke(BLUE, 1.5, opacity=0.8)
            traj.add_updater(update_trajectory_V)

        # self.add(traj_1,traj_2,traj_3,traj_4,traj_5)
        # self.add(traj_4,traj_5)
        self.add(traj_1)
        # self.add(traj_1)
        # self.add(traj_1)

        def update_position_dot(self,dt):
            x_dot, y_dot, z_dot = hoover(self.get_center()[ 0 ], self.get_center()[ 1 ], self.get_center()[ 2 ])
            x = x_dot * 0.01
            y = y_dot * 0.01
            z = z_dot * 0.01
            # self.move_to((self.get_x()+x,self.get_y()+y,self.get_z()+z))
            self.shift(x * RIGHT + y * UP + z * OUT)

        dot_1.add_updater(update_position_dot)
        dot_2.add_updater(update_position_dot)
        dot_3.add_updater(update_position_dot)
        dot_4.add_updater(update_position_dot)
        dot_5.add_updater(update_position_dot)
        # trace = TracedPath(dot)
        # self.add(trace)
        # self.play()
        self.wait(120)


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
        self.wait(0.3)
        self.play(Create(triangle_perimeter))
        self.play(Create(plane))
        self.bring_to_back(plane)
        self.play(triangle_perimeter.animate.set_color(BLUE_D))
        self.bring_to_back(triangle_perimeter)
        self.wait()
        self.move_camera(theta=-90 * DEGREES, phi=75 * DEGREES, zoom=0.8, run_time=4)
        self.play(Create(entropy1), run_time=1.5)
        self.wait()
        self.renderer.camera.add_fixed_in_frame_mobjects(dot_updater_text)
        self.play(FadeIn(dot_updater_text))
        self.add_fixed_in_frame_mobjects(dot_updater_text)
        self.play(Create(xysphere))
        self.wait(0.3)
        self.play(x.animate.set_value(1.0), y.animate.set_value(0.0), run_time=2)
        self.wait(0.3)
        self.play(x.animate.set_value(0.0), y.animate.set_value(0.0), run_time=2)
        self.wait()
        self.move_camera(theta=-180 * DEGREES, phi=75 * DEGREES, zoom=0.8, run_time=3)
        self.wait()
        self.play(Create(entropy2), run_time=1.5)
        self.wait(0.3)
        self.play(x.animate.set_value(0.0), y.animate.set_value(1.0), run_time=2)
        self.wait(0.3)
        self.play(x.animate.set_value(0.0), y.animate.set_value(0.0), run_time=2)
        self.move_camera(theta=-315 * DEGREES, phi=75 * DEGREES, zoom=0.8, run_time=3)
        self.wait(0.3)
        self.play(
            Create(entropy3),
            x.animate.set_value(1.0),
            y.animate.set_value(0.0),
            run_time=1.5
        )
        self.wait(0.3)
        self.play(x.animate.set_value(0.0), y.animate.set_value(1.0), run_time=2)
        self.wait(0.3)
        self.play(x.animate.set_value(1.0), y.animate.set_value(0.0), run_time=2)
        self.wait()
        self.move_camera(theta=-420 * DEGREES, phi=75 * DEGREES, zoom=0.6, run_time=4)
        self.begin_ambient_camera_rotation(rate=-0.1)
        self.wait()
        self.play(Create(surface))
        self.play(
            Uncreate(entropy1),
            Uncreate(entropy2),
            Uncreate(entropy3)
        )
        self.wait(0.3)
        self.play(x.animate.set_value(0.3), y.animate.set_value(0.3), run_time=1)

        x_line = DashedLine(axes.c2p(x.get_value(), 0, 0), axes.c2p(x.get_value(), y.get_value(), 0), color=YELLOW)
        y_line = DashedLine(axes.c2p(0, y.get_value(), 0), axes.c2p(x.get_value(), y.get_value(), 0), color=YELLOW)
        z_line = DashedLine(axes.c2p(x.get_value(), y.get_value(), 0), axes.c2p(*self.func(x.get_value(), y.get_value())), color=YELLOW)

        x_line.add_updater(lambda l: l.put_start_and_end_on(
            axes.c2p(x.get_value(), 0, 0),
            axes.c2p(x.get_value(), y.get_value(), 0)
        )
                           )

        y_line.add_updater(lambda l: l.put_start_and_end_on(
            axes.c2p(0, y.get_value(), 0),
            axes.c2p(x.get_value(), y.get_value(), 0)
        )
                           )

        z_line.add_updater(lambda l: l.put_start_and_end_on(
            axes.c2p(x.get_value(), y.get_value(), 0),
            axes.coords_to_point(*self.func(x.get_value(), y.get_value()))
        )
                           )

        self.play(Create(x_line), Create(y_line), FadeOut(xysphere))
        self.play(Create(z_line))
        self.play(Create(sphere))
        self.wait(0.3)
        self.play(x.animate.set_value(0.1), y.animate.set_value(0.1), run_time=1.5)
        self.wait()
        self.play(x.animate.set_value(0.6), y.animate.set_value(0.3), run_time=1.5)
        self.wait()
        self.play(x.animate.set_value(0.4), y.animate.set_value(0.5), run_time=1.5)
        self.wait()


