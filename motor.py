from gpiozero import Button, LED
from time import sleep



wait = 0.001 # seconds

ctrlA = LED(6) # IN1
ctrlB = LED(13) # IN2
ctrlC = LED(19) # IN3
ctrlD = LED(26) # IN4

def runMotor():
	while True:
		ctrlA.on()
		ctrlB.off()
		ctrlC.off()
		ctrlD.off()
		sleep(wait)

		ctrlA.on()
		ctrlB.on()
		ctrlC.off()
		ctrlD.off()
		sleep(wait)

		ctrlA.off()
		ctrlB.on()
		ctrlC.off()
		ctrlD.off()
		sleep(wait)

		ctrlA.off()
		ctrlB.on()
		ctrlC.on()
		ctrlD.off()
		sleep(wait)

		ctrlA.off()
		ctrlB.off()
		ctrlC.on()
		ctrlD.off()
		sleep(wait)

		ctrlA.off()
		ctrlB.off()
		ctrlC.on()
		ctrlD.on()
		sleep(wait)

		ctrlA.off()
		ctrlB.off()
		ctrlC.off()
		ctrlD.on()
		sleep(wait)

def stopMotor():
	ctrlA.off()
	ctrlB.off()
	ctrlC.off()
	ctrlD.off()