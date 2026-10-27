from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

axle_lenght = 106#119
wheel_diameter = 49.5#47.7
Rotprecision = 2
Accprecision = 2

parem_mootor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
vasak_mootor = Motor(Port.F, Direction.CLOCKWISE)
tooriist_parem = Motor(Port.E, Direction.CLOCKWISE, gears=None,reset_angle=True)
tooriist_vasak = Motor(Port.B)

#sensor = ColorSensor(Port.C)

db = DriveBase(vasak_mootor, parem_mootor, wheel_diameter, axle_lenght)
#db.use_gyro(True)
db.settings(500, 1500, 400, 400)


def getColor():
    return sensor.color()

def banatree():
    db.straight(173)
    db.turn(-50)
    db.straight(217)
    tooriist_parem.run_angle(150,50)
    #db.settings(300, 300)
    db.straight(-500)
    #db.settings(500, 1500)
    tooriist_parem.run_angle(1000,-50)
    return

def drone():
    db.settings(300, 1000, 600, 1000)
    db.straight(685)
    db.turn(90)
    db.straight(-100)
    db.turn(-70)
    db.settings(700,1500, 400, 400)
    db.straight(-750)
    return

def bigtree():
    tooriist_parem.run_angle(100,100)
    wait(1000)
    resetParem(400, 0)
    return

def antleaf():
    #db.straight(800)
    #db.turn(50)
    #db.straight(80)
    tooriist_vasak.run_angle(50, -32, Stop.BRAKE)
    wait(1000)
    resetVasak(50)
    return

def resetParem(speed=600, angle=45):
    tooriist_parem.run_target(speed, angle)
    return

def resetVasak(speed=600, angle=45):
    tooriist_vasak.run_target(speed, angle)
    return

wait(100)
resetParem(600,0)
bigtree()