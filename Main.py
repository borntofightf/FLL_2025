
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
    timer = StopWatch()
    timer.reset()      
    andar_reto_suave(79,500)


    wait(150)
    turn(-49, 160)
    wait(100)
    andar_reto_suave(9,300)
    andar_reto_suave(-3.5,150)
    b_motor.run_target(1000, -145)
    andar_reto_suave(5,700)
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
    turn(-85, 250)
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
    andar_reto_suave(5.3, 100)
    wait(100)
    turn(-90,100)
    print(hub.imu.heading())
    andar_reto_suave(-3, 50)
    a_motor.run_angle(1000,500)
    andar_reto_suave(6, 80)
    a_motor.run_angle(1000,100)
    andar_reto_suave(5.3, 50)
    b_motor.run_target(100, -71)
    wait(350)
    b_motor.run_target(200, -100)
    a_motor.run_angle(-1000,230)
    andar_reto_suave(-14, 200)
    drive_base.turn(90)
    print((timer.time()) / 1000) 
    a_motor.run_angle(-1000,1000,wait=False)
    left_motor.run_time(1000,2000,wait=False)
    right_motor.run_time(950,2000)

def saida_3():
    timer = StopWatch()
    timer.reset()   
    """Missão M12: Operação de Resgate"""
    b_motor.run_target(1000, -0,wait=False)
    andar_reto_suave(48,500)

    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1100,925)
    wait(200)
    
    andar_reto_suave(-6, 600)
    b_motor.run_target(300, -143)
    andar_reto_suave(-9, 1000)
    b_motor.run_target(1000, -135,wait=False)
    print((timer.time()) / 1000) 
    andar_reto_suave(-47, 1000)

def saida_4():
    timer = StopWatch()
    timer.reset()  
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(28, 250)
    turn(41,50)
    print(hub.imu.heading())
    andar_reto_suave(18.5, 250)
    
    turn(-8,100)
    print(hub.imu.heading())
    b_motor.run_target(500, -129)
    turn(22,100)
    print(hub.imu.heading())
    b_motor.run_target(1000, 0,wait=False)
    wait(100)
    andar_reto_suave(-22, 300)
    wait(200)
    turn(42,150)
    print(hub.imu.heading())
    andar_reto_suave(91.5, 300)
    curva(-90, 100)

    andar_reto_suave(7, 500)
    b_motor.run_target(1000, -125)
    b_motor.run_target(250, -60,wait=False)
    andar_reto_suave(-8, 600)
    turn(34, 300)
    andar_reto_suave(7.5, 500)
    b_motor.run_target(300, -130)
    andar_reto_suave(-5.5, 600)
    b_motor.run_target(1000, -60, wait=False)
    turn(-172, 200)
    a_motor.run_time(1000,3200,wait=False)
    turn(-4, 10)
    wait(3200)
    turn(52, 500)
    print((timer.time()) / 1000)
    andar_reto_suave(-100, 1000)

    

def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    timer = StopWatch()
    timer.reset() 
    b_motor.run_target(800, 0, wait=False)
    andar_reto_suave(40, 300)
    b_motor.run_target(700, -140)
    wait(300)
    b_motor.run_target(200, -50)
    b_motor.run_target(900, -140)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(900, -140)
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
    turn(-75, 250)
    andar_reto_suave(-22,300)
    a_motor.run_angle(1000, 235)
    andar_reto_suave(-22,300)
    a_motor.run_angle(-800, 120,wait=False)
    wait(200)
    turn(100, 300)
    andar_reto_suave(2,300)
    print((timer.time()) / 1000) 


def saida_6():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    timer = StopWatch()
    timer.reset() 
    b_motor.run_target(120, -55,wait=False)

    #a_motor.run_angle(100, 100, wait=False)
    andar_reto_suave(60, 200)
    b_motor.run_target(50, -88, wait=False)
    wait(150)
    turn(-52, 50)
    wait(150)
    print(hub.imu.heading())
    andar_reto_suave(35, 250)
    b_motor.run_target(120, -60)
    andar_reto_suave(5, 250)
    andar_reto_suave(-7, 200)
    turn(-41, 85)
    andar_reto_suave(11.5, 200)
    turn(42, 85)
    andar_reto_suave(-19, 450)
    andar_reto_suave(15.5, 200)
    turn(-49, 100)
    andar_reto_suave(55, 1000)
    a_motor.run_angle(250, 150)
    wait(100)
    turn(-70, 200)
    print(hub.imu.heading())
    b_motor.run_target(200, -110)
    wait(100)
    b_motor.run_target(250, 0, wait=False)
    turn(65, 200)
    andar_reto_suave(25, 200)
    print((timer.time()) / 1000) 


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

