from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, reset, drive_base, a_motor, b_motor,andar_reto,turn, left_motor, right_motor

#Velocidade de Movimento e Curva

drive_base.use_gyro(True)

def saida_1():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    wait(100)
    andar_reto_suave(-100, 250)
    
    b_motor.run_target(1000, -130, wait=False)
    andar_reto_suave(5, 80)
    turn(-90,100)
    a_motor.run_angle(-1000,780)
    andar_reto_suave(9, 80)
    a_motor.run_angle(500,57)
    b_motor.run_target(225, -83)
    wait(1000)
    b_motor.run_target(300, -100)
    andar_reto_suave(-19, 150)
    drive_base.turn(97)
    andar_reto_suave(100, 1000)
    
def saida_2():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    b_motor.run_target(1000, -120, wait=False)
    andar_reto_suave(75,300)
    wait(300)
    turn(-47, 80)
    andar_reto_suave(14,150)
    andar_reto_suave(-4,200)
    b_motor.run_target(1000, -176, wait=False)
    andar_reto_suave(5,200)
    b_motor.run_target(1000, -70, wait=False)
    andar_reto_suave(-21,350)
    turn(-35, 150)
    wait(100)
    andar_reto_suave(16,200)
    a_motor.run_time(1000,1000)
    andar_reto_suave(-12,900)
    turn(-70, 250)
    andar_reto_suave(70,1000)

def saida_3():
    """Missão M12: Operação de Resgate"""
    andar_reto_suave(30, 250)
    andar_reto_suave(13, 150)
    turn(3, 150)
    andar_reto_suave(-20, 150)
    andar_reto_suave(7, 200)
    andar_reto_suave(-80, 300)

def saida_4():
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    andar_reto_suave(30, 250)
    turn(89,200)
    wait(100)
    andar_reto_suave(73, 300)
    turn(90,100)
    andar_reto_suave(12,300)
    turn(-10, 200)
    a_motor.run_time(1000,2500)
    turn(12 ,800)
    andar_reto_suave(-7,400)
    turn(-90, 250)
    andar_reto_suave(7.5,500)
    turn(-90, 250)
    andar_reto_suave(7, 500)
    b_motor.run_target(400, -110)
    b_motor.run_target(250, -60)
    andar_reto_suave(-12, 600)
    turn(90, 600)
    andar_reto_suave(70, 1000)

def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    b_motor.run_target(300, -150, wait=False)
    andar_reto_suave(69, 300)
    b_motor.hold()
    right_motor.run_angle(150, 80)
    b_motor.run_target(300, -168)
    right_motor.run_angle(350, 250)
    andar_reto_suave(-4.5, 200)
    b_motor.run_target(300, -55, wait=False)
    left_motor.run_angle(-300, 140)
    andar_reto_suave(-34,300)
    turn(90, 250)
    a_motor.run_angle(-500, 400)
    andar_reto_suave(10, 250)
    a_motor.run_angle(500, 650)
    andar_reto_suave(-20, 500)

def saida_6():
    """Missões M9: O que está à venda, M10: Desequilíbrio da Balança, M13: Reconstrução da Estátua"""
    b_motor.run_target(1000, 0, wait=False)
    a_motor.run_time(400, 1000, wait=False)
    andar_reto_suave(18,300)
    turn(-48,300)
    andar_reto_suave(34.5, 300)
    a_motor.run_time(-800, 1200)
    a_motor.run_time(800, 2000)
    andar_reto_suave(-1, 300)
    turn(-30, 300)
    wait(100)
    andar_reto_suave(-1, 300)
    turn(28, 300)
    b_motor.run_angle(-250, 155)
    andar_reto_suave(-14, 150)
    andar_reto_suave(3, 150)
    turn(20, 300)
    b_motor.run_target(300, 0, wait=False)
    andar_reto_suave(-30, 300)
    turn(-20, 300)
    andar_reto_suave(-30, 1000)

def saida_7():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    b_motor.run_target(1000, -85, wait=False)
    andar_reto_suave(58, 300)
    turn(-52, 250)
    andar_reto_suave(43.5, 300)
    b_motor.run_target(200, -20)
    andar_reto_suave(-7, 300)
    turn(-41, 200)
    andar_reto_suave(75, 300)
    turn(-90, 250)
    andar_reto_suave(6, 300)
    a_motor.run_time(1000, 800)
    andar_reto_suave(-2, 300)
    b_motor.run_target(50, -90)
    andar_reto_suave(-15, 300)
    turn(70, 250)
    andar_reto_suave(15, 300)
    
# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5", "6", "7")

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
elif selected == "6":
    saida_6()
elif selected == "7":
    saida_7()