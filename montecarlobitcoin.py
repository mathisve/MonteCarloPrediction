import sys
import random
import csv
import numpy as np
import matplotlib.pyplot as plt

n = 365 #number of days we want to simulate.
x = 50 #number of diffirent simulations

csvFile = 'CSV/28_10_2018/market-price.csv'
currentPrice = 5471.82
f = 20

try:
	if(sys.argv[1] == '-v'):
		v = True #Verbose false is default, true for iterative messages (will slow down)
				 #run the following for verbose:
				 #python montecarlobitcoin.py -v
except:
	v = False

def getTrueBitcoinPriceChange():
	truePrice = []
	truePercentualChangeArr = []
	print("Loading CSV file: ", csvFile)
	with open(csvFile) as pricelist:
			csvdoc = csv.reader(pricelist)
			for row in csvdoc:
				currPrice = float(row[1])
				if(v):
					date=row[0]
					print("r:{} $:{}".format(date[:10],currPrice))
				if(int(currPrice) <= 25000):
					truePrice.append(int(currPrice))
					truePercentualChangeArr.append(abs((truePrice[-1]-currPrice)/100))
			avrgPercentualChange = abs(sum(truePercentualChangeArr)/len(truePercentualChangeArr))		


	return (avrgPercentualChange/f)

def MCsimulation(currentPrice,s,x):
	currentSim = []
	for i in range(n*f):
		if(v):
			print("Simulation {} of {}. Day {} of {}".format(s,x,i+1,n*f))
		currentPrice = currentPrice + currentPrice * (random.choice([(change * -1), change]))
		currentSim.append(currentPrice)
	plt.plot(currentSim)

def plot():
	plt.title("Possible Asset price with avrg {}% daily change".format((change*f)*100))
	plt.show()

change = round(getTrueBitcoinPriceChange(),6)
print("Average % change in the past year:", (change*f)*100)
for i in range(x):
	if((i+1)%10==0):
		print("Simulation n: ",i+1)
	MCsimulation(currentPrice,i,x)

plot()
