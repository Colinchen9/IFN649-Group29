import time
# Read data from csv file
import csv
import paho.mqtt.publish as publish


def readFromFile():
	with open('plant_vase1.CSV') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:  # Display column name
				print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:  # display data
				print(f'\tday : {row[3]}, hour:{row[4]}, minute:{row[5]}, moisture:{row[6]}')
				line_count += 1
# 				TODO: Prepocess and send data to MQTT at this point

			publish.single(topic="Test_IFN649", payload=f'\tday : {row[3]}, hour:{row[4]}, minute:{row[5]}, \
		moisture:{row[6]}', hostname="localhost")
			time.sleep(1)
		print(f'Processed {line_count} lines.')


def main():
	readFromFile()


if __name__ == '__main__':
	main()
