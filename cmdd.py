import subprocess
import pprint
import subprocess
import sys

command=r'cd C:\Users\asd93\PycharmProjects\Manim'
pp = pprint.PrettyPrinter(indent=4)

def call_command(command):
    process=subprocess.Popen('powershell -command '+"'"+command+"'", stdin=subprocess.STDOUT,stdout=subprocess.STDOUT, shell=True)
    stdout_value = process.communicate()[0]
    return stdout_value

pg = subprocess.Popen("C:/Users/asd93/PycharmProjects/Manim/venv/Scripts/activate.ps1yfile.ps1 & manim -pql --fps 15 main.py working", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
buff,buffErr = pg.communicate()
import sys
sys.stdout.reconfigure(encoding='utf-8')

buff =buff.decode("utf-8")
print(buff)