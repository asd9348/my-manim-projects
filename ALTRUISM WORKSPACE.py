class model(ThreeDScene):
    def construct(self):

        zygote_tex = Tex('Zygotes',color=BLACK).scale(1)

        text_box_height=zygote_tex.height*1.5

        zygote_box = Rectangle(width= zygote_tex.width*1.5, height= text_box_height, fill_opacity=1, fill_color = WHITE)

        zygote = VGroup(zygote_box,zygote_tex).to_edge(L)
        adult_tex = Tex('Adults').set_color(BLACK).scale(1)

        adult_box = Rectangle(width= adult_tex.width*1.5, height= text_box_height, fill_opacity=1, fill_color = WHITE)

        adult = VGroup(adult_box,adult_tex).next_to(zygote, R, buff= 3)

        survival_arrow = Arrow(start= zygote.get_right(), end= adult.get_left())
        survival_text = Tex('survival', color = GRAY).scale(0.75).next_to(survival_arrow, U,buff=0.1)
        survival = VGroup(survival_arrow,survival_text)

        sex_arrow = Arrow(start= adult.get_right(), end=adult.get_right()+get_dist_btwn_points(zygote.get_right(),adult.get_left())*R )
        sex_text  =Tex('sex', color = PINK).scale(0.75).next_to(sex_arrow, U,buff=0.1)
        sex = VGroup(sex_arrow,sex_text)

        gen_1 = VGroup(zygote, survival, adult)
        gen_1_with_sex=VGroup(zygote, survival, adult, sex)
        gen_2 = gen_1.copy().next_to(gen_1_with_sex, R)

        VGroup(gen_1_with_sex, gen_2).scale(0.7).move_to(O)

        gen_1_brace=BraceBetweenPoints(gen_1[0].get_corner(DL),gen_1[2].get_corner(DR) )
        gen_1_brace_text = Tex(r'Generation 1 (time \emph{t})').scale(0.7).next_to(gen_1_brace, D)


        gen_2_brace=BraceBetweenPoints(gen_2[0].get_corner(DL),gen_2[2].get_corner(DR) )
        gen_2_brace_text = Tex(r'Generation 2 (time \emph{t+1})').scale(0.7).next_to(gen_2_brace, D)

        braces = VGroup(gen_1_brace,gen_1_brace_text,gen_2_brace,gen_2_brace_text)

        self.play(Create(gen_1))

        self.play(Create(sex))

        self.play(Create(VGroup(gen_1_brace,gen_1_brace_text)))

        self.play(Create(gen_2))

        self.play(Create(VGroup(gen_2_brace,gen_2_brace_text)))

        self.wait(5)

# play by gen
class working2(ThreeDScene):

    config.background_color=DARK_GRAY
    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 1.25, 0.25 ],
                          y_range=[ 0, 1.25, 0.25 ],
                          z_range=[ 0, 1.25, 0.25 ],
                          x_length=4,
                          y_length=4,
                          z_length=4,
                          ).move_to(O).shift(IN*1)

        axes.move_to(get_compensated_coor(axes, center_of_mass([ axes.c2p(1, 0, 0), axes.c2p(0, 1, 0), axes.c2p(0, 0, 1)]), O))

        # plane = OpenGLVMobject().set_points_as_corners(
        plane = VMobject().set_points_as_corners(
            [ axes.c2p(1, 0, 0), axes.c2p(0, 1, 0), axes.c2p(0, 0, 1), axes.c2p(1, 0, 0) ]).set_style(fill_opacity=0.5, fill_color=RED)

        line_Dove2Hawk=Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 1, 0))
        line_Dove2Retal=Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 0, 1))
        line_Hawk2Dove=Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 1, 0))
        line_Hawk2Retal=Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 0, 1))



        start_line  = Line(start=line_Dove2Hawk.point_from_proportion(0.3), end=line_Dove2Retal.point_from_proportion(0.3), color= PINK)
        start_line_label = Tex(r'70\% \\Dove').scale(0.7).next_to(start_line.get_start(),UR, buff=0.25)



        x_label = axes.get_x_axis_label('Dove', direction=R)
        y_label = axes.get_y_axis_label('Hawk', direction=U,buff=0.5)
        z_label = axes.get_z_axis_label('Retal', direction=OUT,buff=0.5).rotate(axis=X_AXIS, angle =-90*DG)
        # z_label.rotate(axis=X_AXIS, angle =-90*DG, about_point=z_label.get_center())


        gen_var = Variable(1,'Gen').to_corner(UR)
        gen_num = Integer(1).to_corner(UR)


        self.set_camera_orientation(phi=45 * DG, theta=45 * DG)

        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.add_fixed_in_frame_mobjects(gen_num )

        self.play(Create(axes))
        self.play(Create(plane))
        # start_line_label.set_opacity(0)
        self.add_fixed_orientation_mobjects(start_line_label)


        self.play(Create(VGroup( start_line)))


        def DE(p, q):
            v = 2
            c = 3

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

            return (new_D,new_H,new_R)

        how_many_dot = 9
        dots = []
        paths= []
        for i in range(how_many_dot):
            color = Color(hsl=(i/how_many_dot, 1, 0.5))
            locals()[ f'dot_{i}' ] = Dot(radius=0.05,color = color)
            locals()[ f'dot_{i}' ].p = 0.7
            locals()[ f'dot_{i}' ].q = 0.3-i*0.3/(how_many_dot-1)# range-1만큼해야 전체 범위

            locals()[ f'dot_{i}' ].move_to(axes.c2p(locals()[ f'dot_{i}' ].p, locals()[ f'dot_{i}' ].q, 1-locals()[ f'dot_{i}' ].p-locals()[ f'dot_{i}' ].q))
            locals()[ f'dot_{i}' ].path_diffuse = TracedPath(locals()[ f'dot_{i}' ].get_center, dissipating_time=None, stroke_opacity=[ 1, 0.5 ],stroke_color = color)
            locals()[ f'dot_{i}' ].traj= VMobject()

            paths.append(locals()[ f'dot_{i}' ].path_diffuse)
            dots.append(locals()[ f'dot_{i}' ])

        for i in range(how_many_dot):
            color = Color(hsl=(i/how_many_dot, 1, 0.5))
            locals()[ f'dot_{i}' ] = Dot(radius=0.05,color = color)
            locals()[ f'dot_{i}' ].p = 0.3-i*0.3/(how_many_dot-1)# range-1만큼해야 전체 범위
            locals()[ f'dot_{i}' ].q = 0.7

            locals()[ f'dot_{i}' ].move_to(axes.c2p(locals()[ f'dot_{i}' ].p, locals()[ f'dot_{i}' ].q, 1-locals()[ f'dot_{i}' ].p-locals()[ f'dot_{i}' ].q))
            locals()[ f'dot_{i}' ].path_diffuse = TracedPath(locals()[ f'dot_{i}' ].get_center, dissipating_time=None, stroke_opacity=[ 1, 0.5 ],stroke_color = color)
            locals()[ f'dot_{i}' ].traj= VMobject()

            paths.append(locals()[ f'dot_{i}' ].path_diffuse)
            dots.append(locals()[ f'dot_{i}' ])



        self.play(Create(VGroup(*dots)))
        self.add(*paths)

        self.begin_ambient_camera_rotation(rate=0.06)


        how_many_gen= 30
        for i in range(how_many_gen):
            anims= []
            for dot in dots:
                new_coor = DE(dot.p, dot.q)
                dot.p = new_coor[0]
                dot.q = new_coor[1]
                final_coor =axes.c2p(*new_coor)

                anims.append(dot.animate.move_to(final_coor))

            self.play(AnimationGroup(*anims),
                      gen_num.animate.increment_value(1), rate_func= linear, run_time = 1)
            self.add_fixed_in_frame_mobjects(gen_num)
            self.wait(0.5)
            # self.wait(1)

class vector_3d_whole(ThreeDScene):
    config.background_color = DARK_GRAY

    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 1.25, 0.25 ],
                          y_range=[ 0, 1.25, 0.25 ],
                          z_range=[ 0, 1.25, 0.25 ],
                          x_length=4,
                          y_length=4,
                          z_length=4,
                          ).move_to(O).shift(IN * 1)

        axes.move_to(get_compensated_coor(axes, center_of_mass([ axes.c2p(1, 0, 0), axes.c2p(0, 1, 0), axes.c2p(0, 0, 1) ]), O))


        line_Dove2Hawk = Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 1, 0))
        line_Dove2Retal = Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 0, 1))
        line_Hawk2Dove = Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 1, 0))
        line_Hawk2Retal = Line(start=axes.c2p(1, 0, 0), end=axes.c2p(0, 0, 1))

        start_line = Line(start=line_Dove2Hawk.point_from_proportion(0.3), end=line_Dove2Retal.point_from_proportion(0.3), color=PINK)
        start_line_label = Tex(r'70\% \\Dove').scale(0.7).next_to(start_line.get_start(), UR, buff=0.25)

        x_label = axes.get_x_axis_label('Dove', direction=R)
        y_label = axes.get_y_axis_label('Hawk', direction=U, buff=0.5)
        z_label = axes.get_z_axis_label('Retal', direction=OUT, buff=0.5).rotate(axis=X_AXIS, angle=-90 * DG)
        # z_label.rotate(axis=X_AXIS, angle =-90*DG, about_point=z_label.get_center())

        gen_var = Variable(1, 'Gen').to_corner(UR)
        gen_num = Integer(1).to_corner(UR)

        self.set_camera_orientation(phi=45 * DG, theta=45 * DG)

        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        # self.add_fixed_in_frame_mobjects(gen_num )

        self.play(Create(axes))
        # start_line_label.set_opacity(0)
        # self.add_fixed_orientation_mobjects(start_line_label)

        # self.play(Create(VGroup( start_line)))
        #

        dot_3d_p_tkr = ValueTracker(0.3333)
        dot_3d_q_tkr = ValueTracker(0.3333)
        prism_test = redraw(lambda: Prism(dimensions=[ dot_3d_p_tkr.get_value() * 4 / 1.25,
                                                       dot_3d_q_tkr.get_value() * 4 / 1.25,
                                                       4 / 1.25 - dot_3d_p_tkr.get_value() * 4 / 1.25 - dot_3d_q_tkr.get_value() * 4 / 1.25 ]))
        prism_test.add_updater(lambda x:x.move_to(get_compensated_coor(x, x.get_corner(np.array([ -1, -1, -1 ])), axes.c2p(0, 0, 0))))

        # p=0.1*4/1.25
        # q=0.3333*4/1.25
        # prism_test = Prism(dimensions=[ 1, 5, 2 ])

        prism_test.move_to(get_compensated_coor(prism_test, prism_test.get_corner(np.array([ -1, -1, -1 ])), axes.c2p(0, 0, 0)))

        dot_3d = redraw(lambda: Dot(radius=0.1, fill_opacity=1).move_to(prism_test.get_corner(np.array([ 1, 1, 1 ]))))

        # self.play(Create(prism_test))

        dove_dash_line = redraw(lambda: DashedLine(end=axes.c2p(axes.p2c(dot_3d.get_center())[ 0 ], axes.p2c(dot_3d.get_center())[ 1 ], 0),
                                                   start=axes.c2p(axes.p2c(dot_3d.get_center())[ 0 ], 0, 0)))
        hawk_dash_line = redraw(lambda: DashedLine(end=axes.c2p(axes.p2c(dot_3d.get_center())[ 0 ], axes.p2c(dot_3d.get_center())[ 1 ], 0),
                                                   start=axes.c2p(0, axes.p2c(dot_3d.get_center())[ 1 ], 0)))
        retal_dash_line = redraw(
            lambda: DashedLine(start=axes.c2p(axes.p2c(dot_3d.get_center())[ 0 ], axes.p2c(dot_3d.get_center())[ 1 ], 0),
                               end=dot_3d.get_center()))
        # plane = OpenGLVMobject().set_points_as_corners(
        plane = ThreeDVMobject(shade_in_3d=True).set_points_as_corners(
            [ axes.c2p(1, 0, 0), axes.c2p(0, 1, 0), axes.c2p(0, 0, 1), axes.c2p(1, 0, 0) ]).set_style(fill_opacity=0.5, fill_color=GREY)

        self.play(Create(plane))
        # self.play(Create(dot_3d))

        # self.play(Create(dove_dash_line))
        # self.play(Create(hawk_dash_line))
        # self.play(Create(retal_dash_line))


        self.play(dot_3d_p_tkr.animate.set_value(0.5))

        # self.move_camera(theta=270 * DG, run_time=1)

        def DE(p, q):
            v = 2
            c = 3

            D = p
            H = q
            R = 1 - p - q

            w= 0.5
            D_avg_payoff = w+v * (1 - q) / 2
            H_avg_payoff = w+p * v + (1 - p) * (v - c) / 2
            R_avg_payoff = w+(q * (v - c) + (1 - q) * v) / 2
            avg_payoff = p * D_avg_payoff + q * H_avg_payoff + (1 - p - q) * R_avg_payoff

            delta_D = D * (D_avg_payoff - avg_payoff)
            delta_H = H * (H_avg_payoff - avg_payoff)
            delta_R = R * (R_avg_payoff - avg_payoff)

            new_D = D + delta_D
            new_H = H + delta_H
            new_R = R + delta_R

            if new_R > 1:
                new_R=1
                # print('R is larger than 1')
            if new_H < 0:
                new_H=0
                print('H is smaller than 0')
            if new_R > 1:
                new_R=1
                # print('what the fuck')

            return (new_D, new_H, new_R)

        how_many_dot = 30
        dots = [ ]
        paths = [ ]

        my_RED=Color(hsl=(0,1,0.55))
        my_YELLOW=Color(hsl=(1/6,1,0.55))
        my_BLUE=Color(hsl=(2/3,1,0.55))
        for r in range(how_many_dot):
            for c in range(how_many_dot-r):




                color = interpolate_color(interpolate_color(my_YELLOW ,my_RED,(1/(how_many_dot-1))*c),interpolate_color(my_RED, my_BLUE,(1/(how_many_dot-1))*r),
                (1/(how_many_dot-1))*r)

                locals()[ f'dot_{r}{c}' ] = Dot(radius=0.05, color=color)
                locals()[ f'dot_{r}{c}' ].p = (1/(how_many_dot-1))*r
                locals()[ f'dot_{r}{c}' ].q = (1/(how_many_dot-1))*c  # range-1만큼해야 전체 범위

                locals()[ f'dot_{r}{c}' ].move_to(
                    axes.c2p(locals()[ f'dot_{r}{c}' ].p, locals()[ f'dot_{r}{c}' ].q, 1 - locals()[ f'dot_{r}{c}' ].p - locals()[ f'dot_{r}{c}' ].q))
                locals()[ f'dot_{r}{c}' ].path_diffuse = TracedPath(locals()[ f'dot_{r}{c}' ].get_center, dissipating_time=1,
                                                                 stroke_opacity=[ 1, 0.5 ], stroke_color=color)
                locals()[ f'dot_{r}{c}' ].traj = VMobject()

                paths.append(locals()[ f'dot_{r}{c}' ].path_diffuse)
                dots.append(locals()[ f'dot_{r}{c}' ])

        # for i in range(how_many_dot):
        #     color = Color(hsl=(i / how_many_dot, 1, 0.5))
        #     locals()[ f'dot_{i}' ] = Dot(radius=0.05, color=color)
        #     locals()[ f'dot_{i}' ].p = 0.3 - i * 0.3 / (how_many_dot - 1)  # range-1만큼해야 전체 범위
        #     locals()[ f'dot_{i}' ].q = 0.7
        #
        #     locals()[ f'dot_{i}' ].move_to(
        #         axes.c2p(locals()[ f'dot_{i}' ].p, locals()[ f'dot_{i}' ].q, 1 - locals()[ f'dot_{i}' ].p - locals()[ f'dot_{i}' ].q))
        #     locals()[ f'dot_{i}' ].path_diffuse = TracedPath(locals()[ f'dot_{i}' ].get_center, dissipating_time=None,
        #                                                      stroke_opacity=[ 1, 0.5 ], stroke_color=color)
        #     locals()[ f'dot_{i}' ].traj = VMobject()
        #
        #     paths.append(locals()[ f'dot_{i}' ].path_diffuse)
        #     dots.append(locals()[ f'dot_{i}' ])

        self.play(Create(VGroup(*dots)))
        self.add(*paths)
        self.wait(3)
        # self.begin_ambient_camera_rotation(rate=0.01)


        how_many_gen= 120
        for i in range(how_many_gen):
            anims= []
            for dot in dots:
                new_coor = DE(dot.p, dot.q)
                dot.p = new_coor[0]
                dot.q = new_coor[1]
                final_coor =axes.c2p(*new_coor)

                anims.append(dot.animate.move_to(final_coor))

            self.play(AnimationGroup(*anims),
                      gen_num.animate.increment_value(1), rate_func= linear, run_time = 0.3)
            self.add_fixed_in_frame_mobjects(gen_num)
            self.wait(0.3)

class twod_simplex(ThreeDScene):
    config.background_color = DARK_GRAY

    def construct(self):
        axes = Axes(x_range=[ 0, 1.25, 0.25 ],
                    y_range=[ 0, 1.25, 0.25 ],
                    x_length=6,
                    y_length=6)

        line_org = Line(end=axes.c2p(1, 0), start=axes.c2p(0, 1))

        new_axes = Axes(x_range=[ 0, 1, 0.33333 ],
                        y_range=[ -0.15, 0.15, 0.05 ],
                        x_length=12,
                        y_length=6,
                        x_axis_config={'include_tip':False, 'label_direction':D })

        x_label = new_axes.get_x_axis_label(MathTex('p'), direction=U, buff=0.25)
        y_label = new_axes.get_y_axis_label(MathTex(r'\Delta p'), direction=L, buff=0.5).next_to(new_axes[ 0 ], L)

        label_vals = [  MathTex(r"\frac{1}{3}"), MathTex(r"\frac{2}{3}"), MathTex(r"1") ]
        label_pos = [  0.3333, 0.6666, 1 ]
        label_dict = dict(zip(label_pos, label_vals))

        new_axes.add_coordinates(label_dict)

        curve = new_axes.plot(lambda p: p * (1 - p) * (1 - 3 / 2 * p), color=RED, x_range=[ 0, 1 ])

        def diffrence_eq(p):
            v = 2
            c = 3
            w = 0.7

            w_h = w + p * (v - c) / 2 + (1 - p) * v
            w_d = w + (1 - p) * v / 2

            p_prime = (p * w_h) / (p * w_h + (1 - p) * w_d)

            delta_p = p_prime - p
            return (p_prime, delta_p)


        self.add(axes, line_org)
        self.play(FadeOut(axes),
                  Transform(line_org, new_axes[ 0 ])
                  )
        self.play(Create(x_label))

        self.play(Create(new_axes[ 1 ]))
        self.play(Create(y_label))
        # self.play(Create(curve))

        dot_from_zero = Dot(color= BLUE).move_to(new_axes.c2p(0, 0))
        dot_from_one = Dot(color= RED).move_to(new_axes.c2p(1, 0))

        previous_p = 0.01
        previous_delta_p = 0
        self.play(Create(dot_from_zero))
        wind = SVGMobject('svg/wind.svg').rotate(-45*DG).next_to(new_axes.c2p(0,0),UL,buff=-0.25).set_color(BLUE_A).scale(0.5).set_stroke(width=3)
        self.play(FadeIn(wind,shift=DR),rate_func=linear,run_time=0.5)
        self.play(FadeOut(wind,shift=DR),rate_func=smooth,run_time=1.5)
        self.play(dot_from_zero.animate.move_to(new_axes.c2p(previous_p, 0)))
        below_eq = VMobject().set_points_as_corners([ dot_from_zero.get_center(), dot_from_zero.get_center() ])

        self.add(below_eq)

        how_many_below=30

        for i in range(how_many_below):
            print('previous p is ', previous_p)
            result = diffrence_eq(previous_p)
            new_delta_p = result[ 1 ]
            print('delta_p is ', new_delta_p)

            new_p = result[ 0 ]
            print('new_p is ', new_p)


            self.play(Create(Arrow(start=new_axes.c2p(previous_p, previous_delta_p),
                                   end=new_axes.c2p(new_p, new_delta_p), stroke_width=15, buff=-0.1),
                             max_tip_length_to_length_ratio=0.2,
                             tip_style={'fill_opacity': 1, 'stroke_width': 10, 'width': 1, 'length': 1}
                             ),
                      dot_from_zero.animate.move_to(new_axes.c2p(new_p, 0)),run_time=0.3)

            previous_p = result[ 0 ]
            previous_delta_p = result[ 1 ]

        previous_p = 0.99
        previous_delta_p = 0
        self.play(Create(dot_from_one))
        wind = SVGMobject('wind.svg').rotate(-135 * DG).next_to(new_axes.c2p(1, 0), UR, buff=-0.1).set_color(BLUE_A).scale(0.5).set_stroke(
            width=3)
        self.play(FadeIn(wind, shift=DL), rate_func=smooth,run_time=0.5)
        self.play(FadeOut(wind, shift=DL), rate_func=smooth,run_time=1.5)
        self.play(dot_from_one.animate.move_to(new_axes.c2p(previous_p, 0)))

        how_many_above=20

        for i in range(how_many_above):
            print('previous p is ', previous_p)
            result = diffrence_eq(previous_p)
            new_delta_p = result[ 1 ]
            print('delta_p is ', new_delta_p)

            new_p = result[ 0 ]
            print('new_p is ', new_p)

            # below_eq.add_smooth_curve_to(new_axes.c2p(new_p, new_delta_p))

            self.play(Create(Arrow(start=new_axes.c2p(previous_p, previous_delta_p),
                                   end=new_axes.c2p(new_p, new_delta_p), stroke_width=15, buff=0),
                             max_tip_length_to_length_ratio=0.2,
                             tip_style={'fill_opacity': 1, 'stroke_width': 10, 'width': 1, 'length': 1}
                             ),
                      # Create(Line(start=new_axes.c2p(previous_p, previous_delta_p) , end=new_axes.c2p(new_p, new_delta_p))),
                      dot_from_one.animate.move_to(new_axes.c2p(new_p, 0)),run_time=0.3)

            previous_p = result[ 0 ]
            previous_delta_p = result[ 1 ]

        def diffrence_eq_curve(p):
            v = 2
            c = 3
            w = 0.7
            w_h = w + p * (v - c) / 2 + (1 - p) * v
            w_d = w + (1 - p) * v / 2

            p_prime = (p * w_h) / (p * w_h + (1 - p) * w_d)

            delta_p = p_prime - p
            return delta_p

        eq_curve= new_axes.plot(diffrence_eq_curve, color = RED)

        self.play(Create(eq_curve))

        self.wait(3)
class vector_threed_by_gen(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 1.25, 0.25 ],
                          y_range=[ 0, 1.25, 0.25 ],
                          z_range=[ 0, 1.25, 0.25 ],
                          x_length=4,
                          y_length=4,
                          z_length=4,
                          ).move_to(O)

        # plane = OpenGLVMobject().set_points_as_corners(
        plane = VMobject().set_points_as_corners(
            [ axes.c2p(1, 0, 0), axes.c2p(0, 1, 0), axes.c2p(0, 0, 1), axes.c2p(1, 0, 0) ]).set_style(fill_opacity=0.5, fill_color=RED)

        x_label = axes.get_x_axis_label('Dove')
        y_label = axes.get_y_axis_label('Hawk')
        z_label = axes.get_z_axis_label('Retal').rotate(axis=Z_AXIS, angle=90 * DG)

        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.add(axes, x_label, y_label, z_label)

        self.add(plane)

        gen_tkr = ValueTracker(0)

        def update_position(self):

            def DE(p, q):
                v = 2
                c = 3

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

                return (new_D, new_H, new_R)

            # deltas = DE(self.init_p_tracker.get_value(), self.init_q_tracker.get_value())
            deltas = DE(self.init_p, self.init_q)
            for i in range(ceil(gen_tkr.get_value())):
                self.init_q_tracker.set_value(deltas[ 1 ])
                self.init_p_tracker.set_value(deltas[ 0 ])
                deltas = DE(self.init_p_tracker.get_value(), self.init_q_tracker.get_value())
            new_D = deltas[ 0 ]
            new_H = deltas[ 1 ]
            new_R = deltas[ 2 ]

            new_coor = [ new_D * RIGHT[ 0 ], new_H * UP[ 1 ], new_R * OUT[ 2 ] ]

            print(new_coor)
            print('gen is', gen_tkr.get_value())
            final_coor = axes.c2p(*new_coor)
            self.move_to(final_coor)
            # self.traj.add_smooth_curve_to(final_coor)

        dots = [ ]
        for i in range(3):
            color = Color(hsl=(i / 3, 1, 0.5))
            locals()[ f'dot_{i}' ] = Dot(color=color)
            locals()[ f'dot_{i}' ].init_p = i * 0.1 * 0.3
            locals()[ f'dot_{i}' ].init_q = 0.7
            locals()[ f'dot_{i}' ].init_p_tracker = ValueTracker(i * 0.1 * 0.3)
            locals()[ f'dot_{i}' ].init_q_tracker = ValueTracker(0.7)
            locals()[ f'dot_{i}' ].path_diffuse = TracedPath(locals()[ f'dot_{i}' ].get_center, dissipating_time=None,
                                                             stroke_opacity=[ 1, 0.5 ], stroke_color=color)

            locals()[ f'dot_{i}' ].traj = VMobject()
            dots.append(locals()[ f'dot_{i}' ])
            locals()[ f'dot_{i}' ].add_updater(update_position)
            self.add(locals()[ f'dot_{i}' ], locals()[ f'dot_{i}' ].path_diffuse, locals()[ f'dot_{i}' ].traj)

        # self.set_camera_orientation(phi=45 * DG, theta=135 * DG)
        self.set_camera_orientation(phi=45 * DG, theta=45 * DG)

        self.play(gen_tkr.animate.set_value(1), run_time=1, rate_func=linear)
        self.wait(1)
        self.play(gen_tkr.animate.set_value(2), run_time=1, rate_func=linear)
        self.wait(1)
        self.play(gen_tkr.animate.set_value(3), run_time=1, rate_func=linear)
        self.wait(1)
        self.play(gen_tkr.animate.set_value(4), run_time=1, rate_func=linear)
        self.wait(1)
        self.play(gen_tkr.animate.set_value(5), run_time=1, rate_func=linear)
        self.wait(1)


class vector_threed_default(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 1.25, 0.25 ],
                          y_range=[ 0, 1.25, 0.25 ],
                          z_range=[ 0, 1.25, 0.25 ],
                          x_length=4,
                          y_length=4,
                          z_length=4,
                          ).move_to(O)

        # plane = OpenGLVMobject().set_points_as_corners(
        plane = VMobject().set_points_as_corners(
            [ axes.c2p(1, 0, 0), axes.c2p(0, 1, 0), axes.c2p(0, 0, 1), axes.c2p(1, 0, 0) ]).set_style(fill_opacity=0.5, fill_color=RED)

        x_label = axes.get_x_axis_label('Dove')
        y_label = axes.get_y_axis_label('Hawk')
        z_label = axes.get_z_axis_label('Retal').rotate(axis=Z_AXIS, angle=90 * DG)

        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.add(axes, x_label, y_label, z_label)

        self.add(plane)

        def update_position(self, dt):
            def DE(p, q):
                v = 2
                c = 3

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

                return (new_D, new_H, new_R)

            deltas = DE(self.init_p_tracker.get_value(), self.init_q_tracker.get_value())
            self.init_p_tracker.set_value(deltas[ 0 ])
            self.init_q_tracker.set_value(deltas[ 1 ])
            new_D = deltas[ 0 ]
            new_H = deltas[ 1 ]
            new_R = deltas[ 2 ]

            new_coor = [ new_D * RIGHT[ 0 ], new_H * UP[ 1 ], new_R * OUT[ 2 ] ]

            print(new_coor)
            self.move_to(axes.c2p(*new_coor))

        dots = [ ]
        self.begin_ambient_camera_rotation(rate=0.8)
        for i in range(6):
            color = Color(hsl=(i / 6, 1, 0.5))
            locals()[ f'dot_{i}' ] = Dot(color=color)
            locals()[ f'dot_{i}' ].init_p_tracker = ValueTracker(i * 0.1 * 0.3)
            locals()[ f'dot_{i}' ].init_q_tracker = ValueTracker(0.7)
            locals()[ f'dot_{i}' ].path_diffuse = TracedPath(locals()[ f'dot_{i}' ].get_center, dissipating_time=None,
                                                             stroke_opacity=[ 1, 0.5 ], stroke_color=color)
            dots.append(locals()[ f'dot_{i}' ])
            locals()[ f'dot_{i}' ].add_updater(update_position)
            self.add(locals()[ f'dot_{i}' ], locals()[ f'dot_{i}' ].path_diffuse)

        # self.set_camera_orientation(phi=45 * DG, theta=135 * DG)
        self.set_camera_orientation(phi=45 * DG, theta=45 * DG)

        self.wait(2)

# ternary plot
class ternary_plot_narrative(ThreeDScene):
    config.background_color = DARK_GRAY

    def construct(self):

        # self.add(NumberPlane())

        image = ImageMobject(np.uint8([ [ [ 0, 0, 0 ], [ 255, 255, 0 ], [ 0, 0, 0 ] ],
                                        [ [ 0, 0, 0 ], [ 255, 255, 255 ], [ 0, 0, 0 ] ],
                                        [ [ 0, 0, 255 ], [ 0, 0, 0 ], [ 255, 0, 0 ] ] ],

                                      ))
        image.height = 6

        # self.add(image)

        # self.add(NumberPlane())
        triangle = Triangle().scale_to_fit_width(6).move_to(O)

        # self.add(triangle)

        print(triangle.get_start_anchors())
        triangle_corner_L = triangle.get_start_anchors()[ 1 ]
        triangle_corner_U = triangle.get_start_anchors()[ 0 ]
        triangle_corner_R = triangle.get_start_anchors()[ 2 ]

        triangle_edge_UL = Line(start=triangle_corner_U, end=triangle_corner_L)
        triangle_edge_RU = Line(start=triangle_corner_R, end=triangle_corner_U)
        triangle_edge_LR = Line(start=triangle_corner_L, end=triangle_corner_R)
        triangle_edge_LU = Line(end=triangle_corner_U, start=triangle_corner_L)
        triangle_edge_UR = Line(end=triangle_corner_R, start=triangle_corner_U)
        triangle_edge_RL = Line(end=triangle_corner_L, start=triangle_corner_R)

        self.add(triangle_edge_UL, triangle_edge_RU, triangle_edge_LR)

        H_label = Tex('Hawk', color=RED).next_to(triangle_corner_R, DR, buff=0.5)
        R_label = Tex('Retaliator', color=YELLOW).next_to(triangle_corner_U, U, buff=0.7)
        D_label = Tex('Dove', color=BLUE).next_to(triangle_corner_L, DL, buff=0.5)

        self.add(H_label, R_label, D_label)

        Dove = ValueTracker(0.9999)
        Retal = ValueTracker(0.9999)
        Hawk = ValueTracker(0.00001)

        # background
        # dovek
        bg_dot_1 = Dot(fill_opacity=0, color=BLUE).move_to(triangle_edge_UL.point_from_proportion(Dove.get_value()))
        bg_dot_1.add_updater(lambda x: x.move_to(triangle_edge_UL.point_from_proportion(Dove.get_value())))
        bg_line_1 = redraw(
            lambda: Line(start=bg_dot_1.get_center(), end=triangle_edge_LR.point_from_proportion(1 - Dove.get_value()), stroke_opacity=0,
                         color=BLUE))

        # hawk
        bg_dot_2 = Dot(fill_opacity=0, color=RED).move_to(triangle_edge_LR.point_from_proportion(Hawk.get_value()))
        bg_dot_2.add_updater(lambda x: x.move_to(triangle_edge_LR.point_from_proportion(Hawk.get_value())))
        bg_line_2 = redraw(
            lambda: Line(start=bg_dot_2.get_center(), end=triangle_edge_RU.point_from_proportion(1 - Hawk.get_value()), stroke_opacity=0,
                         color=RED))

        bg_dot_3 = Dot(fill_opacity=0, color=YELLOW).move_to(
            triangle_edge_RU.point_from_proportion((1 - Dove.get_value() - Hawk.get_value())))
        bg_dot_3.add_updater(lambda x: x.move_to(triangle_edge_RU.point_from_proportion((1 - Dove.get_value() - Hawk.get_value()))))
        bg_line_3 = redraw(lambda: Line(start=bg_dot_3.get_center(),
                                        end=triangle_edge_UL.point_from_proportion(1 - (1 - Dove.get_value() - Hawk.get_value())),
                                        stroke_opacity=0, color=YELLOW))

        # bg_dot_1 = Dot(fill_opacity=0, color=BLUE).move_to(triangle_edge_UL.point_from_proportion(Dove.get_value()))
        # bg_dot_1.add_updater(lambda x: x.move_to(triangle_edge_UL.point_from_proportion(Dove.get_value())))
        # bg_line_1 = redraw(
        #     lambda: Line(start=bg_dot_1.get_center(), end=triangle_edge_LR.point_from_proportion(1 - Dove.get_value()), stroke_opacity=0,
        #                  color=BLUE))
        #
        # # hawk
        # bg_dot_2 = Dot(fill_opacity=0, color=RED).move_to(triangle_edge_LR.point_from_proportion(Hawk.get_value()))
        # bg_dot_2.add_updater(lambda x: x.move_to(triangle_edge_LR.point_from_proportion(Hawk.get_value())))
        # bg_line_2 = redraw(
        #     lambda: Line(start=bg_dot_2.get_center(), end=triangle_edge_RU.point_from_proportion(1 - Hawk.get_value()), stroke_opacity=0,
        #                  color=RED))
        #
        # bg_dot_3 = Dot(fill_opacity=0, color=YELLOW).move_to(
        #     triangle_edge_RU.point_from_proportion((1 - Dove.get_value() - Hawk.get_value())))
        # bg_dot_3.add_updater(lambda x: x.move_to(triangle_edge_RU.point_from_proportion((1 - Dove.get_value() - Hawk.get_value()))))
        # bg_line_3 = redraw(lambda: Line(start=bg_dot_3.get_center(),
        #                                 end=triangle_edge_UL.point_from_proportion(1 - (1 - Dove.get_value() - Hawk.get_value())),
        #                                 stroke_opacity=0, color=YELLOW))
        #
        self.add(bg_dot_1, bg_line_1, bg_dot_2, bg_line_2, bg_dot_3, bg_line_3)

        # self.add(dot_1, line_1, dot_2, line_2, dot_3, line_3
        line_opacity = 1
        # dovek
        dot_1 = Dot(color=BLUE).move_to(triangle_edge_UL.point_from_proportion(Dove.get_value()))
        dot_1.add_updater(lambda x: x.move_to(triangle_edge_UL.point_from_proportion(Dove.get_value())))
        line_1 = redraw(lambda: Line(start=dot_1.get_center(), end=triangle_edge_LR.point_from_proportion(1 - Dove.get_value()),
                                     stroke_opacity=line_opacity, color=BLUE))

        # hawk
        dot_2 = Dot(color=RED).move_to(triangle_edge_LR.point_from_proportion(Hawk.get_value()))
        dot_2.add_updater(lambda x: x.move_to(triangle_edge_LR.point_from_proportion(Hawk.get_value())))
        line_2 = redraw(lambda: Line(start=dot_2.get_center(), end=triangle_edge_RU.point_from_proportion(1 - Hawk.get_value()),
                                     stroke_opacity=line_opacity, color=RED))

        dot_3 = Dot(color=YELLOW).move_to(triangle_edge_RU.point_from_proportion((1 - Dove.get_value() - Hawk.get_value())))
        dot_3.add_updater(lambda x: x.move_to(triangle_edge_RU.point_from_proportion((1 - Dove.get_value() - Hawk.get_value()))))
        line_3 = redraw(lambda: Line(start=dot_3.get_center(),
                                     end=triangle_edge_UL.point_from_proportion(1 - (1 - Dove.get_value() - Hawk.get_value())),
                                     stroke_opacity=line_opacity, color=YELLOW))

        inter_method = VGroup(dot_1, line_1, dot_2, line_2, dot_3, line_3)
        # self.add(dot_1, line_1, dot_2, line_2, dot_3, line_3)

        dot_eq = redraw(lambda: Dot(radius=0.1, color=WHITE).move_to(
            line_intersection([ bg_line_1.get_start(), bg_line_1.get_end() ], [ bg_line_2.get_start(), bg_line_2.get_end() ])).set_z_index(
            0.1))

        perp_line_left = redraw(
            lambda: get_perpendicular_line(dot_eq.get_center(), [ triangle_corner_L, triangle_corner_U ]).set_stroke(
                color=RED, width=7))
        perp_line_right = redraw(
            lambda: get_perpendicular_line(dot_eq.get_center(), [ triangle_corner_R, triangle_corner_U ]).set_stroke(
                color=BLUE, width=7))
        perp_line_bottom = redraw(
            lambda: get_perpendicular_line(dot_eq.get_center(), [ triangle_corner_L, triangle_corner_R ]).set_stroke(
                color=YELLOW, width=7))

        # self.add(perp_line_left, perp_line_right,perp_line_bottom)

        start = triangle_corner_R + R * 2

        my_scaler = 1

        vertical_green = redraw(
            lambda: Line(color=YELLOW, stroke_width=13, start=start, end=start + + U * get_line_length(perp_line_bottom)).set_z_index(4))
        vertical_pink = redraw(lambda: Line(color=BLUE, stroke_width=13, start=start, end=start + U * (
                get_line_length(perp_line_right) + get_line_length(perp_line_bottom)) * my_scaler).set_z_index(3))
        vertical_yellow = redraw(lambda: Line(color=RED, stroke_width=13, start=start, end=start + U * (
                get_line_length(perp_line_left) + get_line_length(perp_line_bottom) + get_line_length(
            perp_line_right)) * my_scaler).set_z_index(2))

        # self.play(Create(VGroup(vertical_green, vertical_pink, vertical_yellow)))

        tracing = TracedPath(dot_eq.get_center, dissipating_time=2, stroke_opacity=[ 1, 0 ], stroke_color=RED_E)

        dove_vals = [ r'0\%', r"25\%", r"50\%", r"75\%", r'100\%' ]
        dove_pos = [ 0, 0.25, 0.5, 0.75, 1 ]
        dove_dict = dict(zip(dove_pos, dove_vals))

        dove_num_line = NumberLine(x_range=[ 0, 1, 0.25 ],
                                   length=6,
                                   label_direction=D
                                   ).add_labels(dove_dict, font_size=20)
        dove_num_line.move_to(get_compensated_coor(dove_num_line, dove_num_line.get_start(), triangle_corner_U)).rotate(angle=-120 * DG,
                                                                                                                        about_point=dove_num_line.get_start())
        for label in dove_num_line.labels:
            label.rotate(180 * DG)
        dove_num_line.labels.set_color(BLUE)

        retal_num_line = NumberLine(x_range=[ 0, 1, 0.25 ],
                                    length=6,
                                    label_direction=D).add_labels(dove_dict, font_size=20)

        retal_num_line.move_to(get_compensated_coor(retal_num_line, retal_num_line.get_start(), triangle_corner_R)).rotate(angle=120 * DG,
                                                                                                                           about_point=retal_num_line.get_start())
        for label in retal_num_line.labels:
            label.rotate(180 * DG)
        retal_num_line.labels.set_color(YELLOW)

        hawk_num_line = NumberLine(x_range=[ 0, 1, 0.25 ],
                                   length=6,
                                   label_direction=D).add_labels(dove_dict, font_size=20)
        hawk_num_line.labels.set_color(RED)
        # for label in hawk_num_line.labels:
        #     label.rotate(180 * DG)
        hawk_num_line.move_to(get_compensated_coor(hawk_num_line, hawk_num_line.get_start(), triangle_corner_L))

        self.add(dove_num_line, retal_num_line, hawk_num_line)
        self.add(dot_eq, tracing)

        def DE(p, q):
            v = 2
            c = 3

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

            return [ new_D, new_H, new_R ]


        self.play(Dove.animate.set_value(0.9), Hawk.animate.set_value(0.00001))
        self.wait(1)

        self.play(Dove.animate.set_value(0.5), Hawk.animate.set_value(0.00001))
        self.wait(1)

        self.play(Dove.animate.set_value(0.9999), Hawk.animate.set_value(0.00001))
        self.wait(1)

        self.play(Dove.animate.set_value(0.9), Hawk.animate.set_value(0.099))
        self.wait(1)
        for i in range(10):
            coor = DE(Dove.get_value(), Hawk.get_value())

            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)
        self.wait(1)



        self.play(Dove.animate.set_value(0.9999), Hawk.animate.set_value(0.00001))
        self.wait(1)

        self.play(Dove.animate.set_value(0.8), Hawk.animate.set_value(0.1))
        self.wait(1)

        for i in range(10):
            coor = DE(Dove.get_value(), Hawk.get_value())

            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)


        for i in range(10):
            coor = DE(Dove.get_value(), Hawk.get_value())

            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)

        self.play(Dove.animate.set_value(0.9999), Hawk.animate.set_value(0.00001))
        self.wait(1)

        self.play(Dove.animate.set_value(0.3), Hawk.animate.set_value(0.00001))
        self.wait(1)

        self.play(Dove.animate.set_value(0.3), Hawk.animate.set_value(0.15))
        self.wait(1)

        for i in range(20):
            coor = DE(Dove.get_value(), Hawk.get_value())

            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)


        self.play(Dove.animate.set_value(0.00001), Hawk.animate.set_value(0.9999))
        self.wait(1)

        self.play(Dove.animate.set_value(0.099), Hawk.animate.set_value(0.9))
        self.wait(1)

        for i in range(20):
            coor = DE(Dove.get_value(), Hawk.get_value())
            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)

        self.play(Dove.animate.set_value(0.00001), Hawk.animate.set_value(0.9999))
        self.wait(1)

        self.play(Dove.animate.set_value(0.1), Hawk.animate.set_value(0.8))
        self.wait(1)

        for i in range(20):
            coor = DE(Dove.get_value(), Hawk.get_value())
            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)


        self.play(Dove.animate.set_value(0.00001), Hawk.animate.set_value(0.9999))
        self.wait(1)

        self.play(Dove.animate.set_value(0.00001), Hawk.animate.set_value(0.9))
        self.wait(1)

        for i in range(20):
            coor = DE(Dove.get_value(), Hawk.get_value())
            self.play(Dove.animate.set_value(coor[ 0 ]), Hawk.animate.set_value(coor[ 1 ]), rate_func=linear, run_time=0.5)

        self.wait(3)

