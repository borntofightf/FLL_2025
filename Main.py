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
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    #M2
    andar_reto_suave(79,500)
    turn(-56, 125)
    turn(13, 150)
    b_motor.run_target(1000, -145,wait=False)
    andar_reto_suave(14,150)
    andar_reto_suave(-11,350)
    #M1
    b_motor.run_target(1000, -85)
    andar_reto_suave(-7,200)
    turn(-48, 150)
    wait(100)
    andar_reto_suave(13,200)

    a_motor.run_time(1000,1000)
    andar_reto_suave(-11,900)
    turn(-70, 250)
    andar_reto_suave(70,1000,acele=1000)
    
def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""

    a_motor.run_angle(-1000,450,wait=False)
    andar_reto_suave(-102, 400)
    wait(100)
    b_motor.run_target(1000, -135,wait=False)
    andar_reto_suave(5, 80)
    wait(100)
    turn(-90,100)
    andar_reto_suave(-2, 80)
    a_motor.run_angle(-1000,220)
    andar_reto_suave(4, 100)
    a_motor.run_angle(-250,14,wait=False)
    andar_reto_suave(6, 100)


    a_motor.run_angle(500,40)
    b_motor.run_target(225, -80)
    wait(350)
    b_motor.run_target(300, -100)
    andar_reto_suave(-14, 200)
    drive_base.turn(95)
    a_motor.run_angle(250,250,wait=False)
    andar_reto_suave(100, 1000,acele=1000)

def saida_3():
    """Missão M12: Operação de Resgate"""
    andar_reto_suave(31,1000)
    andar_reto_suave(22, 250)
    andar_reto_suave(-2, 250)
    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1000,1250)
    andar_reto_suave(-15, 150)
    a_motor.run_time(1000,1250,wait=False)
    andar_reto_suave(-80, 300)
    
def saida_4():
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(28, 220)
    turn(40,40)
    andar_reto_suave(19.5, 220)
    b_motor.run_target(500, -120)
    turn(17,100)
    wait(100)
    b_motor.run_target(1000, 0,wait=False)
    wait(200)
    andar_reto_suave(-21, 300)
    turn(47,150)

    andar_reto_suave(75, 300)

    turn(91,100)
    andar_reto_suave(13,250)
    turn(-6, 200)
    a_motor.run_time(1000,2500)
    andar_reto_suave(-8,400)
    turn(-90, 200)
    andar_reto_suave(13,200)
    turn(-90, 200)
    
    b_motor.run_target(200, -100,wait=False)
    andar_reto_suave(8, 500)
    b_motor.run_target(400, -125)
    b_motor.run_target(250, -60)
    andar_reto_suave(-9, 600)
    turn(33, 600)
    andar_reto_suave(8, 200)
    b_motor.run_target(200, -130)
    andar_reto_suave(-10, 200)
    b_motor.run_target(200, -60, wait=False)
    turn(67, 200)
    andar_reto_suave(70, 1000,acele=1000)

def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    andar_reto_suave(40, 300)
    b_motor.run_target(1000, -118)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(650, -120)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(650, -120)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(650, -120)
    b_motor.run_target(1000, 0)
    turn(-20, 200)
    andar_reto_suave(33, 300)
    turn(61, 200)
    andar_reto_suave(4.5, 200)
    wait(200)
    turn(-61, 250)
    andar_reto_suave(-5.5, 200)
    turn(-88, 250)
    andar_reto_suave(-42,300)

    turn(95, 250)
    a_motor.run_angle(-1000, 205,False)
    andar_reto_suave(6.5, 250)
    a_motor.run_angle(-1000, 205)
    andar_reto_suave(11, 250)
    a_motor.run_angle(700, 450)
    left_motor.run_time(-800,6000,wait=False)
    right_motor.run_time(-500,6000,wait=False)

def saida_6():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    
    andar_reto_suave(54, 250)
    b_motor.run_target(500, -81, wait=False)
    turn(-60, 100)

    andar_reto_suave(36, 300)
    b_motor.run_target(120, 0)
    wait(100)
    andar_reto_suave(7, 200)
    wait(100)
    andar_reto_suave(-8, 200)
    turn(-42, 150)
    andar_reto_suave(16, 200)
    turn(46, 200)
    andar_reto_suave(-25, 350)
    andar_reto_suave(11.5, 200)
    turn(-56, 200)
    andar_reto_suave(57, 1000)
    wait(100)
    a_motor.run_angle(300, 150)
    andar_reto_suave(13, 380)
    turn(-40, 600)

# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5", "6","7")

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