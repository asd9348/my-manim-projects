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

