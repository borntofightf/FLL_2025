from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor, b_motor,andar_reto, sensor_cor, andar_reto_com_sensor,turn

#Velocidade de Movimento e Curva

velocidade_reta = 620
aceleracao_reta = 500
velocidade_curva = 260
aceleracao_curva = 500
drive_base.settings(straight_speed=velocidade_reta)
drive_base.settings(straight_acceleration=aceleracao_reta)
drive_base.settings(turn_rate=velocidade_reta)
drive_base.settings(turn_acceleration=aceleracao_curva)
drive_base.use_gyro(True)

def saida_1():
    andar_reto_suave(125,250)
    wait(100)
    andar_reto_suave(140,-250)

def saida_2():
    """Missões M9: O que está à venda, M10: Desequilíbrio da Balança, M13: Reconstrução da Estátua"""
    #Inicio das Missões M9: O que está à venda, M10: Desequilíbrio da Balança
    b_motor.run_target(1000, 0, wait=False)
    a_motor.run_time(250,400, wait=False)
    andar_reto_suave(21,150)
    drive_base.turn(48)
    andar_reto_suave(45,150)
    drive_base.turn(5)
    b_motor.run_angle(150, 160, wait=False)
    a_motor.run_time(-200, 1100)
    a_motor.run_time(200, 1900)
    andar_reto_suave(20, -250)
    b_motor.run_target(-150, 0)
    andar_reto(1, 150)
    a_motor.run_time(200, 900, wait=False)
    drive_base.turn(-54)
    andar_reto_suave(68, 150)
    drive_base.turn(48)
    andar_reto(25, 200)
    a_motor.run_time(-100, 1500)
    drive_base.turn(-67)
    andar_reto_suave(100, 250)
    #Fim das Missões M9: O que está à venda, M10: Desequilíbrio da Balança e Inicio da Missão M5: Reconstrução da Estátua
    
def saida_3():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    #Inicio da Missão M1: Escavação Supercial
    b_motor.run_target(300, -125, wait=False)
    andar_reto_suave(88, 100)
    drive_base.turn(-40)
    andar_reto_suave(30, 100)

def saida_4():
    """Missão M12: Operação de Resgate"""
    #Inicio da Missão M12: Operação de Resgate
    b_motor.run_target(1000, 0, wait=False)
    andar_reto_suave(61, 150)
    b_motor.run_target(-1000, 125)
    #Fim da Missão M12: Operação de Resgate
    wait(200)
    andar_reto_suave(65, -350)

def saida_5():
    
    andar_reto_suave(135, 200)
    turn(90, 150)
    a_motor.run_angle(150, 200)
    turn(-4, 150)
    andar_reto_suave(20, 200)
    a_motor.run_angle(-150, 50)
    wait(500)
    andar_reto_suave(20, -200)


# Choose a letter.
selected = hub_menu("1", "2", "3", "4", "5")

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