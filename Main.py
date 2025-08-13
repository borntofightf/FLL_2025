from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor, b_motor,andar_reto

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
    andar_reto_suave(28,150)
    drive_base.turn(48)
    andar_reto_suave(33,150)
    b_motor.run_angle(150, 160, wait=False)
    a_motor.run_time(-350, 1100)
    a_motor.run_time(200, 1100)
    andar_reto_suave(20, -250)
    b_motor.run_target(-150, 0)
    andar_reto_suave(5, 250)
    drive_base.turn(-55)
    andar_reto_suave(105, 250)
    drive_base.turn(48)
    andar_reto(15, 200)
    drive_base.turn(-60)
    andar_reto_suave(100, 250)
    #Fim das Missões M9: O que está à venda, M10: Desequilíbrio da Balança e Inicio da Missão M5: Reconstrução da Estátua
    
def saida_3():
    """Missões M1: Escavação Supercial, M2: Revelação do Mapa"""
    #Inicio da Missão M1: Escavação Supercial
    b_motor.run_target(1000, 0, wait=False)
    andar_reto_suave(97, 150)
    drive_base.turn(-95)
    wait(150)
    andar_reto(13,200)
    a_motor.run_time(500, 400)
    wait(150)
    andar_reto(15,-200)
    drive_base.turn(94)
    wait(100)
    #Fim da Missão M1: Escavação Supercial e Inicio da Missão M2: Revelação do Mapa
    andar_reto_suave(19,350)
    drive_base.turn(-55)
    wait(100)
    andar_reto(13,200)
    andar_reto(2,-200)
    b_motor.run_target(1000, 125)
    andar_reto_suave(14,-250)
    b_motor.run_target(-250, 50, wait=False)
    #Fim da Missão M2: Revelação do Mapa
    drive_base.turn(85)
    andar_reto(80, -1000)

def saida_4():
    """Missão M12: Operação de Resgate"""
    #Inicio da Missão M12: Operação de Resgate
    b_motor.run_target(1000, 0, wait=False)
    andar_reto_suave(61, 150)
    b_motor.run_target(-1000, 125)
    #Fim da Missão M12: Operação de Resgate
    wait(200)
    andar_reto_suave(65, -350)


# Choose a letter.
selected = hub_menu("1", "2", "3", "4")

# Based on the selection, run a program.
if selected == "1":
    saida_1()
elif selected == "2":
    saida_2()
elif selected == "3":
    saida_3()
elif selected == "4":
    saida_4()