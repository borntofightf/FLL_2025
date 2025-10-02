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
    andar_reto_suave(78,500)
    wait(100)
    turn(-46, 100)
    andar_reto_suave(14,150)
    andar_reto_suave(-4,200)
    b_motor.run_target(1000, -145)
    andar_reto_suave(5,200)
    andar_reto_suave(-11,350)
    b_motor.run_target(1000, -85)
    andar_reto_suave(-6,200)
    turn(-48, 150)
    wait(100)
    andar_reto_suave(13.5,200)
    a_motor.run_time(1000,1000)
    andar_reto_suave(-11,900)
    turn(-70, 250)
    andar_reto_suave(70,1000)
    
def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    wait(100)
    a_motor.run_angle(-1000,700,wait=False)
    andar_reto_suave(-102, 300)
    b_motor.run_target(1000, -124)
    andar_reto_suave(5.5, 80)
    turn(-90,100)
    andar_reto_suave(8, 80)
    a_motor.run_angle(500,60)
    b_motor.run_target(225, -80)
    wait(500)
    b_motor.run_target(300, -100)
    andar_reto_suave(-19, 150)
    a_motor.run_angle(300,300,wait=False)
    drive_base.turn(110)
    andar_reto_suave(100, 1000)

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
    andar_reto_suave(73, 350)
    turn(90,100)
    andar_reto_suave(14.5,300)
    turn(-5, 200)
    a_motor.run_time(1000,2550)
    turn(5 ,800)
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
    b_motor.run_target(500, -118)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(500, -120)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(500, -120)
    b_motor.run_target(1000, 0)
    andar_reto_suave(24, 300)
    b_motor.run_target(600, -135)
    turn(3, 200)
    wait(200)
    b_motor.run_target(500, -90, wait=False)
    turn(-3, 200)
    right_motor.run_angle(350, 135)
    b_motor.run_target(500, -120)
    andar_reto_suave(1.5, 300)
    right_motor.run_angle(500, 150)
    andar_reto_suave(2, 150)
    right_motor.run_angle(-350, 40)
    andar_reto_suave(-2, 150)
    b_motor.run_target(300, -55)
    andar_reto_suave(4,100)
    turn(-48, 250)
    andar_reto_suave(-40,300)
    turn(87, 250)
    andar_reto_suave(7.5, 250)
    a_motor.run_angle(-500, 400)
    andar_reto_suave(9, 250)
    a_motor.run_angle(500, 500)
    turn(-15, 200)
    andar_reto_suave(-30, 500)

def saida_6():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    b_motor.run_target(1000, -81, wait=False)
    andar_reto_suave(56, 200)
    turn(-48, 50)
    wait(100)
    andar_reto_suave(36, 300)
    b_motor.run_target(120, -20)
    wait(100)
    andar_reto_suave(8, 200)
    wait(100)
    andar_reto_suave(-5, 200)
    turn(-44, 150)
    
    andar_reto_suave(6.5, 200)
    turn(43, 200)
    andar_reto_suave(-14, 230)
    a_motor.run_angle(-1000, 300,wait=False)
    andar_reto_suave(-18, 100)
    andar_reto_suave(11, 200)
    turn(-45, 200)
    andar_reto_suave(-26, 200)
    turn(68, 200)
    andar_reto_suave(-100, 800)

def saida_7():
    andar_reto_suave(31, 200)
    turn(-91, 200)
    andar_reto_suave(64, 400)
    b_motor.run_target(200, -140,wait=False)
    turn(31, 250)
    andar_reto_suave(16, 250)
    b_motor.run_target(100, -55,wait=False)
    turn(19, 150)
    andar_reto_suave(2, 200)
    turn(30, 250)
    andar_reto_suave(5, 350)
    a_motor.run_angle(-1000, 450)
    andar_reto_suave(-15, 1000)


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