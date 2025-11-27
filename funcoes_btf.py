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
drive_base = DriveBase(left_motor, right_motor, 60, 109)

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

def exp_aproximada(x):
    """Calcula uma exponencial aproximada para rampas."""
    termo = 1
    soma = 1
    for i in range(1, 6):
        termo *= x / i
        soma += termo
    return soma

# ---------------- Funções principais ----------------

def andar_reto(cms, pot):
    """Anda reto em linha com velocidade constante."""
    drive_base.stop()
    reset()
    drive_base.settings(straight_acceleration=500,straight_speed=pot)
    distancia_feita = 0
    parar()
    wait(150)
    drive_base.use_gyro(True)
    drive_base.straight(cms*10)

    parar()

def andar_reto_suave(cm, pot):
    """Anda reto com rampa de aceleração/desaceleração suave."""
    drive_base.settings(straight_speed=pot)
    drive_base.settings(straight_acceleration=300)
    parar()
    wait(100)
    drive_base.use_gyro(True)
    drive_base.straight(cm*10)
    
def turn(graus, potencia):    
    velocidade_curva = potencia
    aceleracao_curva = 600
    parar()
    wait(150)
    drive_base.settings(turn_rate=velocidade_curva)
    drive_base.use_gyro(True)
    drive_base.turn(graus)

def curva(graus, potencia):    
    velocidade_curva = potencia
    aceleracao_curva = 600
    parar()
    wait(100)
    drive_base.settings(turn_rate=velocidade_curva)
    drive_base.use_gyro(True)
    drive_base.arc(20, angle=graus)


