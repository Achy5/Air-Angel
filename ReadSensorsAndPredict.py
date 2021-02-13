import Sensors_read as sensors
import time
from joblib import load
import numpy as np
import math

regr = load("regr.joblib")
xscaler = load("xscaler.joblib")
yscaler = load("yscaler.joblib")

def ReadAllSensors():
                temphum = sensors.temp_hum()
                bar = sensors.barometer()
                if isinstance(temphum,tuple) == False:
                    if math.isnan(temphum):
                        return math.nan
                else:
                    arr = np.array([[temphum[0],temphum[1],bar]])
                    arrsc = xscaler.transform(arr)
                    pr = regr.predict(arrsc)
                    prinv = yscaler.inverse_transform(pr)
                    a = [time.strftime("%c"), temphum[0], temphum[1], bar,
                            round(prinv[0][0],2), round(prinv[0][1],2), round(prinv[0][2],2), round(prinv[0][3],2)]
                    return a

