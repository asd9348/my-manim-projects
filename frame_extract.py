# # import ffmpeg
# # stream = ffmpeg.input('input.mp4')
# # stream = ffmpeg.hflip(stream)
# # stream = ffmpeg.output(stream, 'output.mp4')
# # ffmpeg.run(stream)
#
# from moviepy.editor import *
#
#
# clip = VideoFileClip('test2.mp4')
# # frame_t = int(clip.fps * clip.duration)
# # print(frame_t)
# n_frames = clip.reader.nframes
# print(n_frames)
#
# # ext_clip = clip.to_ImageClip(t=frame_t, duration=4)
#
# # clip.save_frame("frame2.png", t = frame_t)
#
# fram_iter = ([frame[0,:,0].max()for frame in clip.iter_frames()])
#
# print(type(fram_iter[0]))

# from moviepy.editor import VideoFileClip
# import numpy as np
# import os
# from datetime import timedelta
#
# def format_timedelta(td):
#     """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05)
#     omitting microseconds and retaining milliseconds"""
#     result = str(td)
#     try:
#         result, ms = result.split(".")
#     except ValueError:
#         return result + ".00".replace(":", "-")
#     ms = int(ms)
#     ms = round(ms / 1e4)
#     return f"{result}.{ms:02}".replace(":", "-")
#
# def main(video_file):
#     # load the video clip
#     video_clip = VideoFileClip(video_file)
#     # make a folder by the name of the video file
#     filename, _ = os.path.splitext(video_file)
#     filename += "-moviepy"
#     if not os.path.isdir(filename):
#         os.mkdir(filename)
#
#     # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
#     saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
#     # if SAVING_FRAMES_PER_SECOND is set to 0, step is 1/fps, else 1/SAVING_FRAMES_PER_SECOND
#     step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
#     # iterate over each possible frame
#     for current_duration in np.arange(0, video_clip.duration, step):
#         # format the file name and save it
#         frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
#         frame_filename = os.path.join(filename, f"frame{frame_duration_formatted}.jpg")
#         # save the frame with the current duration
#         video_clip.save_frame(frame_filename, current_duration)

###############################################################################################################

# import cv2
# video_name = "4k.mp4" # or any other extension like .avi etc
# vidcap = cv2.VideoCapture(video_name)
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite("frame%d.png" % count, image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1

###############################################################################################################
# import os
# import time
# import datetime
#
# fileLocation = r"C:\Users\asd93\PycharmProjects\Manim\media\videos\main\2160p60\partial_movie_files\lec1_s7_supply_and_demand"
# year = 2017
# month = 11
# day = 5
# hour = 19
# minute = 50
# second = 0
#
# date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
# modTime = time.mktime(date.timetuple())
#
# os.utime(fileLocation, (modTime, modTime))
#
###############################################################################################################


import os
from pathlib import Path
import datetime
import time
import platform
from pprint import pprint
import shutil

import time

p = Path("4k.mp4")

# p.write_text('test')

# time.sleep(10)

# p.write_text('update')
#
# def file_copy(src_file_or_dir, dst_dir):
#     dst_dir = dst_dir.joinpath(src_file_or_dir.name)
#     # if not dst_dir.exists():
#     #     # print('it exists')
#     #     src_file_or_dir.replace(dst_dir)
#     #     src_file_or_dir.move
#     # else:
#     #     print("the file already exists!!!")
#
#     with dst_dir.open(mode='xb') as f:
#         f.write(src_file_or_dir.read_bytes())
#
#     src_file_or_dir.unlink()
#
# def file_copy_with_new_name(src_file_or_dir, new_name, dst_dir,if_copy):
#     if if_copy:
#         dst_file_name = new_name +' copy' +src_file_or_dir.suffix
#
#     else:
#         dst_file_name = new_name + src_file_or_dir.suffix
#
#     dst_dir = dst_dir.joinpath(dst_file_name)
#     # if not dst_dir.exists():
#     #     # print('it exists')
#     #     src_file_or_dir.replace(dst_dir)
#     #     src_file_or_dir.move
#     # else:
#     #     print("the file already exists!!!")
#
#     with dst_dir.open(mode='xb') as f:
#         f.write(src_file_or_dir.read_bytes())
#
#     src_file_or_dir.unlink()
#

# print(p.stat()[9])
main_dir = Path(r'C:\Users\asd93\PycharmProjects\Manim\media\videos\main\2160p60\partial_movie_files\lec1_s2')
all_files = main_dir.rglob('*.*')
# print(Q)
file_list = [x for x in all_files if x.is_file() or x.is_dir()]
size_list = list(map(lambda x:x.stat().st_size,file_list))
c_time_list = list(map(lambda x:x.stat()[9],file_list))

# print(file_list[1].stat().st_size)
pprint(file_list)
print(size_list)
print(c_time_list)

file_list_with_ctime = []
for file in file_list:
    c_time = file.stat()[9]
    file_list_with_ctime.append([c_time, file])

file_list_with_ctime.sort()
pprint(file_list_with_ctime)


print(main_dir.name)

folder_name = main_dir.name + ' (for edit)'
# desktop
new_work_folder = Path(r'C:\Users\asd93\Desktop\Manim work') / folder_name
# new_work_folder.touch()


if not new_work_folder.exists():
    new_work_folder.mkdir(parents=True)

print(file_list_with_ctime[2][1].suffix)

i = 0

for file_with_time in file_list_with_ctime:
    i += 1
    # file_copy(file_with_time[1],new_work_folder)
    # file_copy_with_new_name(file_with_time[1],str(i),new_work_folder,False)
    shutil.copy(file_with_time[1],new_work_folder.joinpath(str(i)+file_with_time[1].suffix))
    # time.sleep(2)
    # shutil.copy(file_with_time[1],new_work_folder.joinpath(str(i)+'_copy'+file_with_time[1].suffix))
    # time.sleep(2)

    # file_copy_with_new_name(file_with_time[1],str(i),new_work_folder,True)

#
#
#
#     destination = main_dir.joinpath(file.name)
#     if file.stat().st_size > 1000000000:
#         if not destination.exists():
#             # print('it exists')
#             file.replace(destination)
#
        # with main_dir.open(mode='xb') as f:
        #     f.write(q.read_bytes())

# for file in file_list:
#     print(file.name)
#     print(main_dir.joinpath(file.name))
#     destination = main_dir.joinpath(file.name)
#     if file.stat().st_size > 1000000000:
#         if not destination.exists():
#             # print('it exists')
#             file.replace(destination)
#
#         # with main_dir.open(mode='xb') as f:
#         #     f.write(q.read_bytes())

