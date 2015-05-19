import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

# access data and remove null values
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

# apply collections.Counter to get a count of the observations of each number of credit lines
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# graph the data
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

# perform chi square test to check how well the data fits a normal distribution
chi, p = stats.chisquare(freq.values())
print chi, p

# 2408.433146517214, 0.0