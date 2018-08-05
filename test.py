import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# PINS
orange = 4 # BCM 4, Pin 7
yellow = 17 # BCM 17, Pin 11
green = 27 # BCM 27, Pin 13
blue = 22 # BCM 22, Pin 15
pins = [orange, yellow, green, blue]

for i in pins:
    gpio.setup(i, gpio.OUT)
    gpio.output(i, gpio.LOW)

Steps = 512

# Sequence
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
WaitTime = .17/float(1000)

# doStep
def doStep (step):
    # for active in step:
        # gpio.output(pins[0], active)
        # print active
        # time.sleep(WaitTime)
    gpio.output(pins[0], step[0])
    time.sleep(WaitTime)
    gpio.output(pins[1], step[1])
    time.sleep(WaitTime)
    gpio.output(pins[2], step[2])
    time.sleep(WaitTime)
    gpio.output(pins[3], step[3])
    time.sleep(WaitTime)


print "Spin Time"
for i in range(Steps):
    for step in HalfSeq:
        doStep(step)

print "turning off motor"
for i in pins:
    gpio.output(i, gpio.LOW)
