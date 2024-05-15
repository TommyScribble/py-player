from gpiozero import Button, LED
from time import sleep
from signal import pause
import pygame
from threading import Thread


button = Button(2)

pygame.mixer.init()
pygame.mixer.music.load('./dream.mp3')
isPlaying = True


wait = 0.001 # seconds

ctrlA = LED(6) # IN1
ctrlB = LED(13) # IN2
ctrlC = LED(19) # IN3
ctrlD = LED(26) # IN4

def runMotor():
	global isPlaying
	while isPlaying:
		#1
		ctrlA.on()
		ctrlB.off()
		ctrlC.off()
		ctrlD.off()
		sleep(wait)

		#2
		ctrlA.on()
		ctrlB.on()
		ctrlC.off()
		ctrlD.off()
		sleep(wait)

		#3
		ctrlA.off()
		ctrlB.on()
		ctrlC.off()
		ctrlD.off()
		sleep(wait)

		#4
		ctrlA.off()
		ctrlB.on()
		ctrlC.on()
		ctrlD.off()
		sleep(wait)

		#5
		ctrlA.off()
		ctrlB.off()
		ctrlC.on()
		ctrlD.off()
		sleep(wait)

		#6
		ctrlA.off()
		ctrlB.off()
		ctrlC.on()
		ctrlD.on()
		sleep(wait)

		#7
		ctrlA.off()
		ctrlB.off()
		ctrlC.off()
		ctrlD.on()
		sleep(wait)

		#8
		ctrlA.on()
		ctrlB.off()
		ctrlC.off()
		ctrlD.on()
		sleep(wait)

def stopMotor():
	global isPlaying
	isPlaying = False
	ctrlA.off()
	ctrlB.off()
	ctrlC.off()


def playMusic():
	global isPlaying
	print("Hello Jo Lane, I'm playing your tune!")
	pygame.mixer.music.play()
	isPlaying = True
	Thread(target=runMotor).start()

def stopMusic():
	global isPlaying
	print("Goodbye Jo Lane, your music is boring.")
	pygame.mixer.music.stop()
	isPlaying = False
	stopMotor()
	

button.when_pressed = playMusic
button.when_released = stopMusic

pause()
