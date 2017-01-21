import RPi.GPIO as GPIO
import time

PIN_IN1 = 8
PIN_IN2 = 10
PIN_IN3 = 24
PIN_IN4 = 26

HIGH = 1
LOW = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#  Motor 1
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)

# Motor 2
GPIO.setup(PIN_IN3, GPIO.OUT)
GPIO.setup(PIN_IN4, GPIO.OUT)

# Main loop to test motor controll
while True:
	print "rotating both motors forward"
	
	# Motor 1
	GPIO.output(PIN_IN1, HIGH)
	GPIO.output(PIN_IN2, LOW)
	
	# Motor 2
	GPIO.output(PIN_IN3, HIGH)
	GPIO.output(PIN_IN4, LOW)
	time.sleep(3)
	
	print "turning direction 1"
	
	# Motor 1
	GPIO.output(PIN_IN1, HIGH)
	GPIO.output(PIN_IN2, LOW)
	
	# Motor 2
	GPIO.output(PIN_IN3, LOW)
	GPIO.output(PIN_IN4, HIGH)
	time.sleep(3) 
	
	print "rotating both motors reverse"
	
	# Motor 1 (working)
	GPIO.output(PIN_IN1, LOW)
	GPIO.output(PIN_IN2, HIGH)
	
	# Motor 2 (not working)
	GPIO.output(PIN_IN3, LOW)
	GPIO.output(PIN_IN4, HIGH)
	time.sleep(3)
	
	print "stopping both motors"
	
	# Motor 1
	GPIO.output(PIN_IN1, LOW)
	GPIO.output(PIN_IN2, LOW)
	
	# Motor 2
	GPIO.output(PIN_IN3, LOW)
	GPIO.output(PIN_IN4, LOW)
	time.sleep(1) 
	
	print "turning direction 2"
	
	# Motor 1
	GPIO.output(PIN_IN1, LOW)
	GPIO.output(PIN_IN2, HIGH)
		
	# Motor 2
	GPIO.output(PIN_IN3, HIGH)
	GPIO.output(PIN_IN4, LOW)
	time.sleep(3) 

