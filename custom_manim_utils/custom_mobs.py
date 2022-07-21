from manim import *

import pyttsx3
import os
import datetime
import time

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



