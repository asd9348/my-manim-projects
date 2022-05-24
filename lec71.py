from manim import *
import numpy as np
import random
import scipy.stats as scipy_stats


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

