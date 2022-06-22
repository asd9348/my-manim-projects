
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

