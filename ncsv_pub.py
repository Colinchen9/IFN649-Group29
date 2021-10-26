import time
# Read data from csv file
import csv
import paho.mqtt.publish as publish


def readFromFile():
	with open('Train.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		alert = ''
		for row in csv_reader:
			if line_count == 0:  # Display column name
				print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:  # display data
				print(f'\tdatetime : {row[0]}, soil_moisture:{row[1]}, air_temperature:{row[9]}, air_humidity:{row[10]}, \
				pressure:{row[11]}')
				if float(row[1]) < 67:
					print("\t soil not wet enough, need some water for irrigation")
					alert = 'soil not wet enough'
				# elif float(row[2]) < 40:
				# 	print("suitable zone")
				elif float(row[1]) > 80:
					print('too wet, soil wet enough')
					alert = 'too wet'

				if float(row[9]) < 15:
					print("\t so cold, need to open the heater")
					alert = 'so cold'

				elif float(row[9]) > 28:
					print('so hot, need to open air-conditioner')
					alert = 'so hot'

				if float(row[10]) < 60:
					print("\t too dry, need to open the air humidifier")
					alert = 'too dry'

				elif float(row[10]) > 85:
					print('alert： need to reduce humidity')
					alert = 'wet enough'

				line_count += 1
# 				TODO: Prepocess and send data to MQTT at this point
# 				publish.single(topic="Test_IFN649", payload=alert, hostname="localhost")
				print()
			# 	publish.single(topic="Test_IFN649", payload=f'\tdatetime : {row[1]}, moisture:{row[2]}, \
			# soil_temperature:{row[3]}', hostname="localhost")
				publish.single(topic="soil_moisture", payload=f"datetime : {row[0]}, soil_moisture: {row[1]} ", hostname="174.129.60.239")
				publish.single(topic="air_temperature", payload=f"datetime : {row[0]}, air_temperature: {row[9]} ", hostname="174.129.60.239")
				publish.single(topic="air_humidity", payload=f"datetime : {row[0]}, air_temperature: {row[10]} ", hostname="174.129.60.239")
				publish.single(topic="pressure", payload=f"datetime : {row[0]}, pressure: {row[11]} ", hostname="174.129.60.239")
				time.sleep(1)
		print(f'Processed {line_count} lines.')


def main():
	readFromFile()


if __name__ == '__main__':
	main()
