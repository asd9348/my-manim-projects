class working2(ThreeDScene):

    def construct(self):
        pmt_circle = Circle(stroke_width=10, radius=3, color=WHITE).rotate(PI / 2)
        pmt_circle_12 = Arc(radius=3, color=WHITE, angle=2 * PI / 3).rotate(PI / 2, about_point=O)
        pmt_circle_23 = Arc(radius=3, color=WHITE, angle=2 * PI / 3).rotate(PI / 2 + 2 * PI / 3, about_point=O)
        pmt_circle_31 = Arc(radius=3, color=WHITE, angle=2 * PI / 3).rotate(PI / 2 + 2 * 2 * PI / 3, about_point=O)
        dummy_radius = 3.7
        circle_dummy = Circle(radius=dummy_radius, color=WHITE).rotate(PI / 2)
        self.add(pmt_circle)

        letter_1 = LabeledDot(r'\phi 1 ', color=GREEN).move_to(pmt_circle.point_from_proportion(0))
        letter_2 = LabeledDot(r'\phi 2 ', color=GREEN).move_to(pmt_circle.point_from_proportion(1 / 3))
        letter_3 = LabeledDot(r'\phi 3 ', color=GREEN).move_to(pmt_circle.point_from_proportion(2 / 3))

        pos_label_1 = Tex('1').next_to(letter_1, U)
        pos_label_2 = Tex('2').next_to(letter_2, DL)
        pos_label_3 = Tex('3').next_to(letter_3, DR)

        P_2_ops = MathTex('\hat{P}_2').scale(1.5)
        d_arrow_1 = DoubleArrow(start=letter_2.get_corner(UR), end=letter_1.get_corner(DL), color=GREEN_B)

        swap = Tex('Swap!').next_to(P_2_ops, D)

        P_3_ops = MathTex('\hat{P}_3').scale(1.5)

        shift = Tex(r'Shift to the right\\by one unit!').scale_to_fit_width(2).next_to(P_3_ops, D)
        c_arrow_12 = CurvedArrow(stroke_width=2, stroke_color=GREY, radius=dummy_radius,
                                 start_point=circle_dummy.point_from_proportion(0 + 0.05),
                                 end_point=circle_dummy.point_from_proportion(1 / 3 - 0.05)).scale(0.9)
        c_arrow_23 = CurvedArrow(stroke_width=2, stroke_color=GREY, radius=dummy_radius,
                                 start_point=circle_dummy.point_from_proportion(1 / 3 + 0.05),
                                 end_point=circle_dummy.point_from_proportion(2 / 3 - 0.05))
        c_arrow_31 = CurvedArrow(stroke_width=2, stroke_color=GREY, radius=dummy_radius,
                                 start_point=circle_dummy.point_from_proportion(2 / 3 + 0.05),
                                 end_point=circle_dummy.point_from_proportion(1 - 0.05))

        self.play(Create(letter_1),
                  Create(letter_2),
                  Create(letter_3), )
        self.wait(1)
        self.play(Create(pos_label_1),
                  Create(pos_label_2),
                  Create(pos_label_3), )

        self.play(Write(P_2_ops))
        self.wait(1)

        # self.play(Create(c_arrow_12),
        #           Create(c_arrow_21),)
        self.play(Create(d_arrow_1), )
        self.wait(1)

        self.play(Write(swap))
        self.play(Indicate(swap))
        self.wait(1)

        self.play(Swap(letter_1, letter_2))
        self.wait(1)

        self.play(Unwrite(P_2_ops),
                  Uncreate(d_arrow_1),
                  Unwrite(swap),
                  Swap(letter_1, letter_2), run_time=2)
        self.wait(1)

        self.play(Write(P_3_ops))

        self.play(Write(shift))
        self.play(Indicate(shift))

        self.play(Create(c_arrow_12),
                  Create(c_arrow_23),
                  Create(c_arrow_31),
                  )

        p_3_2_123_1 = MathTex(r'\hat{P}_3^2 (123)').move_to(L * 6)
        p_3_2_123_2 = MathTex(r'\hat{P}_3 \hat{P}_3(123) ').move_to(p_3_2_123_1)
        p_3_2_123_3 = MathTex(r'\hat{P}_3(312)=(231) ').move_to(p_3_2_123_1)

        self.play(Write(p_3_2_123_1))
        self.play(Write(p_3_2_123_1))
        self.play(Write(p_3_2_123_1))

        self.play(MoveAlongPath(letter_1, pmt_circle_12),
                  MoveAlongPath(letter_2, pmt_circle_23),
                  MoveAlongPath(letter_3, pmt_circle_31),
                  )

        # self.play()

        self.wait(2)


class working2(ThreeDScene):

    def construct(self):
        p_2_123 = MathTex(r'\hat{P}_2 (123)=(213)')
        p_3_123 = MathTex(r'\hat{P}_3 (123)=(312)')
        p_2_2_123 = MathTex(r'\hat{P}_2^2 (123)=\hat{P}_2 \hat{P}_2(123) =\hat{P}_2(312)=(123)')
        p_3_2_123 = MathTex(r'\hat{P}_3^2 (123)=\hat{P}_3 \hat{P}_3(123) =\hat{P}_3(312)=(231)')

        pmt_circle = Circle(stroke_width=10, radius=3, color=WHITE).rotate(PI / 2)
        pmt_circle_12 = Arc(radius=3, color=WHITE, angle=2 * PI / 3).rotate(PI / 2, about_point=O)
        pmt_circle_23 = Arc(radius=3, color=WHITE, angle=2 * PI / 3).rotate(PI / 2 + 2 * PI / 3, about_point=O)
        pmt_circle_31 = Arc(radius=3, color=WHITE, angle=2 * PI / 3).rotate(PI / 2 + 2 * 2 * PI / 3, about_point=O)
        dummy_radius = 3.7
        circle_dummy = Circle(radius=dummy_radius, color=WHITE).rotate(PI / 2)
        self.add(pmt_circle)

        letter_1 = LabeledDot(r'\phi_1 ', color=GREEN).move_to(pmt_circle.point_from_proportion(0))
        letter_2 = LabeledDot(r'\phi_2 ', color=GREEN).move_to(pmt_circle.point_from_proportion(1 / 12))
        letter_3 = LabeledDot(r'\phi_3 ', color=GREEN).move_to(pmt_circle.point_from_proportion(2 / 12))
        letter_4 = LabeledDot(r'\phi_4 ', color=GREEN).move_to(pmt_circle.point_from_proportion(3 / 12))
        letter_5 = LabeledDot(r'\phi_5 ', color=GREEN).move_to(pmt_circle.point_from_proportion(4 / 12))
        letter_dots_1 = LabeledDot(r'\dots ', ).move_to(pmt_circle.point_from_proportion(5 / 12)).set_z_index(1.1)
        letter_j_minus_1 = LabeledDot(r'\phi_{j-1} ', color=GREEN).move_to(pmt_circle.point_from_proportion(6 / 12))
        letter_j = LabeledDot(r'\phi_{j}', color=GREEN).move_to(pmt_circle.point_from_proportion(7 / 12))
        letter_j_plus_1 = LabeledDot(r'\phi_{j+1} ', color=GREEN).move_to(pmt_circle.point_from_proportion(8 / 12))
        letter_j_plus_2 = LabeledDot(r'\phi_{j+2} ', color=GREEN).move_to(pmt_circle.point_from_proportion(9 / 12))
        letter_dots_2 = LabeledDot(r'\dots ', ).move_to(pmt_circle.point_from_proportion(10 / 12)).set_z_index(1.1)
        letter_n = LabeledDot(r'\phi_{n}', color=GREEN).move_to(pmt_circle.point_from_proportion(11 / 12))
        letter_n_minus_1 = LabeledDot(r'\phi_{n-1}', color=GREEN).move_to(pmt_circle.point_from_proportion(10 / 12))
        letter_j_minus_2 = LabeledDot(r'\phi_{j-2}', color=GREEN).move_to(pmt_circle.point_from_proportion(5 / 12))
        letter_j_minus_3 = LabeledDot(r'\phi_{j-3}', color=GREEN).move_to(pmt_circle.point_from_proportion(5 / 12))
        letters = VGroup(letter_1,
                         letter_2,
                         letter_3,
                         letter_4,
                         letter_5,
                         letter_dots_1,
                         letter_j_minus_1,
                         letter_j,
                         letter_j_plus_1,
                         letter_j_plus_2,
                         letter_dots_2,
                         letter_n,
                         letter_n_minus_1,
                         letter_j_minus_2,
                         letter_j_minus_3
                         )
        path_arc=Arc(radius=3, color=WHITE, angle= 2*PI / 12).rotate(PI / 2, about_point=O)
        path_arc_long=Arc(radius=3, color=WHITE, angle=2*2 * PI / 12).rotate(PI / 2, about_point=O)
        path_1=path_arc.copy().rotate( 2*0 * PI / 12, about_point=O)
        path_2=path_arc.copy().rotate( 2*1 * PI / 12, about_point=O)
        path_3=path_arc.copy().rotate( 2*2 * PI / 12, about_point=O)
        path_4=path_arc.copy().rotate( 2*3 * PI / 12, about_point=O)
        path_5=path_arc.copy().rotate( 2*4 * PI / 12, about_point=O)
        path_6=path_arc.copy().rotate( 2*5 * PI / 12, about_point=O)
        path_7=path_arc.copy().rotate( 2*6 * PI / 12, about_point=O)
        path_8=path_arc.copy().rotate( 2*7 * PI / 12, about_point=O)
        path_9=path_arc.copy().rotate( 2*8 * PI / 12, about_point=O)
        path_10=path_arc.copy().rotate( 2*9 * PI / 12, about_point=O)
        path_11=path_arc.copy().rotate( 2*10 * PI / 12, about_point=O)
        path_12=path_arc.copy().rotate( 2*11 * PI / 12, about_point=O)
        # path_11=path_arc.copy().rotate( 2*11 * PI / 12, about_point=O)
        for letter in letters:
            letter.scale_to_fit_width(0.7)
        pos_label_1 = Tex('1').next_to(letter_1, U)
        pos_label_2 = Tex('2').next_to(letter_2, DL)
        pos_label_3 = Tex('3').next_to(letter_3, DR)

        P_2_ops = MathTex('\hat{P}_2').scale(1.5)
        d_arrow_P2 = DoubleArrow(stroke_width= 5,start=letter_2.get_center(), end=letter_1.get_center(),buff=0.4, color=GREEN_B)
        swap = Tex('Swap!').next_to(P_2_ops, D)

        P_4_ops = MathTex('\hat{P}_4').scale(1.5)
        P_j_ops = MathTex('\hat{P}_j').scale(1.5)
        P_n_ops = MathTex('\hat{P}_n').scale(1.5)
        self.play(Create(letters))
        self.play(Create(pos_label_1))
        # self.play(Create(letter_n_minus_1),
        #           Create(letter_j_minus_2))

        # self.add(letter_n_minus_1, letter_j_minus_2)


        self.play(Write(P_2_ops))
        self.play(Write(swap))
        self.play(Create(d_arrow_P2), )
        self.play(Indicate(swap))
        self.play(Swap(letter_1, letter_2))
        self.wait(1)
        self.play(ReplacementTransform(P_2_ops,P_4_ops),
                  Uncreate(d_arrow_P2),
                  Unwrite(swap))

        cycle = Tex(r'Cycle!').next_to(P_4_ops, D)
        self.play(Indicate(cycle))
        self.play(CyclicReplace(letter_2, letter_1,letter_3, letter_4))
        self.wait(1)
        self.play(ReplacementTransform(P_4_ops,P_j_ops))

        self.wait(1)

        self.play(Indicate(cycle))
        self.play(CyclicReplace(letter_4, letter_2,letter_1, letter_3,letter_5, letter_j_minus_2, letter_j_minus_1,letter_j))
        self.wait(1)
        shift = Tex(r'Shift to the right\\by one unit!').scale_to_fit_width(2).next_to(P_n_ops, D)

        self.play(ReplacementTransform(P_j_ops,P_n_ops),
                  ReplacementTransform(cycle,shift))
        self.wait(0.5)

        c_arrow_Pn = VGroup(Circle(stroke_width=3, color= GREY,radius=3.7),
                            Triangle(fill_opacity=1,fill_color=GREY,stroke_opacity=0).scale_to_fit_width(0.3).rotate(PI/2).move_to(3.7*U))

        self.play(Indicate(shift))
        self.play(Create(c_arrow_Pn),
                  pos_label_1.animate.next_to(letter_j,D))


        path_anims= [MoveAlongPath(letter_j, path_1),
                     MoveAlongPath(letter_4, path_2),
                     MoveAlongPath(letter_2, path_3),
                     MoveAlongPath(letter_1, path_4),
                     MoveAlongPath(letter_3, path_5),
                     MoveAlongPath(letter_j_minus_3, path_6),
                     MoveAlongPath(letter_j_minus_2, path_7),
                     MoveAlongPath(letter_j_minus_1, path_8),
                     MoveAlongPath(letter_j_plus_1, path_9),
                     MoveAlongPath(letter_j_plus_2, path_10),
                     MoveAlongPath(letter_n_minus_1 , path_11),
                     MoveAlongPath(letter_n , path_12),
                     ]
        # self.play(AnimationGroup(*path_anims,lag_ratio=0.3) ,run_time=5)
        self.play(CyclicReplace(letter_j,
                                letter_4,
                                letter_2,
                                letter_1,
                                letter_3,
                                letter_j_minus_3,
                                letter_j_minus_2,
                                letter_j_minus_1,
                                letter_j_plus_1,
                                letter_j_plus_2,
                                letter_n_minus_1,
                                letter_n
                                ))
        #
        self.wait(5)
