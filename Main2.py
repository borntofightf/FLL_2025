
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
timer = StopWatch()

def saida_1():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    timer = StopWatch()
    timer.reset()      
    andar_reto_suave(79,500)
    wait(150)
    turn(-49, 100)
    wait(250)
    andar_reto_suave(9,300)
    andar_reto_suave(-4,150)
    b_motor.run_target(1000, -145)
    andar_reto_suave(4.5,700)
    andar_reto_suave(-7,350)
    b_motor.run_target(1000, -110)
    b_motor.run_target(300, -100,wait=False)
    andar_reto_suave(-10,150)
    b_motor.run_target(300, -95,wait=False)
    turn(-47, 200)
    wait(100)
    andar_reto_suave(13,600)
    a_motor.run_time(1000,1000,wait=False)
    wait(300)
    andar_reto_suave(-2,600)
    turn(-88, 250)
    print((timer.time()) / 1000) 
    left_motor.run_time(1000,2000,wait=False)
    right_motor.run_time(700,1800)


def saida_2():
    timer = StopWatch()
    timer.reset()     
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    wait(100)
    a_motor.run_angle(1000,1500,wait=False)
    andar_reto_suave(-102, 400)
    wait(100)
    b_motor.run_target(800, -137,wait=False)
    andar_reto_suave(5, 100)
    wait(100)
    turn(-90,100)
    print(hub.imu.heading())
    wait(100)
    andar_reto_suave(-3, 60)
    a_motor.run_angle(1000,500)
    andar_reto_suave(6, 60)
    a_motor.run_angle(1000,100)
    andar_reto_suave(5.3, 50)
    b_motor.run_target(100, -71)
    wait(350)
    b_motor.run_target(200, -100)
    a_motor.run_angle(-1000,200)
    andar_reto_suave(-14, 200)
    drive_base.turn(82)
    print((timer.time()) / 1000) 
    a_motor.run_angle(-1000,1000,wait=False)
    left_motor.run_time(1000,2000,wait=False)
    right_motor.run_time(950,2000)

def saida_3():
    timer = StopWatch()
    timer.reset()   
    """Missão M12: Operação de Resgate"""
    b_motor.run_target(1000, -0,wait=False)
    andar_reto_suave(46,500)
    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1100,935,wait=False)
    wait(400)
    andar_reto_suave(-6, 600)
    b_motor.run_target(300, -143)
    print((timer.time()) / 1000) 
    andar_reto_suave(-47, 1000)

def saida_4():
    timer = StopWatch()
    timer.reset()  
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(-2, 1000)
    andar_reto_suave(28, 700)
    wait(150)
    turn(40,90)
    print(hub.imu.heading())
    wait(150)
    andar_reto_suave(20, 700)
    turn(-8, 150)
    print(hub.imu.heading())
    b_motor.run_target(500, -130)
    turn(20,90)
    andar_reto_suave(2, 50)
    print(hub.imu.heading())
    b_motor.run_target(170, 0,wait=False)
    wait(250)
    andar_reto_suave(-2, 220)
    turn(-24,500)
    print((timer.time()) / 1000)
    print(hub.imu.heading())
    andar_reto_suave(-10, 220)


def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    timer = StopWatch()
    timer.reset()
    b_motor.run_target(100, -0, wait=False)
    andar_reto_suave(-2, 1000)
    andar_reto_suave(25, 200)
    wait(150)
    turn(-92, 200)
    wait(150)
    andar_reto_suave(48, 250)
    turn(-41, 200)
    a_motor.run_time(1000,3750,wait=False)
    turn(-4.6, 100)
    andar_reto_suave(-0.4, 100)

    wait(3000)
    turn(39, 1000)
    andar_reto_suave(5, 500)
    turn(77, 200)
    andar_reto_suave(8.5, 300)
    b_motor.run_target(1000, -120)
    b_motor.run_target(500, -80, wait=False)
    andar_reto_suave(-8.5, 300)
    turn(36, 300)
    andar_reto_suave(9, 500)
    b_motor.run_target(400, -135)
    andar_reto_suave(-6.5, 600)
    b_motor.run_target(500, 0, wait=False)
    turn(70, 1000)
    print((timer.time()) / 1000) 
    andar_reto_suave(70, 1000)

def saida_6():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    timer = StopWatch()
    timer.reset() 
    b_motor.run_target(800, 0, wait=False)
    andar_reto_suave(40, 300)
    b_motor.run_target(700, -140)
    wait(300)
    b_motor.run_target(200, -50)
    b_motor.run_target(800, -140)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(800, -140)
    wait(300)
    b_motor.run_target(200, -30)
    b_motor.run_target(1000, -140)
    b_motor.run_target(1000, 0)
    turn(-20, 200)
    andar_reto_suave(30, 300)
    turn(54, 200)
    andar_reto_suave(6, 200)
    turn(-38, 350)
    andar_reto_suave(2.5, 200)
    turn(-30, 900)
    andar_reto_suave(-4.5, 200)
    turn(-73, 250)
    andar_reto_suave(-22,300)
    a_motor.run_angle(1000, 235)
    andar_reto_suave(-22,300)
    a_motor.run_angle(-1000, 150)

    turn(100, 300)
    andar_reto_suave(2,300)
    print((timer.time()) / 1000) 

def saida_7():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    timer = StopWatch()
    timer.reset() 
    andar_reto_suave(-2, 1000)
    b_motor.run_target(120, -45,wait=False)

    #a_motor.run_angle(100, 100, wait=False)
    andar_reto_suave(48, 250)
    b_motor.run_target(50, -86, wait=False)
    wait(150)
    turn(-48, 50)
    wait(150)
    print(hub.imu.heading())
    andar_reto_suave(38.5, 250)
    b_motor.run_target(120, -60)
    andar_reto_suave(4.5, 250)
    andar_reto_suave(-6, 200)
    turn(-45, 85)
    print(hub.imu.heading())
    andar_reto_suave(16.3, 200)
    turn(48, 85)
    andar_reto_suave(-29, 250)
    turn(-23, 600)
    wait(300)
    andar_reto_suave(-3, 200)
    andar_reto_suave(14, 200)
    turn(-45, 100)
    andar_reto_suave(46, 1000)
    a_motor.run_angle(250, 150)
    wait(100)
    turn(-70, 200)
    print(hub.imu.heading())
    b_motor.run_target(200, -110)
    wait(150)
    b_motor.run_target(250, 0, wait=False)
    andar_reto_suave(-4.5, 1000)
    turn(28, 1000)
    print((timer.time()) / 1000) 


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
