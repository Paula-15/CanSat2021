import radio
import time


outputLog = None

def main():
	radio.init()

	outputLog = open('dataTARS.txt', 'a')


	while True:
		packet = radio.rfm69.receive(timeout = 2)

		if packet is None:
			radio.display.fill(0)
			radio.display.text('No packet', 25, 15, 1)
			radio.display.show()
		else:
			dataLine = packet.decode()

			outputLog.write(dataLine)
			outputLog.flush()

			fields = dataLine.split (' ')

#			timeStamp = float(fields[0])
			temperature = float(fields[0])
			humedad = float(fields[1])
			presion = float(fields[2])
			altitud = float(fields[3])

#			outputLog.write("xxx %f %f %f %f %f\n" % (timeStamp, temperature, humedad, presion, altitud))
#			print("\nTime: %0.2f s" % (timeStamp - startTime))
			print("Temperature: %0.1f C" % temperature)
			print("Humedad: %0.1f %%" % humedad)
			print("Presión: %0.1f hPa" % presion)
			print("Altitud: %0.2f meters" % altitud)

			radio.display.fill(0)
#			radio.display.text('%0.2f  P:%0.1f hPa' % (timeStamp - startTime, presion), 2, 2, 1)
			radio.display.text('T:%0.1f C  Hum:%0.2f%%' % (temperature, humedad), 2, 13, 1)
			radio.display.text('Alt:%0.2fm' % (altitud), 2, 25, 1)
			radio.display.show()


	radio.close()
	outputLog.close()




try:
	main()

except KeyboardInterrupt:
	radio.close()
	outputLog.close()
	print("Out")

