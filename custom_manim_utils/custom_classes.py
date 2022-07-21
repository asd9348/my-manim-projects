
import manim.utils.space_ops
from manim import *

import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_mobs import *
from manim_physics import *
from manim_gearbox import *
# from manim_fontawesome import regular
from pathlib import Path

config.frame_width = 16
config.frame_height = 9
# background_color = W02
from pprint import pprint


class three_d_mob(VGroup):
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

