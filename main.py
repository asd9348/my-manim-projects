from manim import *
import itertools as it

config.frame_width = 16
config.frame_height = 9
from hashlib import sha256
import binascii

from colour import Color

utils.tex.TexTemplate(tex_compiler="latex")


# def sha256_bit_int(message):
#     hexdigest = sha256(message.encode('utf-8')).hexdigest()
#     return int(hexdigest, 16)
#

def sha256_bit_string(message):
    hexdigest = sha256(message.encode('utf-8')).hexdigest()
    return bin(int(hexdigest, 16))[ 2: ]


#
# def bit_string_to_mobject(bit_string):
#     line = Tex("0" * 32)
#     pre_result = VGroup(*[
#         line.copy() for row in range(8)
#     ])
#     pre_result.arrange(DOWN, buff=SMALL_BUFF)
#     result = VGroup(*it.chain(*pre_result))
#     result.scale(0.7)
#     bit_string = (256 - len(bit_string)) * "0" + bit_string
#     result
#
#     for i, (bit, part) in enumerate(zip(bit_string, result)):
#         if bit == "1":
#             one = Tex("1")[ 0 ]
#             one.replace(part, dim_to_match=1)
#             result.submobjects[ i ] = one
#
#     return result
#

def msg_to_mob(msg, width, rows, buff=0.2):
    if rows % 2 != 0:
        raise Exception('2의 배수가 아닙니다.')

    msg = sha256_bit_string(msg)

    half_rows = int(rows / 2)
    i = 0
    chopped_list = [ msg[ i: i + width ] for i in range(0, len(msg), width) ]
    starts = chopped_list[ :half_rows - 1 ]
    ends = chopped_list[ -half_rows - 1: ]

    starts.extend(ends)
    starts.insert(half_rows, r"\vdots")

    mobs = VGroup()
    for row in range(rows + 1):
        mobs.add(MathTex(starts[ row ]))
        # if row= half_rows:
        # mobs.add(MathTex(""))

    mobs.arrange_in_grid(6, 1, buff=buff)

    return mobs


#
# def sha256_tex_mob(message, n_forced_start_zeros=30):
#     true_bit_string = sha256_bit_string(message)
#     n = n_forced_start_zeros
#     bit_string = "0" * n + true_bit_string[ n: ]
#     return bit_string_to_mobject(bit_string)
#

def create_asset_mob(text, width=0.5, height=0.3, fill_color=GREEN, stroke_color=GREEN):
    box = Rectangle(width=width, height=height, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1)
    text = Text(text, color=BLACK).scale(height)

    return VGroup(box, text)


def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
    person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

    box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
    text = Text(asset_name, color=BLACK).scale(asset_height)

    asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

    return VGroup(person, asset)


class working(Scene):
    def construct(self):
        defi_text = Tex("DeFi", substrings_to_isolate=[ "De", "Fi" ])

        self.play(Write(defi_text))

        defi_text_extended = Tex("Decentralized Finance", substrings_to_isolate=[ "Decentralized", "Finance" ])
        # self.add(index_labels(defi_text))
        self.add(index_labels(defi_text_extended))

        self.play(TransformMatchingShapes(defi_text[ 0 ], defi_text_extended[ 0 ].move_to([ 0, 0.5, 0 ])),
                  TransformMatchingShapes(defi_text[ 1 ], defi_text_extended[ 2 ].move_to([ 0, -0.5, 0 ])))
        self.wait(1)
        self.play(FadeOut(defi_text_extended))

        cefi_text = Tex("CeFi", substrings_to_isolate=[ "Ce", "Fi" ])

        self.play(Write(cefi_text))

        cefi_text_extended = Tex("Centralized Finance", substrings_to_isolate=[ "Centralized", "Finance" ])
        self.play(TransformMatchingShapes(cefi_text[ 0 ], cefi_text_extended[ 0 ].move_to([ 0, 0.5, 0 ])),
                  TransformMatchingShapes(cefi_text[ 1 ], cefi_text_extended[ 2 ].move_to([ 0, -0.5, 0 ])))
        self.wait(1)
        self.play(FadeOut(cefi_text_extended))

        market_rect = RoundedRectangle(corner_radius=0.5, height=6.0, width=4.5)
        market_rect_text = Tex("Market").next_to(market_rect, UP, buff=0.2)
        market = VGroup(market_rect, market_rect_text)

        self.play(Create(market))
        self.wait(1)

        # person_a = LabeledDot("A",radius=0.4,fill_opacity=1.0, color='#3FF3FF')
        # person_a_asset = create_asset_mob("¥")
        # A = VGroup(person_a, person_a_asset.next_to(person_a,DOWN, buff =0.1))

        A = create_entity("A", 0.5, WHITE, "€", GREEN, 0.5, 0.3)
        B = create_entity("B", 0.5, WHITE, "$", GREEN, 0.5, 0.3)
        C = create_entity("C", 0.5, WHITE, "₩", GREEN, 0.5, 0.3)
        D = create_entity("D", 0.5, WHITE, "BTC", ORANGE, 0.5, 0.3)
        E = create_entity("E", 0.5, WHITE, "ETH", BLUE, 0.5, 0.3)
        F = create_entity("F", 0.5, WHITE, "RICE", YELLOW, 0.5, 0.3)
        G = create_entity("G", 0.5, WHITE, "", GREEN, 0.5, 0.3)
        H = create_entity("H", 0.5, WHITE, "USD", GREEN, 0.5, 0.3)

        # self.play(Create(create_asset_mob("$")))

        self.play(Create(A.to_edge(UR)))
        self.wait(1)


class lec1_s1(Scene):
    def construct(self):
        pass


class lec1_s2(Scene):
    def construct(self):
        pass


class lec1_s3(Scene):
    def construct(self):
        pass


class lec1_s4(Scene):
    def construct(self):
        pass


class lec1_s5(Scene):
    def construct(self):
        pass


class lec1_s6(Scene):
    def construct(self):
        pass


class lec1_s7(Scene):
    def construct(self):
        pass


class eliptical(Scene):
    def construct(self):
        var = Variable(-2, Tex("x value"), num_decimal_places=3)
        my_tracker = var.tracker

        ax = Axes().move_to(ORIGIN)
        graph = ax.plot(
            lambda x: x + 3,
            color=RED, )

        # c2p_point2 = plane.c2p(my_tracker.get_value(), graph.get_point_from_function(my_tracker.get_value()))
        graph1 = ax.plot_implicit_curve(lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3, color=RED
                                        )

        def get_my_dot():
            # c2p_point2 = ax.c2p(my_tracker.get_value(), graph.get_point_from_function(1))
            # c2p_point2 = ax.c2p(*graph.get_point_from_function(my_tracker.get_value()))
            c2p_point2 = ax.c2p(my_tracker.get_value(),
                                graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 0 ])

            c2p_point1 = ax.c2p(my_tracker.get_value(),
                                graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 0 ])
            c2p_point2 = ax.c2p(my_tracker.get_value(),
                                graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 1 ])
            point2_y_val = graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 1 ]
            dot1 = Dot(c2p_point1, color=YELLOW)
            dot2 = Dot(c2p_point2, color=BLUE)

            arrow1 = Arrow(ax.get_center(), dot1.get_center(), buff=0)
            arrow1 = Arrow(ax.get_center(), dot2.get_center(), buff=0)
            # label = Tex(f"({my_tracker.get_value()},{point2_y_val})").next

            group = VGroup(dot1, dot2, arrow1)
            return group

        dots = always_redraw(lambda: get_my_dot())
        self.play(Create(var))
        self.play(Create(dots), Create(ax), Create(graph1))
        self.play(my_tracker.animate.set_value(3))
        self.wait(1)
        self.play(my_tracker.animate.set_value(-2))


class working_aside(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[ -10, 10 ], y_range=[ -10, 10 ], background_line_style={"stroke_opacity": 0.8},
                            axis_config={"include_numbers": True, "stroke_width": 10, "color": PURPLE})

        # graph = ImplicitFunction(
        #     lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3,
        #     color=YELLOW
        # )
        # plane.plot(graph)

        ax = Axes(
            x_range=[ -10, 10, 1 ],
            y_range=[ -100, 100, 1 ],
            tips=False,

        )

        graph1 = plane.plot_implicit_curve(lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3, color=RED
                                           )

        point = ax.c2p(5, 3)

        dot = Dot(point)
        v_line = plane.get_line_from_axis_to_point(1, point, line_func=Line, line_config={}, color=BLUE, stroke_width=5)

        my_tracker = ValueTracker(3)

        c2p_point1 = plane.c2p(my_tracker.get_value(),
                               graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 0 ])
        c2p_point2 = plane.c2p(my_tracker.get_value(),
                               graph1.get_points_from_function(my_tracker.get_value(), "-y ** 2 + x ** 3 - 3 * x + 3")[ 1 ])

        dot1 = always_redraw(lambda: Dot(c2p_point1, color=YELLOW))
        dot2 = Dot(c2p_point2, color=BLUE, radius=0.2)
        # dot1.add_updater(lambda mob : mob.ne)

        # h_line = Line(start=plane.c2p(0,graph.get_point_from_function(1)), end=plane.c2p(-2,graph.get_curve_functions(1)))

        # label = plane.get_graph_label(graph=graph1,label=Tex("this is a point"),x_val=4.798567064438934, dot=True, direction=DR, dot_config={"color":BLUE})
        # t_label = plane.get_T_label(x_val=4, graph=graph1, label=Tex("x-value"))

        # area = plane.get_area(graph1, x_range=(-1,5))
        # self.play(Create(graph1), Create(plane), Create(dot), Create(v_line), Create(h_line))
        self.play(Create(NumberPlane()), Create(graph1), Create(dot1), Create(dot2))
        self.play(my_tracker.animate.set_value(5))
        self.wait(0.5)
        self.play(Create(dot1))
        self.wait(0.5)

        # self.play(my_tracker.animate.set_value(0))
        # self.play(ApplyMethod(my_tracker.set_value(),2, run_time=2))

        #
        # backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
        # backg_plane.add_coordinates()
        #
        # my_plane = NumberPlane(x_range = [-6,6], x_length = 5,
        # y_range = [-10,10], y_length=5)
        # my_plane.add_coordinates()
        # my_plane.shift(RIGHT*3)
        #
        # my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5),
        # x_range=[-6,6], color = GREEN_B)
        #
        # label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(
        #     my_plane, UP, buff=0.2)
        #
        # area = my_plane.get_area(graph = my_function,
        # x_range = [-5,5], color = BLUE)
        #
        # horiz_line = Line(
        #     start = my_plane.c2p(0, my_function.underlying_function(-2)),
        # end = my_plane.c2p(-2, my_function.underlying_function(-2)),
        # stroke_color = YELLOW, stroke_width = 10)
        #
        # self.play(backg_plane.animate.set_opacity(0.2))
        # self.wait()
        # self.play(DrawBorderThenFill(my_plane), run_time=2)
        # self.wait()
        # self.play(Create(my_function), Write(label), run_time=2)
        # self.wait()
        # self.play(FadeIn(area), run_time = 2)
        # self.wait()
        # self.play(Create(horiz_line), run_time = 2)
        # self.wait()

        # banner = ManimBanner()
        title = Title("How does a computer understand a letter?")
        # btc_msg1 = sha256_tex_mob("BTC")
        # btc_msg2 = Tex(sha256_bit_string("BTC"))
        # btc_msg3 = bit_string_to_mobject("BTC")
        # self.play(Create(btc_msg3))

        # self.play(Write(title, run_time=1))

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

        def dot_position(mobject):
            mobject.set_value(dot.get_center()[ 0 ])
            mobject.next_to(dot)

        dot = Dot(RIGHT * 3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        # self.add(dot, label)
        Text1 = Text("BTC")
        # text_int = Va
        # tracker = ValueTracker(sha256_bit_int(5))

        a = Integer(0)

        a.add_updater(lambda a: a.set_value(tracker.get_value()))
        # decimal = MathTex(r"")

        # def int_to_bin(int_mob):
        #     val = int(int_mob.get_value())
        #     bin1 = format(val, '0256b')[0:63]
        #     # bin2 = format(val, '0256b')[64:127]
        #     # bin3 = format(val, '0256b')[128:191]
        #     bin4 = format(val, '0256b')[192:255]
        #
        #     return VGroup(Tex(bin1),MathTex(r"\vdots"),Tex(bin4)).arrange_in_grid(3,1,buff=0.2)
        # def bin_list(int_mob):
        #     val = int(int_mob.get_value())
        #     bin1 = format(val, '0256b')[0:63]
        #     bin2 = format(val, '0256b')[64:127]
        #     bin3 = format(val, '0256b')[128:191]
        #     bin4 = format(val, '0256b')[192:255]
        #     bin_list=[bin1,bin2,bin3,bin4]
        #
        #     return bin_list

        # decimal= always_redraw(int_to_bin(tracker).next_to(a, DOWN))
        # decimal= Text("2").add_updater(lambda x : int_to_bin(tracker).next_to(a, DOWN))
        # decimal= always_redraw(lambda : int_to_bin(tracker).move_to(DOWN).scale(0.7))

        circle = Circle(radius=1, color=RED)

        square = Square(1, color=BLUE)
        # group = VGroup(circle)

        circle.add(square)
        circle.arrange_in_grid(2, 1, buff=2)
        #
        self.add(msg_to_mob("BTC", 32, 4))

        # self.play(Create(Text1))
        # self.play(Create(a), Create(decimal))
        # self.play(tracker.animate.set_value(1565645),run_time=1)
        # self.play(Text1.animate.set_value("djfkd"),run_time=1)
        # self.play(ApplyMethod(tracker.set_value(),1231231231231236456789789789789789879789789789789789, run_time=2)

        # tracker.set_value(12312312312312123131312312312313123123113123123121233)
        # a.set_value(50)
        # self.wait(2)

        # start = 2.0
        #
        # x_var = Variable(start, 'x', num_decimal_places=3)
        # sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
        # Group(x_var, sqr_var).arrange(DOWN)
        #
        # sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))
        #
        # self.add(x_var, sqr_var)
        # self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
        # self.wait(0.1)


class IntroduceSHA256(Scene):
    def construct(self):
        self.introduce_evaluation()
        self.inverse_function_question()
        self.issue_challenge()
        self.shift_everything_down()
        self.guess_and_check()

    def introduce_evaluation(self):
        messages = [
            "3Blue1Brown",
            "3Blue1Crown",
            "Mathologer",
            "Infinite Series",
            "Numberphile",
            "Welch Labs",
            "3Blue1Brown",
        ]
        groups = VGroup()
        for message in messages:
            lhs = TexText(
                "SHA256", "(``", message, "'') =",
                arg_separator=""
            )
            lhs.set_color_by_tex(message, BLUE)
            digest = sha256_tex_mob(message)
            digest.next_to(lhs, RIGHT)
            group = VGroup(lhs, digest)
            group.to_corner(UP + RIGHT)
            group.shift(MED_LARGE_BUFF * DOWN)
            groups.add(group)

        group = groups[ 0 ]
        lhs, digest = group
        sha, lp, message, lp = lhs
        sha_brace = Brace(sha, UP)
        message_brace = Brace(message, DOWN)
        digest_brace = Brace(digest, DOWN)
        sha_text = sha_brace.get_text("", "Hash function")
        sha_text.set_color(YELLOW)
        message_text = message_brace.get_text("Message/file")
        message_text.set_color(BLUE)
        digest_text = digest_brace.get_text("``Hash'' or ``Digest''")
        brace_text_pairs = [
            (sha_brace, sha_text),
            (message_brace, message_text),
            (digest_brace, digest_text),
        ]

        looks_random = TexText("Looks random")
        looks_random.set_color(MAROON_B)
        looks_random.next_to(digest_text, DOWN)

        self.add(group)
        self.remove(digest)
        for brace, text in brace_text_pairs:
            if brace is digest_brace:
                self.play(LaggedStartMap(
                    FadeIn, digest,
                    run_time=4,
                    lag_ratio=0.05
                ))
                self.wait()
            self.play(
                GrowFromCenter(brace),
                Write(text, run_time=2)
            )
            self.wait()
        self.play(Write(looks_random))
        self.wait(2)
        for mob in digest, message:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m: (m.set_color, YELLOW),
                rate_func=there_and_back,
                run_time=1
            ))
        self.wait()
        self.play(FadeOut(looks_random))

        new_lhs, new_digest = groups[ 1 ]
        char = new_lhs[ 2 ][ -5 ]
        arrow = Arrow(UP, ORIGIN, buff=0)
        arrow.next_to(char, UP)
        arrow.set_color(RED)
        self.play(ShowCreation(arrow))
        for new_group in groups[ 1: ]:
            new_lhs, new_digest = new_group
            new_message = new_lhs[ 2 ]
            self.play(
                Transform(lhs, new_lhs),
                message_brace.stretch_to_fit_width, new_message.get_width(),
                message_brace.next_to, new_message, DOWN,
                MaintainPositionRelativeTo(message_text, message_brace),
                MaintainPositionRelativeTo(sha_brace, lhs[ 0 ]),
                MaintainPositionRelativeTo(sha_text, sha_brace)
            )
            self.play(Transform(
                digest, new_digest,
                run_time=2,
                lag_ratio=0.5,
                path_arc=np.pi / 2
            ))
            if arrow in self.get_mobjects():
                self.wait()
                self.play(FadeOut(arrow))
        self.wait()

        new_sha_text = TexText(
            "Cryptographic", "hash function"
        )
        new_sha_text.next_to(sha_brace, UP)
        new_sha_text.shift_onto_screen()
        new_sha_text.set_color(YELLOW)
        new_sha_text[ 0 ].set_color(GREEN)
        self.play(Transform(sha_text, new_sha_text))
        self.wait()

        self.lhs = lhs
        self.message = message
        self.digest = digest
        self.digest_text = digest_text
        self.message_text = message_text

    def inverse_function_question(self):
        arrow = Arrow(3 * RIGHT, 3 * LEFT, buff=0)
        arrow.set_stroke(width=8)
        arrow.set_color(RED)
        everything = VGroup(*self.get_mobjects())
        arrow.next_to(everything, DOWN)
        words = TexText("Inverse is infeasible")
        words.set_color(RED)
        words.next_to(arrow, DOWN)

        self.play(ShowCreation(arrow))
        self.play(Write(words))
        self.wait()

    def issue_challenge(self):
        desired_output_text = TexText("Desired output")
        desired_output_text.move_to(self.digest_text)
        desired_output_text.set_color(YELLOW)
        new_digest = sha256_tex_mob("Challenge")
        new_digest.replace(self.digest)
        q_marks = TexText("???")
        q_marks.move_to(self.message_text)
        q_marks.set_color(BLUE)

        self.play(
            Transform(
                self.digest, new_digest,
                run_time=2,
                lag_ratio=0.5,
                path_arc=np.pi / 2
            ),
            Transform(self.digest_text, desired_output_text)
        )
        self.play(
            FadeOut(self.message),
            Transform(self.message_text, q_marks)
        )
        self.wait()

    def shift_everything_down(self):
        everything = VGroup(*self.get_top_level_mobjects())
        self.play(
            everything.scale, 0.85,
            everything.to_edge, DOWN
        )

    def guess_and_check(self):
        groups = VGroup()
        for x in range(32):
            message = "Guess \\#%d" % x
            lhs = TexText(
                "SHA256(``", message, "'') = ",
                arg_separator=""
            )
            lhs.set_color_by_tex("Guess", BLUE)
            digest = sha256_tex_mob(message)
            digest.next_to(lhs, RIGHT)
            group = VGroup(lhs, digest)
            group.scale(0.85)
            group.next_to(self.digest, UP, aligned_edge=RIGHT)
            group.to_edge(UP)
            groups.add(group)

        group = groups[ 0 ]
        self.play(FadeIn(group))
        for new_group in groups[ 1: ]:
            self.play(Transform(
                group[ 0 ], new_group[ 0 ],
                run_time=0.5,
            ))
            self.play(Transform(
                group[ 1 ], new_group[ 1 ],
                run_time=1,
                lag_ratio=0.5
            ))
