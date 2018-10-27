import random
import csv
import numpy as np
import matplotlib.pyplot as plt

n = 365 #number of days we want to simulate.
csvFile = 'CSV/28_10_2018/market-price.csv'
currentPrice = 5471.82
f = 20
change = 0

def getTrueBitcoinPriceChange():
	truePrice = []
	truePercentualChangeArr = []
	with open(csvFile) as pricelist:
			csvdoc = csv.reader(pricelist)
			for row in csvdoc:
				currPrice = float(row[1])
				if(int(currPrice) <= 25000):
					truePrice.append(int(currPrice))
					truePercentualChangeArr.append(abs((truePrice[-1]-currPrice)/100))
			avrgPercentualChange = abs(sum(truePercentualChangeArr)/len(truePercentualChangeArr))		


	return (avrgPercentualChange/f)

def MCsimulation(currentPrice):
	currentSim = []
	for i in range(n*f):
		currentPrice = currentPrice + currentPrice * (random.choice([(change * -1), change]))
		currentSim.append(currentPrice)
	plt.plot(currentSim)

def plot():
	plt.title("Possible BTC price with avrg {}% daily change".format((change*f)*100))
	plt.show()

change = round(getTrueBitcoinPriceChange(),6)
print("Average % change in the past year:", (change*f)*100)
for i in range(100):
	if((i+1)%10==0):
		print("Simulation n: ",i+1)
	MCsimulation(currentPrice)

plot()
