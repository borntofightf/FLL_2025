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
    a_motor.run_angle(-1000,700,wait=False)
    andar_reto_suave(-102, 300)
    b_motor.run_target(1000, -124)
    andar_reto_suave(5.5, 80)
    turn(-91,100)
    andar_reto_suave(7.5, 80)
    a_motor.run_angle(500,50)
    b_motor.run_target(225, -80)
    wait(500)
    b_motor.run_target(300, -100)
    andar_reto_suave(-19, 150)
    a_motor.run_angle(300,300,wait=False)
    drive_base.turn(110)
    andar_reto_suave(100, 1000)
    
def saida_2():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    andar_reto_suave(78,330)
    wait(200)
    turn(-47, 80)
    andar_reto_suave(14,150)
    andar_reto_suave(-4,200)
    b_motor.run_target(1000, -140)
    andar_reto_suave(5,200)
    andar_reto_suave(-12.5,350)
    b_motor.run_target(1000, -85)
    andar_reto_suave(-5.5,200)
    turn(-48, 150)
    wait(100)
    andar_reto_suave(13,200)
    a_motor.run_time(1000,1000)
    andar_reto_suave(-11,900)
    turn(-70, 250)
    andar_reto_suave(70,1000)

def saida_3():
    """Missão M12: Operação de Resgate"""
    andar_reto_suave(30,700)
    andar_reto_suave(14, 250)
    turn(3, 150)
    a_motor.run_time(1000,950)
    wait(100)
    a_motor.run_time(1000,700)
    andar_reto_suave(-15, 150)
    a_motor.run_time(-1000,700,wait=False)

    andar_reto_suave(-80, 300)
    

def saida_4():
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(30, 200)
    turn(90,150)
    wait(100)
    andar_reto_suave(73, 300)
    turn(90,100)
    andar_reto_suave(12,300)
    turn(-10, 200)
    a_motor.run_time(1000,2550)
    turn(10 ,800)
    andar_reto_suave(-7,400)
    turn(-90, 250)
    andar_reto_suave(14,500)
    turn(-92, 250)
    andar_reto_suave(5, 500)
    b_motor.run_target(400, -125)
    b_motor.run_target(250, -60)
    andar_reto_suave(-9, 600)
    turn(97, 600)
    andar_reto_suave(70, 1000)

def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    andar_reto_suave(40, 300)
    b_motor.run_target(300, -110)
    wait(350)
    b_motor.run_target(100, -50)
    b_motor.run_target(300, -110)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(300, -120)
    b_motor.run_target(1000, 0)
    andar_reto_suave(21.5, 300)
    b_motor.run_target(500, -107)
    turn(-17, 250)
    right_motor.run_angle(350, 100)
    andar_reto_suave(4.5, 300)
    b_motor.run_target(500, -120)
    right_motor.run_angle(400, 140)
    right_motor.run_angle(-350, 40)
    andar_reto_suave(-2, 150)
    b_motor.run_target(300, -55)
    andar_reto_suave(6,100)
    left_motor.run_angle(-300, 230)
    andar_reto_suave(-36,300)
    turn(90, 250)
    andar_reto_suave(3.5, 250)
    a_motor.run_angle(-500, 400)
    andar_reto_suave(9, 250)
    a_motor.run_angle(500, 650)
    andar_reto_suave(-30, 500)

def saida_6():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    b_motor.run_target(1000, -79, wait=False)
    andar_reto_suave(55, 200)
    turn(-50, 150)
    wait(100)
    andar_reto_suave(36, 300)
    b_motor.run_target(120, -20)
    wait(100)
    turn(-45, 150)
    wait(100)
    andar_reto_suave(45, 350)
    turn(-90, 250)
    andar_reto_suave(-31, 350)
    andar_reto_suave(22, 250)
    turn(90, 250)
    andar_reto_suave(33, 250)
    turn(-95, 150)
    a_motor.run_time(-1000, 900,wait=False)
    wait(100)
    andar_reto_suave(9, 300)
    #b_motor.run_target(50, -90, wait=False)
    
    andar_reto_suave(-13, 300)
    a_motor.run_time(-1000,400,wait=False)
    turn(-17, 250)
    
    andar_reto_suave(13, 200)
    a_motor.run_time(1000, 850,wait=False)
    wait(180)
    turn(-35, 250)
    wait(400)
    turn(25, 250)
    andar_reto_suave(-15, 300)
    a_motor.run_time(1000, 600)
    b_motor.run_target(80, -97)
    andar_reto_suave(11, 200)
    andar_reto_suave(-10, 400)
    turn(80, 250)
    andar_reto_suave(19, 300)

    
# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5", "6")

# Based on the selection, run a program.
if selected == "1":
    saida_2()
elif selected == "2":
    saida_1()
elif selected == "3":
    saida_3()
elif selected == "4":
    saida_4()
elif selected == "5":
    saida_5()
elif selected == "6":
    saida_6()
