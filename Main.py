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
    b_motor.run_target(300, -81, wait=False)
    andar_reto_suave(103, 150)
    drive_base.turn(-42)
    a_motor.run_angle(-400, 200)
    andar_reto_suave(14, 100)
    b_motor.run_angle(200, 250, wait=False)
    andar_reto(20,-300)
    drive_base.turn(-105)
    andar_reto(44, 1000)

def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    #Inicio das Missões M3: Exploradora de Minas, M4: Extração Segura
    andar_reto_suave(140, -150)
    a_motor.run_time(-1000,1200)
    andar_reto_suave(12.5, 100)
    drive_base.turn(-90)
    andar_reto_suave(20, 50)
    a_motor.run_time(100,200)

def saida_3():
    """Missão M12: Operação de Resgate"""
    #Inicio da Missão M12: Operação de Resgate
    andar_reto_suave(45, 150)
    andar_reto(14, 100)
    wait(100)
    drive_base.turn(2)
    andar_reto(23, -100)
    andar_reto(10, 100)
    left_motor.run_time(200, 400)
    andar_reto(90, -250)

def saida_4():
    """Missão M11: Pesca de Artefatos"""
    #Inicio da Missão M11: Pesca de Artefatos
    andar_reto_suave(44, 150)
    drive_base.turn(89)
    andar_reto_suave(99, 500)
    drive_base.turn(90)
    andar_reto(10,150)
    drive_base.turn(-3)
    a_motor.run_time(1000,4000)
    drive_base.turn(10)
    andar_reto(11,-150)
    drive_base.turn(-75)
    andar_reto(60,1000)

    

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
    a_motor.run_time(-700, 1300)
    a_motor.run_time(800, 1900)
    drive_base.turn(-8)
    andar_reto_suave(23, -350)
    andar_reto_suave(10, 200)
    b_motor.run_target(-150, 0)
    andar_reto_suave(3, -350)

    drive_base.turn(-35)
    drive_base.turn(37)
    andar_reto_suave(5, 200)
    drive_base.turn(-20)
    andar_reto_suave(50, -800)

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