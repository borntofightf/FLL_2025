from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, reset, drive_base, a_motor, b_motor,andar_reto,turn, left_motor, right_motor,turn2

#Velocidade de Movimento e Curva

drive_base.use_gyro(True)
timer = StopWatch()

def saida_1():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    timer = StopWatch()
    timer.reset()      
    andar_reto_suave(79,500)
    wait(400)
    turn(-46.7, 125)
    andar_reto(-2,300)
    print(hub.imu.heading())
    wait(800)
    andar_reto(11,450)
    andar_reto_suave(-3.5,150)
    b_motor.run_target(1000, -143)
    andar_reto_suave(4,700)
    andar_reto_suave(-6.5,350)
    b_motor.run_target(1000, -110)
    b_motor.run_target(100, -80,wait=False)
    andar_reto_suave(-10,150)
    b_motor.run_target(300, -90,wait=False)
   
    print("S1")
    turn(-46, 200)
    print(hub.imu.heading())
    andar_reto_suave(12.5,400)
    a_motor.run_time(1000,1000,wait=False)
    wait(300)
    andar_reto_suave(-5,600)
    turn(-80, 250)
    
    drive_base.settings(turn_rate=1000)
    drive_base.curve(1050,30)
    print((timer.time()) / 1000) 


def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    andar_reto_suave(1, 200)
    drive_base.reset()
    drive_base.stop()
    hub.imu.reset_heading(0)
    a_motor.run_angle(1000,1500,wait=False)
    b_motor.run_target(100, -40,wait=False)
    andar_reto_suave(-93, 800)
    andar_reto_suave(-7, 100)
    wait(250)
    b_motor.run_target(100, -133,wait=False)
    andar_reto(4.3, 80)
    wait(200)
    turn(-90.8,125)
    print(hub.imu.heading())
    a_motor.run_angle(1000,500)
    andar_reto(4.8,50)
    a_motor.run_angle(900,110,wait=False)
    b_motor.run_target(100, -120,wait=False)
    wait(200)
    turn2(-0.2,30)
    print(hub.imu.heading())
    andar_reto(4.9,50)
    
    a_motor.run_angle(-1000,210,wait=False)
    b_motor.run_time(200, 440)
    wait(600)
    andar_reto(-2,100)
    b_motor.run_target(300, -110)
    andar_reto_suave(-9, 200)
    a_motor.run_angle(-1000,1000,wait=False)
    turn(83,300)
    b_motor.run_target(300, -80,wait=False)
    
    left_motor.run_time(1000,2200,wait=False)
    right_motor.run_time(910,2200)

def saida_3(): 
    """Missão M12: Operação de Resgate"""
    b_motor.run_target(1000, -0,wait=False)
    andar_reto_suave(48,600)
    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1100,950,wait=False)
    wait(400)
    andar_reto_suave(-6, 600)
    b_motor.run_target(400, -143)

    andar_reto_suave(-20, 1000)
    b_motor.run_target(1000, -0,wait=False)
    andar_reto_suave(-25, 1000)
    

def saida_4():  
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(44, 700)
    b_motor.run_target(500, -130)

    left_motor.run_angle(130,50)
    andar_reto_suave(2, 500)
    print(hub.imu.heading())
    b_motor.run_target(390, -60)
    turn(5,200)
    andar_reto_suave(-13, 1000)



def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    drive_base.reset()
    b_motor.run_target(100, -0, wait=False)
    andar_reto_suave(-0.5, 500)
    drive_base.stop()
    hub.imu.reset_heading(0)
    drive_base.settings(turn_rate=200)
    drive_base.curve(250,-90)
    turn2(-90,28)
    print(hub.imu.heading())
    andar_reto(38.7, 300)
    print(hub.imu.heading())
    turn(-90.3, 200)
    andar_reto(7.5, 150)
    right_motor.run_time(200,200)
    a_motor.run_time(1000,2300)
    right_motor.run_time(-200,250)
    andar_reto(-7, 400)
    turn2(-89.5, 30)
    print(hub.imu.heading())
    andar_reto(11.5, 400)
    turn(-89, 200)
    andar_reto(7, 300)
    andar_reto(-1, 500)
    b_motor.run_target(1000, -120)
    b_motor.run_target(500, -80, wait=False)
    andar_reto_suave(-8.5, 300)
    turn(30, 300)
    andar_reto_suave(8, 500)
    b_motor.run_target(400, -133)
    andar_reto_suave(-8, 600)
    b_motor.run_target(500, 0, wait=False)
    turn(63, 300)

    andar_reto(75, 800)
   

def saida_6():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    b_motor.run_target(200, -10, wait=False)
    
    andar_reto(40, 600)
    b_motor.run_target(650, -140)
    
    wait(300)
    b_motor.run_target(200, -50)
    b_motor.run_target(700, -140)

    wait(350)
    b_motor.run_target(350, -50)
    b_motor.run_target(800, -140)
    wait(300)
    b_motor.run_target(350, -30)
    b_motor.run_target(900, -140)

    b_motor.run_target(300, -10,wait=False)
    andar_reto(-27, 800)
    
def saida_7():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    b_motor.run_target(150, -10, wait=False)
    a_motor.run_time(1000, 250, wait=False)
    andar_reto_suave(-0.5, 300)
    
    drive_base.reset()
    wait(150)
    a_motor.run_time(-500, 500, wait=False)
    andar_reto(66, 400)
    a_motor.run_time(-500, 850)
    andar_reto(8,250)
    a_motor.run_time(800, 900)
    andar_reto_suave(-2, 200)
    right_motor.run_angle(250,80)
    andar_reto(1.5,500)
    right_motor.run_angle(400,88)
    andar_reto(-6,500)
    turn(-63, 100)
    andar_reto_suave(-26, 800)
    drive_base.settings(turn_rate=150)
    drive_base.curve(310,-100) 
    andar_reto_suave(28, 800) 
    
    
    
  


def saida_8():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
    b_motor.run_target(50, -79,wait=False)
    andar_reto(-0.5, 150)
    drive_base.stop()
    hub.imu.reset_heading(0)
    drive_base.reset()
    drive_base.use_gyro(True)
    wait(150)

    andar_reto(38, 175)
    print(hub.imu.heading())
    
    drive_base.settings(turn_rate=200,turn_acceleration=150)
    drive_base.curve(200,-47.5)
    wait(150)
    turn2(-47.5, 30)
    wait(300)
    print(hub.imu.heading())
    b_motor.run_target(50, -79,wait=False)
    andar_reto(35.1, 250,wa=False)
    wait(1500)
    b_motor.run_target(100, -59)
    andar_reto(-6, 200)
    drive_base.use_gyro(True)
    drive_base.settings(turn_rate=200,turn_acceleration=150)
    drive_base.curve(-85,44)
    turn2(-44,30)
    andar_reto(74.4, 700)
    turn(-70, 350)
    andar_reto(5, 500)
    b_motor.run_target(300, -120)
    wait(170)
    b_motor.run_target(300, -112, wait=False)
    andar_reto(-3.8, 500)
    b_motor.run_target(50, -55, wait=False)
    a_motor.run_angle(-8000,360)
    andar_reto(8, 800)
    andar_reto(-10, 500)
    turn(72,350)
    andar_reto(-52.4, 1000)
    turn(42,300)
    drive_base.settings(straight_acceleration=450,straight_speed=300)
    drive_base.use_gyro(False)
    drive_base.straight(-17*10)
    wait(400)

    andar_reto(9, 1000)





# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5", "6", "7","8")

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
    saida_7()
elif selected == "7":
    saida_6()
elif selected == "8":
    saida_8()