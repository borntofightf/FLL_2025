from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base

#Velocidade de Movimento e Curva

velocidade_reta = 620
aceleracao_reta = 500
velocidade_curva = 250
aceleracao_curva = 500
drive_base.settings(straight_speed=velocidade_reta)
drive_base.settings(straight_acceleration=aceleracao_reta)
drive_base.settings(turn_rate=velocidade_reta)
drive_base.settings(turn_acceleration=aceleracao_curva)

andar_reto_suave(50,350)
drive_base.turn(90)