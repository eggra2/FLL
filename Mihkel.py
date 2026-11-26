from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch #voib olla hub_menu

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
    """Waits for any button press to proceeed(except centre)."""
    while not any(hub.buttons.pressed()):
        wait(10)
        pass
    return

#Tööriista alumine osa pikkem/alla poole
def run5vana():
    """Teeb Garden ja JungleRoots. Masin Sinine x telg 8'nda joone peale X=8 Y=0"""
    #Go to compost
    db.straight(51)
    db.turn(-52.5)
    db.straight(565)
    db.turn(52.5)
    db.straight(193.5)
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

def run5():
    """Teeb Garden ja JungleRoots. Masin Sinine x telg 8'nda joone peale X=8 Y=0"""
    #Go to compost
    db.straight(51)
    db.turn(-52.5)
    db.straight(630)
    db.turn(51)
    db.straight(88)
    db.turn(-88)
    #run into compost
    db.settings(straight_acceleration=200,straight_speed=400,turn_rate=400)
    db.straight(65)
    db.settings(straight_acceleration=3000,straight_speed=400,turn_rate=400)
    #get back bump and seed
    db.straight(-170)
    db.settings(straight_acceleration=1800,straight_speed=400,turn_rate=400)
    db.straight(80)
    db.turn(-137)
    #return to base
    db.straight(720)
    return

def run4(): #x=3, y=0, sinine
    #sõida lapse juurde
    db.straight(20)
    db.turn(-15)
    db.straight(685)
    db.turn(54)
    db.straight(140)
    db.stop()
    tooriist_parem.run_angle(100,135)
    tooriist_parem.run_angle(300,-135,wait=False)
    db.straight(-120)
    #tagasi ja ring
    db.turn(-90)
    db.straight(-190)
    db.turn(50)
    db.settings(200)
    db.straight(-300,wait=False)
    wait(1400)
    db.settings(450)
    db.straight(-300)

    return

def run3():
    """Leaves, pushes compost and vert leaves, and puu tugi, x=16 y=0"""
    tooriist_parem.reset_angle(0)
    tooriist_vasak.run_angle(60,58,wait=False)
    tooriist_parem.run_angle(400,-150,wait=False)
    db.straight(770)
    db.turn(-39)
    #pickup leaves
    db.straight(80)
    tooriist_vasak.run_angle(300,170)
    tooriist_vasak.run_angle(200,-210,wait=False)
    #move to compost while dropping leaves
    db.arc(700,-50)
    #drive slowly into compost
    db.settings(straight_speed=175)
    db.straight(-150)
    tooriist_vasak.run_angle(700,210)
    db.settings(straight_speed=400)
    db.straight(100)
    db.settings(straight_speed=300,turn_acceleration=1000,turn_rate=500)
    tooriist_parem.run_angle(100,140,wait=False)
    db.turn(110)
    db.straight(280)
    db.turn(70)
    db.straight(400)
    db.turn(45)
    db.straight(150)
    db.turn(-90)
    db.settings(straight_speed=100)
    db.straight(130)
    db.straight(-2)
    db.turn(6)
    db.settings(straight_speed=400)
    #Loo white cum up
    tooriist_parem.dc(-100)
    wait(200)
    tooriist_parem.stop()
    #mine puu togue juurde
    db.straight(-100)
    db.turn(90,absolute=True)
    tooriist_parem.run_target(600,0,wait=False)
    db.straight(280)
    db.turn(-4)
    db.straight(130)
    #loo puu tuge yles
    tooriist_parem.dc(-100)
    wait(150)
    tooriist_parem.stop()
    tooriist_parem.run_target(600,0)
    db.straight(-60)#-45
    db.turn(29)#30
    wait(500)
    tooriist_parem.dc(-100)
    #tooriist_parem.run_angle(50,-60)
    #tooriist_parem.dc(60)
    wait(200)
    #tooriist_parem.stop()
    tooriist_parem.run_target(600,0)
    db.turn(170,absolute=True)
    db.straight(700)
    return

def run2():#Starting pos on all vasakult 4 ruut(parem külg)
    """Root, BigTree ja Antleaf. Punane X=7 Y=0"""
    db.settings(
        straight_speed=400,#max 432, saab panna 450
        straight_acceleration=900,#max 5000
        turn_rate=300,#max 370, saab panna 400
        turn_acceleration=400)#max 5000
    tooriist_vasak.run_angle(200,-130)
    db.straight(100)
    db.turn(45)
    db.straight(70)
    db.turn(-45)
    db.straight(560+10)
    #L66 root yles
    tooriist_parem.dc(100)
    wait(200)
    tooriist_parem.brake()
    db.straight(-23)
    tooriist_vasak.run_angle(50,150)
    wait(1000)
    tooriist_vasak.run_angle(50,-150)
    #move back
    db.straight(-90)
    db.turn(90)
    db.straight(280-7)
    db.turn(0,absolute=True)
    tooriist_parem.run_until_stalled(-600,duty_limit=16)
    tooriist_parem.run_angle(300,50)
    db.settings(straight_speed=150)
    db.straight(145)
    db.turn(7)
    tooriist_parem.run_angle(300,50)
    db.turn(-7)
    db.settings(straight_speed=300)
    db.straight(-70)
    db.straight(220)
    tooriist_parem.run_angle(300,100)
    db.straight(70)
    wait(400)
    db.straight(-200)
    return

def run1():
    """Droon ja banana tree. Start Punane X=4 Y=0
        Pullback tomba punansestjoonest hiina seinani x2"""
    db.settings(straight_speed=300)
    #resetParem()
    #waitforButtonPress()
    #resetVasak(angle=180)
    db.straight(800-100)#-10
    wait(200)
    tooriist_parem.run_until_stalled(450,duty_limit=50)
    tooriist_parem.run_angle(450, -150)
    db.straight(-700,wait=False)
    wait(600)
    tooriist_parem.run_angle(450,120,wait=False)
    db.straight(-500)
    db.stop()

    # X=16 now bananatree
    waitforButtonPress()
    tooriist_parem.run_angle(600,-240,wait=False)
    wait(500)
    tooriist_vasak.run_until_stalled(-400,duty_limit=20)
    wait(200)
    tooriist_vasak.run_angle(300,70,wait=False)
    db.arc(400,distance=410)
    tooriist_vasak.run_angle(200,80,wait=False)
    db.settings(straight_speed=120)
    db.straight(-150)
    db.settings(straight_speed=400)
    db.straight(-400)
    return

def test():
    """for testing things"""
    tooriist_parem.dc(-70)
    wait(10000)
    return

def ttest():
    """for testing things v2"""
    return

"""Call functions here"""

#test()
#ttest()
#run2()
run4alt()
"""
Todo:
Program bigtree and root(run 2)
"""
