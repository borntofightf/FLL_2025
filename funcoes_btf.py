# ==========================================================
# 🧠 Funções para a FLL
# ----------------------------------------------------------
# Criadores: Deivid e Jean
# Versão: 10.1
# Funções disponíveis:
#   - Andar reto com aceleração suave
#   - Curvar com giroscópio e compensação de inércia
#   - Reset e parada segura de motores
# ==========================================================

# ------------------ Importações ---------------------------
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Axis, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# ------------------ Configuração Inicial ------------------
# Inicializa o hub e define orientações
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)

# Motores principais do drive base
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

# Motores adicionais (braços ou acessórios)
a_motor = Motor(Port.A)
b_motor = Motor(Port.B)

# Configuração da base motriz
# Parâmetros:
#   60  -> diâmetro da roda (mm)
#   110 -> distância entre rodas (mm)
drive_base = DriveBase(left_motor, right_motor, 60, 110)

# Configurações iniciais de movimento
velocidade_curva = 260
aceleracao_curva = 455
drive_base.settings(turn_rate=velocidade_curva, turn_acceleration=aceleracao_curva)

# Constante de conversão (1 cm ≈ 18.94 graus dos motores)
graus_por_cm = 18.94

# Habilita o uso do giroscópio por padrão
drive_base.use_gyro(True)

# ==========================================================
# 🔧 Funções auxiliares
# ==========================================================

def reset():
    """Reseta o giroscópio e os ângulos dos motores principais."""
    hub.imu.reset_heading(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)


def parar():
    """Faz o robô parar com precisão, mantendo os motores travados."""
    left_motor.hold()
    right_motor.hold()


# ==========================================================
# 🚗 Funções principais de movimento
# ==========================================================

def andar_reto_suave(cm, pot, acele=445, usar_gyro=True):
    
    """
    Move o robô em linha reta com aceleração e desaceleração suaves.

    Parâmetros:
        cm (float): distância em centímetros (positiva = frente, negativa = trás)
        pot (int): velocidade máxima do movimento
        acele (int): aceleração linear (padrão = 445)
        usar_gyro (bool): define se o giroscópio deve ser usado para manter a reta
    """
    drive_base.settings(straight_speed=pot, straight_acceleration=acele)
    hub.imu.reset_heading(0)
    drive_base.use_gyro(usar_gyro)
    parar()
    wait(100)
    drive_base.straight(cm * 10)  # Conversão de cm para mm


def turn(graus, potencia, acele=600):
    """
    Realiza uma curva precisa usando o giroscópio, com compensação de inércia.

    Parâmetros:
        graus (float): ângulo de rotação (+ direita, - esquerda)
        potencia (int): velocidade da curva
        acele (int): aceleração da curva (padrão = 600)
    """
    fator_compensacao = 0.97 
    hub.imu.reset_heading(0) # Reduz 3% do giro para evitar ultrapassagem do alvo
    drive_base.use_gyro(True)
    parar()
    wait(100)
    drive_base.settings(turn_rate=potencia, turn_acceleration=acele)
    drive_base.turn(graus * fator_compensacao)
