# Funções para a FLL
# Criadores: Deivid e Jean
# Versão: 1.1
# Funções: Andar Reto, Andar Reto com Rampa, Curva

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port,Axis, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase


hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)

# Motores principais
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

# Motores adicionais
a_motor = Motor(Port.A)
b_motor = Motor(Port.B)


# DriveBase configurado
drive_base = DriveBase(left_motor, right_motor, 60, 115)

# Limites de controle dos motores

velocidade_curva = 260
aceleracao_curva = 455
drive_base.settings(turn_rate=velocidade_curva)
drive_base.settings(turn_acceleration=aceleracao_curva)
graus_por_cm = 18.94
drive_base.use_gyro(True)

# ---------------- Funções auxiliares ----------------

def reset():
    """Reseta giroscópio e ângulo dos motores."""
    hub.imu.reset_heading(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def parar():
    """Segura os motores principais."""
    left_motor.hold()
    right_motor.hold()



# ---------------- Funções principais ----------------

def andar_reto(cms, pot,wa=True):
    """Anda reto em linha com velocidade constante."""
    drive_base.stop()
    reset()
    drive_base.settings(straight_acceleration=450,straight_speed=pot)
    drive_base.use_gyro(True)
    
    drive_base.straight(cms*10,wait=wa)


def andar_reto_suave(cm, pot,wa=True):
    """Anda reto com rampa de aceleração/desaceleração suave."""
    drive_base.settings(straight_speed=pot)
    drive_base.settings(straight_acceleration=400)
    parar()
    wait(100)
    drive_base.use_gyro(True)
    drive_base.straight(cm*10,wait=wa)
    
def turn(graus, potencia):    
    velocidade_curva = potencia
    aceleracao_curva = 300
    parar()
    wait(150)
    drive_base.settings(turn_rate=velocidade_curva,turn_acceleration=aceleracao_curva)
    drive_base.use_gyro(True)
    drive_base.turn(graus)



def turn2(graus, potencia):    
    velocidade_curva = potencia
    aceleracao_curva = 300
    parar()
    wait(150)
    drive_base.settings(turn_rate=velocidade_curva,turn_acceleration=aceleracao_curva)
    drive_base.use_gyro(True)
    drive_base.turn(graus)

