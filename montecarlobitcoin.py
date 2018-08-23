import random
import csv
import numpy as np
import matplotlib.pyplot as plt

n = 365 #number of days we want to simulate.
csvFile = 'market-price.csv'
currentPrice = 5471.82
f = 5

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


change = round(getTrueBitcoinPriceChange(),6)
print("Average % change in the past year:", change)
for i in range(100):
	MCsimulation(currentPrice)

plt.title("Possible BTC price with avrg {}% daily change".format((change*100)*f))
plt.show()