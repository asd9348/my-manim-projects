from manim import *
import numpy as np
import random


class NumGenerator(Scene):
    def construct(self):
        num_gen_text = Tex("Number Generator: ").to_edge(UL)

        self.play(Write(num_gen_text))

        i = 0

        for k in range(10):
            a = np.random.normal(loc=100, scale=15)  # Randomly selecting a number from a normal distribution
            num = DecimalNumber(num_decimal_places=0).set_value(a)
            num.next_to(num_gen_text, RIGHT)

            self.play(Write(num))
            self.play(num.animate.to_edge(DL).shift(RIGHT * i))
            i += 1.3

        self.wait()


class MobjectLoop(Scene):
    def construct(self):
        i = 0
        k = 0
        for k in range(10):
            circ = Circle(fill_color=BLUE, fill_opacity=0.4,
                          sheen_factor=0.5, radius=0.5).to_edge(DR)
            num = DecimalNumber(num_decimal_places=0).set_value(k)
            k += 1

            self.play(DrawBorderThenFill(circ), circ.animate.shift(UP * i + LEFT * i), run_time=0.5)
            self.play(Write(num), num.animate.next_to(circ, LEFT), run_time=0.5)
            i += 0.75

        self.wait()


class Image(Scene):
    def construct(self):
        svg = SVGMobject(f"{HOME2}\\bat.svg")
        image = ImageMobject(f"{HOME}\\door.png")

        self.play(DrawBorderThenFill(svg))
        self.play(FadeIn(image))
        self.wait()


class ArcIntegrals(Scene):
    def construct(self):

        plane_config = dict(
            axis_config={
                "include_tip": True, "include_numbers": True,
                "include_ticks": True, "line_to_number_buff": 0.05,
                "stroke_color": WHITE, "stroke_width": 0.5,
                "number_scale_val": 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config={
                "exclude_zero_from_default_numbers": True,
                "label_direction": DOWN, "stroke_color": WHITE,
                "x_min": 0, "x_max": 5, "unit_size": 1,
                "numbers_to_show": range(0, 6, 1),
            },
            y_axis_config={
                "exclude_zero_from_default_numbers": True,
                "label_direction": UR, "stroke_color": WHITE,
                "x_min": 0,  # not y_min
                "x_max": 7,  # not y_max
                "unit_size": 0.8, "numbers_to_show": range(0, 8, 1),
            },
            background_line_style={
                "stroke_width": 1, "stroke_opacity": 0.75,
                "stroke_color": GREEN_A,
            }
        )
        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = LEFT * 5 + DOWN * 3
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI / 2)

        graph = plane.get_graph(lambda x: 0.2 * (x - 1) * (x - 2) * (x - 3) + 2, x_min=0, x_max=5, color=PURPLE_A)

        self.play(Write(plane))
        self.play(ShowCreation(graph))
        self.wait()

        def get_line_integral(x, graph, dx=1, x_min=None, x_max=None):

            dots = VGroup()
            lines = VGroup()
            result = VGroup(dots, lines)

            x_range = np.arange(x_min, x_max, dx)
            colors = color_gradient([ BLUE_B, GREEN_B ], len(x_range))

            for x, color in zip(x_range, colors):
                p1 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x, graph))
                p2 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x + dx, graph))
                dots.add(p1, p2)
                dots.set_fill(colors, opacity=0.8)

                line = Line(p1.get_center(), p2.get_center(), stroke_color=RED, stroke_width=5)
                lines.add(line)

            return result

        k = ValueTracker(2)

        line_int = always_redraw(lambda:
                                 get_line_integral(x=0, graph=graph, dx=k.get_value(), x_min=0, x_max=5))

        val_tex = MathTex("dx=").to_edge(UL)
        val = DecimalNumber(num_decimal_places=2).next_to(val_tex, RIGHT)
        val.add_updater(lambda x: x.set_value(k.get_value()))

        self.play(ShowCreation(line_int))
        self.wait()
        self.add(val_tex, val)
        self.play(k.animate.set_value(1 / 10), run_time=15)
        self.wait()


class Neuroplasticity(Scene):
    def construct(self):

        def get_random_neural_network(num_neurons=None,
                                      num_layers=None, strength=None, multiple=None):
            r = 0
            layers = VGroup()
            for layer in range(num_layers):
                new_layer = VGroup(*[ Circle(radius=0.25, fill_color=BLUE, fill_opacity=0.75,
                                             sheen_factor=0.5, sheen_direction=UL,
                                             stroke_width=0.5, stroke_color=WHITE) for k in range(num_neurons) ])
                new_layer.arrange(DOWN, buff=0.3).shift(RIGHT * (r + 0.8))
                r += 0.8
                layers.add(new_layer)

            lines = VGroup()
            b = 0
            for line in range(num_layers - 1):
                new_line_set = VGroup(*[ Line(
                    layers[ b ][ random.randint(0, num_neurons - 1) ],
                    layers[ b + 1 ][ random.randint(0, num_neurons - 1) ],
                    stroke_color=(GREEN), stroke_width=1.5,
                    stroke_opacity=strength) for k in range(round(strength * multiple)) ])
                lines.add(new_line_set)
                b += 1

            result = VGroup(layers, lines)
            return result

        weak_title = Tex("Weak Plasticity").set_color(PURPLE).scale(0.75).to_edge(UL).shift(RIGHT * 0.5)
        weak_network = get_random_neural_network(
            num_neurons=5, num_layers=3, strength=0.4, multiple=20
        ).next_to(weak_title, DOWN, buff=0.5)

        strong_title = Tex("Strong Plasticity").set_color(PURPLE).scale(0.75).to_edge(UR)
        k = ValueTracker(0.2)
        strong_network = always_redraw(lambda: get_random_neural_network(
            num_neurons=8, num_layers=5, strength=k.get_value(), multiple=80
        ).next_to(strong_title, DOWN, buff=0.5))

        self.play(LaggedStart(
            Write(weak_title), ShowCreation(weak_network)),
            lag_ratio=1, run_time=3)
        self.wait()
        self.play(Write(strong_title))
        self.play(ShowCreation(strong_network), run_time=3)
        self.play(k.animate.set_value(0.95), run_time=10)

        def get_axes(self):
            axes_config = dict(
                axis_config={
                    "include_tip": False,
                    "include_ticks": True, "line_to_number_buff": 0.5,
                    "stroke_color": WHITE, "stroke_width": 2,
                    "number_scale_val": 0.5,
                    "tip_scale": 0.5,
                },
                x_axis_config={
                    "exclude_zero_from_default_numbers": True, "include_numbers": False,
                    "label_direction": DR, "stroke_color": WHITE,
                    "x_min": 0, "x_max": 1.2, "tick_frequency": 0.2,
                    "unit_size": 5, "numbers_to_show": None,
                },
                y_axis_config={
                    "exclude_zero_from_default_numbers": True, "include_numbers": False,
                    "label_direction": UR, "stroke_color": WHITE,
                    "x_min": 0,  # not y_min
                    "x_max": 2,  # not y_max
                    "unit_size": 3, "numbers_to_show": None,
                })

            return Axes(**axes_config)


class Test(Scene):
    def construct(self):

        ax = get_axes(self).to_edge(DL, buff=1)
        labels = VGroup()
        lab1 = MathTex("<155").scale(0.3).next_to(ax.x_axis.number_to_point(0.1), DOWN)
        lab2 = MathTex("155-164").scale(0.3).next_to(ax.x_axis.number_to_point(0.3), DOWN)
        lab3 = MathTex("165-174").scale(0.3).next_to(ax.x_axis.number_to_point(0.5), DOWN)
        lab4 = MathTex("175-184").scale(0.3).next_to(ax.x_axis.number_to_point(0.7), DOWN)
        lab5 = MathTex("185-194").scale(0.3).next_to(ax.x_axis.number_to_point(0.9), DOWN)
        lab6 = MathTex("195<").scale(0.3).next_to(ax.x_axis.number_to_point(1.1), DOWN)
        labels.add(lab1, lab2, lab3, lab4, lab5, lab6)

        door = ImageMobject(f"{HOME}\\door.png").scale(0.4).shift(RIGHT * 5 + UP * 1.5)

        self.play(LaggedStart(ShowCreation(ax), Write(labels)), run_time=3, lag_ratio=0.5)
        self.play(FadeIn(door))
        self.wait()

        p = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0

        for k in range(3):
            man = ImageMobject(f"{HOME}\\man.png").set_height(1).move_to(door)
            tape = ImageMobject(f"{HOME}\\tape.png").set_height(1)
            self.play(FadeIn(man), man.animate.to_edge(UP))
            self.play(FadeIn(tape), tape.animate.next_to(man, RIGHT, buff=0.1))

            k = np.random.normal(loc=175, scale=10)
            num = Integer().set_value(k).scale(0.75).next_to(tape)

            self.play(Write(num), run_time=0.25)
            boxed_res = Group(man, tape, num)
            box = SurroundingRectangle(boxed_res, stroke_color=YELLOW, stroke_width=2)
            sample = Group(box, man, tape, num)

            self.play(ShowCreation(box), sample.animate.set_width(0.75), run_time=0.5)

            if k < 155:
                self.play(sample.animate.move_to(ax.x_axis.number_to_point(0.1)).shift(UP * (0.2 + p)))
                p += 0.4
            elif 155 <= k <= 164:
                self.play(sample.animate.move_to(ax.x_axis.number_to_point(0.3)).shift(UP * (0.2 + b)))
                b += 0.4
            elif 165 <= k <= 174:
                self.play(sample.animate.move_to(ax.x_axis.number_to_point(0.5)).shift(UP * (0.2 + c)))
                c += 0.4
            elif 175 <= k <= 184:
                self.play(sample.animate.move_to(ax.x_axis.number_to_point(0.7)).shift(UP * (0.2 + d)))
                d += 0.4
            elif 184 < k <= 194:
                self.play(sample.animate.move_to(ax.x_axis.number_to_point(0.9)).shift(UP * (0.2 + e)))
                e += 0.4
            else:
                self.play(sample.animate.move_to(ax.x_axis.number_to_point(1.1)).shift(UP * (0.2 + f)))
                f += 0.4

        self.wait()

        def func(x):
            return scipy_stats.norm.pdf(x, 0.6, 0.2)

        curve = ax.get_graph(func, x_min=0, x_max=1.2, color=RED_C)

        self.play(ShowCreation(curve), FadeOut(door))
        self.wait()

