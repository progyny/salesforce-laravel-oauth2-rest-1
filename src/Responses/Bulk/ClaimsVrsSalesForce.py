import csv

with open('/Users/darren.lopez/Desktop/tina/Claims_Extract_Complete.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	print(readCSV)