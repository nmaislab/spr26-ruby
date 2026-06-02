import spidev
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

spi = spidev.SpiDev()
spi.open(0,0)

def read_adc(channel):
	adc = spi.xfer2([1,(8+channel) << 4,0])
	return ((adc[1]&3) << 8) + adc[2]
	
while True:
	value = read_adc(0)
	print(value)
	client.publish("pulse/data", value)
	time.sleep(0.1)
