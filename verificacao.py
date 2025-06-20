from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

try:
    motor = Motor(Port.A)
    motor.run_angle(500, 90)
except ValueError:
    print("Erro de valor: verifique os parâmetros passados.")
except OSError:
    print("Erro de hardware: confira a conexão do motor.")
except Exception as e:
    print("Erro inesperado:", e)