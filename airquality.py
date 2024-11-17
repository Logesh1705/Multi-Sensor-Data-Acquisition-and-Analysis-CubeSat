from machine 
from chittiSat.mq2 import MQ2
from chittiSat.assistant import dashboard
import utime


sensor = MQ2(pinData = 26)

sensor.calibrate()

while True:
    LPG = sensor.readLPG()
    Smoke = sensor.readSmoke()
    Methane = sensor.readMethane()
    Hydrogen = sensor.readHydrogen()
    
    dashboard.sendAir(LPG, Smoke, Methane ,Hydrogen)
    
    
  
    