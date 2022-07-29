from machine import Pin,ADC
from utime import sleep


# aqui se define el pin del relay

motor = Pin(25, Pin.OUT)


# aqui se define el pin del sensorHumedad

sensorHumedad = ADC(Pin (34))
sensorHumedad.atten(ADC.ATTN_11DB)
sensorHumedad.width(ADC.WIDTH_10BIT)

while True:

    s = sensorHumedad.read()
    
    
    if s < 800 : # valor minimo de humedad
    
        motor.value(1)
        print("la tierra esta mojada", s)
    

    else: 
        motor.value(0)
        print ("la tierra esta muy seca", s)

    
    
    
    
    
    
    


