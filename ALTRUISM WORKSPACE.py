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

class twodsimplex(ThreeDScene):
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
        wind = SVGMobject('svgs/wind.svg').rotate(-45*DG).next_to(new_axes.c2p(0,0),UL,buff=-0.25).set_color(BLUE_A).scale(0.5).set_stroke(width=3)
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
        wind = SVGMobject('svgs/wind.svg').rotate(-135 * DG).next_to(new_axes.c2p(1, 0), UR, buff=-0.1).set_color(BLUE_A).scale(0.5).set_stroke(
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

class explicit_sol(MovingCameraScene):

    def construct(self):
        t = LabeledDot(r't', radius=0.5).scale_to_fit_width(1.2)
        t_plus_1 = LabeledDot(r't+1').scale_to_fit_width(1.2)
        t_plus_2 = LabeledDot(r't+2').scale_to_fit_width(1.2)
        t_plus_3 = LabeledDot(r't+3').scale_to_fit_width(1.2)

        ts = VGroup(t, t_plus_1, t_plus_2, t_plus_3).arrange(D, buff=0.7).to_edge(L)

        t_plus_1_text_1 = MathTex(r'n_{A,t+1}={{(\# \ zygotes \ per \ individual) \times n_{A,t} \times (A \ type \ survival)}}',
                                  font_size=40) \
            .next_to(t_plus_1, R, buff=0.5)

        t_plus_1_text_2 = MathTex(r'zn_{A,t}V(A)', font_size=40).next_to(t_plus_1_text_1[ 0 ], R)
        self.play(FadeIn(t_plus_1, shift=D))

        self.play(FadeIn(t, target_position=t_plus_1))

        self.play(Write(t_plus_1_text_1))
        self.wait(1)

        self.play(Transform(t_plus_1_text_1[ 1 ], t_plus_1_text_2))
        self.wait(1)

        self.play(FadeIn(t_plus_2, target_position=t_plus_1))
        self.wait(1)

        t_plus_2_text_1 = MathTex(r'n_{A,t+1}={{(\# \ zygotes \ per \ individual) \times n_{A,t+1} \times (A \ type \ survival)}}',
                                  font_size=40) \
            .next_to(t_plus_2, R, buff=0.5)

        t_plus_2_text_2 = MathTex(r'z\{zn_{A,t}V(A)\}V(A)', font_size=40).next_to(t_plus_2_text_1[ 0 ], R)
        t_plus_2_text_3 = MathTex(r'n_{A,t}\{zV(A)\}^2', font_size=40).next_to(t_plus_2_text_1[ 0 ], R)

        self.play(Write(t_plus_2_text_1))
        self.wait(1)

        self.play(ReplacementTransform(t_plus_2_text_1[ 1 ], t_plus_2_text_2))
        self.wait(1)

        self.play(ReplacementTransform(t_plus_2_text_2, t_plus_2_text_3))
        self.wait(1)

        self.play(FadeIn(t_plus_3, target_position=t_plus_2))
        self.wait(1)

        t_plus_3_text_1 = MathTex(r'n_{A,t+1}={{(\# \ zygotes \ per \ individual) \times n_{A,t+2} \times (A \ type \ survival)}}',
                                  font_size=40) \
            .next_to(t_plus_3, R, buff=0.5)

        t_plus_3_text_2 = MathTex(r'z[z\{zn_{A,t}V(A)\}V(A)]V(A)', font_size=40).next_to(t_plus_3_text_1[ 0 ], R)
        t_plus_3_text_3 = MathTex(r'n_{A,t}\{zV(A)\}^3', font_size=40).next_to(t_plus_3_text_1[ 0 ], R)

        self.play(Write(t_plus_3_text_1))
        self.wait(1)
        self.play(ReplacementTransform(t_plus_3_text_1[ 1 ], t_plus_3_text_2))
        self.wait(1)

        self.play(ReplacementTransform(t_plus_3_text_2, t_plus_3_text_3))
        self.wait(1)

        self.play(t.animate.shift(D * t.get_y()),
                  FadeOut(VGroup(t_plus_1_text_1), target_position=[ VGroup(t_plus_1_text_1).get_x(), 0, 0 ]),
                  FadeOut(VGroup(t_plus_2_text_1[ 0 ], t_plus_2_text_3),
                          target_position=[ VGroup(t_plus_2_text_1[ 0 ], t_plus_2_text_3).get_x(), 0, 0 ]),
                  FadeOut(VGroup(t_plus_3_text_1[ 0 ], t_plus_3_text_3),
                          target_position=[ VGroup(t_plus_3_text_1[ 0 ], t_plus_3_text_3).get_x(), 0, 0 ]),
                  FadeOut(VGroup(t_plus_1, ), target_position=[ t_plus_1.get_x(), 0, 0 ]),
                  FadeOut(VGroup(t_plus_2, ), target_position=[ t_plus_1.get_x(), 0, 0 ]),
                  FadeOut(VGroup(t_plus_3, ), target_position=[ t_plus_1.get_x(), 0, 0 ]),
                  )
        general_form = MathTex(r'n_{A,t}=n_{A,0}\{zV(A)\}^t', font_size=40).next_to(t, R, buff=0.5)
        general_form_b = MathTex(r',\ n_{B,t}=n_{B,0}\{zV(B)\}^t', font_size=40).next_to(general_form, R, buff=0.1)

        self.play(FadeIn(general_form, shift=U))
        self.wait(1)

        self.play(FadeIn(general_form_b, shift=L))
        self.wait(1)

        self.play(FadeOut(general_form), FadeOut(general_form_b), FadeOut(t))

        function = MathTex(r'p_t &=\frac{n_{A,t}}{ n_{A,t}+n_{B,t} } \\ '
                           r'&=\frac{n_{A,0}V(A)^t}{n_{A,0}V(A)^t+n_{B,0}V(A)^t} \\'
                           r'&=\frac{n_{A,t}}{1+(\frac{n_{A,0}}{n_{A,0}})+(\frac{V(A)}{V(A)})^t} ')

        function[ 0 ][ 17:47 ].shift(D * 0.2)
        function[ 0 ][ 47: ].shift(D * 0.4)
        function.move_to(O)

        div_by = MathTex(r'\big/ n_{A,0}V(A)^t')
        div_by_1 = MathTex(r'/ n_{A,0}V(A)^t').scale(0.65).next_to(function[ 0 ][ 17:47 ], R).shift(U * 0.4)
        div_by_2 = MathTex(r'/ n_{A,0}V(A)^t').scale(0.65).next_to(function[ 0 ][ 17:47 ], R).shift(D * 0.4)

        self.play(Write(function[ 0 ][ 0:17 ]))
        self.wait(0.5)
        self.play(FadeIn(function[ 0 ][ 17:47 ], shift=R))
        self.wait(0.5)

        self.play(FadeIn(div_by_1, shift=L),
                  FadeIn(div_by_2, shift=L),
                  )
        self.wait(0.5)

        self.play(FadeIn(function[ 0 ][ 47: ], shift=R),
                  FadeOut(div_by_1, shift=R),
                  FadeOut(div_by_2, shift=R))
        self.wait(1)



        self.play(VGroup(function).animate.to_edge(L))

        axes = Axes(x_range=[ 0, 20 ],
                    y_range=[ 0, 1, 0.25 ],
                    x_length=5.5,
                    y_length=5.5,
                    tips=False).shift(R * 3)


        label_vals = [  MathTex(r"0"), MathTex(r"1") ]
        label_pos = [  0, 1 ]
        y_label_dict = dict(zip(label_pos, label_vals))
        x_label_dict = {}

        axes[1].add_labels(y_label_dict)

        x_label = axes.get_x_axis_label('t', edge=D, direction=D)
        y_label = axes.get_y_axis_label('p_t', edge=L, direction=L)

        self.play(Create(axes))
        self.play(Write(VGroup(x_label, y_label)))
        self.wait(1)

        V_A = 0.8
        V_B = 0.5
        n_A = 1
        n_B = 99
        z = 1

        condition = MathTex(r'V(A)&=0.8\\'
                            r'V(B)&=0.5\\'
                            r'n_{A,0}&=1\\'
                            r'n_{B,0}&=99\\'
                            r'z&=1'
                            ).scale(0.8).to_edge(R).shift(D*1)

        self.play(Create(condition))
        self.wait(1)

        curve = axes.plot(lambda t: 1 / (1 + (n_B / n_A) * (V_B / V_A) ** t))
        x_tkr = ValueTracker(20)

        curve.add_updater(
            lambda x: x.become(axes.plot(lambda t: 1 / (1 + (n_B / n_A) * (V_B / V_A) ** t), x_range=[ 0, x_tkr.get_value() ])))

        curve_deriv = axes.plot_derivative_graph(curve, color=RED)

        self.play(Create(curve))
        self.wait(1)


        self.play(Create(curve_deriv))
        self.wait(1)


        self.play(x_tkr.animate.set_value(100),
                  self.camera.frame.animate.shift(R*18))

        self.wait(5)
class working2(MovingCameraScene):
    def construct(self):

        func = lambda pos: np.array([-pos[1] , pos[0], 0])/3
        self.add(ArrowVectorField(func))

        stream_lines = StreamLines(
            func,
            x_range=[-8, 8, 1],
            y_range=[-4, 4, 1],
            stroke_width=1,
            virtual_time=15,  # use shorter lines
            max_anchors_per_line=30,  # better performance with fewer anchors
        )
        # self.play(stream_lines.create())  # uses virtual_time as run_time

        self.wait(1)

        self.add(stream_lines)
        # self.play(Create(stream_lines))
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        # self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        self.wait(10)

class torus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        axes[ 0 ].set_color(RED)
        axes[ 1 ].set_color(GREEN)
        axes[ 2 ].set_color(BLUE)

        # self.add(axes)

        # self.set_camera_orientation(phi =45*DG,theta=-80*DG, )
        # self.set_camera_orientation(zoom=0.6 )
        self.set_camera_orientation(phi=45 * DG, theta=-80 * DG, zoom=0.6)
        # self.move_camera(theta=45*DG)

        array = [ ]

        u_min = -10
        u_max = 10
        v_min = -4
        v_max = 4
        for v in np.linspace(v_min, v_max, 10):
            row = [ ]
            for u in np.linspace(u_min, u_max, 20):
                row.append([ u, v, 0 ])
            array.append(row)

        point_list = np.array(array)
        # print(point_list)

        n = point_list.shape[ 1 ]
        m = point_list.shape[ 0 ]

        points = VGroup()
        points_without_rc = VGroup()
        faces = VGroup()
        faces_without_rc = VGroup()

        for row in range(0, m):
            row_group = VGroup()
            for col in range(0, n):
                coor = point_list[ row, col ]

                dot = Dot().move_to(coor)
                dot.r = row
                dot.c = col
                row_group.add(dot)
                points_without_rc.add(dot)

            points.add(row_group)
            # points.add(Dot3D().move_to(coor))

        # self.add(points)

        for row in range(0, m - 1):
            row_group = VGroup()
            for col in range(0, n - 1):
                sqDL = points[ row ][ col ]
                sqDR = points[ row ][ col + 1 ]
                sqUR = points[ row + 1 ][ col + 1 ]
                sqUL = points[ row + 1 ][ col ]

                globals()[ f'{row}_{col}' ] = points[ row ][ col ]
                globals()[ f'{row}_{col + 1}' ] = points[ row ][ col + 1 ]
                globals()[ f'{row + 1}_{col + 1}' ] = points[ row + 1 ][ col + 1 ]
                globals()[ f'{row + 1}_{col}' ] = points[ row + 1 ][ col ]

                face = ThreeDVMobject().set_points_as_corners([ sqDL.get_center(), sqDR.get_center(), sqUR.get_center(),
                                                                sqUL.get_center(),
                                                                sqDL.get_center() ]).set_style(fill_color=RED, fill_opacity=0.4,
                                                                                               stroke_width=0.5, stroke_color=GRAY,
                                                                                               stroke_opacity=0.5)

                face.sqDL = points[ row ][ col ]
                face.sqDR = points[ row ][ col + 1 ]
                face.sqUR = points[ row + 1 ][ col + 1 ]
                face.sqUL = points[ row + 1 ][ col ]

                face.r = row
                face.c = col

                row_group.add(face)

                # print(face.sqDL)

                def face_func(mob):
                    updated_mob = mob.set_points_as_corners(
                        [ mob.sqDL.get_center(), mob.sqDR.get_center(), mob.sqUR.get_center(), mob.sqUL.get_center(),
                          mob.sqDL.get_center() ])

                    return updated_mob

                face.add_updater(face_func)
                faces_without_rc.add(face)
            faces.add(row_group)

        self.add(faces)
        # self.add(index_labels(faces))
        # self.add(index_labels(faces[0]))
        self.wait(1)

        coloring_anims = [ ]
        for i in range(len(faces)):
            coloring_anims.append(
                faces[ i ].animate.set_color(Color(hue=i / len(faces), saturation=1, luminance=0.6)))

        faces[ 0 ].set_style(fill_color=BLUE, fill_opacity=0.7)
        faces[ -1 ].set_style(fill_color=GREEN, fill_opacity=0.7)

        for face in faces_without_rc:
            if face.c == 0:
                face.set_style(fill_color=YELLOW, fill_opacity=0.7)
            if face.c == 18:
                face.set_style(fill_color=ORANGE, fill_opacity=0.7)

        points_without_rc.set_opacity(opacity=0)

        roll_up_anims = [ ]
        for point in points_without_rc:
            x = point.get_center()[ 0 ]
            y = point.get_center()[ 1 ]
            z = point.get_center()[ 2 ]

            new_x = x
            new_y = np.cos(270 * DG + 90 / ((v_max - v_min) / 4) * y * DG) * (v_max - v_min) / 2 / PI
            new_z = np.sin(270 * DG + 90 / ((v_max - v_min) / 4) * y * DG) * (v_max - v_min) / 2 / PI

            new_coor = np.array([ new_x, new_y, new_z ])

            roll_up_anims.append(point.animate.move_to(new_coor))

            # for opengl
            # point.move_to(new_coor)

        self.play(*roll_up_anims, run_time=3)
        print(points_without_rc[ 0 ].get_center())

        round_up_anims = [ ]

        for point in points_without_rc:
            x = point.get_center()[ 0 ]
            y = point.get_center()[ 1 ]
            z = point.get_center()[ 2 ]

            new_x = np.cos(270 * DG + 90 / ((u_max - u_min) / 4) * x * DG) * (-2 / PI * y + 6 / PI)
            new_y = np.sin(270 * DG + 90 / ((u_max - u_min) / 4) * x * DG) * (-2 / PI * y + 6 / PI)
            new_z = z

            new_coor = np.array([ new_x, new_y, new_z ])

            round_up_anims.append(point.animate.move_to(new_coor))
            # for opengl
            # point.move_to(new_coor)

        self.play(*round_up_anims, run_time=3)

        self.wait(1)

        self.move_camera(phi=90 * DG, theta=-80 * DG, zoom=1.2)
        self.wait(1)
        # self.set_camera_orientation(phi =90*DG,theta=-80*DG)

        self.begin_ambient_camera_rotation(rate=0.3)
        self.move_camera(phi=0, run_time=10, rate_func=linear)

        self.wait(5)

class eq_anal(MovingCameraScene):

    def construct(self):

        self.add(NumberPlane())
        slice_1 = Polygon([-2,6,0],[2,-6,0],[15,-6,0],[15,6,0], fill_color=RED)
        slice_2 = Polygon([-2,6,0],[2,-6,0],[-15,-6,0],[-15,6,0], fill_color=BLUE).set_style(stroke_opacity=0)

        # self.play(Create(slice_1))
        self.add(slice_1,slice_2)


        hole_1= Dot(radius=0.5,color =BLUE).move_to([-6,-2,0]).set_z_index(2)
        hole_2= Dot(radius=0.5, color =RED).move_to([6,2,0]).set_z_index(2)

        dot_exam= Dot().move_to([2,1,0])

        self.play(Create(hole_1))
        self.play(Create(hole_2))


        self.play(Create(dot_exam))

        unit = Line(start=dot_exam.get_center(), end=hole_2.get_center()).get_unit_vector()


        self.play(dot_exam.animate.shift(unit*0.5))
        self.play(dot_exam.animate.shift(unit*1))
        self.play(dot_exam.animate.shift(unit*1.5))
        self.play(dot_exam.animate.move_to(hole_2))

        self.remove(dot_exam)

        speed_scaler=0.04
        def left_update_pos(mob,dt):

            if float(get_dist_btwn_points(mob.get_center(),hole_1.get_center()))>0.3:
                dist=float(get_dist_btwn_points(mob.get_center(),hole_1.get_center()))
                unit=Line(start=mob.get_center(), end=hole_1.get_center()).get_unit_vector()
                mob.shift(unit*((dist*speed_scaler)))

        p1 = Dot().move_to([-7,3,0])
        p1.add_updater(left_update_pos)
        p2 = Dot().move_to([-5,2.7,0])
        p2.add_updater(left_update_pos)
        p3 = Dot().move_to([-6,1,0])
        p3.add_updater(left_update_pos)
        p4 = Dot().move_to([-2,1.3,0])
        p4.add_updater(left_update_pos)
        p5 = Dot().move_to([-4,-3.5,0])
        p5.add_updater(left_update_pos)
        p6 = Dot().move_to([-2,-1.5,0])
        p6.add_updater(left_update_pos)

        def right_update_pos(mob,dt):

            if float(get_dist_btwn_points(mob.get_center(),hole_2.get_center()))>0.3:
                dist=float(get_dist_btwn_points(mob.get_center(),hole_2.get_center()))
                unit=Line(start=mob.get_center(), end=hole_2.get_center()).get_unit_vector()
                mob.shift(unit*((dist*speed_scaler)))

        p7 = Dot().move_to([1,3.3,0])
        p7.add_updater(right_update_pos)
        p8 = Dot().move_to([2,2,0])
        p8.add_updater(right_update_pos)
        p9 = Dot().move_to([5,3,0])
        p9.add_updater(right_update_pos)
        p10 = Dot().move_to([1,-1,0])
        p10.add_updater(right_update_pos)
        p11 = Dot().move_to([3,-3,0])
        p11.add_updater(right_update_pos)
        p12 = Dot().move_to([7,-2,0])
        p12.add_updater(right_update_pos)
        p13 = Dot().move_to([4,0,0])
        p13.add_updater(right_update_pos)

        left_dots = VGroup(p1,p2,p3,p4,p5,p6).set_color(BLUE_B)
        right_dots = VGroup(p7,p8,p9,p10,p11,p12,p13).set_color(RED_B)
        all_dots=VGroup(p1,p2,p3,p4,p5,p6,p11,p12,p13,p9,p10,p7,p8)



        area_opacity=0.3


        self.add(all_dots)




        # for dot in all_dots:
        #     self.add(dot)
        #     self.wait(0.3)

        # self.play(Create(VGroup(p1,p2,p3,p4,p5,p6)))
        # self.play(AnimationGroup(*left_dots_anim,lag_ratio=0.7),run_time=8)
        # self.play(Create(VGroup(p7,p8,p9,p10,p11, p12,p13)))
        # self.play(AnimationGroup(*right_dots_anim,lag_ratio=0.7),run_time=8)

        self.wait(6)

        for dot in all_dots:
            dot.clear_updaters()
            # self.wait(0.3)

        self.remove(all_dots)

        for dot in all_dots:
            self.remove(dot)

        dots_grid_all= VGroup()
        dots_grid_1= []
        for i in np.linspace(-8, 8, 17):
            for j in np.linspace(-4,4,9):
                if j < -3*i:
                    dots_grid_1.append(Dot(radius=0.1,color =BLUE, fill_opacity=area_opacity).move_to([i,j,0]))

                elif j > -3*i :
                    dots_grid_1.append(Dot(radius=0.1,color =RED, fill_opacity=area_opacity).move_to([i,j,0]))

                else:
                    pass

        dots_grid_1_group=VGroup(*dots_grid_1)
        self.play(FadeIn(dots_grid_1_group))
        self.wait(1)

        dots_grid_05= []
        for i in np.linspace(-8, 8,33):
            for j in np.linspace(-4,4,17):
                if j < -3*i:
                    dots_grid_05.append(Dot(radius=0.1,color =BLUE, fill_opacity=area_opacity).move_to([i,j,0]))

                elif j > -3*i :
                    dots_grid_05.append(Dot(radius=0.1,color =RED, fill_opacity=area_opacity).move_to([i,j,0]))

                else:
                    pass
        dots_grid_05_group=VGroup(*dots_grid_05)

        self.play(FadeIn(dots_grid_05_group),
                  FadeOut(dots_grid_1_group))
        self.wait(0.5)

        # self.remove(dots_grid_1_group)

        dots_grid_25= []
        for i in np.linspace(-8, 8, 65):
            for j in np.linspace(-4,4,33):
                if j < -3*i:
                    dots_grid_25.append(Dot(radius=0.1,color =BLUE, fill_opacity=area_opacity).move_to([i,j,0]))

                elif j > -3*i :
                    dots_grid_25.append(Dot(radius=0.1,color =RED, fill_opacity=area_opacity).move_to([i,j,0]))

                else:
                    pass
        dots_grid_25_group=VGroup(*dots_grid_25)

        self.play(FadeIn(VGroup(*dots_grid_25)),
                  FadeOut(dots_grid_05_group))
        self.wait(0.5)

        # self.remove(dots_grid_05_group)



        self.play(slice_1.animate.set_fill(opacity=area_opacity),
                  slice_2.animate.set_fill(opacity=area_opacity),
                  FadeOut(dots_grid_25_group))


        dot_eq = Dot()



        self.play(Create(dot_eq))


        hole_2_unit = Line(start=dot_eq.get_center(), end=hole_2.get_center()).get_unit_vector()
        hole_1_unit = Line(start=dot_eq.get_center(), end=hole_1.get_center()).get_unit_vector()

        hole_2_unit = Line(start=dot_eq.get_center(), end=hole_2.get_center()).get_unit_vector()
        hole_1_unit = Line(start=dot_eq.get_center(), end=hole_1.get_center()).get_unit_vector()

        speed_scaler=0.1

        q_mark_1 =Tex('?').scale(2).rotate(30*DG).next_to(hole_1_unit*0.5+dot_eq.get_center(),L,buff=0.78).shift(D*2)
        self.play(Write(q_mark_1))
        q_mark_2 =Tex('?').scale(2).rotate(-25*DG).next_to(hole_2_unit*0.5+dot_eq.get_center(),R,buff=0.78).shift(U*2)
        self.play(Write(q_mark_2))

        wind = SVGMobject('svgs/wind.svg').flip(axis=Y_AXIS).next_to(dot_eq.get_center(),-hole_1_unit,buff=0).rotate(45*DG).set_color(BLUE_A).scale(0.3).set_stroke(width=3)
        self.play(FadeIn(wind,shift=hole_1_unit),rate_func=linear,run_time=0.5)
        self.play(FadeOut(wind,shift=hole_1_unit),
                  dot_eq.animate.shift(hole_1_unit*0.5),
                  rate_func=smooth,run_time=1.5)
        self.wait(0.5)


        dot_eq.add_updater(left_update_pos)

        self.wait(3)

        self.remove(dot_eq)

        dot_eq_2=Dot()
        self.play(Create(dot_eq_2))

        wind = SVGMobject('svgs/wind.svg').next_to(dot_eq_2.get_center(),-hole_2_unit,buff=0).rotate(45*DG).set_color(BLUE_A).scale(0.3).set_stroke(width=3)
        self.play(FadeIn(wind,shift=hole_2_unit),rate_func=linear,run_time=0.5)

        self.play(FadeOut(wind,shift=hole_2_unit),
                  dot_eq_2.animate.shift(hole_2_unit * 0.3),
                  rate_func=smooth,run_time=1.5)
        self.wait(0.5)


        dot_eq_2.add_updater(right_update_pos)




        self.wait(3)

        self.remove(dot_eq, dot_eq_2)
        self.play(FadeOut(VGroup(hole_1, hole_2, slice_1,slice_2, q_mark_2,q_mark_1)))


        spiral_path=SVGMobject('svgs/spiral.svg', unpack_groups=False).scale(2).to_edge(DR)[1].reverse_points()
        line_1=Line(start=[-9,-3,0], end=[9,3,0])
        line_2=Line(start=[2,2,0], end=[-1,5,0])
        line_3=Line(start=[-3,-2,0], end=[1,-5,0])
        p1= Dot().move_to([-9,-3,0])
        p2= Dot().move_to([2,2,0])
        p3= Dot().move_to([-3,-2,0])

        p4=Dot().move_to([-7,3,0])
        p5=Dot().move_to(spiral_path.get_start())




        self.add(TracedPath(p1.get_center,dissipating_time=3,stroke_opacity=[1,0]))
        self.add(TracedPath(p2.get_center,dissipating_time=3,stroke_opacity=[1,0]))
        self.add(TracedPath(p3.get_center,dissipating_time=3,stroke_opacity=[1,0]))
        self.add(TracedPath(p4.get_center,dissipating_time=2,stroke_opacity=[1,0]))
        self.add(TracedPath(p5.get_center,dissipating_time=4,stroke_opacity=[1,0]))

        self.play(Create(VGroup(p1,p2,p3,p4,p5)))

        self.play(p1.animate.move_to([9,3,0]),
                  p2.animate.move_to([-1,5,0]),
                  p3.animate.move_to([1,-5,0]),
                  MoveAlongPath(p5,spiral_path),
                  Rotate(p4,angle=6*PI, about_point=p4.get_center()+D*1+R*1),
                  run_time=10, rate_func=linear)


        self.wait(5)


class eq_anal_1(MovingCameraScene):
    config.background_color = DARK_GRAY

    def construct(self):
        delta_p_0 = MathTex(r'\Delta p = p(1-p)\frac{V(A)-V(B)}{\bar{w}}{{=0}}').scale(2)

        self.play(Write(delta_p_0[ 0 ]))
        self.wait(0.5)
        self.play(FadeIn(delta_p_0[ 1 ], shift=L))

        self.play(delta_p_0.animate.to_edge(U, buff=0.75))

        self.play(delta_p_0[ 0 ][ 9:18 ].animate.set_color(BLUE),
                  delta_p_0[ 0 ][ 3 ].animate.set_color(GREEN),
                  delta_p_0[ 0 ][ 4:9 ].animate.set_color(RED))

        conds = MathTex(r'p&=0\\'
                        r'p&=1\\'
                        r'V(A)&=V(B)', color=GREEN).scale(2).shift(D)

        conds[ 0 ][ 3:6 ].set_color(RED)
        conds[ 0 ][ 6: ].set_color(BLUE)

        self.play(Write(conds[ 0 ][ 0:3 ]))
        self.play(Write(conds[ 0 ][ 3:6 ]))
        self.play(Write(conds[ 0 ][ 6: ]))

        self.play(conds.animate.to_edge(R).shift(U * 0.5).scale(0.75))
        self.play(AnimationGroup(FadeOut(delta_p_0[ 1 ], shift=R),
                                 delta_p_0[ 0 ].animate.scale(0.5).to_edge(UR, buff=0.75).shift(D + R * 0.25), lag_ratio=0.7)
                  )

        # self.add(index_labels(delta_p_0[0]))
        #

        axes = Axes(x_range=[ 0, 1, 1 ],
                    y_range=[ 0, 1, 1 ],
                    x_length=6,
                    y_length=6,
                    tips=False).to_edge(L, buff=1)
        x_label = axes.get_x_axis_label('p', edge=D, direction=D)
        y_label = axes.get_y_axis_label("p'", edge=L, direction=L)
        axis_labels = VGroup(x_label, y_label)

        p_prime_1_label = MathTex('1').scale(0.8).next_to(axes.c2p(0, 1), L)
        p_1_label = MathTex('1').scale(0.8).next_to(axes.c2p(1, 0), D)
        p_0_label = MathTex('0').scale(0.8).next_to(axes.c2p(0, 0), DL, buff=0.2)
        tick_labels = VGroup(p_prime_1_label, p_1_label, p_0_label)

        dashed_line = axes.plot(lambda x: x, x_range=[ 0, 1 ])
        dashed_line_label = axes.get_graph_label(dashed_line, label=r"p'=p", x_val=1, direction=R)

        dashed_line = DashedVMobject(dashed_line)
        v_a = 0.6
        v_b = 0.2
        w = np.average([ v_a, v_b ])
        curve = axes.plot(lambda p: p * (1 - p) * (v_a - v_b) / w + p, color=YELLOW)

        func = lambda p: p * (1 - p) * (v_a - v_b) / w + p

        self.play(Create(axes))
        self.play(Create(axis_labels))
        self.play(Create(tick_labels))

        self.play(Create(dashed_line))
        self.play(Create(dashed_line_label))

        v_a_v_b_conds = MathTex(r'V(A)=0.7\\V(B)=0.2').next_to(conds[ 0 ][ 3:6 ], D, buff=0.4).set_color(YELLOW)

        self.play(ReplacementTransform(conds[ 0 ][ 6: ], v_a_v_b_conds))

        self.play(Create(curve))

        lines = VGroup()
        dot_green_tkr = ValueTracker(0)
        dot_green = redraw(
            lambda: Dot(color=GREEN).move_to(axes.c2p(dot_green_tkr.get_value(), func(dot_green_tkr.get_value()))))

        self.play(Create(dot_green))

        self.play(dot_green_tkr.animate.set_value(0.05))

        def green_dot_func():
            dot_green_v_line_1 = DashedLine(start=axes.c2p(dot_green_tkr.get_value(), 0), end=dot_green)
            self.play(Create(dot_green_v_line_1))

            dot_green_h_line_1 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_1))

            dot_green_v_line_2 = DashedLine(start=dot_green_h_line_1.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_2))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_2 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_2))

            dot_green_v_line_3 = DashedLine(start=dot_green_h_line_2.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_3))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_3 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_3))

            dot_green_v_line_4 = DashedLine(start=dot_green_h_line_3.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_4))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_4 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_4))

            dot_green_v_line_5 = DashedLine(start=dot_green_h_line_4.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_5))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_5 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_5))

            dot_green_v_line_6 = DashedLine(start=dot_green_h_line_5.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_6))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_6 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_6))

            dot_green_v_line_7 = DashedLine(start=dot_green_h_line_6.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_7))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_7 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_7))

            dot_green_v_line_8 = DashedLine(start=dot_green_h_line_7.get_end(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(func(dot_green_tkr.get_value()))))
            self.play(Create(dot_green_v_line_8))

            self.play(dot_green_tkr.animate.set_value(func(dot_green_tkr.get_value())))

            dot_green_h_line_8 = DashedLine(start=dot_green.get_center(),
                                            end=axes.c2p(func(dot_green_tkr.get_value()), func(dot_green_tkr.get_value())))
            self.play(Create(dot_green_h_line_8))

            lines.add(dot_green_v_line_1)
            lines.add(dot_green_h_line_1)
            lines.add(dot_green_v_line_2)
            lines.add(dot_green_h_line_2)
            lines.add(dot_green_v_line_3)
            lines.add(dot_green_h_line_3)
            lines.add(dot_green_v_line_4)
            lines.add(dot_green_h_line_4)
            lines.add(dot_green_v_line_5)
            lines.add(dot_green_h_line_5)
            lines.add(dot_green_v_line_6)
            lines.add(dot_green_h_line_6)
            lines.add(dot_green_v_line_7)
            lines.add(dot_green_h_line_7)
            lines.add(dot_green_v_line_8)
            lines.add(dot_green_h_line_8)

            # lines.reverse_direction()

            return lines

        lines = green_dot_func()

        self.play(Uncreate(dot_green))
        #
        # for line in lines:
        #     line.reverse_direction()
        self.play(Uncreate(lines))

        lines = VGroup()
        dot_red_tkr = ValueTracker(1)
        dot_red = redraw(
            lambda: Dot(color=RED).move_to(axes.c2p(dot_red_tkr.get_value(), func(dot_red_tkr.get_value()))))

        self.play(Create(dot_red))

        self.play(dot_red_tkr.animate.set_value(0.9))

        def red_dot_func():
            dot_red_v_line_1 = DashedLine(start=axes.c2p(dot_red_tkr.get_value(), 0), end=dot_red)
            self.play(Create(dot_red_v_line_1))

            dot_red_h_line_1 = DashedLine(start=dot_red.get_center(),
                                          end=axes.c2p(func(dot_red_tkr.get_value()), func(dot_red_tkr.get_value())))
            self.play(Create(dot_red_h_line_1))

            dot_red_v_line_2 = DashedLine(start=dot_red_h_line_1.get_end(),
                                          end=axes.c2p(func(dot_red_tkr.get_value()), func(func(dot_red_tkr.get_value()))))
            self.play(Create(dot_red_v_line_2))

            self.play(dot_red_tkr.animate.set_value(func(dot_red_tkr.get_value())))

            dot_red_h_line_2 = DashedLine(start=dot_red.get_center(),
                                          end=axes.c2p(func(dot_red_tkr.get_value()), func(dot_red_tkr.get_value())))
            self.play(Create(dot_red_h_line_2))

            lines.add(dot_red_v_line_1)
            lines.add(dot_red_h_line_1)
            lines.add(dot_red_v_line_2)
            lines.add(dot_red_h_line_2)

            # lines.reverse_direction()

            return lines

        lines = red_dot_func()

        self.play(Uncreate(dot_red))
        #
        # for line in lines:
        #     line.reverse_direction()
        self.play(Uncreate(lines))

        self.wait(10)
class simplex(ThreeDScene):

    def construct(self):

        # self.add(NumberPlane())
        self.set_camera_orientation(phi=30*DG)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.begin_ambient_camera_rotation(rate=0.05,about='phi')

        dot = Dot()
        line =Line(start=[-5,-1,0],end=[-3,-2,0], color =BLUE)


        vertex_coords = [
            [2, 2, 0],
            [4, 2, 0],
            [3,2+ np.sin(60*DG)*2, 0],
        ]
        faces_list = [
            [0, 1, 2]
        ]

        tri =Triangle(fill_opacity=0.5, fill_color=RED).move_to(O).shift(R*3+U*3).scale(1.5)

        vertex_coords = [
            [0, 0, 0],
            [2, 0, 0],
            [1, np.sin(60*DG)*2, 0],
            center_of_mass([[0, 0, 0],[2, 0, 0],[1, np.sin(60*DG)*2, 0]])+OUT*np.sin(60*DG)*2
        ]
        faces_list = [
            [0, 1, 2],
            [1, 2, 3],
            [2, 0, 3],
            [1, 0, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list,faces_config={'fill_opacity':0.3, 'fill_color':RED})
        pyramid = Tetrahedron(faces_config={'fill_opacity':0.3, 'fill_color':RED}).scale(3)

        pyramid[ 1 ][0].scale(0.5).set_style(fill_opacity=1,stroke_opacity=1)
        pyramid[ 1 ][1].scale(0.5).set_style(fill_opacity=1,stroke_opacity=1)
        pyramid[ 1 ][2].scale(0.5).set_style(fill_opacity=1,stroke_opacity=1)
        pyramid[ 1 ][3].scale(0.5).set_style(fill_opacity=1,stroke_opacity=1)


        self.play(Create(dot))
        self.wait(2)
        self.play(ReplacementTransform(dot,line))
        self.wait(2)
        self.play(ReplacementTransform(line,tri))
        self.wait(2)
        self.play(ReplacementTransform(tri,pyramid.faces))
        self.wait(25)

class maps(MovingCameraScene):


    def construct(self):

        # svg_test=SVGMobject('svgs/지하철노선도_gradation.svg')
        svg_test=SVGMobject('svgs/지도.svg', unpack_groups=False).scale(2)

        svg_test[ 0 ][ 1 ].set_style(stroke_width=15)

        svg_test.save_state()
        svg_test[ :3 ].arrange_in_grid(10, 15, buff=1)
        # self.play()

        self.play(Create(svg_test[0]))
        self.wait(1)
        self.play(Create(svg_test[1]))
        self.wait(1)
        self.play(Create(svg_test[2]))
        self.wait(1)

        self.play(svg_test.animate.restore())

        anims=[]
        for store in svg_test[2]:
            anims.append(FadeOut(store))

        self.wait(1)

        self.play(AnimationGroup(*anims, lag_ratio=0.5))
        self.wait(1)

        anims=[]
        for metro in svg_test[1]:
            anims.append(FadeOut(metro))


        self.play(AnimationGroup(*anims, lag_ratio=0.5))




        self.wait(3)
