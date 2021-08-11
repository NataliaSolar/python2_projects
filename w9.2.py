
import yfinance as yf
from matplotlib import pyplot as plt
import statsmodels.api as sm
import numpy as np

apple = list(yf.download('AAPL', '2015-01-01', '2021-03-01')['Adj Close'])
msft = list(yf.download('MSFT', '2015-01-01', '2021-03-01')['Adj Close'])
spy = list(yf.download('SPY', '2015-01-01', '2021-03-01')['Adj Close'])
tsla = list(yf.download('TSLA', '2015-01-01', '2021-03-01')['Adj Close'])
xom = list(yf.download('XOM', '2015-01-01', '2021-03-01')['Adj Close'])
fb = list(yf.download('FB', '2015-01-01', '2021-03-01')['Adj Close'])
crm = list(yf.download('CRM', '2015-01-01', '2021-03-01')['Adj Close'])


spy = sm.add_constant(spy)
msft = sm.add_constant(msft)
model = sm.OLS(xom, spy)
result = model.fit()
print(result.summary())

#plt.scatter(apple, msft)
#plt.show()

fb = list(yf.download('FB', '2015-01-01', '2021-03-01')['Adj Close'])
crm = list(yf.download('CRM', '2015-01-01', '2021-03-01')['Adj Close'])
cvx = list(yf.download('CVX', '2015-01-01', '2021-03-01')['Adj Close'])
aig = list(yf.download('AIG', '2015-01-01', '2021-03-01')['Adj Close'])
