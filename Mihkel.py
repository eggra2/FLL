from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(
    top_side=Axis.Z,
    front_side=Axis.X)

axle_lenght = 140
wheel_diameter = 49.5

parem_mootor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
vasak_mootor = Motor(Port.F, Direction.CLOCKWISE)
tooriist_parem = Motor(Port.B, Direction.COUNTERCLOCKWISE)
tooriist_vasak = Motor(Port.A)

#sensor = ColorSensor(Port.C)
db = DriveBase(parem_mootor, vasak_mootor, wheel_diameter, axle_lenght)
db.use_gyro(True)
db.settings(
    straight_speed=500,
    straight_acceleration=1500,
    turn_rate=400,
    turn_acceleration=400)


def getColor():
    return sensor.color()

def resetParem(speed=600, angle=45):
    tooriist_parem.run_target(speed, angle)
    return

def resetVasak(speed=600, angle=45):
    tooriist_vasak.run_target(speed, angle)
    return

def resetRiist(speed=400,angle=0):
    tooriist_parem.run_target(speed,angle,wait=False)
    tooriist_vasak.run_target(speed,angle,wait=False)
    while not (tooriist_parem.done() and tooriist_vasak.done()):
        pass
    return

def banatree():
    db.straight(173)
    db.turn(50)
    db.straight(217)
    tooriist_parem.run_angle(150,50)
    #db.settings(300, 300)
    db.straight(-500)
    #db.settings(500, 1500)
    tooriist_parem.run_angle(1000,-50)
    return

def drone():
    db.settings(
    straight_speed=300,
    straight_acceleration=1000,
    turn_rate=600,
    turn_acceleration=1000)
    db.straight(713)
    db.turn(-50)
    db.turn(50)
    db.settings(700,1500, 400, 400)
    db.straight(-700)
    return

def bigtree():#Starting pos on all vasakult 4 ruut(parem külg)
    db.straight(150)
    db.turn(45)
    db.straight(200)
    db.turn(-47)
    db.straight(390)
    wait(200)
    tooriist_parem.run_angle(999, 250,wait=False)
    tooriist_vasak.run_angle(999,250)
    wait(200)
    resetRiist()
    return

def antleaf():
    return

def test():
    tooriist_parem.dc(-100)
    tooriist_vasak.dc(-100)
    wait(300)
    resetRiist()
    return

wait(300)
drone()
