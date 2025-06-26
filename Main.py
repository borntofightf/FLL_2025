from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.tools import hub_menu
hub = PrimeHub()

from funcoes_btf import andar_reto_suave, curva, reset, drive_base, a_motor, b_motor



#Velocidade de Movimento e Curva

velo_reta = 620
aceleracao_reta = 500
velo_curva = 260
aceleracao_curva = 500
drive_base.settings(straight_speed=velo_reta)
drive_base.settings(straight_acceleration=aceleracao_reta)
drive_base.settings(turn_rate=velo_curva)
drive_base.settings(turn_acceleration=aceleracao_curva)
drive_base.use_gyro(True)

def M1_M2_M3():
    b_motor.run_target(1000, 0, wait=False)
    a_motor.run_angle(-1000, 550, wait=False)
    andar_reto_suave(76, 350)
    drive_base.turn(-95)
    andar_reto_suave(10, 350)
    wait(200)
    a_motor.run_angle(1000, 650)
    andar_reto_suave(15, -350)
    drive_base.turn(94)
    wait(100)
    andar_reto_suave(28,350)
    drive_base.turn(-55)
    wait(100)
    andar_reto_suave(13,350)
    a_motor.run_angle(-1200, 650)
    andar_reto_suave(16,-350)
    wait(100)
    drive_base.turn(67)
    andar_reto_suave(10, 350)
    b_motor.run_target(1000, 40)
    andar_reto_suave(10,-250)
    drive_base.turn(75)
    andar_reto_suave(18,300)
    drive_base.turn(70)
    a_motor.run_angle(1200, 650)
    andar_reto_suave(6,-300)
    drive_base.turn(-70)
    andar_reto_suave(20,-500)
    drive_base.turn(110)
    andar_reto_suave(80, 350)

def M12_areia():
    b_motor.run_target(1000, 0, wait=False)
    andar_reto_suave(55, 200)
    b_motor.run_target(-1000, -115)
    wait(200)
    andar_reto_suave(65, -350)

M1_M2_M3()
