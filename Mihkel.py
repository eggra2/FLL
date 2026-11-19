from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(
    top_side=Axis.Z,
    front_side=Axis.X)


axle_lenght = 123.8#140#133.7
wheel_diameter = 49.2

parem_mootor = Motor(Port.B, Direction.CLOCKWISE,profile=7)#profile on mitu kraadi see saab off olla. default 11
vasak_mootor = Motor(Port.F, Direction.COUNTERCLOCKWISE,profile=7)
tooriist_parem = Motor(Port.A,profile=8)
tooriist_vasak = Motor(Port.E,profile=8)

#sensor = ColorSensor(Port.C)
db = DriveBase(vasak_mootor, parem_mootor, wheel_diameter, axle_lenght)
db.use_gyro(True)
db.settings(
    straight_speed=400,#max 432, saab panna 450
    straight_acceleration=1500,#max 5000
    turn_rate=400,#max 370, saab panna 400
    turn_acceleration=600)#max 5000

def resetParem(speed=600, angle=0):
    """Resets parem tooriist to zero angle"""
    tooriist_parem.run_target(speed, angle)
    return

def resetVasak(speed=600, angle=0):
    """Resets vasak tooriist to zero angle"""
    tooriist_vasak.run_target(speed, angle)
    return

def resetRiist(speed=400,angle=0):
    """Resets both tooriist motors to zero angle"""
    tooriist_parem.run_target(speed,angle,wait=False)
    tooriist_vasak.run_target(speed,angle,wait=False)
    while not (tooriist_parem.done() and tooriist_vasak.done()):
        pass
    return

def zerovasaktooriist(speed=200):
    """Sets the motor's zero angle to mechanical endpoint"""
    vasak_mootor.reset_angle(vasak_mootor.run_until_stalled(speed,duty_limit=30))
    return

def zeroparemtooriist(speed=200):
    """Sets the motor's zero angle to mechanical endpoint"""
    parem_mootor.reset_angle(parem_mootor.run_until_stalled(speed,duty_limit=30))
    return

def waitforButtonPress():
    """Waits for Center button press to proceeed."""
    while not any(hub.buttons.pressed()):
        wait(10)
        pass
    return

def banatree():
    """deprecated, use run1"""
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
    """deprecated, use run1"""
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

def run2():#Starting pos on all vasakult 4 ruut(parem külg)
    """Root ja BigTree. Punane X=7 Y=0"""
    db.settings(
        straight_speed=400,#max 432, saab panna 450
        straight_acceleration=900,#max 5000
        turn_rate=300,#max 370, saab panna 400
        turn_acceleration=400)#max 5000
    #tooriist_vasak.run_angle(200,-130)
    db.straight(100)
    db.turn(45)
    db.straight(60)
    db.turn(-45)
    db.straight(555+30)
    #resetRiist()
    return

def antleaf():
    return
#Tööriista alumine osa pikkem/alla poole
def gardenNJungleRoots():
    """Teeb Garden ja JungleRoots. Masin Sinine x telg 8'nda joone peale X=8 Y=0"""
    #Go to compost
    db.straight(51)
    db.turn(-52.5)
    db.straight(570-8)
    db.turn(52.5)
    db.straight(193-10.5+10)
    db.turn(-88)
    #run into compost
    db.settings(straight_acceleration=200,straight_speed=400,turn_rate=400)
    db.straight(50+6)
    db.settings(straight_acceleration=1500,straight_speed=850,turn_rate=400)
    #get back bump and seed
    db.straight(-150)
    db.straight(80)
    db.turn(-137)
    #return to base
    db.straight(620)
    return

def run1():
    """Droon ja banana tree. Start Punane X=0 Y=1"""
    resetRiist()
    waitforButtonPress()
    resetVasak(angle=200)
    db.straight(805)
    wait(200)
    tooriist_parem.run_angle(450, 170)
    tooriist_parem.run_angle(450, -170)
    db.straight(-800)
    resetRiist()
    return

def test():
    """for testing things"""
    tooriist_parem.dc(100)
    wait(200)
    resetRiist()
    return

def ttest():
    """for testing things v2"""
    tooriist_parem.dc(100)
    wait(500)
    resetParem()
    return

wait(100)
#tooriist_vasak.run_angle(200,-130)
#run2()
run1()

"""
Todo:
Program bigtree and root
"""
