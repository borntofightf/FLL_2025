from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor, b_motor



#Velocidade de Movimento e Curva

velocidade_reta = 620
aceleracao_reta = 500
velocidade_curva = 260
aceleracao_curva = 500
drive_base.settings(straight_speed=velocidade_reta)
drive_base.settings(straight_acceleration=aceleracao_reta)
drive_base.settings(turn_rate=velocidade_reta)
drive_base.settings(turn_acceleration=aceleracao_curva)
drive_base.use_gyro(True)
def M2_grama():
    a_motor.run_angle(-1000, 500, wait=False)
    andar_reto_suave(75, 350)
    drive_base.turn(-95)
    andar_reto_suave(10, 350)
    wait(200)
    a_motor.run_angle(1000, 450)
    andar_reto_suave(15, -350)
    drive_base.turn(90)
    andar_reto_suave(27,350)
    drive_base.turn(-50)
    andar_reto_suave(12,350)
    a_motor.run_angle(-1000, 700, wait=False)
    andar_reto_suave(18,-350)
    drive_base.turn(140)

M2_grama()