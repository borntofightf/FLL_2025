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

def saida_3():
    """Missões M1: Tridente 2.0, M2: Grama, M3: Indianaa Jones"""
    #Inicio da Missão M1: Tridente 2.0
    b_motor.run_target(1000, 0, wait=False)
    a_motor.run_angle(-1000, 550, wait=False)
    andar_reto_suave(84, 250)
    drive_base.turn(-97)
    andar_reto_suave(15, 150)
    wait(200)
    a_motor.run_angle(1000, 1700)
    wait(200)
    a_motor.run_angle(-1000, 600)
    wait(150)
    andar_reto_suave(15, -350)
    drive_base.turn(94)
    wait(100)
    #Fim da Missão M1: Tridente 2.0 e Inicio da Missão M2: Grama
    a_motor.run_angle(1000, 800, wait=False)
    andar_reto_suave(19,350)
    drive_base.turn(-54)
    wait(100)
    andar_reto_suave(18,350)
    a_motor.run_angle(-1200, 650, wait=False)
    wait(200)
    andar_reto_suave(28,-350)
    wait(100)
    drive_base.turn(110)
    b_motor.run_angle(-1000, 110)

def saida_4():
    """Missão M12: Vem e Vai"""
    b_motor.run_target(1000, 0, wait=False)
    andar_reto_suave(55, 200)
    b_motor.run_target(-1000, -115)
    wait(200)
    andar_reto_suave(65, -350)

saida_3()
