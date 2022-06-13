

from pathlib import Path
from pprint import pprint
import shutil

main_dir = Path(r'C:\Users\asd93\PycharmProjects\Manim\media\videos\defi_lec_2\2160p60\partial_movie_files\L_02_S_08_amm_xyk_adv_px_up_3')
all_files = main_dir.rglob('*.*')
file_list = [x for x in all_files if x.is_file() or x.is_dir()]
size_list = list(map(lambda x:x.stat().st_size,file_list))
c_time_list = list(map(lambda x:x.stat()[9],file_list))


file_list_with_ctime = []

for file in file_list:
    c_time = file.stat()[9]
    file_list_with_ctime.append([c_time, file])

file_list_with_ctime.sort()


folder_list = [x.stem for x in main_dir.parent.iterdir() if x.is_file() or x.is_dir()]
pprint(folder_list)
# pprint(file_list_with_ctime)


folder_name = main_dir.name + ' (for edit)'
new_work_folder = Path(r'C:\Users\asd93\Desktop\Manim work') / folder_name


if not new_work_folder.exists():
    new_work_folder.mkdir(parents=True)

# print(file_list_with_ctime[2][1].suffix)

i = 0

for file_with_time in file_list_with_ctime:
    i += 1
    # file_copy(file_with_time[1],new_work_folder)
    # file_copy_with_new_name(file_with_time[1],str(i),new_work_folder,False)
    shutil.copy(file_with_time[1],new_work_folder.joinpath(file_with_time[1].parent.stem[:9]+'_C_'+'{0:03d}'.format(i)+file_with_time[1].suffix))
    # time.sleep(2)
    # shutil.copy(file_with_time[1],new_work_folder.joinpath(str(i)+'_copy'+file_with_time[1].suffix))
    # time.sleep(2)

    # file_copy_with_new_name(file_with_time[1],str(i),new_work_folder,True)

#