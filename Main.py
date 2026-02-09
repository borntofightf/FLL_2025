
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
    wait(400)
    turn(-46.8, 100)
    print(hub.imu.heading())
    wait(400)
    andar_reto_suave(9,300)
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
    a_motor.run_angle(1000,1500,wait=False)
    andar_reto_suave(-93, 800)
    
    andar_reto_suave(-7, 100)
    
    wait(150)
    
    b_motor.run_target(100, -140,wait=False)
    andar_reto(4.4, 100)
    

    turn(-91,110)
    a_motor.run_angle(1000,500)
    andar_reto(4.8,50)

    a_motor.run_angle(900,100,wait=False)
    b_motor.run_target(100, -120,wait=False)
    wait(200)
    andar_reto(4.3,50)
    

    
    a_motor.run_angle(-1000,225,wait=False)
    b_motor.run_target(150, -50,wait=False)

   
    wait(800)
    b_motor.run_target(500, -110)
    andar_reto_suave(-11, 200)
    a_motor.run_angle(-1000,1000,wait=False)
    drive_base.turn(84)
    
    left_motor.run_time(1000,2200,wait=False)
    right_motor.run_time(925,2200)

def saida_3():
    timer = StopWatch()
    timer.reset()   
    """Missão M12: Operação de Resgate"""
    b_motor.run_target(1000, -0,wait=False)
    andar_reto_suave(48,600)
    a_motor.control.limits(acceleration=1000)
    a_motor.run_time(-1100,950,wait=False)
    wait(400)
    andar_reto_suave(-6, 600)
    b_motor.run_target(300, -143)
    print((timer.time()) / 1000) 
    andar_reto_suave(-20, 1000)
    b_motor.run_target(1000, -0,wait=False)
    andar_reto_suave(-25, 1000)
    


def saida_4():
    timer = StopWatch()
    timer.reset()  
    """Missões M10: Desequilíbrio da Balança, M11: Pesca de Artefatos"""
    b_motor.run_target(500, 0, wait=False)
    andar_reto_suave(44, 700)

    print(hub.imu.heading())
    b_motor.run_target(500, -130)

    left_motor.run_angle(100,53)
    andar_reto_suave(2, 500)
    print(hub.imu.heading())
    b_motor.run_target(500, -60)
    
    left_motor.run_angle(-200,30)
    andar_reto_suave(-10, 1000)
    
    print((timer.time()) / 1000)


def saida_5():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""
    timer = StopWatch()
    timer.reset()  
    b_motor.run_target(100, -0, wait=False)
  
    drive_base.settings(turn_rate=200)
    drive_base.curve(255,-91)
    andar_reto(37.2, 300)
    print(hub.imu.heading())
    turn(-89, 200)
    andar_reto(8.5, 200)
    right_motor.run_time(200,260)
    a_motor.run_time(1000,2400)
    right_motor.run_time(-200,250)
    
    andar_reto_suave(-7, 500)
    
    turn(-90, 200)
    andar_reto(11.5, 500)
    turn(-88.5, 200)


    andar_reto_suave(6.3, 300)
    b_motor.run_target(1000, -120)
    b_motor.run_target(500, -80, wait=False)
    andar_reto_suave(-8.5, 300)
    turn(30, 300)
    andar_reto_suave(8, 500)
    b_motor.run_target(400, -135)
    andar_reto_suave(-8, 600)
    b_motor.run_target(500, 0, wait=False)
    turn(60, 300)
    print((timer.time()) / 1000)
    andar_reto_suave(78, 800)
   

def saida_6():
    """Missões M5: Quem Viveu Aqui?, M6: Forja, M7: Levamento de Peso"""

    b_motor.run_target(800, -45, wait=False)
    a_motor.run_time(-1000, 250, wait=False)


    andar_reto_suave(-1, 500)

    andar_reto_suave(40.4, 300)
    b_motor.run_target(700, -140)
    wait(300)
    b_motor.run_target(200, -50)
    b_motor.run_target(800, -140)
    wait(350)
    b_motor.run_target(200, -50)
    b_motor.run_target(800, -140)
    wait(300)
    b_motor.run_target(200, -30)
    b_motor.run_target(900, -140)
    b_motor.run_target(100, -10)
    
    andar_reto(31, 240)
    
    turn(-19.5, 400)
    andar_reto(7.5, 180)
    turn(-23, 900)
    andar_reto_suave(-7.5, 200)
    turn(-54.5, 250)


    andar_reto_suave(-16,300)
    a_motor.run_angle(1000, 320)
    andar_reto_suave(-12,900)
    a_motor.run_angle(-400, 190,wait=False)
    andar_reto_suave(5,300)
    wait(600)
    b_motor.run_target(100, -5)
    andar_reto_suave(-14.5,800)
    a_motor.run_angle(-500, 100,wait=False)
   
    turn(100, 600)
  


def saida_7():
    """Missões M3: Exploradora de Minas, M13: Reconstrução da Estátua, M14: Fórum, M15: Marcação do Sítio Arqueológico"""
  
    b_motor.run_target(100, -80,wait=False)
    andar_reto_suave(34, 200)
    wait(200)
    drive_base.settings(turn_rate=200)
    drive_base.curve(290,-47.5)
    andar_reto_suave(36.5, 200,wa=False)
    wait(1475)
    b_motor.run_target(100, -59)
    andar_reto(-8.5, 150)
    turn(-43, 200)
    andar_reto(19, 200)
    turn(44, 100)
    andar_reto_suave(-18, 250)
    turn(-13, 600)
    andar_reto_suave(-2, 200)

    andar_reto_suave(14.5, 300)
    turn(-50, 600)
   
    
    andar_reto(48.5, 500)
  
    turn(-71, 350)
    b_motor.run_target(300, -125)
    wait(170)
    andar_reto(-3, 500)
    b_motor.run_target(150, -59, wait=False)
    a_motor.run_angle(8000,360,wait=False)
    andar_reto(9.5, 800)

    
    andar_reto(-10, 500)
    
    turn(70, 350)
    andar_reto(-35, 500)




def blibioteca():
    """lugar onde voce pode ver seus movimentos basicos e preder a usalos"""
    # Os codigos são executados de cima pra baixo
    #PONTENCIAS DE 1000 á 0
                    
    andar_reto_suave(10,200) # ANDAR RETO POR 20 CMS COM POTENCIA DE 200
    andar_reto_suave(-10,200) # ANDAR PRA TRAS POR 20 CMS COM POTENCIA DE 200

    turn(90,200)#girar pra direita até 90 graus
    turn(-90,200)#girar pra direita até 90 graus
    
    a_motor.run_target(325, -105)#garra com engrenagem, mover ate certo grau 
    a_motor.run_time(300, -105)# mover a garra por certo tempo

    b_motor.run_target(325, -105)#garra da direita, mover ate certo grau 
    b_motor.run_time(300, -105)# mover a garra por certo tempo

def saida_IS():
    """aqui voce vai testar seus codigos"""
    #missões
    andar_reto_suave(58,200)
    turn(20,200)
    b_motor.run_target(325, -135)
    turn(10, 200)
    b_motor.run_target(325, 0)
    turn(-36,200)
    andar_reto_suave(18,200)
    right_motor.run_angle(250,300)
    right_motor.run_angle(250,-300)
    andar_reto_suave(-3,200)
    turn(85,200)
    andar_reto_suave(8,200)
    a_motor.run_time(530, 800)
    andar_reto_suave(30,200)

    



    #missão 1, fazer o robo girar 90 e 45 graus
    
    #missão 2, fazer o robo andar pra frente e pra tras
    #missão 3, mover a garra
    #tentar efetuar uma saida


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

