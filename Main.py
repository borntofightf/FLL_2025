from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor

#Velocidade de Movimento e Curva

velocidade_reta = 620
aceleracao_reta = 500
velocidade_curva = 250
aceleracao_curva = 500
drive_base.settings(straight_speed=velocidade_reta)
drive_base.settings(straight_acceleration=aceleracao_reta)
drive_base.settings(turn_rate=velocidade_reta)
drive_base.settings(turn_acceleration=aceleracao_curva)

def M2_grama():
    andar_reto_suave(87,350)
    drive_base.turn(-25)
    andar_reto_suave(17, 350)
    a_motor.run_angle(1500, 600, wait=False)
    wait(50)
    andar_reto_suave(20, -350)
    drive_base.turn(35)
    andar_reto_suave(95,-350)

M2_grama()