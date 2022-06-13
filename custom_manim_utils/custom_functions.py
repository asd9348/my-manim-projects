from manim import *

import pyttsx3
import os

from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
from tempfile import NamedTemporaryFile
from pathlib import Path
import shutil
from pprint import pprint


def get_mid_btwn_mobs(mob_a, mob_b, center_datum=True):
    if center_datum:
        mob_a_coor = mob_a.get_center()
        mob_b_coor = mob_b.get_center()

        midpoint()

    else:
        pass


def there_and_back_expo(t: float) -> float:
    return -t + 1


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


def speak(self, title='dummy title', txt='dummy text', speed=1.4, keep_pitch=False, lang='ko', update=False):
    dirpath = Path(rf'.\audio_cache\{title}')
    if dirpath.exists() and dirpath.is_dir():
        if update:
            shutil.rmtree(dirpath)

    # Path(rf'.\audio_cache\{title} ').mkdir(parents=True, exist_ok=True)
    Path(rf'.\audio_cache\{title}\uncut').mkdir(parents=True, exist_ok=True)

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
                sound = AudioSegment.from_file(gtts_file_path_text)
                new_audio_seg.export(file_path_text)

            else:
                print("File dosent exist. Creating...")

                if clip != '':
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

                else:
                    print('it is empty text')

        else:
            # whene it is for pause
            cut_muffled_pause_sound = muffled_pause_sound[ :clip * 1000 ]
            cut_muffled_pause_sound.export(rf".\audio_cache\{title}\{title + 'L' + str(i) + ' ' + str(clip) + 's pause'}.mp3")
            file_list.append(cut_muffled_pause_sound)

    concated_audio = AudioSegment.from_file('tesst.mp3')[ :100 ] - 50
    for file in file_list:
        concated_audio = concated_audio + file
        concated_audio.export(final_file_path_text)

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
