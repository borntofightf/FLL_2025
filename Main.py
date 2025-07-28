from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor, b_motor,andar_reto

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
    #a_motor.run_angle(-1000, 550, wait=False)
    andar_reto_suave(97, 150)
    drive_base.turn(-95)
    wait(150)
    andar_reto(13,200)
    #a_motor.run_angle(2000, 1700
    a_motor.run_angle(500, 150, wait=False)
    wait(150)
    andar_reto(15,-200)
    drive_base.turn(94)
    wait(100)
    #Fim da Missão M1: Tridente 2.0 e Inicio da Missão M2: Grama
    andar_reto_suave(19,350)
    drive_base.turn(-55)
    wait(100)
    andar_reto(13,200)
    andar_reto(2,-200)
    b_motor.run_target(1000, 125)
    andar_reto_suave(14,-250)
    b_motor.run_target(-250, 50, wait=False)
    #andar_reto_suave(28,-350)
    #Fim da Missão M2: Grama
    drive_base.turn(85)
    andar_reto(80, -1000)

def saida_4():
    """Missão M12: Vem e Vai"""
    #Inicio da Missão M12: Vem e Vai
    b_motor.run_target(1000, 0, wait=False)
    andar_reto_suave(61, 150)
    b_motor.run_target(-1000, 125)
    #Fim da Missão M12: Vem e Vai e Volta para a Base
    wait(200)
    andar_reto_suave(65, -350)


# Choose a letter.
selected = hub_menu("1", "2", "3", "4")

# Based on the selection, run a program.
if selected == "1":
    pass
elif selected == "2":
    pass
elif selected == "3":
    saida_3()
elif selected == "4":
    saida_4()