
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, reset, drive_base, a_motor, b_motor,andar_reto,turn, left_motor, right_motor, curva

#Velocidade de Movimento e Curva

drive_base.use_gyro(True)

def saida_1():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    andar_reto_suave(79.5,500)
    wait(150)
    turn(-49, 160)
    wait(100)
    andar_reto_suave(9,300)
    andar_reto_suave(-3.5,150)
    b_motor.run_target(1000, -145)
    andar_reto_suave(7,700)
    andar_reto_suave(-7,350)
    b_motor.run_target(1000, -110)
    b_motor.run_target(300, -100,wait=False)
    andar_reto_suave(-12,150)
    b_motor.run_target(300, -95,wait=False)
    turn(-45, 200)
    wait(100)
    andar_reto_suave(13,600)
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
    b_motor.run_target(800, -137,wait=False)
    andar_reto_suave(5, 100)
    wait(100)
    turn(-88,100)
    andar_reto_suave(-3, 100)
    a_motor.run_angle(1000,500)
    andar_reto_suave(6, 125)
    a_motor.run_angle(1000,110)
    andar_reto_suave(5.7, 130)
    b_motor.run_target(100, -71)
    wait(350)
    b_motor.run_target(200, -100)
    a_motor.run_angle(-1000,230)
    andar_reto_suave(-14, 200)
    drive_base.turn(95)
    a_motor.run_angle(-1000,1000,wait=False)
    left_motor.run_time(1000,2000,wait=False)
    right_motor.run_time(950,2000)

def saida_3():
    """Missão M12: Operação de Resgate"""
    andar_reto_suave(46,1000)

    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1100,1000)
    wait(200)
    
    andar_reto_suave(-4, 600)
    b_motor.run_target(300, -140)
    andar_reto_suave(-9, 600)
    b_motor.run_target(1000, -130,wait=False)
    andar_reto_suave(-90, 1000)

def saida_4():
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(28.5, 250)
    turn(42,50)
    print(hub.imu.heading())
    andar_reto_suave(19.5, 250)
    b_motor.run_target(500, -125)
    turn(-10,200)
    print(hub.imu.heading())
    wait(250)
    turn(22,100)
    print(hub.imu.heading())
    wait(100)
    b_motor.run_target(1000, 0,wait=False)
    wait(100)
    andar_reto_suave(-22, 300)
    wait(200)
    turn(40,150)

    print(hub.imu.heading())
    andar_reto_suave(92, 300)
    curva(-90, 100)


    b_motor.run_target(200, -100,wait=False)
    andar_reto_suave(6, 500)
    b_motor.run_target(700, -125)
    b_motor.run_target(250, -60,wait=False)
    andar_reto_suave(-9, 600)
    turn(31, 300)
    andar_reto_suave(8, 500)
    b_motor.run_target(300, -130)
    andar_reto_suave(-11, 600)
    b_motor.run_target(1000, -60, wait=False)
    
    turn(-130, 100)
    andar_reto_suave(-6, 200)
    turn(-35, 500)
    andar_reto_suave(-2, 1000)
    a_motor.run_time(1000,3000)
    turn(40, 500)
    andar_reto_suave(-100, 1000)


def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    b_motor.run_target(800, 0, wait=False)
    andar_reto_suave(40, 300)
    b_motor.run_target(700, -140)
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
    turn(57, 200)
    andar_reto_suave(6.5, 200)
    turn(-38, 350)
    andar_reto_suave(2.5, 200)
    turn(-30, 900)
    andar_reto_suave(-4.5, 200)
    turn(-77, 250)
    andar_reto_suave(-22,300)
    a_motor.run_angle(1000, 235)
    andar_reto_suave(-22,300)
    a_motor.run_angle(-800, 120,wait=False)
    turn(97, 300)


def saida_6():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    b_motor.run_target(120, -55,wait=False)
    #a_motor.run_angle(100, 100, wait=False)
    andar_reto_suave(47, 300)
    wait(300)
    b_motor.run_target(500, -88, wait=False)
    turn(-51, 50)
    print(hub.imu.heading())
    andar_reto_suave(39, 500)
    b_motor.run_target(120, -60)
    andar_reto_suave(5, 200)
    andar_reto_suave(-5, 200)
    turn(-43, 100)
    print(hub.imu.heading())
    andar_reto_suave(18, 200)
    turn(44, 200)
    andar_reto_suave(-17, 225)
    wait(100)
    andar_reto_suave(11.5, 200)
    turn(-47, 200)
    print(hub.imu.heading())

    andar_reto_suave(55, 1000)
    a_motor.run_angle(250, 150)
    wait(100)
    turn(-90, 200)

    
    
    
    print(hub.imu.heading())
    b_motor.run_target(200, -115)
    wait(100)
    b_motor.run_target(250, 0, wait=False)

    turn(89, 200)
    andar_reto_suave(16, 200)


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

