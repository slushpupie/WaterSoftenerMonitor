import RPi.GPIO as GPIO
import time
import json
from statsd import StatsClient

def avg(a, b, c):
  list = []
  if a < 200 and a > 0:
    list.append(a)
  if b < 200 and b > 0:
    list.append(b)
  if c < 200 and c > 0:
    list.append(c)
  return (sum(list)/len(list))

def debug(args):
  # print(args)
  return False

try:
  GPIO.setmode(GPIO.BCM)
   
  TRIG = 23
  ECHO = 24
   
  debug("Distance Measurement In Progress")
   
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)
   
  GPIO.output(TRIG, False)
  debug("Waiting For Sensor To Settle")
  time.sleep(5)
  
  pulse_start = 0
  
  debug("Sending start signal")
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
   
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
   
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
   
try:
  GPIO.setmode(GPIO.BCM)

  TRIG = 23
  ECHO = 24

  debug("Distance Measurement In Progress")

  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

  GPIO.output(TRIG, False)
  debug("Waiting For Sensor To Settle")
  time.sleep(5)

  pulse_start = 0

  debug("Sending start signal")
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  debug("Reading return signal")
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()


  debug("Calculating")

  pulse_duration = pulse_end - pulse_start

  # Speed of sound at sea level:
  # 331.5 m/s
  # 33150 cm/s
  # Round trip = 33150/2 = 16575

  # Speed of sound at 900ft elevation (Blaine, MN)
  # 33920 cm/s
  # 33920/2 = 16960
  distance1 = round(pulse_duration * 16960,2)

  debug("Distance 1 %s" % distance1)

  time.sleep(0.5)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)
  GPIO.output(TRIG, False)
  time.sleep(2)
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start
  distance2 = round(pulse_duration * 16960,2)
  debug("Distance 2 %s" % distance2)

  time.sleep(0.5)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)
  GPIO.output(TRIG, False)
  time.sleep(2)
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start
  distance3 = round(pulse_duration * 16960,2)

  debug("Distance 3 %s" % distance3)

  distance = round(avg(distance1,distance2,distance3),2)
  debug("Average %s" % distance)

  j = {}
  j["distance"] = distance
  j["updated"] = int(time.time())
  
  sc = StatsClient()
  sc.gauge('watersoftener.distance',distance)
  
  with open('/var/www/distance.json', 'w') as outfile:
    json.dump(j,outfile) 
  
finally:  
  GPIO.cleanup()
