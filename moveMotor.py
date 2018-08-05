import RPi.GPIO as gpio
import time


def runMotor(Steps = 4048, WaitTime = .17/float(1000)):
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    # PINS
    orange = 4 # BCM 4, Pin 7
    yellow = 17 # BCM 17, Pin 11
    green = 27 # BCM 27, Pin 13
    blue = 22 # BCM 22, Pin 15
    pins = [orange, yellow, green, blue]

    # Sequence for 28byj-48 Stepper Motor
    Seq = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]
    HalfSeq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]

    # Clear out pins
    for i in pins:
        gpio.setup(i, gpio.OUT)
        gpio.output(i, gpio.LOW)

    # doStep
    def doStep (step):
        for i in range(0,4):
            gpio.output(pins[i], step[i])
            time.sleep(WaitTime)
    def turnOffPins():
        for i in pins:
            gpio.output(i, gpio.LOW)
        print "turning off motor"



    print "Spin Time"
    for i in range(Steps):
        whichStep = i % 8
        doStep(HalfSeq[whichStep])
    turnOffPins()
