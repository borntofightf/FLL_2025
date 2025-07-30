from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def programa1():
    hub.display.text("Rodando 1")
    wait(2000)

def programa2():
    hub.display.text("Rodando 2")
    wait(2000)

def programa3():
    hub.display.text("Rodando 3")
    wait(2000)

def programa4():
    hub.display.text("Rodando 4")
    wait(2000)

# Lista de programas para facilitar o acesso pelo índice
programas = [programa1, programa2, programa3, programa4]

# Índice atual (0 a 3)
indice = 0

# Loop de seleção
while True:
    hub.display.number(indice + 1)

    # Espera por botão ser pressionado
    while not hub.buttons.pressed():
        wait(10)

    # Quando botão for pressionado
    botoes = hub.buttons.pressed()
    if Button.LEFT in botoes:
        indice = (indice - 1) % 4  # Navega para esquerda
    elif Button.RIGHT in botoes:
        indice = (indice + 1) % 4  # Navega para direita
    elif Button.CENTER in botoes:
        # Executa o programa selecionado
        hub.display.text("Executando")
        programas[indice]()  # Chama a função
        hub.display.clear()

    # Espera botão ser solto antes de continuar
    while hub.buttons.pressed():
        