import grovepi
import math
import time
from Adafruit_BME280 import *

temp_hum_sensor = 4
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
            
def temp_hum():
    timeout = time.time() + 5
    while True:
        try:
            [temp,humidity] = grovepi.dht(temp_hum_sensor,1)
            if time.time() > timeout:
                break
        except IOError:
            print ("Error")
    if math.isnan(temp) == False and math.isnan(humidity) == False:
         return temp, humidity
    else:
        return math.nan   

def barometer():
    
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    hectoconverted = round(hectopascals,2)
    humidity = sensor.read_humidity() 

    return hectoconverted
        
        
