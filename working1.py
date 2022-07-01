import subprocess
import pprint
import subprocess, time, os, sys

command = r'cd C:\Users\asd93\PycharmProjects\Manim'
pp = pprint.PrettyPrinter(indent=4)




p = subprocess.Popen(f"C:/Users/asd93/PycharmProjects/Manim/venv/Scripts/activate.ps1yfile.ps1 & manim -pql --fps 7 main.py working1",
                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)

for line in p.stdout:
    if line.decode('utf-8') == '                                                                                           ':
        pass
    else:
        print(line.decode('utf-8'))
# for line in iter(p.stdout.readline, b''):
#     print(line.decode('utf-8'))


#
# buff, buffErr = pg.communicate()
#
# sys.stdout.reconfigure(encoding='utf-8')
#
# buff = buff.decode("utf-8")
# print(buff)
#


#
#
#
# import subprocess
# import pprint
# import subprocess
# import sys
#
# command=r'cd C:\Users\asd93\PycharmProjects\Manim'
# pp = pprint.PrettyPrinter(indent=4)
#
# def call_command(command):
#     process=subprocess.Popen('powershell -command '+"'"+command+"'", stdin=subprocess.STDOUT,stdout=subprocess.STDOUT, shell=True)
#     stdout_value = process.communicate()[0]
#     return stdout_value
#
# pg = subprocess.Popen("C:/Users/asd93/PycharmProjects/Manim/venv/Scripts/activate.ps1yfile.ps1 & manim -pqk main.py working1", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
# buff,buffErr = pg.communicate()
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
#
# buff =buff.decode("utf-8")
# print(buff)
