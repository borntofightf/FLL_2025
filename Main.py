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
    andar_reto_suave(125,250)
    wait(100)
    andar_reto_suave(140,-250)

def saida_2():
    """Missões M9: O que está à venda, M10: Desequilíbrio da Balança, M13: Reconstrução da Estátua"""
    #Inicio das Missões M9: O que está à venda, M10: Desequilíbrio da Balança
    b_motor.run_target(1000, 0, wait=False)
    
    andar_reto_suave(31,150)
    drive_base.turn(44)
    a_motor.run_time(250,400, wait=False)
    andar_reto_suave(34,150)
    drive_base.turn(5)
    b_motor.run_time(-200, 1200)
    b_motor.hold()
    a_motor.run_time(-300, 1150)
    a_motor.run_time(600, 1900)
    andar_reto_suave(15, -350)
    andar_reto_suave(3, 200)
    b_motor.run_target(-150, 0)
    andar_reto_suave(5, -250)
    a_motor.run_time(200, 1700, wait=False)
    b_motor.run_time(-200, 1200)
    drive_base.turn(-50)
    b_motor.run_target(-150, 0)
    andar_reto_suave(70, 350)
    drive_base.turn(25)
    andar_reto(25,200)
    drive_base.turn(-37)
    andar_reto_suave(120, 200)
    #Fim das Missões M9: O que está à venda, M10: Desequilíbrio da Balança e Inicio da Missão M5: Reconstrução da Estátua
    
def saida_3():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    #Inicio da Missão M1: Escavação Supercial
    b_motor.run_target(300, -110, wait=False)
    andar_reto_suave(101, 170)
    drive_base.turn(-43)
    andar_reto_suave(25, 60)
    b_motor.run_angle(250, 50)
    andar_reto(23,-250)
    drive_base.turn(-19)
    a_motor.run_angle(-400, 500)
    andar_reto(10, 100)
    a_motor.run_angle(400, 550)
    andar_reto(13, -150)
    drive_base.turn(-125)
    andar_reto(60, 300)

def saida_4():
    """Missão M12: Operação de Resgate"""
    #Inicio da Missão M12: Operação de Resgate
    andar_reto_suave(47, 150)
    andar_reto(15, 100)
    wait(100)
    drive_base.turn(2)
    andar_reto(25, -100)
    andar_reto(13, 100)
    andar_reto(90, -250)

def saida_5():
    andar_reto_suave(135, 200)
    turn(90, 150)
    a_motor.run_angle(150, 200)
    turn(-4, 150)
    andar_reto_suave(20, 200)
    a_motor.run_angle(-150, 50)
    wait(500)
    andar_reto_suave(20, -200)

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