from manim import *
import numpy as np


class DualGraphs(GraphScene):
    def construct(self):
        self.x_min = -3
        self.x_max = 3
        self.y_min = 0
        self.y_max = 8
        self.x_axis_width = 6
        self.y_axis_height = 4
        self.axes_color = GRAY
        self.graph_origin = DOWN * 2 + LEFT * 3
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-3, 3 + 1, 1))
        self.y_labeled_nums = list(range(0, 8 + 1, 1))

        self.setup_axes(animate=True)

        # CREATING A CUSTOMISED NUMBER PLANE
        plane_config = dict(
            axis_config={
                "include_tip": False,
                "include_numbers": True,
                "include_ticks": True,
                "line_to_number_buff": 0.05,
                "stroke_color": WHITE,
                "stroke_width": 0.5,
                "number_scale_val": 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config={
                "exclude_zero_from_default_numbers": True,
                "label_direction": DOWN,
                "stroke_color": WHITE,
                "x_min": -2,
                "x_max": 2,
                "unit_size": 1,
                "numbers_to_show": range(-2, 2 + 1, 1),
            },
            y_axis_config={
                "exclude_zero_from_default_numbers": True,
                "label_direction": UR,
                "stroke_color": WHITE,
                "x_min": -4,  # not y_min
                "x_max": 4,  # not y_max
                "unit_size": 0.5,
                "numbers_to_show": range(-4, 4 + 1, 1),
            },
            background_line_style={
                "stroke_width": 1,
                "stroke_opacity": 0.75,
                "stroke_color": YELLOW_C,
            }
        )

        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = RIGHT * 3
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI / 2)

        ##ADDING ALL THE STUFF TO THE SCENE##

        quad = self.get_graph(lambda x: x ** 2, x_min=-3, x_max=3, color=RED_D)

        linear = plane.get_graph(lambda x: 2 * x, x_min=-2, x_max=2, color=BLUE_D)

        quad_title = TextMobject("$f(x)=x^2$").next_to(self.axes, UP, buff=0.).set_color(RED_D)
        linear_title = TextMobject(r"$\dfrac{df(x)}{dx}=2x$").next_to(plane, UP, buff=0).set_color(BLUE_D)

        text = TextMobject("I ", "am ", "keen ", "for ", "some ", "derivatives", ".... ", "MAAATE!!").scale(0.8).to_edge(DOWN)
        text[ 0 ].set_color(BLUE_D)
        text[ 1 ].set_color(RED_D)
        text[ 2 ].set_color(BLUE_D)
        text[ 3 ].set_color(RED_D)
        text[ 4 ].set_color(BLUE_D)
        text[ 5 ].set_color(RED_D)
        text[ 6 ].set_color(BLUE_D)
        text[ 7 ].set_color(RED_D)

        self.play(Write(plane), run_time=2)
        self.play(ShowCreation(quad), ShowCreation(linear), runtime=2)
        self.wait()
        self.play(ShowCreation(quad_title), ShowCreation(linear_title), runtime=2)
        self.wait()
        self.play(FadeIn(text))
        self.wait()