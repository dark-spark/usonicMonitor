#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.IN)				

monON = True

def reading(sensor):

	if sensor == 0:
		
		GPIO.setup(17,GPIO.OUT)
		GPIO.setup(27,GPIO.IN)
		GPIO.output(17, GPIO.LOW)
		
		time.sleep(0.3)
		GPIO.output(17, True)
		
		time.sleep(0.00001)
		
		GPIO.output(17, False)

		while GPIO.input(27) == 0:
		  signaloff = time.time()
		
		while GPIO.input(27) == 1:
		  signalon = time.time()
		
		timepassed = signalon - signaloff

		distance = timepassed * 17000
		
		return distance
		
		GPIO.cleanup()

	else:
		print "Incorrect usonic() function varible."

while True:
	
	while GPIO.input(22) == 1:

		if lastReading == True && reading(0) > 100:
			
			if monON == True:

				#print "Turning Monitor OFF"
				monON = False
				os.system("sudo /usr/local/bin/monitor.sh off")
		
		else:
		
			if monON == False:

				#print "Turning Monitor ON"
				monON = True
				os.system("sudo /usr/local/bin/monitor.sh on")
				time.sleep(20)

		if reading(0) > 100:

			lastReading = True
		
		else:

			lastReading = False

		time.sleep(1)

time.sleep(30)
