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
    #Inicio da Missão M1: Escavação Supercial
    b_motor.run_target(1000, -88, wait=False)
    andar_reto_suave(70,300)
    wait(300)
    drive_base.turn(-40)
    andar_reto_suave(5,200)
    drive_base.turn(2)
    andar_reto_suave(5,200)
    b_motor.run_target(150, 0)
    andar_reto_suave(-14,500)
    drive_base.turn(-50)
    wait(100)
    
    andar_reto_suave(12,80)

    a_motor.run_time(-1000,1000)
    andar_reto_suave(-9,900)
    drive_base.turn(-70)
    andar_reto_suave(70,1000)


    
def saida_2():
    """Missões M3: Exploradora de Minas, M4: Extração Segura"""
    #Inicio das Missões M3: Exploradora de Minas, M4: Extração Segura

    a_motor.run_time(-1000,1200,wait=False)

    wait(100)
    andar_reto_suave(-100, 250)
    b_motor.run_target(1000, -140, wait=False)
    andar_reto_suave(6.5, 80)
    drive_base.turn(-89)
    wait(200)
    andar_reto_suave(9, 80)
    a_motor.run_time(1000,700)
    b_motor.run_target(150, -75)
    wait(500)
    b_motor.run_target(150, -140)
    andar_reto_suave(-18, 150)
    drive_base.turn(90)
    andar_reto_suave(60, 1000)
    drive_base.turn(30)
    andar_reto_suave(30, 1000)

def saida_3():
    """Missão M12: Operação de Resgate"""
    #Inicio da Missão M12: Operação de Resgate
    andar_reto_suave(45, 150)
    andar_reto(14, 100)
    wait(100)
    drive_base.turn(2)
    andar_reto(23, -100)
    andar_reto(10, 100)
    left_motor.run_time(200, 400)
    andar_reto(90, -250)

def saida_4():
    """Missão M11: Pesca de Artefatos"""
    #Inicio da Missão M11: Pesca de Artefatos
    andar_reto_suave(30, 150)
    drive_base.turn(89)
    andar_reto_suave(68, 250)
    drive_base.turn(90)
    andar_reto_suave(11,350)
    drive_base.turn(-3)
    a_motor.run_time(1000,4000)
    drive_base.turn(10)
    andar_reto_suave(-10,400)
    drive_base.turn(-80)
    andar_reto_suave(100,1000)
    

    

def saida_5():
    """Missões M9: O que está à venda, M10: Desequilíbrio da Balança, M13: Reconstrução da Estátua"""
    #Inicio das Missões M9: O que está à venda, M10: Desequilíbrio da Balança
    b_motor.run_target(1000, 0, wait=False)
    
    andar_reto_suave(19,150)
    
    drive_base.turn(44)
    wait(100)
    andar_reto_suave(33,200)
    b_motor.run_target(300, -109)
    b_motor.hold()
    a_motor.run_time(-1000, 700)
    a_motor.run_time(800, 1900)
    andar_reto_suave(-22, 600)
    andar_reto_suave(11, 200)
    b_motor.run_target(-150, 0)
    andar_reto_suave(-50, 800)

def saida_6():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    #Inicio das Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso
    andar_reto_suave(72, 300)
    right_motor.run_angle(300, 270)
    andar_reto_suave(-12, 200)
    left_motor.run_angle(-300, 100)
    andar_reto_suave(-32,300)
    drive_base.turn(90)
    a_motor.run_angle(-500, 400)
    andar_reto_suave(10, 250)
    a_motor.run_angle(500, 650)
    left_motor.run_angle(-300, 70)
    andar_reto_suave(-10, 200)


def saida_7():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    #Inicio das Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso
    b_motor.run_target(1000, -58, wait=False)
    andar_reto_suave(59, 300)
    drive_base.turn(-46)
    andar_reto_suave(35, 300)
    b_motor.run_target(400, 0)
    andar_reto_suave(-8.5, 300)
    drive_base.turn(-43)
    andar_reto_suave(75, 300)
    drive_base.turn(-90)
    
    andar_reto_suave(8, 300)
    drive_base.turn(-20)
    andar_reto_suave(3, 300)
    a_motor.run_time(1000,1000)
    andar_reto_suave(5, 700)
    andar_reto_suave(-15, 300)
    b_motor.run_target(200, -120)
    andar_reto_suave(-15, 300)
    
    


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