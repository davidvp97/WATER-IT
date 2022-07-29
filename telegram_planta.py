#------------------------------ [IMPORT]------------------------------------


import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot

import utime

TOKEN = '5518631023:AAGKTDdIDGl5W9tUVBAp0uSL7k37S5ySAU0'

#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)
sensorHumedad = ADC(Pin (34))


#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

def map(x):
    return int((x - 0) * (125 - 25) / (180 - 0) + 25)
    

#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("ADRIANA", "Bayro761"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    print("ok")
    
    @bot.add_message_handler("Planta")
    def help(update):
        update.reply('''¡Hola Soy tu planta! \U0001FAB4
                     \n Me alegra hablar con tigo
                     \n te gustaria saber si tengo sed \U0001F4A7 :
                     
                     
                     Humedad: 2
                    
                     
                     \n Gracias por cuidarme \U0001F49A ,no me descuides''')
    
    
                     
        
    @bot.add_message_handler("2")
    def help(update):
        sensorHumedad.read()
        hum = sensorHumedad.read()
        update.reply("La Humedad es," + str(hum) + "\U0001F4A7")
    
    
    
    bot.start_loop()
    
      

else:
       print ("Imposible conectar")
       miRed.active (False)