from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, a_motor

def Saida3():
    andar_reto_suave(105,350)
    curva(-57, 200)
    andar_reto_suave(10,350)
    andar_reto_suave(10,-350)
    curva(70,550)
    andar_reto_suave(120,-350)


# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3")

# Based on the selection, run a program.
if selected == "1":
    import hello_world
elif selected == "2":
    import sound
elif selected == "3":
    Saida3()

