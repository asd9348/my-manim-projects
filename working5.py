import subprocess
import pprint
import subprocess, time, os, sys

command = r'cd C:\Users\asd93\PycharmProjects\Manim'
pp = pprint.PrettyPrinter(indent=4)




p = subprocess.Popen("C:/Users/asd93/PycharmProjects/Manim/venv/Scripts/activate.ps1yfile.ps1 & manim -pqm --fps 7 main.py working5",
                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)


for line in p.stdout:
    if line.decode('utf-8') == '                                                                                           ':
        pass
    else:
        print(line.decode('utf-8'))