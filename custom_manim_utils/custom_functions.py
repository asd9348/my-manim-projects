from manim import *
import manim
import pyttsx3
import os
import datetime
import time
import open3d as o3d

from datetime import timedelta
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
from tempfile import NamedTemporaryFile
from pathlib import Path
import shutil
from pprint import pprint

from custom_manim_utils.custom_consts import *
# from custom_manim_utils.custom_color_consts import *
# from custom_manim_utils.custom_ import *



from typing import *

import numpy as np
from colour import Color

from manim import config
# from manim.constants import *
from manim.mobject.geometry.arc import Circle
from manim.mobject.geometry.polygram import Square
from manim.mobject.mobject import *
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.opengl.opengl_mobject import OpenGLMobject
from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from manim.utils.color import *
from manim.utils.iterables import tuplify
from manim.utils.space_ops import normalize, perpendicular_bisector, z_to_vector



def three_d_space_zxy(self,axes):
    # 실제로 사용하게될 ㅌ제트축을 카피해서 마지막 서브 모브젝트로 넣어놓고 원하는 위치로 이동시키기, 원래 제트축은 움직이지 않았음
    new_y_axis = axes[ 1 ].copy()
    x_axis = axes[ 0 ]
    y_axis = axes[ 1 ]
    z_axis = axes[ 2 ]
    new_y_axis.move_to(get_compensated_coor(new_y_axis, new_y_axis.get_start(), x_axis.get_end()))
    #
    # 보조선 작성 루틴 , 틱 위치 개수하고 잘 보기
    x_range, y_range, z_range = axes.x_range, axes.y_range, axes.z_range

    x_tick_pos = np.arange(x_range[ 0 ], x_range[ 1 ] + 0.01, x_range[ 2 ])
    y_tick_pos = np.arange(y_range[ 0 ], y_range[ 1 ] + 0.01, y_range[ 2 ])
    z_tick_pos = np.arange(z_range[ 0 ], z_range[ 1 ] + 0.01, z_range[ 2 ])

    x_axis_aux_line, y_axis_aux_line, z_axis_aux_line = VGroup(), VGroup(), VGroup()

    for x, y, z in zip(x_tick_pos[ 0: ], y_tick_pos[ 1: ], z_tick_pos[ 1: ], ):
        z_axis_aux_line.add(
            VMobject().set_points_as_corners(
                [ axes.c2p(x_tick_pos[ -1 ], y_tick_pos[ -1 ], z), axes.c2p(0, y_tick_pos[ -1 ], z), axes.c2p(0, 0, z) ])
                .set_stroke(opacity=0.3,
                            width=2,
                            color=GRAY))
        y_axis_aux_line.add(
            VMobject().set_points_as_corners([ axes.c2p(1, y, 0), axes.c2p(0, y, 0), axes.c2p(0, y, z_tick_pos[ -1 ]) ])
                .set_stroke(opacity=0.3,
                            width=2,
                            color=GRAY))
        x_axis_aux_line.add(
            VMobject().set_points_as_corners(
                [ axes.c2p(x, 0, 0), axes.c2p(x, y_tick_pos[ -1 ], 0), axes.c2p(x, y_tick_pos[ -1 ], z_tick_pos[ -1 ]) ])
                .set_stroke(opacity=0.3,
                            width=2,
                            color=GRAY))

    origin_vertical_aux_line = VMobject().set_points_as_corners(
        [ axes.c2p(x_tick_pos[ -1 ], y_tick_pos[ -1 ], 0), axes.c2p(x_tick_pos[ -1 ], y_tick_pos[ -1 ], z_tick_pos[ -1 ]) ]) \
        .set_stroke(opacity=0.3,
                    width=2,
                    color=GRAY)
    aux_lines = VGroup(x_axis_aux_line, y_axis_aux_line, z_axis_aux_line, origin_vertical_aux_line)
    # 제트축 넘버들을 픽ㅅ드 오리엔테이션 적용 전에 전부 위로 향하게 돌려줌
    for number in z_axis.numbers:
        number.rotate(90 * DEGREES, axis=X_AXIS).rotate(90 * DEGREES)

    self.add_fixed_orientation_mobjects(*x_axis.numbers)
    self.add_fixed_orientation_mobjects(*new_y_axis.numbers)
    self.add_fixed_orientation_mobjects(*z_axis.numbers)

    # 기존 좌표계가 틀어지지 않게 모두 이동은 같이 하되 제트 축은 보여주지 않을 것임

    new_axes = VGroup(x_axis, new_y_axis, z_axis, aux_lines).move_to(UP)

    return new_axes


def is_in_triangle(point, A, B, C, contain_border=False):
    COM = center_of_mass(A, B, C)
    if is_on_left_by_points(A, B, COM) and \
            is_on_left_by_points(B, C, COM) and \
            is_on_left_by_points(C, A, COM):
        if is_on_left_by_points(A, B, point, contain_border=contain_border) and \
                is_on_left_by_points(B, C, point, contain_border=contain_border) and \
                is_on_left_by_points(C, A, point, contain_border=contain_border):

            return True
        else:
            return False

    else:
        if is_on_right_by_points(A, B, point, contain_border=contain_border) and \
                is_on_right_by_points(B, C, point, contain_border=contain_border) and \
                is_on_right_by_points(C, A, point, contain_border=contain_border):
            return True

        else:
            return False

def axes2space(axes):

    new_z_axis = axes[ 2 ].copy().move_to(get_compensated_coor(axes[ 2 ], axes[ 2 ].get_start(), axes[ 0 ].get_start()))
    axes.y_axis.move_to(get_compensated_coor(axes.y_axis, axes.y_axis.get_start(), axes.x_axis.get_end()))
    axes.remove(axes[ 2 ])
    axes.add(new_z_axis)
    axes.z_axis = new_z_axis
    axes.x_axis.set_color(RED)
    axes.y_axis.set_color(GREEN)
    axes.z_axis.set_color(BLUE)

    return axes


# a = [ 1, 1, 0 ]
# b = [ 2, 1.5, 0 ]
# c = [ 1, 2, 0 ]



def dollar_val_surface_triangle(self, u, v):
    if is_in_triangle([ u, v, 0 ], a, b, c):
        k = ((1 + u) / (1 + v)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
        curr_val = hold_val * (1 + z) - 1
    else:
        pass
    #
    #     # if
    #     angle = angle_of_vector(np.array([ u, v, 0 ]))
    #     u = np.cos(angle) * 0.5
    #     v = np.sin(angle) * 0.5
    #     k = ((1 + u) / (1 + v)) - 1
    #     z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
    #     hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
    #     curr_val = hold_val * (1 + z) - 1
    # return np.array([ u, v, curr_val ])
# 3D file Import
def get_ply_file_triangles(file_name):
    mesh = o3d.io.read_triangle_mesh(file_name)
    # mesh.compute_vertex_normals()
    return np.asarray(mesh.triangles)


def get_ply_file_vertexs(file_name):
    mesh = o3d.io.read_triangle_mesh(file_name)
    # mesh.compute_vertex_normals()
    return np.asarray(mesh.vertices)

# GEOMETRY
def get_tangent_line(coor_sys, graph, x_point, line_length=3):
    """ debugging is needed """
    slope = coor_sys.slope_of_tangent(x_point, graph)
    if coor_sys.angle_of_tangent(x_point, graph) <= PI / 2:
        angle = coor_sys.angle_of_tangent(x_point, graph)
    else:
        angle = PI - coor_sys.angle_of_tangent(x_point, graph)

    y_intercept = graph.underlying_function(x_point) - slope * x_point
    tangent_func = lambda x: slope * x + y_intercept
    adjacent_len = np.cos(angle) * line_length

    tangent_line = coor_sys.plot(tangent_func, x_range=[ x_point - adjacent_len / 2, x_point + adjacent_len / 2 ])

    return tangent_line
def my_c2p(axes, x, y, z):
    origin = axes.x_axis.get_start() + OUT * (0 - axes.z_range[ 0 ]) * axes.z_length / (
            abs(axes.z_range[ 0 ]) + abs(axes.z_range[ 1 ]))
    x_dif = axes.x_axis.number_to_point(x) - np.array([ origin[ 0 ], 0, 0 ])
    y_dif = axes.y_axis.number_to_point(y) - np.array([ 0, origin[ 1 ], 0 ])
    z_dif = axes.z_axis.number_to_point(z) - np.array([ 0, 0, origin[ 2 ] ])

    result = origin + x_dif + y_dif + z_dif

    return result
def get_slope_with_two_points(p1, p2):
    slope = (p2[ 1 ] - p1[ 1 ]) / (p2[ 0 ] - p1[ 0 ])

    return slope
def get_y_intersect_with_two_points(p1, p2):
    slope = (p2[ 1 ] - p1[ 1 ]) / (p2[ 0 ] - p1[ 0 ])

    y_intersect = p1[ 1 ] - slope * p1[ 0 ]

    return y_intersect
def get_unit_v_by_angle(angle):
    unit_v = np.array([ np.cos(angle), np.sin(angle), 0 ])

    return unit_v
def get_perpendicular_line(point, line):
    if type(line) is list:
        temp_line = Line(start=line[ 0 ], end=line[ 1 ])
    else:
        temp_line = line

    unit_v = temp_line.get_unit_vector()

    if is_on_left(temp_line, point):
        new_unit_v_angle = angle_of_vector(unit_v) + PI / 2
    else:
        new_unit_v_angle = angle_of_vector(unit_v) - PI / 2

    new_unit_v = np.array([ np.cos(new_unit_v_angle), np.sin(new_unit_v_angle), 0 ])
    hypotenuse = get_dist_btwn_points(point, temp_line.get_end())
    theta = get_angle_ABC(temp_line.get_end(), point, point + new_unit_v)
    perpendicular_length = np.cos(theta) * hypotenuse

    return Line(start=point, end=point + new_unit_v * perpendicular_length)
def is_on_left(line, point, contain_border=False):
    a = line.get_start()
    b = line.get_end()
    c = point
    if contain_border == False:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) > 0
    else:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) >= 0


def is_on_right(line, point, contain_border=False):
    a = line.get_start()
    b = line.get_end()
    c = point
    if contain_border == False:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) > 0
    else:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) >= 0


def is_on_left_by_points(start, end, point, contain_border=False):
    a = start
    b = end
    c = point
    if contain_border == False:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) < 0
    else:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) <= 0


def is_on_right_by_points(start, end, point, contain_border=False):
    a = start
    b = end
    c = point

    if contain_border == False:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) < 0
    else:
        return ((b[ 0 ] - a[ 0 ]) * (c[ 1 ] - a[ 1 ]) - (b[ 1 ] - a[ 1 ]) * (c[ 0 ] - a[ 0 ])) <= 0
def get_line_length(line):
    """라인 모브젝트를 넣으면 길이를 반환."""

    start = line.get_start()
    end = line.get_end()
    length = np.linalg.norm(end - start)
    return length


def get_dist_btwn_points(a, b):
    dist = np.linalg.norm(a - b)
    return dist


def move_point_with_angle_and_length(start, angle, length):
    unit_v = np.array([ np.cos(angle), np.sin(angle), 0 ])
    return start + unit_v * length


def get_angle_ABC(a, b, c):
    """점 abc를 넣으면 선분 ba 와 선분 bc사이의 각도를 반환."""
    ba_unit_v = Line(start=b, end=a).get_unit_vector()
    bc_unit_v = Line(start=b, end=c).get_unit_vector()

    angle = angle_between_vectors(ba_unit_v, bc_unit_v)

    return angle


def get_halfway(A, B, z=0):
    if isinstance(A, np.ndarray):
        point_A = A
    else:
        point_A = A.get_center()

    if isinstance(B, np.ndarray):
        point_B = B
    else:
        point_B = B.get_center()

    if point_A[ 0 ] * point_B[ 0 ] > 0:
        x_dist = abs(point_A[ 0 ] - point_B[ 0 ]) / 2
        y_dist = abs(point_A[ 1 ] - point_B[ 1 ]) / 2

    else:
        x_dist = (abs(point_A[ 0 ]) + abs(point_B[ 0 ])) / 2
        y_dist = (abs(point_A[ 1 ]) + abs(point_B[ 1 ])) / 2

    if point_A[ 0 ] < point_B[ 0 ]:
        x = point_A[ 0 ] + x_dist
    else:
        x = point_B[ 0 ] + x_dist

    if point_A[ 1 ] < point_B[ 1 ]:
        y = point_A[ 1 ] + y_dist
    else:
        y = point_B[ 1 ] + y_dist

    return np.array([ x, y, z ])

def get_compensated_coor(main_mob, point_inside_main_mob, point_goes_to):

    x_compen = main_mob.get_x() - point_inside_main_mob[ 0 ]
    y_compen = main_mob.get_y() - point_inside_main_mob[ 1 ]
    z_compen = main_mob.get_z() - point_inside_main_mob[ 2 ]

    x = point_goes_to[ 0 ] + x_compen
    y = point_goes_to[ 1 ] + y_compen
    z = point_goes_to[ 2 ] + z_compen

    return [ x, y, z ]


# System
def redraw(func):
    mob = func()
    mob.add_updater(lambda m: mob.become(func()))
    return mob

# Icons Mobs
def coin(coin_ticker, type='color', radius=1):
    """type : black , color, icon, white
    coin ticker in lower case
    """

    svg_folder = Path('./svgs')
    svg_file = svg_folder / 'coin' / f'{type}' / f'{coin_ticker}.svg'
    # pprint(list(svg_folder.iterdir()))

    return SVGMobject(svg_file).scale_to_fit_width(radius * 2)












#
# def get_compensated_coor(main_mob, point_inside_main_mob, point_goes_to):
#     x_compen = main_mob.get_x() - point_inside_main_mob[ 0 ]
#     y_compen = main_mob.get_y() - point_inside_main_mob[ 1 ]
#
#     x = point_goes_to[ 0 ] + x_compen
#     y = point_goes_to[ 1 ] + y_compen
#
#
#
#     return [ x, y, 0 ]
#

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


class BoxWithContent(RoundedRectangle):

    def __init__(
            self,
            # label: str or SingleStringMathTex or Text or Tex,
            width: float or None = None,
            height: float or None = None,
            corner_radius: float or None = None,
            direction: np.ndarray = UP,
            obj: Mobject = Mobject,
            **kwargs, ) -> None:

        # if isinstance(label, str):
        #     from manim import Tex
        #
        #     rendered_label = Tex(label, color=WHITE)
        # else:
        #     rendered_label = label

        print(obj.width)
        print(type(obj.width))

        if width is None:
            width = 0.2 + float(obj.width)
        if height is None:
            height = 0.2 + float(obj.height)

        if corner_radius is None:
            corner_radius = 0.2

        super().__init__(width=width, height=height, corner_radius=corner_radius, **kwargs)
        self.move_to(obj)
        obj.add(self)


def create_asset_mob(text, width=0.5, height=0.3, fill_color=GREEN, stroke_color=GREEN):
    box = Rectangle(width=width, height=height, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1)
    text = Text(text, color=BLACK).scale(height)

    return VGroup(box, text)


def create_box_asset(text, font_size, text_color=BLACK, width=0.5, height=0.3, fill_color=GREEN, stroke_color=GREEN, stroke_width=10,
                     stroke_opacity=0):
    box = Rectangle(width=width, height=height, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1,
                    stroke_opacity=stroke_opacity)
    text = Tex(text, color=text_color, font_size=font_size)

    return VGroup(box, text)


def create_circle_asset(input_text, font_size=25, text_color=BLACK, radius=0.5, fill_color=GREEN, stroke_color=GREEN, stroke_width=10,
                        stroke_opacity=0):
    circle = Circle(radius=radius, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1, stroke_width=stroke_width,
                    stroke_opacity=stroke_opacity)
    if type(input_text) is str:
        text = Tex(input_text, color=text_color, font_size=font_size)
    else:
        text = input_text
    return VGroup(circle, text)


def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height, asset_text_color=BLACK,
                  scaler=1):
    person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

    box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
    text = manim.Text(asset_name, color=asset_text_color).scale(scaler * asset_height)

    asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

    return VGroup(person, asset)


def speak(self, title='dummy title', txt='dummy text', speed=1.4, keep_pitch=False, lang='ko', update=False):
    def format_td(seconds, digits=3):
        isec, fsec = divmod(round(seconds * 10 ** digits), 10 ** digits)
        return ("{}.{:0%d.0f}" % digits).format(timedelta(seconds=isec), fsec)

    dirpath = Path(rf'.\audio_cache\{title}')
    if dirpath.exists() and dirpath.is_dir():
        if update:
            shutil.rmtree(dirpath)

    # Path(rf'.\audio_cache\{title} ').mkdir(parents=True, exist_ok=True)
    Path(rf'.\audio_cache\{title}\uncut').mkdir(parents=True, exist_ok=True)
    Path(rf'.\audio_cache\{title}\pause').mkdir(parents=True, exist_ok=True)

    output = ''

    init_pause_sound = AudioSegment.from_file(rf'.\custom_manim_utils\dummy.mp3')
    muffled_pause_sound = init_pause_sound - 50

    init_cut_text_list = txt.split('#')
    cut_text_list = [ ]
    cut_text_list.append(init_cut_text_list[ 0 ])

    for clip in init_cut_text_list[ 1: ]:
        pause_length = int(clip[ 0 ])
        actual_text = clip[ 1: ]
        cut_text_list.append(pause_length)
        cut_text_list.append(actual_text)

    pprint(cut_text_list)

    file_list = [ ]
    audio_pos_end = 0

    missing_file_counter = 0
    for i in range(len(cut_text_list)):
        clip = cut_text_list[ i ]

        if type(clip) is str:

            file_path_obj = Path(rf".\audio_cache\{title}\{title + 'L' + str(i) + ' ' + clip}.mp3")
            file_path_text = rf".\audio_cache\{title}\{title + 'L' + str(i) + ' ' + clip}.mp3"
            final_file_path_obj = Path(rf'.\audio_cache\{title}\uncut\{title}.mp3')
            final_file_path_text = rf'.\audio_cache\{title}\uncut\{title}.mp3'

            if file_path_obj.is_file():
                print("File exist. Using the existing one...")

                gtts_file_path_text = file_path_text
                new_audio_seg = AudioSegment.from_file(gtts_file_path_text)
                new_audio_seg.export(file_path_text, bitrate='312k')
                file_list.append(new_audio_seg)
                audio_pos_start = audio_pos_end
                audio_pos_end += new_audio_seg.duration_seconds
                output += f'# TODO {new_audio_seg.duration_seconds} secs ' + clip + '\n' + rf'# TODO {format_td(audio_pos_start)}  ~  {format_td(audio_pos_end)}'




            else:

                if clip != '':
                    print("File dosent exist. Creating...")
                    missing_file_counter = 1

                    gTTS(text=clip, lang=lang).write_to_fp(
                        gtts_sound := NamedTemporaryFile(delete=False, dir=r"C:\Users\asd93\PycharmProjects\Manim\audio_cache\temp"))
                    gtts_file_path_text = gtts_sound.name
                    gtts_sound.close()

                    if keep_pitch:
                        sound = AudioSegment.from_file(gtts_file_path_text)
                        new_audio_seg = speedup(sound, playback_speed=speed)
                        new_audio_seg.export(file_path_text)
                    else:
                        sound = AudioSegment.from_file(gtts_file_path_text)
                        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
                            "frame_rate": int(sound.frame_rate * speed)})
                        new_audio_seg = sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
                        new_audio_seg.export(file_path_text)

                    file_list.append(new_audio_seg)
                    audio_pos_start = audio_pos_end
                    audio_pos_end += new_audio_seg.duration_seconds
                    output += f'# TODO {new_audio_seg.duration_seconds} secs' + clip + '\n' + rf'# TODO {format_td(audio_pos_start)}  ~  {format_td(audio_pos_end)}' '\n'

                else:
                    print('it is empty text')


        else:
            # whene it is for pause
            cut_muffled_pause_sound = muffled_pause_sound[ :clip * 1000 ]
            cut_muffled_pause_sound.export(rf".\audio_cache\{title}\pause\{title + 'L' + str(i) + ' ' + str(clip) + 's pause'}.mp3")
            file_list.append(cut_muffled_pause_sound)
            audio_pos_start = audio_pos_end
            audio_pos_end += cut_muffled_pause_sound.duration_seconds
            output += f'# TODO {cut_muffled_pause_sound.duration_seconds}secs' + ' pause' + '\n' + rf'# TODO {format_td(audio_pos_start)}  ~  {format_td(audio_pos_end)}' + '\n\n'
    if missing_file_counter == 1:
        print('Creating concated file')

        concated_audio = AudioSegment.from_file(r'.\custom_manim_utils\dummy.mp3')[ :100 ] - 50
        for file in file_list:
            concated_audio = concated_audio + file
            concated_audio.export(final_file_path_text)

    else:
        print('Using existing concated file')

    print(output)

    self.add_sound(final_file_path_text)


def speak_deprecated(self, txt, speed=1.4, keep_pitch=False, lang='ko'):
    init_pause_sound = AudioSegment.from_file(r'.\custom_manim_utils\dummy.mp3')
    muffled_pause_sound = init_pause_sound - 50

    init_cut_text_list = txt.split('#')
    cut_text_list = [ ]
    print(init_cut_text_list)
    cut_text_list.append(init_cut_text_list[ 0 ])

    for clip in init_cut_text_list[ 1: ]:
        pause_length = int(clip[ 0 ])
        actual_text = clip[ 1: ]
        cut_text_list.append(pause_length)
        cut_text_list.append(actual_text)

    file_list = [ ]
    for clip in cut_text_list:

        if type(clip) is str:
            gTTS(text=clip, lang=lang).write_to_fp(
                gtts_sound := NamedTemporaryFile(delete=False, dir=r"C:\Users\asd93\PycharmProjects\Manim\audio_cache"))
            file_name = gtts_sound.name
            gtts_sound.close()

            if keep_pitch:
                sound = AudioSegment.from_file(file_name)
                new_audio_seg = speedup(sound, playback_speed=speed)
                new_audio_seg.export(
                    final_audio := NamedTemporaryFile(delete=False, dir=r"C:\Users\asd93\PycharmProjects\Manim\audio_cache"))
                final_audio_name = final_audio.name
                final_audio.close()
            else:
                sound = AudioSegment.from_file(file_name)
                sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
                    "frame_rate": int(sound.frame_rate * speed)})
                new_audio_seg = sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
                new_audio_seg.export(
                    final_audio := NamedTemporaryFile(delete=False, dir=r"C:\Users\asd93\PycharmProjects\Manim\audio_cache"))
                final_audio_name = final_audio.name
                final_audio.close()

            file_list.append(new_audio_seg)


        else:

            cut_muffled_pause_sound = muffled_pause_sound[ :clip * 1000 ]
            file_list.append(cut_muffled_pause_sound)

    concated_audio = AudioSegment.from_file('tesst.mp3')[ :100 ] - 50
    for file in file_list:
        concated_audio = concated_audio + file

    concated_audio.export(
        final_audio := NamedTemporaryFile(delete=False, dir=r"C:\Users\asd93\PycharmProjects\Manim\audio_cache"))
    final_audio_name = final_audio.name
    final_audio.close()

    self.add_sound(final_audio_name)


def bezier_branch_creater(str8_start_width=1, str8_end_width=1, branch=5, branch_width=2, branch_height=7):
    start_line = Line(ORIGIN, R)

    clearance = branch_height / (branch - 1)

    branches = VGroup()

    for i in range(branch):
        curve = CubicBezier(R,
                            R + R * (branch_width / 2),
                            R + R * (branch_width / 2) + U * ((branch_height / 2) - clearance * i),
                            R + R * (branch_width) + U * ((branch_height / 2) - clearance * i))

        end_line = Line(curve.get_end(), curve.get_end() + R * str8_end_width)

        bezier = VGroup(start_line.copy(), curve, end_line)

        branches.add(bezier)

    return branches


class ThreeDVMobject(VMobject, metaclass=ConvertToOpenGL):
    def __init__(self, shade_in_3d=True, **kwargs):
        super().__init__(shade_in_3d=shade_in_3d, **kwargs)


class MySurface(VGroup, metaclass=ConvertToOpenGL):

    def __init__(
            self,
            func: Callable[ [ float, float ], np.ndarray ],
            point1: np.ndarray = np.array([ 1, 0, 0 ]),
            point2: np.ndarray = np.array([ -1, 0, 0 ]),
            point3: np.ndarray = np.array([ 0, 1, 0 ]),
            u_range: Sequence[ float ] = [ 0, 1 ],
            v_range: Sequence[ float ] = [ 0, 1 ],
            resolution: Sequence[ int ] = 32,
            surface_piece_config: dict = {},
            fill_color: Color = BLUE_D,
            fill_opacity: float = 1.0,
            checkerboard_colors: Sequence[ Color ] = [ BLUE_D, BLUE_E ],
            stroke_color: Color = LIGHT_GREY,
            stroke_width: float = 0.5,
            should_make_jagged: bool = False,
            pre_function_handle_to_anchor_scale_factor: float = 0.00001,
            **kwargs,
    ) -> None:
        self.u_range = u_range
        self.v_range = v_range
        super().__init__(**kwargs)
        self.resolution = resolution
        self.surface_piece_config = surface_piece_config
        self.fill_color = fill_color
        self.fill_opacity = fill_opacity
        self.checkerboard_colors = checkerboard_colors
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.should_make_jagged = should_make_jagged
        self.pre_function_handle_to_anchor_scale_factor = (
            pre_function_handle_to_anchor_scale_factor
        )
        self.func = func
        self._setup_in_uv_space()
        self.apply_function(lambda p: func(p[ 0 ], p[ 1 ]))
        if self.should_make_jagged:
            self.make_jagged()

    def _get_u_values_and_v_values(self):

        u_values = [ -1, 0, 1 ]
        v_values = [ 0, 1, 0 ]

        return u_values, v_values

    def _setup_in_uv_space(self):
        u_values, v_values = self._get_u_values_and_v_values()
        faces = VGroup()
        for i in range(len(u_values)):
            u1 = u_values[ i ]
            u2 = u_values[ i + 1 ]
            v1 = v_values[ i ]
            v2 = v_values[ i + 1 ]
            face = ThreeDVMobject()
            face.set_points_as_corners(
                [
                    [ 1, 0, 0 ],
                    [ 1, 0, 5 ],
                    [ 0, 1, 0 ],
                    [ 0, 1, 5 ],
                    [ 1, 0, 0 ],
                ],
            )
            faces.add(face)
            face.u_index = i
            face.v_index = j
            face.u1 = u1
            face.u2 = u2
            face.v1 = v1
            face.v2 = v2
        faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)
        faces.set_stroke(
            color=self.stroke_color,
            width=self.stroke_width,
            opacity=self.stroke_opacity,
        )
        self.add(*faces)
        if self.checkerboard_colors:
            self.set_fill_by_checkerboard(*self.checkerboard_colors)

    def set_fill_by_checkerboard(self, *colors, opacity=None):
        n_colors = len(colors)
        for face in self:
            c_index = (face.u_index + face.v_index) % n_colors
            face.set_fill(colors[ c_index ], opacity=opacity)
        return self

    def set_fill_by_value(
            self,
            axes: Mobject,
            colors: Union[ Iterable[ Color ], Color ],
            axis: int = 2,
    ):
        """Sets the color of each mobject of a parametric surface to a color relative to its axis-value

        Parameters
        ----------
        axes :
            The axes for the parametric surface, which will be used to map axis-values to colors.
        colors :
            A list of colors, ordered from lower axis-values to higher axis-values. If a list of tuples is passed
            containing colors paired with numbers, then those numbers will be used as the pivots.
        axis :
            The chosen axis to use for the color mapping. (0 = x, 1 = y, 2 = z)

        Returns
        -------
        :class:`~.Surface`
            The parametric surface with a gradient applied by value. For chaining.

        Examples
        --------
        .. manim:: FillByValueExample
            :save_last_frame:

            class FillByValueExample(ThreeDScene):
                def construct(self):
                    resolution_fa = 42
                    self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
                    axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
                    def param_surface(u, v):
                        x = u
                        y = v
                        z = np.sin(x) * np.cos(y)
                        return z
                    surface_plane = Surface(
                        lambda u, v: axes.c2p(u, v, param_surface(u, v)),
                        resolution=(resolution_fa, resolution_fa),
                        v_range=[0, 5],
                        u_range=[0, 5],
                        )
                    surface_plane.set_style(fill_opacity=1)
                    surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
                    self.add(axes, surface_plane)
        """

        ranges = [ axes.x_range, axes.y_range, axes.z_range ]

        if type(colors[ 0 ]) is tuple:
            new_colors, pivots = [ [ i for i, j in colors ], [ j for i, j in colors ] ]
        else:
            new_colors = colors

            pivot_min = ranges[ axis ][ 0 ]
            pivot_max = ranges[ axis ][ 1 ]
            pivot_frequency = (pivot_max - pivot_min) / (len(new_colors) - 1)
            pivots = np.arange(
                start=pivot_min,
                stop=pivot_max + pivot_frequency,
                step=pivot_frequency,
            )

        for mob in self.family_members_with_points():
            axis_value = axes.point_to_coords(mob.get_midpoint())[ axis ]
            if axis_value <= pivots[ 0 ]:
                mob.set_color(new_colors[ 0 ])
            elif axis_value >= pivots[ -1 ]:
                mob.set_color(new_colors[ -1 ])
            else:
                for i, pivot in enumerate(pivots):
                    if pivot > axis_value:
                        color_index = (axis_value - pivots[ i - 1 ]) / (
                                pivots[ i ] - pivots[ i - 1 ]
                        )
                        color_index = min(color_index, 1)
                        mob_color = interpolate_color(
                            new_colors[ i - 1 ],
                            new_colors[ i ],
                            color_index,
                        )
                        if config.renderer == "opengl":
                            mob.set_color(mob_color, recurse=False)
                        else:
                            mob.set_color(mob_color, family=False)
                        break

        return self

# Specific shapes
