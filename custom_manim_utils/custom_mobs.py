from manim import *

import pyttsx3
import os
import datetime
import time
from manim.opengl import *

from datetime import timedelta
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
from tempfile import NamedTemporaryFile
from pathlib import Path
import shutil
from pprint import pprint

import manim.utils.space_ops
from manim import *

import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
# from custom_manim_utils.custom_mobs import *
from manim_physics import *
from manim_gearbox import *
# from manim_fontawesome import regular
from pathlib import Path
from custom_manim_utils.custom_consts import *
#

import itertools as it
import random
from math import ceil, floor
from typing import Callable, Iterable, Sequence

import numpy as np
from colour import Color
from PIL import Image

from manim.animation.updaters.update import UpdateFromAlphaFunc
from manim.mobject.geometry.line import Vector
from manim.mobject.graphing.coordinate_systems import CoordinateSystem
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject

import itertools as it
import random
from math import ceil, floor
from typing import Callable, Iterable, Sequence

import numpy as np
from colour import Color
from PIL import Image

from manim.animation.updaters.update import UpdateFromAlphaFunc
from manim.mobject.geometry.line import Vector
from manim.mobject.graphing.coordinate_systems import CoordinateSystem
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject

from manim import config
from manim.animation.composition import AnimationGroup, Succession
from manim.animation.creation import Create
from manim.animation.indication import ShowPassingFlash
from manim.constants import OUT, RIGHT, UP
from manim.mobject.mobject import Mobject
from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from manim.utils.bezier import interpolate, inverse_interpolate
from manim.utils.color import BLUE_E, GREEN, RED, YELLOW, color_to_rgb, rgb_to_color
from manim.utils.rate_functions import ease_out_sine, linear
from manim.utils.simple_functions import sigmoid

DEFAULT_SCALAR_FIELD_COLORS: list = [BLUE_E, GREEN, YELLOW, RED]
class CircleAsset(Circle):
    # from manim import

    def __init__(
            self,
            label: str or SingleStringMathTex or Text or Tex = None,
            radius: float or None = None,
            direction: np.array = None,
            buff: float = 0.25,
            color: str = C_BTC,
            font_size: float = None,
            width: float = None,
            **kwargs) -> None:

        # def __init__(self, corner_radius=0.5, **kwargs):
        #     super().__init__(**kwargs)
        #     self.corner_radius = corner_radius
        #     self.round_corners(self.corner_radius)
        #
        if radius is None:
            radius = 0.5

        if width is None:
            width = (2 * radius) * 0.8

        if isinstance(label, str):
            from manim import Tex
            rendered_label = Tex(rf'\textbf{{{label}}}', color=color)

        elif isinstance(label, type(None)):
            from manim import Tex
            rendered_label = Tex(rf'\textbf{{new}}', color=color)
        else:
            rendered_label = label

        if width is not None:
            rendered_label.scale(width / rendered_label.width)

        if direction is None:
            direction = O

        super().__init__(radius=radius, **kwargs)

        rendered_label.next_to(self, direction, buff=buff)
        self.add(rendered_label)

    # def set_label(self,
    #               label: str = None,
    #               font_size: float = 50,
    #               color: str = C_BTC,
    #               **kwargs):
    #     self.remove(self[ 1 ])
    #
    #     if isinstance(label, str):
    #         from manim import Tex
    #
    #         rendered_label = Tex(rf'\textbf{{{label}}}', font_size=font_size, color=color)
    #     elif isinstance(label, type(None)):
    #         from manim import Tex
    #         rendered_label = Tex(rf'\textbf{{new}}', font_size=font_size, color=color)
    #     else:
    #         rendered_label = label
    #
    #     self.add(rendered_label)


class LabeledRectangle(RoundedRectangle):

    def __init__(
            self,
            label: str or SingleStringMathTex or Text or Tex,
            width: float or None = None,
            height: float or None = None,
            corner_radius: float or None = None,
            direction: np.ndarray = UP,
            **kwargs, ) -> None:

        if isinstance(label, str):
            from manim import Tex

            rendered_label = Tex(label, color=WHITE)
        else:
            rendered_label = label

        if width is None:
            width = 0.2 + max(rendered_label.width, rendered_label.height)
        if height is None:
            height = 0.2 + max(rendered_label.height, rendered_label.height)

        if corner_radius is None:
            corner_radius = 0.2

        super().__init__(width=width, height=height, corner_radius=corner_radius, **kwargs)
        rendered_label.next_to(self, direction)
        self.add(rendered_label)



class ThreeDVMobjectFromPLY(VGroup):
    # self.vertex = [ ]
    # self.vertex = [ ]

    def __init__(self, filename, scaler=1, **kwargs
                 ) -> None:

        file= Path(filename)


        self.vertexs = get_ply_file_vertexs(filename) * scaler
        self.triangles = get_ply_file_triangles(filename)
        super().__init__(**kwargs)
        # self._setup_faces()
        # self.apply_function(lambda p: func(p[ 0 ], p[ 1 ]))
        # if self.should_make_jagged:
        #     self.make_jagged()

        dots = VGroup()
        for vertex in self.vertexs:
            vertex3d = Dot3D(vertex)

            dots.add(vertex3d)

        self.add(*dots)

        faces = VGroup()

        for triangle in self.triangles:
            face = ThreeDVMobject()
            face.set_points_as_corners([
                self.vertexs[ triangle[ 0 ] ],
                self.vertexs[ triangle[ 1 ] ],
                self.vertexs[ triangle[ 2 ] ] ])
            faces.add(face)

        faces.set_stroke(
            color=self.stroke_color,
            width=self.stroke_width,
            opacity=self.stroke_opacity,
        )

        faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)

        self.add(*faces)

class OpenGLThreeDVMobjectFromPLY(VGroup):
    # self.vertex = [ ]
    # self.vertex = [ ]

    def __init__(self, filename, scaler=1, **kwargs
                 ) -> None:

        file= Path(filename)


        self.vertexs = get_ply_file_vertexs(filename) * scaler
        self.triangles = get_ply_file_triangles(filename)
        super().__init__(**kwargs)
        # self._setup_faces()
        # self.apply_function(lambda p: func(p[ 0 ], p[ 1 ]))
        # if self.should_make_jagged:
        #     self.make_jagged()

        dots = OpenGLVGroup()
        for vertex in self.vertexs:
            vertex3d = Dot(vertex)

            dots.add(vertex3d)

        self.add(*dots)

        faces = OpenGLVGroup()

        for triangle in self.triangles:
            face = ThreeDVMobject()
            face.set_points_as_corners([
                self.vertexs[ triangle[ 0 ] ],
                self.vertexs[ triangle[ 1 ] ],
                self.vertexs[ triangle[ 2 ] ] ])
            faces.add(face)

        faces.set_stroke(
            color=self.stroke_color,
            width=self.stroke_width,
            opacity=self.stroke_opacity,
        )

        faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)

        self.add(*faces)

class ThreeDVMobjectFromCustom(VGroup):
    # self.vertex = [ ]
    # self.vertex = [ ]

    def __init__(self, vertexs, triangles, scaler=1, **kwargs
                 ) -> None:
        self.vertexs = np.array(vertexs) * scaler
        self.triangles = np.array(triangles)
        super().__init__(**kwargs)
        # self._setup_faces()
        # self.apply_function(lambda p: func(p[ 0 ], p[ 1 ]))
        # if self.should_make_jagged:
        #     self.make_jagged()

        dots = VGroup()
        for vertex in self.vertexs:
            vertex3d = Dot3D(vertex)

            dots.add(vertex3d)

        self.add(*dots)

        faces = VGroup()

        for triangle in self.triangles:
            face = ThreeDVMobject()
            face.set_points_as_corners([
                self.vertexs[ triangle[ 0 ] ],
                self.vertexs[ triangle[ 1 ] ],
                self.vertexs[ triangle[ 2 ] ] ])
            faces.add(face)

        faces.set_stroke(
            color=self.stroke_color,
            width=self.stroke_width,
            opacity=self.stroke_opacity,
        )

        faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)

        self.add(*faces)

class PointCloudMobject(VGroup):
    # self.vertex = [ ]
    # self.vertex = [ ]

    def __init__(self, vertexs, triangles, scaler=1, **kwargs
                 ) -> None:
        self.vertexs = np.array(vertexs) * scaler
        self.triangles = np.array(triangles)
        super().__init__(**kwargs)
        # self._setup_faces()
        # self.apply_function(lambda p: func(p[ 0 ], p[ 1 ]))
        # if self.should_make_jagged:
        #     self.make_jagged()

        dots = VGroup()
        for vertex in self.vertexs:
            vertex3d = Dot3D(vertex)

            dots.add(vertex3d)

        self.add(*dots)

        # faces = VGroup()
        #
        # for triangle in self.triangles:
        #     face = ThreeDVMobject()
        #     face.set_points_as_corners([
        #         self.vertexs[ triangle[ 0 ] ],
        #         self.vertexs[ triangle[ 1 ] ],
        #         self.vertexs[ triangle[ 2 ] ] ])
        #     faces.add(face)
        #
        # faces.set_stroke(
        #     color=self.stroke_color,
        #     width=self.stroke_width,
        #     opacity=self.stroke_opacity,
        # )
        #
        # faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)

        # self.add(*faces)
class PointCloudFromCustom(VGroup):

    def __init__(self, vertexs, scaler=1, **kwargs
                 ) -> None:
        self.vertexs = np.array(vertexs) * scaler
        super().__init__(**kwargs)

        dots = VGroup()
        for vertex in self.vertexs:
            vertex3d = Dot3D(vertex)

            dots.add(vertex3d)

        self.add(*dots)



        class OpenGLCharge(OpenGLVGroup):
            def __init__(
                    self,
                    magnitude: float = 1,
                    point: np.ndarray = ORIGIN,
                    add_glow: bool = True,
                    **kwargs,
            ) -> None:
                """An electrostatic charge object. Commonly used for :class:`~ElectricField`.

                Parameters
                ----------
                magnitude
                    The strength of the electrostatic charge.
                point
                    The position of the charge.
                add_glow
                    Whether to add a glowing effect. Adds rings of
                    varying opacities to simulate glowing effect.
                kwargs
                    Additional parameters to be passed to ``VGroup``.
                """
                OpenGLVGroup.__init__(self, **kwargs)
                self.magnitude = magnitude
                self.point = point
                self.radius = (abs(magnitude) * 0.4 if abs(magnitude) < 2 else 0.8) * 0.3

                if magnitude > 0:
                    label = OpenGLVGroup(
                        Rectangle(width=0.32 * 1.1, height=0.006 * 1.1),
                        Rectangle(width=0.006 * 1.1, height=0.32 * 1.1),
                    )
                    color = RED
                    layer_colors = [ RED_D, RED_A ]
                    layer_radius = 4
                else:
                    label = Rectangle(width=0.27, height=0.003)
                    color = BLUE
                    layer_colors = [ "#3399FF", "#66B2FF" ]
                    layer_radius = 2

                if add_glow:  # use many arcs to simulate glowing
                    layer_num = 20
                    color_list = color_gradient(layer_colors, layer_num)
                    opacity_func = lambda t: 1500 * (1 - abs(t - 0.009) ** 0.0001)
                    rate_func = lambda t: t ** 2

                    for i in range(layer_num):
                        self.add(
                            Arc(
                                radius=layer_radius * rate_func((0.5 + i) / layer_num),
                                angle=TAU,
                                color=color_list[ i ],
                                stroke_width=101
                                             * (rate_func((i + 1) / layer_num) - rate_func(i / layer_num))
                                             * layer_radius,
                                stroke_opacity=opacity_func(rate_func(i / layer_num)),
                            ).shift(point)
                        )

                self.add(Dot(point=self.point, radius=self.radius, color=color))
                self.add(label.scale(self.radius / 0.3).shift(point))
                for mob in self:
                    mob



class CustomStreamLines(VectorField):
    """StreamLines represent the flow of a :class:`VectorField` using the trace of moving agents.

    Vector fields are always based on a function defining the vector at every position.
    The values of this functions is displayed by moving many agents along the vector field
    and showing their trace.

    Parameters
    ----------
    func
        The function defining the rate of change at every position of the vector field.
    color
        The color of the vector field. If set, position-specific coloring is disabled.
    color_scheme
        A function mapping a vector to a single value. This value gives the position in the color gradient defined using `min_color_scheme_value`, `max_color_scheme_value` and `colors`.
    min_color_scheme_value
        The value of the color_scheme function to be mapped to the first color in `colors`. Lower values also result in the first color of the gradient.
    max_color_scheme_value
        The value of the color_scheme function to be mapped to the last color in `colors`. Higher values also result in the last color of the gradient.
    colors
        The colors defining the color gradient of the vector field.
    x_range
        A sequence of x_min, x_max, delta_x
    y_range
        A sequence of y_min, y_max, delta_y
    z_range
        A sequence of z_min, z_max, delta_z
    three_dimensions
        Enables three_dimensions. Default set to False, automatically turns True if
        z_range is not None.
    noise_factor
        The amount by which the starting position of each agent is altered along each axis. Defaults to :code:`delta_y / 2` if not defined.
    n_repeats
        The number of agents generated at each starting point.
    dt
        The factor by which the distance an agent moves per step is stretched. Lower values result in a better approximation of the trajectories in the vector field.
    virtual_time
        The time the agents get to move in the vector field. Higher values therefore result in longer stream lines. However, this whole time gets simulated upon creation.
    max_anchors_per_line
        The maximum number of anchors per line. Lines with more anchors get reduced in complexity, not in length.
    padding
        The distance agents can move out of the generation area before being terminated.
    stroke_width
        The stroke with of the stream lines.
    opacity
        The opacity of the stream lines.

    Examples
    --------

    .. manim:: BasicUsage
        :save_last_frame:

        class BasicUsage(Scene):
            def construct(self):
                func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
                self.add(StreamLines(func))

    .. manim:: SpawningAndFlowingArea
        :save_last_frame:

        class SpawningAndFlowingArea(Scene):
            def construct(self):
                func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
                stream_lines = StreamLines(
                    func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
                )

                spawning_area = Rectangle(width=6, height=4)
                flowing_area = Rectangle(width=8, height=6)
                labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
                for lbl in labels:
                    lbl.add_background_rectangle(opacity=0.6, buff=0.05)

                self.add(stream_lines, spawning_area, flowing_area, *labels)

    """

    def __init__(
        self,
        func: Callable[[np.ndarray], np.ndarray],
        color: Color or None = None,
        color_scheme: Callable[[np.ndarray], float] or None = None,
        min_color_scheme_value: float = 0,
        max_color_scheme_value: float = 2,
        colors: Sequence[Color] = DEFAULT_SCALAR_FIELD_COLORS,
        # Determining stream line starting positions:
        x_range: Sequence[float] = None,
        y_range: Sequence[float] = None,
        z_range: Sequence[float] = None,
        three_dimensions: bool = False,
        noise_factor: float or None = None,
        n_repeats=1,
        # Determining how lines are drawn
        dt=0.05,
        virtual_time=3,
        max_anchors_per_line=100,
        padding=3,
        # Determining stream line appearance:
        stroke_width=1,
        opacity=1,
        **kwargs,
    ):
        self.x_range = x_range or [
            floor(-config["frame_width"] / 2),
            ceil(config["frame_width"] / 2),
        ]
        self.y_range = y_range or [
            floor(-config["frame_height"] / 2),
            ceil(config["frame_height"] / 2),
        ]
        self.ranges = [self.x_range, self.y_range]

        if three_dimensions or z_range:
            self.z_range = z_range or self.y_range.copy()
            self.ranges += [self.z_range]
        else:
            self.ranges += [[0, 0]]

        for i in range(len(self.ranges)):
            if len(self.ranges[i]) == 2:
                self.ranges[i] += [0.5]
            self.ranges[i][1] += self.ranges[i][2]

        self.x_range, self.y_range, self.z_range = self.ranges

        super().__init__(
            func,
            color,
            color_scheme,
            min_color_scheme_value,
            max_color_scheme_value,
            colors,
            **kwargs,
        )

        self.noise_factor = (
            noise_factor if noise_factor is not None else self.y_range[2] / 2
        )
        self.n_repeats = n_repeats
        self.virtual_time = virtual_time
        self.max_anchors_per_line = max_anchors_per_line
        self.padding = padding
        self.stroke_width = stroke_width

        half_noise = self.noise_factor / 2
        np.random.seed(0)
        start_points = np.array(
            [
                (x - half_noise) * RIGHT
                + (y - half_noise) * UP
                + (z - half_noise) * OUT
                + self.noise_factor * np.random.random(3)
                for n in range(self.n_repeats)
                for x in np.arange(*self.x_range)
                for y in np.arange(*self.y_range)
                for z in np.arange(*self.z_range)
            ],
        )

        def outside_box(p):
            return (
                p[0] < self.x_range[0] - self.padding
                or p[0] > self.x_range[1] + self.padding - self.x_range[2]
                or p[1] < self.y_range[0] - self.padding
                or p[1] > self.y_range[1] + self.padding - self.y_range[2]
                or p[2] < self.z_range[0] - self.padding
                or p[2] > self.z_range[1] + self.padding - self.z_range[2]
            )

        max_steps = ceil(virtual_time / dt) + 1
        if not self.single_color:
            self.background_img = self.get_colored_background_image()
            if config["renderer"] == "opengl":
                self.values_to_rgbas = self.get_vectorized_rgba_gradient_function(
                    min_color_scheme_value,
                    max_color_scheme_value,
                    colors,
                )
        for point in start_points:
            points = [point]
            for _ in range(max_steps):
                last_point = points[-1]
                new_point = last_point + dt * func(last_point)
                if outside_box(new_point):
                    break
                points.append(new_point)
            step = max_steps
            if not step:
                continue
            if config["renderer"] == "opengl":
                line = OpenGLVMobject()
            else:
                line = VMobject()
            line.duration = step * dt
            step = max(1, int(len(points) / self.max_anchors_per_line))
            line.set_points_smoothly(points[::step])
            if self.single_color:
                line.set_stroke(self.color)
            else:
                if config["renderer"] == "opengl":
                    # scaled for compatibility with cairo
                    line.set_stroke(width=self.stroke_width / 4.0)
                    norms = np.array(
                        [np.linalg.norm(self.func(point)) for point in line.points],
                    )
                    line.set_rgba_array_direct(
                        self.values_to_rgbas(norms, opacity),
                        name="stroke_rgba",
                    )
                else:
                    if np.any(self.z_range != np.array([0, 0.5, 0.5])):
                        line.set_stroke(
                            [self.pos_to_color(p) for p in line.get_anchors()],
                        )
                    else:
                        line.color_using_background_image(self.background_img)
                    line.set_stroke(width=self.stroke_width, opacity=opacity)
            self.add(line)
        self.stream_lines = [*self.submobjects]

    def create(
        self,
        lag_ratio: float or None = None,
        run_time: Callable[[float], float] or None = None,
        **kwargs,
    ) -> AnimationGroup:
        """The creation animation of the stream lines.

        The stream lines appear in random order.

        Parameters
        ----------
        lag_ratio
            The lag ratio of the animation.
            If undefined, it will be selected so that the total animation length is 1.5 times the run time of each stream line creation.
        run_time
            The run time of every single stream line creation. The runtime of the whole animation might be longer due to the `lag_ratio`.
            If undefined, the virtual time of the stream lines is used as run time.

        Returns
        -------
        :class:`~.AnimationGroup`
            The creation animation of the stream lines.

        Examples
        --------

        .. manim:: StreamLineCreation

            class StreamLineCreation(Scene):
                def construct(self):
                    func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
                    stream_lines = StreamLines(
                        func,
                        color=YELLOW,
                        x_range=[-7, 7, 1],
                        y_range=[-4, 4, 1],
                        stroke_width=3,
                        virtual_time=1,  # use shorter lines
                        max_anchors_per_line=5,  # better performance with fewer anchors
                    )
                    self.play(stream_lines.create())  # uses virtual_time as run_time
                    self.wait()

        """
        if run_time is None:
            run_time = self.virtual_time
        if lag_ratio is None:
            lag_ratio = run_time / 2 / len(self.submobjects)

        animations = [
            Create(line, run_time=run_time, **kwargs) for line in self.stream_lines
        ]
        random.shuffle(animations)
        return AnimationGroup(*animations, lag_ratio=lag_ratio)

    def start_animation(
        self,
        warm_up=True,
        flow_speed: float = 1,
        time_width: float = 0.3,
        rate_func: Callable[[float], float] = linear,
        line_animation_class: type[ShowPassingFlash] = ShowPassingFlash,
        **kwargs,
    ) -> None:
        """Animates the stream lines using an updater.

        The stream lines will continuously flow

        Parameters
        ----------
        warm_up : bool, optional
            If `True` the animation is initialized line by line. Otherwise it starts with all lines shown.
        flow_speed
            At `flow_speed=1` the distance the flow moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of this flow.
        time_width
            The proportion of the stream line shown while being animated
        rate_func
            The rate function of each stream line flashing
        line_animation_class
            The animation class being used

        Examples
        --------

        .. manim:: ContinuousMotion

            class ContinuousMotion(Scene):
                def construct(self):
                    func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
                    stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
                    self.add(stream_lines)
                    stream_lines.start_animation(warm_up=False, flow_speed=1.5)
                    self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        """

        for line in self.stream_lines:
            run_time = line.duration / flow_speed
            line.anim = line_animation_class(
                line,
                run_time=run_time,
                rate_func=rate_func,
                time_width=time_width,
                **kwargs,
            )
            line.anim.begin()
            line.time = random.random() * self.virtual_time
            if warm_up:
                line.time *= -1
            self.add(line.anim.mobject)

        def updater(mob, dt):
            for line in mob.stream_lines:
                line.time += dt * flow_speed
                if line.time >= self.virtual_time:
                    line.time -= self.virtual_time
                line.anim.interpolate(np.clip(line.time / line.anim.run_time, 0, 1))

        self.add_updater(updater)
        self.flow_animation = updater
        self.flow_speed = flow_speed
        self.time_width = time_width

    def end_animation(self) -> AnimationGroup:
        """End the stream line animation smoothly.

        Returns an animation resulting in fully displayed stream lines without a noticeable cut.

        Returns
        -------
        :class:`~.AnimationGroup`
            The animation fading out the running stream animation.

        Raises
        ------
        ValueError
            if no stream line animation is running

        Examples
        --------

        .. manim:: EndAnimation

            class EndAnimation(Scene):
                def construct(self):
                    func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
                    stream_lines = StreamLines(
                        func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
                    )
                    self.add(stream_lines)
                    stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
                    self.wait(1)
                    self.play(stream_lines.end_animation())

        """

        if self.flow_animation is None:
            raise ValueError("You have to start the animation before fading it out.")

        def hide_and_wait(mob, alpha):
            if alpha == 0:
                mob.set_stroke(opacity=0)
            elif alpha == 1:
                mob.set_stroke(opacity=1)

        def finish_updater_cycle(line, alpha):
            line.time += dt * self.flow_speed
            line.anim.interpolate(min(line.time / line.anim.run_time, 1))
            if alpha == 1:
                self.remove(line.anim.mobject)
                line.anim.finish()

        max_run_time = self.virtual_time / self.flow_speed
        creation_rate_func = ease_out_sine
        creation_staring_speed = creation_rate_func(0.001) * 1000
        creation_run_time = (
            max_run_time / (1 + self.time_width) * creation_staring_speed
        )
        # creation_run_time is calculated so that the creation animation starts at the same speed
        # as the regular line flash animation but eases out.

        dt = 1 / config["frame_rate"]
        animations = []
        self.remove_updater(self.flow_animation)
        self.flow_animation = None

        for line in self.stream_lines:
            create = Create(
                line,
                run_time=creation_run_time,
                rate_func=creation_rate_func,
            )
            if line.time <= 0:
                animations.append(
                    Succession(
                        UpdateFromAlphaFunc(
                            line,
                            hide_and_wait,
                            run_time=-line.time / self.flow_speed,
                        ),
                        create,
                    ),
                )
                self.remove(line.anim.mobject)
                line.anim.finish()
            else:
                remaining_time = max_run_time - line.time / self.flow_speed
                animations.append(
                    Succession(
                        UpdateFromAlphaFunc(
                            line,
                            finish_updater_cycle,
                            run_time=remaining_time,
                        ),
                        create,
                    ),
                )
        return AnimationGroup(*animations)

