from manim import *

config.frame_width = 16
config.frame_height = 9
q=0.3
from colour import Color

utils.tex.TexTemplate(tex_compiler="latex")

class intro(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-30,30 , 1],
            y_range=[0, 1, 1],
            tips=False,

        )


        sig_func = FunctionGraph(
            lambda x: 1/(1+e**(-x)),
            color=RED,
        )


        sig=ax.plot(lambda x: 1/(1+e**(-x)))
        sig.set_color(color= [RED, GREEN, BLUE])
        vertical = Line(start=np.array([0, 10, 0.]), end=np.array([0, -10, 0.]))
        vertical.set_color(color= [RED, GREEN, BLUE])

        horizontal = Line(end=np.array([20, 0, 0]), start=np.array([-20, 0, 0]))
        horizontal.set_color(color= [RED, GREEN, BLUE])


        self.play(Create(sig))

        self.play(ReplacementTransform(sig,horizontal,rate_func=linear))
        self.play(ReplacementTransform(horizontal, vertical, rate_func=linear))

        vertical_2 = vertical.copy()

        vertical_n_black_1= VGroup(vertical, Square(10,fill_color=BLACK, fill_opacity=1).next_to(vertical, LEFT ,buff=0))
        vertical_n_black_2= VGroup(vertical_2, Square(10,fill_color=BLACK, fill_opacity=1).next_to(vertical_2, RIGHT,buff=0))

        defi_text =Tex("DeFi").move_to(np.array([0,0,-1]))

        self.add(defi_text)

        self.play(vertical_n_black_1.animate.shift(LEFT*10),vertical_n_black_2.animate.shift(RIGHT*10), rate_functions= rush_from,run_time=0.7)

        self.wait(2)


class all(Scene):
    def construct(self):
        bianry_explained.construct(self)
        bit_and_byte_explained.construct(self)
        hex_explained.construct(self)
        ascii_explained.construct(self)


class ascii_explained(Scene):
    def construct(self):
        # banner = ManimBanner()
        title = Title("How does a computer understand a letter?")

        explain_txt_1 = Tex("컴퓨터는 아")

        self.play(Write(title, run_time=1))

        ascii_table = MathTable(
            [ [ "Alpha", "Decimal", "Hex" ],
              [ "A", 65, 41 ],
              [ "B", 66, 42 ],
              [ "L", 76, "4C" ],
              [ "X", 88, 58 ],
              [ "Y", 89, 59 ],
              [ "Z", 90, "5A" ]
              ],
            include_outer_lines=True)

        ascii_table.scale(0.7)

        self.play(Create(ascii_table))
        self.play(ascii_table.animate.shift(4 * LEFT))
        self.wait(1)

        explain_txt_2 = Tex(r"Hex 한 자리는 4자리의 2진수로 표현됩니다.\\"
                            r"두 자리면 256가지를 표현하고 1byte가 됩니다").move_to(RIGHT * 3 + UP * 2)
        explain_txt_2.scale(0.7)

        self.play(FadeIn(explain_txt_2, shift=UP))

        ascii_table.get_cell((4, 1), color=RED)

        hex_to_bin = MathTex(r"01001100", substrings_to_isolate=[ "0100" ]).move_to(RIGHT * 3)
        hex_to_bin2 = MathTex(r"0100 \quad 1100", substrings_to_isolate=[ "0100" ]).move_to(RIGHT * 3)
        middle = MathTex(r"4 \quad 12", substrings_to_isolate=[ "4" ]).move_to(RIGHT * 3 + DOWN * 1)
        bin_to_hex = MathTex(r"4 \quad C", substrings_to_isolate=[ "4" ]).move_to(RIGHT * 3 + DOWN * 2)
        final = Tex(r"0", "x", "4", "C").move_to(RIGHT * 3 + DOWN * 1)

        hex_to_bin[ 0 ].set_color(RED)
        hex_to_bin[ 1 ].set_color(BLUE)
        hex_to_bin2[ 0 ].set_color(RED)
        hex_to_bin2[ 1 ].set_color(BLUE)
        bin_to_hex[ 0 ].set_color(RED)
        bin_to_hex[ 1 ].set_color(BLUE)
        middle[ 0 ].set_color(RED)
        middle[ 1 ].set_color(BLUE)
        final[ 2 ].set_color(RED)
        final[ 3 ].set_color(BLUE)

        group = VGroup(hex_to_bin, middle, bin_to_hex)

        sq_height = ascii_table[ 3 ].get_y() - ascii_table[ 4 ].get_y()
        sq_wid = ascii_table[ 10 ].get_x() - ascii_table[ 9 ].get_x()

        my_sq = Rectangle(width=sq_wid, height=sq_height, color=RED, stroke_width=5).align_to(ascii_table.get_cell((4, 1)), UL)

        decimal = ascii_table[ 0 ][ 10 ].copy()
        self.play(Create(my_sq))
        self.play(decimal.animate.scale(1.5).move_to(UP + RIGHT * 3))

        # self.add(index_labels(table_cols))
        # self.play(Create(ascii_table.get_cell((4,1),color= RED)),
        #           Create(ascii_table.get_cell((4,3),color = RED)))
        # self.add(index_labels(ascii_table[0]))

        # self.add(index_labels(hex_to_bin))
        # self.add(index_labels(bin_to_hex))
        # self.add(index_labels(middle))
        self.play(Write(hex_to_bin))
        self.play(Transform(hex_to_bin, hex_to_bin2))
        self.play(Write(middle))
        self.play(Write(bin_to_hex))
        self.wait(1)
        self.play(Transform(group, final))
        self.wait(1)

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ])


class bianry_explained(Scene):
    def construct(self):
        # banner = ManimBanner()
        title = Title("What is Binary?")
        self.play(Write(title, run_time=1))

        zero = MathTex(r"0", font_size=150)
        one = MathTex(r"1", font_size=150)

        zero_n_one = VGroup(zero, one)

        self.play(Write(zero.move_to(LEFT), run_time=0.5), Write(one.move_to(RIGHT), run_time=1))

        # number = format(45645546846567823476789678, 'b')

        # zeros_n_ones=Tex(r"\parbox{1cm} {...1001000110110000001100010100110110000001100010101110...}", font_size=150)
        # zeros_n_ones.scale(0.6)a

        zeros_n_ones = Paragraph("100100011011000000110001010011011001",
                                 "000011001001000110110000001100010100",
                                 "110110000001100010101110100100001100",
                                 "000011001001000110101100000011001001",
                                 "110110000001100010100110110000001100",
                                 "101110100101100000011001001000110101", font_size=50, font='Batang', line_spacing=1)
        zeros_n_ones.scale(0.6)

        self.play(ReplacementTransform(zero_n_one, zeros_n_ones, run_time=1))

        simple_bin = MathTex(r"1011", font_size=150, substrings_to_isolate=[ '1', '0', '1', '1' ]).shift(UP * 1)
        simple_bin[ 0 ].set_color(RED)
        simple_bin[ 1 ].set_color(YELLOW)
        simple_bin[ 2 ].set_color(GREEN)
        simple_bin[ 3 ].set_color(BLUE)
        # self.add(index_labels(simple_bin))
        self.wait(1)

        self.play(ReplacementTransform(zeros_n_ones, simple_bin))
        self.wait(1)

        arrow1 = Arrow(start=simple_bin[ 3 ].get_bottom() + DOWN * 2, end=simple_bin[ 3 ].get_bottom() + DOWN * 0.05, buff=0.2)
        arrow_lable1_1 = MathTex(r"2^n \times \  0 \  OR \  1").next_to(arrow1, DOWN)
        arrow_label1_2 = MathTex(r"2^0 \times 1").next_to(arrow_lable1_1, DOWN)
        # arrow_lable1_1.add_updater(lambda x : x.next_to(arrow1, DOWN*2))
        word_spacing = (arrow1.get_x() - simple_bin[ 2 ].get_x())

        arrow_label2_2 = MathTex(r"2^1 \times 1").next_to(arrow_lable1_1, DOWN).shift(word_spacing * LEFT)
        arrow_label3_2 = MathTex(r"2^2 \times 0").next_to(arrow_lable1_1, DOWN).shift(word_spacing * 2 * LEFT)
        arrow_label4_2 = MathTex(r"2^3 \times 1").next_to(arrow_lable1_1, DOWN).shift(word_spacing * 3 * LEFT)

        # self.add(index_labels(arrow_label2))
        # arrow_label2[3].set_color(BLUE)

        animations = [
            Create(arrow1),
            Create(arrow_lable1_1),
            Create(arrow_label1_2)
        ]

        self.play(AnimationGroup(*animations, lag_ratio=0.3))
        arrow_lable1_1.add_updater(lambda arrow_label: arrow_label.next_to(arrow1, DOWN))

        # self.play(Create(arrow1),
        #           Create(arrow_lable1_1),
        #           Create(arrow_label1_2), lag_ration= 0.2)
        self.wait(1)

        self.play(arrow1.animate.shift(word_spacing * LEFT), ReplacementTransform(arrow_label1_2, arrow_label2_2))
        self.play(arrow1.animate.shift(word_spacing * LEFT), ReplacementTransform(arrow_label2_2, arrow_label3_2))
        self.play(arrow1.animate.shift(word_spacing * LEFT), ReplacementTransform(arrow_label3_2, arrow_label4_2))
        self.wait(2)

        animations = [
            FadeOut(arrow1),
            FadeOut(arrow_lable1_1),
            FadeOut(arrow_label1_2)
        ]

        # self.play(AnimationGroup(*animations, lag_ratio=0.3))
        self.play(FadeOut(arrow1),
                  FadeOut(arrow_lable1_1),
                  FadeOut(arrow_label4_2), lag_ratio=0.5)

        self.wait(2)

        target1 = MathTex(r"2^0 \times 1", substrings_to_isolate=[ "2^0", r"\times", "1" ], font_size=80).move_to(np.array([ 6, 0, 0 ]))
        target1[ 4 ].set_color(BLUE)
        # self.add(index_labels(target1))
        target1_1 = MathTex(r"1 \times 1", substrings_to_isolate=[ "1", r"\times", "1" ], font_size=80).move_to(np.array([ 6, 0, 0 ]))
        target1_1[ 4 ].set_color(BLUE)
        # self.add(index_labels(target1_1))

        target2 = MathTex(r"2^1 \times 1", substrings_to_isolate=[ "2^1", r"\times", "1" ], font_size=80).move_to(np.array([ 2, 0, 0 ]))
        target2[ 4 ].set_color(GREEN)
        target2_1 = MathTex(r"2 \times 1", substrings_to_isolate=[ "2", r"\times", "1" ], font_size=80).move_to(np.array([ 2, 0, 0 ]))
        target2_1[ 4 ].set_color(GREEN)
        # # self.add(index_labels(target1))
        #
        target3 = MathTex(r"2^2 \times 0", substrings_to_isolate=[ "2^2", r"\times", "0" ], font_size=80).move_to(np.array([ -2, 0, 0 ]))
        target3[ 4 ].set_color(YELLOW)
        target3_1 = MathTex(r"4 \times 0", substrings_to_isolate=[ "4", r"\times", "0" ], font_size=80).move_to(np.array([ -2, 0, 0 ]))
        target3_1[ 4 ].set_color(YELLOW)

        # # self.add(index_labels(target1))
        #
        target4 = MathTex(r"2^3 \times 1", substrings_to_isolate=[ "2^3", r"\times", "1" ], font_size=80).move_to(np.array([ -6, 0, 0 ]))
        target4[ 4 ].set_color(RED)
        target4_1 = MathTex(r"8 \times 1", substrings_to_isolate=[ "8", r"\times", "1" ], font_size=80).move_to(np.array([ -6, 0, 0 ]))
        target4_1[ 4 ].set_color(RED)

        # # self.add(index_labels(target1))

        # target2 = MathTex(r"2^0 + 1 \plus",substrings_to_isolate=["2^0", r"\times", "1"]).next_to(target1)
        # target3 = MathTex(r"2^0 + 1 \plus",substrings_to_isolate=["2^0", r"\times", "1"]).next_to(target1)
        # target4 = MathTex(r"2^0 + 1",substrings_to_isolate=["2^0", r"\times", "1"]).next_to(target1)

        animations = [
            TransformMatchingShapes(simple_bin[ 3 ], target1),
            TransformMatchingShapes(simple_bin[ 2 ], target2),
            TransformMatchingShapes(simple_bin[ 1 ], target3),
            TransformMatchingShapes(simple_bin[ 0 ], target4)
        ]
        # self.play(TransformMatchingShapes(simple_bin[ 3 ], target1),
        #           TransformMatchingShapes(simple_bin[ 2 ], target2),
        #           TransformMatchingShapes(simple_bin[ 1 ], target3),
        #           TransformMatchingShapes(simple_bin[ 0 ], target4))


        self.play(AnimationGroup(*animations, lag_ratio=0.3))

        animations = [
            ReplacementTransform(target1, target1_1),
            ReplacementTransform(target2, target2_1),
            ReplacementTransform(target3, target3_1),
            ReplacementTransform(target4, target4_1)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.2))

        # self.play(ReplacementTransform(target1, target1_1),
        #           ReplacementTransform(target2, target2_1),
        #           ReplacementTransform(target3, target3_1),
        #           ReplacementTransform(target4, target4_1))

        animations = [
            target1_1.animate.move_to(DOWN * 2),
            target2_1.animate.move_to(DOWN),
            target3_1.animate.move_to(ORIGIN),
            target4_1.animate.move_to(UP)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.2))
        self.wait(1)


        bin_group = VGroup(target4_1, target3_1, target2_1, target1_1)
        plus = MathTex(r"8 + 0 + 2 + 1 = 11", font_size=100, substrings_to_isolate=[ "8", "0", "2", "1", '=11' ])
        # self.add(index_labels(plus))
        plus[ 6 ].set_color(BLUE)
        plus[ 4 ].set_color(GREEN)
        plus[ 2 ].set_color(YELLOW)
        plus[ 0 ].set_color(RED)
        plus_sign = VGroup(plus[1], plus[3], plus[5])

        animations = [
            TransformMatchingShapes(target4_1, plus[ 0 ]),
            TransformMatchingShapes(target3_1, plus[ 2 ]),
            TransformMatchingShapes(target2_1, plus[ 4 ]),
            TransformMatchingShapes(target1_1, plus[ 6 ])
        ]
        # self.play(, lag_ratio= 1)
        self.play(AnimationGroup(*animations, lag_ratio=0.25))
        self.wait(1)

        self.play(Create(plus_sign))

        # self.play(Transform(bin_group,plus[0:7]))
        self.play(Write(plus[ 7:10 ]))
        # self.play(Write(plus[1]))
        # self.play(target1_1.animate.move_to(UP),
        #           target2_1.animate.move_to(ORIGIN),
        #           target3_1.animate.move_to(DOWN),
        #           target4_1.animate.move_to(DOWN * 2),
        #           lag_ratio=0.2)
        #
        self.wait(2)
        # bins= VGroup()
        # bins.add(target1,target2,target3,target4)
        # bins.arrange_in_grid(1,4, buff = 0.2)
        target3_1 = MathTex(r"4 \times 0", substrings_to_isolate=[ "4", r"\times", "0" ]).move_to(np.array([ -2, -3, 0 ]))
        target3_1[ 4 ].set_color(YELLOW)
        # self.play(circle.animate.move_to(RIGHT * 4), rate_func=there_and_back)

        # self.play(Create(target3_1.to_edge(LEFT)))

        # t1 = MathTex(r"\frac {x_1 x_2}{x_1 + x_2}={{5}}")
        # eq = MathTex(r"\frac {x_1 x_2}{x_1 + x_2}=5 \int_{i=1}^n", substrings_to_isolate=[r"\frac {x_1 x_2}{x_1 + x_2}=","5","\int_", "{i=1}", "^n"],font_size=100)
        # eq2 = MathTex(r"\frac{1}{x_1} + \frac{1}{x_2}")
        # eq[ 0:2 ].set_color(RED)
        # self.add(index_labels(eq))
        # self.play(FadeIn(eq[0:2]))

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ])


class bit_and_byte_explained(Scene):
    def construct(self):
        title = Title("What is Bit and Byte?")

        self.play(Write(title, run_time=1))

        # table = r"""
        # \begin{table}[]
        # \centering
        # \begin{tabular}{|l|l|l|l|l|}\hline
        # &  & \multicolumn{2}{l}{End} &  \\\hline
        # Top &  & Bottom & Bottom &  \\
        # & Top & 40 & 160 & 200 \\
        # & Bottom & 640 & 160 & 800 \\
        # &  & 200 & 800 & 1000 \\\hline
        # \end{tabular}
        # \end{table}
        # """
        # tex_table = Tex(table)
        # self.play(Write(tex_table))

        # t0 = Table(
        #     [["First", "Second"],
        #     ["Third","Fourth"]],
        #     row_labels=[Text("R1"), Text("R2")],
        #     col_labels=[Text("C1"), Text("C2")],
        #     top_left_entry=Text("TOP"))
        # t0.add_highlighted_cell((2,2), color=GREEN)
        # x_vals = np.linspace(-2,2,5)
        # y_vals = np.exp(x_vals)
        # t1 = DecimalTable(
        #     [x_vals, y_vals],
        #     row_labels=[MathTex("x"), MathTex("f(x)")],
        #     include_outer_lines=True)
        # t1.add(t1.get_cell((2,2), color=RED))
        t2 = MathTable(
            [ [ 1, 0, 1, 1, 0, 0, 1, 1 ] ],
            include_outer_lines=True)

        # t2.add(t2.get_cell(1, 1), color=RED)
        # t2.get_horizontal_lines()[:3].set_color(BLUE)
        # t2.get_vertical_lines()[:3].set_color(BLUE)
        # t2.get_horizontal_lines()[:3].set_z_index(1)
        # cross = VGroup(
        #     Line(UP + LEFT, DOWN + RIGHT),
        #     Line(UP + RIGHT, DOWN + LEFT))
        # a = Circle().set_color(RED).scale(0.5)
        # b = cross.set_color(BLUE).scale(0.5)
        # t3 = MobjectTable(
        #     [[a.copy(),b.copy(),a.copy()],
        #     [b.copy(),a.copy(),a.copy()],
        #     [a.copy(),b.copy(),b.copy()]])
        # t3.add(Line(
        #     t3.get_corner(DL), t3.get_corner(UR)
        # ).set_color(RED))
        # vals = np.arange(1,21).reshape(5,4)
        # t4 = IntegerTable(
        #     vals,
        #     include_outer_lines=True
        # )
        # g1 = Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(UP, buff=1)
        # g2 = Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        self.play(Create(t2, run_time=0.8))
        # ApplyMethod(a.move_to, RIGHT * 4, rate_func=there_and_back)
        # self.wait(1)

        red_rec = t2.get_cell((1, 1), color=RED)
        bit = Tex("1 bit").next_to(red_rec, DOWN)
        byte = Tex(r"8 bits = 1 byte").next_to(t2, DOWN)

        self.play(Create(red_rec), Create(bit), run_time=1)
        self.wait(1)

        self.play(FadeOut(red_rec), FadeOut(bit))
        self.wait(1)

        red_row = SurroundingRectangle(t2.get_rows()[ 0 ], color=RED)
        red_rows = t2.get_horizontal_lines().copy()
        red_cols = t2.get_vertical_lines().copy()
        red_rows.set_color(RED)
        red_cols.set_color(RED)
        sq = VGroup(red_rows, red_cols[ 5 ], red_cols[ -1 ])
        sq_height = red_rows[ 0 ].get_y() - red_rows[ 1 ].get_y()

        sq_wid = red_cols[ 1 ].get_x() - red_cols[ 0 ].get_x()
        my_sq = Rectangle(width=sq_wid, height=sq_height, color=RED, stroke_width=10).move_to(t2.get_center())
        # whole_rec = VGroup(red_rows, red_cols[0], red_cols[1])

        # self.play(Create(red_rows[1]),
        #           DrawBorderThenFill(red_cols[0]),
        #           DrawBorderThenFill(red_cols[1]))

        what_is_byte = Tex(r"bit는 컴퓨터에서 정보의 최소단위지만 너무 작아, \\컴퓨터가 조작하는 정보의 최소 처리 단위는 byte입니다.").next_to(byte, DOWN)
        what_is_byte2 = Tex(r"2의 8제곱은 256으로 1 byte는 \\256가지 정보를 표현할 수 있습니다.").next_to(byte, DOWN)
        self.play(Create(my_sq), Write(byte), Write(what_is_byte))
        self.wait(1)
        self.play(TransformMatchingShapes(what_is_byte, what_is_byte2))

        # self.play()

        self.wait(1)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ])


class hex_explained(Scene):
    def construct(self):
        # banner = ManimBanner()
        title = Title("What is Hex?")

        self.play(Write(title, run_time=1))

        hex_num = MathTex(r"0123456789", font_size=150).move_to(UP)
        hex_alpha = MathTex(r"ABCDEF", font_size=150).next_to(hex_num, DOWN)

        hex_num_alpha = VGroup(hex_num, hex_alpha)
        animations = [ Write(hex_num, run_time=0.5),
                       Write(hex_alpha, run_time=0.5)

                       ]
        # self.play(AnimationGroup(*animations, lag_ratio=1))
        self.play(Write(hex_num, run_time=0.5))
        self.wait(1)
        self.play(Write(hex_alpha, run_time=0.5))
        self.wait(1)

        self.add(hex_num_alpha)
        self.remove(hex_num, hex_alpha)

        explain_text_1 = Tex(r"이렇게 숫자 2개로 표현하면 2진법,\\우리가 평소에 보듯이 10단위로 자릿수를 바꾸면 10진법,\\ 16개로 표현하면 16진법이라 부릅니다.)")

        self.play(TransformMatchingShapes(hex_num_alpha, explain_text_1))
        self.wait(1)

        explain_text_2 = Tex(r"0(0x00)~255(0xFF)\\이렇게 생긴 걸 한번쯤 보셨을 수도 있습니다.\\"
                             r"이것이 16진법표기고, 0x는 이것이 16진수라는 것을\\"
                             r"표현하기 위한 표시입니다. 16진법은 영어로 Hexadecimal입니다")

        self.play(FadeOut(explain_text_1))
        self.play(FadeIn(explain_text_2))

        simple_hex = MathTex(r"54BF", font_size=150, substrings_to_isolate=[ '5', '4', 'B', 'F' ]).shift(UP * 1)
        simple_hex[ 0 ].set_color(RED)
        simple_hex[ 1 ].set_color(YELLOW)
        simple_hex[ 2 ].set_color(GREEN)
        simple_hex[ 3 ].set_color(BLUE)
        # self.add(index_labels(simple_bin))
        self.wait(1)
        # self.add(index_labels(simple_hex))

        self.play(ReplacementTransform(explain_text_2, simple_hex))
        self.wait(1)

        arrow1 = Arrow(start=simple_hex[ 3 ].get_bottom() + DOWN * 2, end=simple_hex[ 3 ].get_bottom() + DOWN * 0.05, buff=0.2)
        arrow_lable1_1 = MathTex(r"16^n \times \  0~F(15)").next_to(arrow1, DOWN)
        arrow_label1_2 = MathTex(r"16^0 \times F(15)").next_to(arrow_lable1_1, DOWN)
        y_val = arrow_label1_2.get_y()
        arrow_y_val = arrow1.get_y()
        # arrow_lable1_1.add_updater(lambda x : x.next_to(arrow1, DOWN*2))
        word_spacing = (arrow1.get_x() - simple_hex[ 2 ].get_x())
        word_spacing2 = (simple_hex[ 1 ].get_x() - simple_hex[ 2 ].get_x())
        word_spacing3 = (simple_hex[ 0 ].get_x() - simple_hex[ 1 ].get_x())

        arrow_label2_2 = MathTex(r"16^1 \times B(11)").move_to(np.array([ simple_hex[ 2 ].get_x(), y_val, 0 ]))
        arrow_label3_2 = MathTex(r"16^2 \times 4").move_to(np.array([ simple_hex[ 1 ].get_x(), y_val, 0 ]))
        arrow_label4_2 = MathTex(r"16^3 \times 5").move_to(np.array([ simple_hex[ 0 ].get_x(), y_val, 0 ]))

        # self.add(index_labels(arrow_label2))
        # arrow_label2[3].set_color(BLUE)

        animations = [
            Create(arrow1),
            Create(arrow_lable1_1),
            Create(arrow_label1_2)
        ]

        self.play(AnimationGroup(*animations, lag_ratio=0.3))
        arrow_lable1_1.add_updater(lambda arrow_label: arrow_label.next_to(arrow1, DOWN))

        # self.play(Create(arrow1),
        #           Create(arrow_lable1_1),
        #           Create(arrow_label1_2), lag_ration= 0.2)
        self.wait(1)

        self.play(arrow1.animate.move_to(np.array([ simple_hex[ 2 ].get_x(), arrow_y_val, 0 ])),
                  ReplacementTransform(arrow_label1_2, arrow_label2_2))
        self.play(arrow1.animate.move_to(np.array([ simple_hex[ 1 ].get_x(), arrow_y_val, 0 ])),
                  ReplacementTransform(arrow_label2_2, arrow_label3_2))
        self.play(arrow1.animate.move_to(np.array([ simple_hex[ 0 ].get_x(), arrow_y_val, 0 ])),
                  ReplacementTransform(arrow_label3_2, arrow_label4_2))
        self.wait(2)

        animations = [
            FadeOut(arrow1),
            FadeOut(arrow_lable1_1),
            FadeOut(arrow_label1_2)
        ]

        # self.play(AnimationGroup(*animations, lag_ratio=0.3))
        self.play(FadeOut(arrow1),
                  FadeOut(arrow_lable1_1),
                  FadeOut(arrow_label4_2), lag_ratio=0.5)

        self.wait(2)

        my_font = 50

        target1 = MathTex(r"16^0 \times F(15)", substrings_to_isolate=[ "16^0", r"\times", "F(15)" ], font_size=my_font).move_to(
            np.array([ 6, 0, 0 ]))
        target1[ 4 ].set_color(BLUE)
        # self.add(index_labels(target1))
        target1_1 = MathTex(r"1 \times F(15)", substrings_to_isolate=[ "1", r"\times", "F(15)" ], font_size=my_font).move_to(
            np.array([ 6, 0, 0 ]))
        target1_1[ 4 ].set_color(BLUE)
        # self.add(index_labels(target1_1))

        target2 = MathTex(r"16^1 \times B(11)", substrings_to_isolate=[ "16^1", r"\times", "B(11)" ], font_size=my_font).move_to(
            np.array([ 2, 0, 0 ]))
        target2[ 4 ].set_color(GREEN)
        target2_1 = MathTex(r"16 \times B(11)", substrings_to_isolate=[ "16", r"\times", "B(11)" ], font_size=my_font).move_to(
            np.array([ 2, 0, 0 ]))
        target2_1[ 4 ].set_color(GREEN)
        # # self.add(index_labels(target1))
        #
        target3 = MathTex(r"16^2 \times 4", substrings_to_isolate=[ "16^2", r"\times", "4" ], font_size=my_font).move_to(
            np.array([ -2, 0, 0 ]))
        target3[ 4 ].set_color(YELLOW)
        target3_1 = MathTex(r"256 \times 4", substrings_to_isolate=[ "256", r"\times", "4" ], font_size=my_font).move_to(
            np.array([ -2, 0, 0 ]))
        target3_1[ 4 ].set_color(YELLOW)

        # # self.add(index_labels(target1))
        #
        target4 = MathTex(r"16^3 \times 5", substrings_to_isolate=[ "16^3", r"\times", "5" ], font_size=my_font).move_to(
            np.array([ -6, 0, 0 ]))
        target4[ 4 ].set_color(RED)
        target4_1 = MathTex(r"4096 \times 5", substrings_to_isolate=[ "4096", r"\times", "5" ], font_size=my_font).move_to(
            np.array([ -6, 0, 0 ]))
        target4_1[ 4 ].set_color(RED)

        animations = [
            TransformMatchingShapes(simple_hex[ 3 ], target1),
            TransformMatchingShapes(simple_hex[ 2 ], target2),
            TransformMatchingShapes(simple_hex[ 1 ], target3),
            TransformMatchingShapes(simple_hex[ 0 ], target4)
        ]
        # self.play(TransformMatchingShapes(simple_bin[ 3 ], target1),
        #           TransformMatchingShapes(simple_bin[ 2 ], target2),
        #           TransformMatchingShapes(simple_bin[ 1 ], target3),
        #           TransformMatchingShapes(simple_bin[ 0 ], target4))
        self.play(AnimationGroup(*animations, lag_ratio=0.3))

        animations = [
            ReplacementTransform(target1, target1_1),
            ReplacementTransform(target2, target2_1),
            ReplacementTransform(target3, target3_1),
            ReplacementTransform(target4, target4_1)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.2))

        # self.play(ReplacementTransform(target1, target1_1),
        #           ReplacementTransform(target2, target2_1),
        #           ReplacementTransform(target3, target3_1),
        #           ReplacementTransform(target4, target4_1))

        animations = [
            target1_1.animate.move_to(DOWN * 2),
            target2_1.animate.move_to(DOWN),
            target3_1.animate.move_to(ORIGIN),
            target4_1.animate.move_to(UP)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.2))
        self.wait(1)

        bin_group = VGroup(target4_1, target3_1, target2_1, target1_1)
        plus = MathTex(r"20480 + 1024 + 176 + 15 = 21695", font_size=100, substrings_to_isolate=[ "20480", "1024", "176", "15", '=21695' ])
        # self.add(index_labels(plus))
        plus[ 6 ].set_color(BLUE)
        plus[ 4 ].set_color(GREEN)
        plus[ 2 ].set_color(YELLOW)
        plus[ 0 ].set_color(RED)
        plus_sign = VGroup(plus[1], plus[3], plus[5])

        #
        # self.play(TransformMatchingShapes(target4_1, plus[ 0 ]))
        # self.play(TransformMatchingShapes(target3_1, plus[ 2 ]))
        # self.play(TransformMatchingShapes(target2_1, plus[ 4 ]))
        # self.play(TransformMatchingShapes(target1_1, plus[ 6 ]))
        # self.play(Write(plus[ 7:10 ]))

        animations = [
            TransformMatchingShapes(target4_1, plus[ 0 ]),
            TransformMatchingShapes(target3_1, plus[ 2 ]),
            TransformMatchingShapes(target2_1, plus[ 4 ]),
            TransformMatchingShapes(target1_1, plus[ 6 ])
        ]
        # self.play(, lag_ratio= 1)
        self.play(AnimationGroup(*animations, lag_ratio=0.25))
        self.wait(1)

        self.play(Create(plus_sign))

        # self.play(Transform(bin_group,plus[0:7]))
        self.play(Write(plus[ 7:10 ]))

        explain_text_3 = Tex(r"16.)")

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ])

#
# class CreateCircle(Scene):
#     def construct(self):
#
#         t1 = MathTex(r"\frac {x_1 x_2}{x_1 + x_2}={{5}}")
#         eq = MathTex(r"\frac {x_1 x_2}{x_1 + x_2}=5 \int_{i=1}^n",
#                      substrings_to_isolate=[ r"\frac {x_1 x_2}{x_1 + x_2}=", "5", "\int_", "{i=1}", "^n" ], font_size=100)
#         eq2 = MathTex(r"\frac{1}{x_1} + \frac{1}{x_2}")
#         eq[ 0:2 ].set_color(RED)
#         self.add(index_labels(eq))
#         self.play(FadeIn(eq[ 0:2 ]))
#
#
#         eqt = MathTex(r"\sum_{i=0}^3 (5 + \sqrt{4^i}) = ?").scale(1.5)
#         self.play(Write(eqt))
#         self.wait()
#
#         eq = MathTex(r"\sum_{i=0}^3 (5 + \sqrt{4^i})").scale(0.8)
#         eq.to_corner(UL, buff=0.5)
#         self.play(Transform(eqt, eq), run_time=2)
#         self.wait()
#
#         R1 = MathTex(r" = (5 + {{\sqrt{4^0}}}) + (5 + {{\sqrt{4^1}}}) + (5 + {{\sqrt{4^2}}}) + (5 + {{\sqrt{4^3}}})")
#         R1.next_to(eq, RIGHT)
#         self.play(Write(R1), run_time=4)
#         self.wait()
#
#         R2 = MathTex(r" = 5 + \sqrt{1} + 5 + \sqrt{4} + 5 + \sqrt{16} + 5 + \sqrt{64}")
#         R2.next_to(eq, DOWN + RIGHT)
#         self.play(Write(R2), run_time=4)
#         self.wait()
#
#         R3 = MathTex(r" = (5 + 1) + (5 + 2) + (5 + 4) + (5 + 8)")
#         R3.next_to(eq, 6 * DOWN + RIGHT)
#         self.play(Write(R3), run_time=4)
#         self.wait()
#
#         R4 = MathTex(r" = 20 + 15 = 35")
#         R4.next_to(eq, 10 * DOWN + RIGHT)
#         self.play(Write(R4), run_time=3)
#         self.wait()
#
#         eq = MathTex(r"\sum_{i=0}^3 (5 + \sqrt{4{{^i}}})").scale(0.8)
#         eq.to_corner(UL, buff=0.5)
#         self.play(Transform(eqt, eq), run_time=2)
#         self.wait()
#         eq[ 1 ].set_color(YELLOW)
#         self.play(ReplacementTransform(eq[ 1 ], eq[ 1 ]))
#         self.wait()
#
#         t = MathTex(r"\int_sex^b f''''(x) dx = f(b)- f(a)")
#         # self.add(t)
#
#         t1 = MathTex(r'E=mc^2 \subset \sum \prod \alpha \beta \gamma \rho \sigma \delta \epsilon \alpha A \beta B \rho \varrho P'
#                      r'\phi \varphi \Phi \lim_{h \to 0} (x-h)')
#         self.play(Write(t1))
#
#         t2 = MathTex(
#             r"\frac{1}{a+b\sqrt{2}} x^{2 \alpha} - 1 = y_{ij} + y_{ij} \int\limits_0^1 x^2 + y^2 \ dx \int_0^1 x^2 + y^2 \ dx   a_1^2 + a_2^2 = a_3^2").next_to(
#             t1, DOWN)
#         self.play(Write(t2))
#         t3 = MathTex(
#             r"\sum_{i=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}}, (a^n)^{r+s} = a^{nr+ns} a_{n_i} \int_{i=1}^n \sum_{i=1}^{\infty}").next_to(
#             t2, DOWN)
#         self.play(Write(t3))
#         t4 = MathTex(r"\iint_V \mu(u,v) \,du\,dv \iiiint_V \mu(t,u,v,w) \,dt\,du\,dv\,dw \int_{a}^{b} x^2 \,dx").next_to(t3, DOWN)
#         self.play(Write(t4))
#
#         r"\frac {x_1 x_2}{x_1 + x_2}"
#
#
#
# class CreateCircle(Scene):
#     def construct(self):
#
#         t1 = MathTex(r"\frac {x_1 x_2}{x_1 + x_2}={{5}}")
#         eq = MathTex(r"\frac {x_1 x_2}{x_1 + x_2}=5 \int_{i=1}^n",
#                      substrings_to_isolate=[ r"\frac {x_1 x_2}{x_1 + x_2}=", "5", "\int_", "{i=1}", "^n" ], font_size=100)
#         eq2 = MathTex(r"\frac{1}{x_1} + \frac{1}{x_2}")
#         eq[ 0:2 ].set_color(RED)
#         self.add(index_labels(eq))
#         self.play(FadeIn(eq[ 0:2 ]))
#
#
#         eqt = MathTex(r"\sum_{i=0}^3 (5 + \sqrt{4^i}) = ?").scale(1.5)
#         self.play(Write(eqt))
#         self.wait()
#
#         eq = MathTex(r"\sum_{i=0}^3 (5 + \sqrt{4^i})").scale(0.8)
#         eq.to_corner(UL, buff=0.5)
#         self.play(Transform(eqt, eq), run_time=2)
#         self.wait()
#
#         R1 = MathTex(r" = (5 + {{\sqrt{4^0}}}) + (5 + {{\sqrt{4^1}}}) + (5 + {{\sqrt{4^2}}}) + (5 + {{\sqrt{4^3}}})")
#         R1.next_to(eq, RIGHT)
#         self.play(Write(R1), run_time=4)
#         self.wait()
#
#         R2 = MathTex(r" = 5 + \sqrt{1} + 5 + \sqrt{4} + 5 + \sqrt{16} + 5 + \sqrt{64}")
#         R2.next_to(eq, DOWN + RIGHT)
#         self.play(Write(R2), run_time=4)
#         self.wait()
#
#         R3 = MathTex(r" = (5 + 1) + (5 + 2) + (5 + 4) + (5 + 8)")
#         R3.next_to(eq, 6 * DOWN + RIGHT)
#         self.play(Write(R3), run_time=4)
#         self.wait()
#
#         R4 = MathTex(r" = 20 + 15 = 35")
#         R4.next_to(eq, 10 * DOWN + RIGHT)
#         self.play(Write(R4), run_time=3)
#         self.wait()
#
#         eq = MathTex(r"\sum_{i=0}^3 (5 + \sqrt{4{{^i}}})").scale(0.8)
#         eq.to_corner(UL, buff=0.5)
#         self.play(Transform(eqt, eq), run_time=2)
#         self.wait()
#         eq[ 1 ].set_color(YELLOW)
#         self.play(ReplacementTransform(eq[ 1 ], eq[ 1 ]))
#         self.wait()
#
#         t = MathTex(r"\int_sex^b f''''(x) dx = f(b)- f(a)")
#         # self.add(t)
#
#         t1 = MathTex(r'E=mc^2 \subset \sum \prod \alpha \beta \gamma \rho \sigma \delta \epsilon \alpha A \beta B \rho \varrho P'
#                      r'\phi \varphi \Phi \lim_{h \to 0} (x-h)')
#         self.play(Write(t1))
#
#         t2 = MathTex(
#             r"\frac{1}{a+b\sqrt{2}} x^{2 \alpha} - 1 = y_{ij} + y_{ij} \int\limits_0^1 x^2 + y^2 \ dx \int_0^1 x^2 + y^2 \ dx   a_1^2 + a_2^2 = a_3^2").next_to(
#             t1, DOWN)
#         self.play(Write(t2))
#         t3 = MathTex(
#             r"\sum_{i=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}}, (a^n)^{r+s} = a^{nr+ns} a_{n_i} \int_{i=1}^n \sum_{i=1}^{\infty}").next_to(
#             t2, DOWN)
#         self.play(Write(t3))
#         t4 = MathTex(r"\iint_V \mu(u,v) \,du\,dv \iiiint_V \mu(t,u,v,w) \,dt\,du\,dv\,dw \int_{a}^{b} x^2 \,dx").next_to(t3, DOWN)
#         self.play(Write(t4))
#
#         r"\frac {x_1 x_2}{x_1 + x_2}"
#
#
# class Count(Animation):
#     def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
#         # Pass number as the mobject of the animation
#         super().__init__(number, **kwargs)
#         # Set start and end
#         self.start = start
#         self.end = end
#
#     def interpolate_mobject(self, alpha: float) -> None:
#         # Set value of DecimalNumber according to alpha
#         value = self.start + (alpha * (self.end - self.start))
#         self.mobject.set_value(value)
#
#         # rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
#         # rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)
#         #
#         # self.play(Create(VGroup(rtarrow0, rtarrow1).arrange(DOWN)))
#         # tex = Tex(r'H아나 씨발ello \LaTeX', color=RED, font_size=144)
#         # self.play(Write(tex, run_time=2))
#
#         #
#         # plane = NumberPlane()
#         # self.play(FadeIn(plane, run_time=1))
#         #
#         # Text.set_default(color=GREEN)
#         #
#         # texte = Text(r"dfjkslfkjsdklfsdl", font_size=48)
#         # self.play(FadeIn(texte, run_time=3))
#         #
#         # polys = VGroup(*[RegularPolygon(5, radius=1) for j in range(5)]).arrange(RIGHT)
#         #
#         # self.play(DrawBorderThenFill(polys, run_time=2))
#         # self.play(
#         #     Rotate(polys[0], PI,run_time=5, rate_func=lambda t: t),
#         #     Rotate(polys[1], PI,run_time=5, rate_func=smooth),
#         #     Rotate(polys[2], PI,run_time=5, rate_func=lambda t: np.sin(t*PI)),
#         #     Rotate(polys[3], PI,run_time=5, rate_func=there_and_back),
#         #     Rotate(polys[4], PI,run_time=5, rate_func=lambda t: 1-abs(1-2*t)))
#
#         # sqs = VGroup(*[Square(color=Color(hue=i/20, saturation=1, luminance=0.5), fill_opacity=0.5) for i in range(20)]).arrange(RIGHT).scale(0.3)
#         # self.play(AnimationGroup(*[DrawBorderThenFill(s) for s in sqs], lag_ratio=0.5, run_time=5))
#
#         #
#         # s = Square()
#         # self.play(s.animate.scale(1/2).shift(LEFT*4))
#         # self.play(s.scale(1/2).animate.shift(RIGHT*4))
#         #
#         # self.add(s.shift(UP*2))
#         # self.wait(2)
#         #
#
#         # Create Decimal Number and add it to scene
#         # number = DecimalNumber().set_color(WHITE).scale(0.5)
#         # Add an updater to keep the DecimalNumber centered as its value changes
#         # number.add_updater(lambda number: number.shift(LEFT*1))
#         #
#         # self.add(number)
#         #
#         # self.wait()
#
#         # Play the Count Animation to count from 0 to 100 in 4 seconds
#         # self.play(Count(number, 0, 100), run_time=4, rate_func=smooth)
#         # self.update_self(0)
#         #
#         # self.wait()
#
#         # p1= [-1,-1,0]
#         # p2= [1,-1,0]
#         # p3= [1,1,0]
#         # p4= [-1,1,0]
#         # a = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
#         # point_start= a.get_start()
#         # point_end  = a.get_end()
#         # point_center = a.get_center()
#         # self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
#         # self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
#         # self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))
#         #
#         # self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
#         # self.add(Dot(a.get_end()).set_color(RED).scale(2))
#         # self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
#         # self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
#         # self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
#         # self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
#         # self.add(*[Dot(x) for x in a.points])
#         # self.add(a)
#         #
