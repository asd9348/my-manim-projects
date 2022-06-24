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


