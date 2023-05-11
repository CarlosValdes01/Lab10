"""
'digital_in.py'
==================================
Example of sending button values
to an Adafruit IO feed.
Author(s): Brent Rubell, Todd Treece
"""
# Import standard python modules
import time

#Importar para leer del puerto serial
import serial

# import Adafruit Blinka
#import board
#import digitalio

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_Kkmk87I8SAYO5kpRW6GL112hmvBd'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'CarlosJV'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Feed name
digital = aio.feeds('digital')
digout = aio.feeds('digout')

# Leer del PIC (contador)--------------------------------------------------------

# Configuración del puerto serial
ser = serial.Serial('COM4', 9600)

#-----------------------------------------------------------------------------------

while True:
    
    data = ser.read().decode(encoding="utf-8", errors="replace").strip()
    print('Button -> ', data)
    aio.send(digital.key, data)

    out = aio.receive(digout.key)
    ser.write((out.value).encode('ascii'))
    print(out)

    # avoid timeout from adafruit io
    time.sleep(0.5)