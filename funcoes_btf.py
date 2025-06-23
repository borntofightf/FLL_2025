# Funções para a FLL
# Criadores: Deivid e Jean
# Versão: 1.1
# Funções: Andar Reto, Andar Reto com Rampa, Curva

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase


hub = PrimeHub()

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

def andar_reto_com_rampa(cms, pot):
    """Anda reto com rampa de aceleração/desaceleração suave."""
    drive_base.stop()
    reset()
    rampa_tamanho = 7  # cm
    distancia_feita = 0
    wait(150)
    drive_base.use_gyro(True)

    while abs(distancia_feita) < abs(cms):
        distancia_feita = ((abs(left_motor.angle()) + abs(right_motor.angle())) / 2) / graus_por_cm
        limite = 1
        if distancia_feita < rampa_tamanho:
            limite = distancia_feita / rampa_tamanho
        elif cms - distancia_feita < rampa_tamanho:
            limite = (cms - distancia_feita) / rampa_tamanho

        velocidade_base = (pot / 3 + (pot - pot / 3) * exp_aproximada(-3 * (1 - limite))) + 1
        velocidade = velocidade_base * (-1 if pot < 0 else 1)

        # Correção do giroscópio com inversão se for para trás
        erro = hub.imu.heading()
        ganho = 2
        correcao = erro * ganho * (-1 if pot < 0 else 1)

        # Aplicar nos motores
        left_motor.run(velocidade - correcao)
        right_motor.run(velocidade + correcao)

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

    print("feito")

    parar()
