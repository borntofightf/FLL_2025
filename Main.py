
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
    andar_reto_suave(79,500)
    wait(150)
    turn(-50, 160)
    wait(100)
    andar_reto_suave(9,300)
    andar_reto_suave(-5,150)
    b_motor.run_target(1000, -145)
    

    andar_reto_suave(7,700)
    andar_reto_suave(-6,350)
    b_motor.run_target(500, -95)
    andar_reto_suave(-12,200)
    turn(-50, 200)
    wait(100)
    andar_reto_suave(15,600)

    a_motor.run_time(1000,1000,wait=False)
    wait(300)
    turn(-85, 250)
    left_motor.run_time(1000,2000,wait=False)
    right_motor.run_time(800,2000)

def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    wait(100)
    a_motor.run_angle(1000,1500,wait=False)
    andar_reto_suave(-102, 400)
    wait(100)
    b_motor.run_target(1000, -140,wait=False)
    andar_reto_suave(5, 80)
    wait(100)
    turn(-90,100)
    andar_reto_suave(-3, 100)
    a_motor.run_angle(1000,555)
    andar_reto_suave(6, 200)
    a_motor.run_angle(1000,120)
    andar_reto_suave(5, 100)

    b_motor.run_target(100, -75)
    wait(350)
    b_motor.run_target(200, -100)
    a_motor.run_angle(-1000,250)



    andar_reto_suave(-14, 200)
    drive_base.turn(95)
    a_motor.run_angle(-1000,1000,wait=False)
    andar_reto_suave(95, 1000)

def saida_3():
    """Missão M12: Operação de Resgate"""
    andar_reto_suave(53,1000)
    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1000,1000)
    wait(200)
    
    andar_reto_suave(-4, 600)
    b_motor.run_target(300, -150)
    andar_reto_suave(-9, 600)
    b_motor.run_target(1000, -130,wait=False)
    andar_reto_suave(-90, 1000)

def saida_4():
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(29, 250)
    turn(45,150)
    print(hub.imu.heading())
    andar_reto_suave(19, 250)
    b_motor.run_target(500, -125)
    turn(-10,200)
    print(hub.imu.heading())
    wait(250)
    turn(22,100)
    print(hub.imu.heading())
    wait(100)
    b_motor.run_target(1000, 0,wait=False)
    wait(300)
    andar_reto_suave(-22, 300)
    turn(38,150)
    print(hub.imu.heading())
    andar_reto_suave(78, 300)

    turn(90,100)
    andar_reto_suave(14,250)

    a_motor.run_time(1000,2500)
    turn(3,100)
    andar_reto_suave(-8,400)
    turn(-88, 200)
    andar_reto_suave(14,200)
    turn(-90, 200)

    b_motor.run_target(200, -100,wait=False)
    andar_reto_suave(5, 500)
    b_motor.run_target(400, -125)
    b_motor.run_target(250, -60,wait=False)
    andar_reto_suave(-9, 600)
    turn(33, 600)
    andar_reto_suave(8, 500)
    b_motor.run_target(300, -130)
    andar_reto_suave(-10, 600)
    b_motor.run_target(1000, -60, wait=False)
    turn(67, 600)
    andar_reto_suave(70, 1000)

def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    b_motor.run_target(800, 0, wait=False)
    andar_reto_suave(40, 300)
    b_motor.run_target(800, -140)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(900, -140)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(900, -140)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(900, -140)
    b_motor.run_target(1000, 0)
    turn(-20, 200)
    andar_reto_suave(30, 300)
    turn(58, 200)
    andar_reto_suave(6, 200)
    turn(-38, 350)
    andar_reto_suave(3, 200)
    turn(-25, 500)
    andar_reto_suave(-5, 200)
    turn(-75, 250)
    andar_reto_suave(-22,300)
    a_motor.run_angle(1000, 235)
    andar_reto_suave(-22,300)
    a_motor.run_angle(-800, 120,wait=False)
    turn(90, 300)


def saida_6():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    andar_reto_suave(52, 300)
    b_motor.run_target(500, -83, wait=False)
    turn(-57,100)
    andar_reto_suave(35, 500)
    b_motor.run_target(120, 0,wait=False)
    andar_reto_suave(9, 200)
    wait(100)
    andar_reto_suave(-10, 200)
    turn(-37, 150)
    andar_reto_suave(17.5, 200)
    turn(40, 200)
    andar_reto_suave(-15, 150)
    wait(100)
    andar_reto_suave(12, 200)
    turn(-49, 200)
    andar_reto_suave(55, 1000)
    wait(100)
    a_motor.run_angle(250, 150)
    turn(-95, 150)
    b_motor.run_target(100, -140)
    wait(100)
    b_motor.run_target(250, 0, wait=False)
    andar_reto_suave(4,200)
    andar_reto_suave(-4,200)

    turn(90, 500)
    andar_reto_suave(14, 1000)

    turn(-19, 200)

# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5", "6")

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
