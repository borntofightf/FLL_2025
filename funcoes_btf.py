# Funções para a FLL
# Criadores: Deivid e Jean
# Versão: 1.1
# Funções: Andar Reto, Andar Reto com Rampa, Curva

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port,Axis
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
drive_base = DriveBase(left_motor, right_motor, 62, 105)

# Limites de controle dos motores
left_motor.control.limits(1000, 2500, 200)
right_motor.control.limits(1000, 2500, 200)
graus_por_cm = 19.5
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
    distancia_feita = 0
    wait(150)
    drive_base.use_gyro(True)

    while abs(distancia_feita) < abs(cms):

        distancia_feita = ((abs(left_motor.angle()) + abs(right_motor.angle())) / 2) / graus_por_cm
        drive_base.drive(pot, 0-hub.imu.heading())

    parar()

def andar_reto_suave(cm, pot):
    """Anda reto com rampa de aceleração/desaceleração suave."""
    drive_base.stop()
    reset()
    graus_cms = 19.5
    rampa_tamanho = 7
    distancia_feita = 0
    wait(150)
    drive_base.use_gyro(True)

    while not abs(distancia_feita) > abs(cm):
        distancia_feita = (abs(left_motor.angle()) + abs(right_motor.angle()) / 2) / graus_cms
        correção = hub.imu.heading() * -1
        direcao = 1
        limite = 1

        if pot < 0:
            direcao = -1
        if distancia_feita < rampa_tamanho:
            limite = distancia_feita / rampa_tamanho
        if cm - distancia_feita < rampa_tamanho:
            limite = (cm - distancia_feita) / rampa_tamanho

        drive_base.drive(pot/3 + ( pot - pot/3) * (exp_aproximada(-3 * (1 - limite) + 1)), hub.imu.heading()*2)
        
    parar()

def curva(graus, pot, motores="Par"):
    """Gira o robô com precisão com base no giroscópio."""
    reset()
    wait(200)
    drive_base.use_gyro(True)

    pot = abs(pot) * (1 if graus > 0 else -1)

    while abs(hub.imu.heading()) < abs(graus):
        if motores == "Par":
            left_motor.run(pot)
            right_motor.run(-pot)
        elif motores.upper() == "E":
            left_motor.run(pot)
        elif motores.upper() == "D":
            right_motor.run(pot)

andar_reto_suave(180, 350)
drive_base.turn(180)
andar_reto_suave(180, 350)