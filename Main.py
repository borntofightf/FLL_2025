from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor, b_motor,andar_reto,turn, left_motor, right_motor

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

def saida_1():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    #Inicio da Missão M1: Escavação Supercial
    b_motor.run_target(300, -110, wait=False)
    andar_reto_suave(100, 170)
    drive_base.turn(-40)
    andar_reto(6, -150)
    andar_reto_suave(25, 60)
    b_motor.run_angle(250, 60)
    andar_reto(23,-250)
    drive_base.turn(-19)
    a_motor.run_angle(-400, 500)
    andar_reto(10, 100)
    a_motor.run_angle(400, 550)
    andar_reto(13, -150)
    drive_base.turn(-115)
    andar_reto(60, 300)

def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    #Inicio das Missões M3: Exploradora de Minas, M4: Extração Segura

def saida_3():
    """Missão M12: Operação de Resgate"""
    #Inicio da Missão M12: Operação de Resgate
    andar_reto_suave(45, 150)
    andar_reto(12, 100)
    wait(100)
    drive_base.turn(2)
    andar_reto(23, -100)
    andar_reto(10, 100)
    left_motor.run_time(200, 400)
    andar_reto(90, -250)

def saida_4():
    """Missão M11: Pesca de Artefatos"""
    #Inicio da Missão M11: Pesca de Artefatos
    andar_reto_suave(45, 150)
    drive_base.turn(90)
    andar_reto_suave(160, 250)
    drive_base.turn(45)
    andar_reto_suave(30, 200)

def saida_5():
    """Missões M9: O que está à venda, M10: Desequilíbrio da Balança, M13: Reconstrução da Estátua"""
    #Inicio das Missões M9: O que está à venda, M10: Desequilíbrio da Balança
    b_motor.run_target(1000, 0, wait=False)
    
    andar_reto_suave(32,100)
    drive_base.turn(45)
    a_motor.run_time(200,200, wait=False)
    andar_reto_suave(33,120)
    b_motor.run_target(300, -114)
    b_motor.hold()
    a_motor.run_time(-300, 1150)
    a_motor.run_time(600, 1900)
    drive_base.turn(-8)
    andar_reto_suave(23, -350)
    andar_reto_suave(10, 200)
    b_motor.run_target(-150, 0)
    andar_reto_suave(4, -350)

    drive_base.turn(-30)
    drive_base.turn(34)
    andar_reto_suave(6, 200)
    drive_base.turn(-15)
    andar_reto_suave(45, -800)

# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5")

# Based on the selection, run a program.
if selected == "1":
    saida_1()
elif selected == "2":
    saida_2()
elif selected == "3":
    saida_3()
elif selected == "4":
    saida_4()
elif selected == "5":
    saida_5()