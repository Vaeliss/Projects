'''analysis on the last 25 years of data (emerging markets data begins in 1995)'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def return_portfolios(expected_returns, cov_matrix):
    '''ritorna diversi tipi di portafogli contenenti gli asset di cui sono forniti ritorni attesi e matrice di correlazione'''
    port_returns = []
    port_volatility = []
    stock_weights = []
    
    selected = (expected_returns.axes)[0]
    
    num_assets = len(selected) 
    num_portfolios = 5000
    
    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, expected_returns)
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)
    
    portfolio = {'Returns': port_returns,
                 'Volatility': port_volatility}
    
    for counter,symbol in enumerate(selected):
        portfolio[symbol +' Weight'] = [Weight[counter] for Weight in stock_weights]
    
    df = pd.DataFrame(portfolio)
    
    column_order = ['Returns', 'Volatility'] + [stock+' Weight' for stock in selected]
    
    df = df[column_order]
   
    return df


#data cleaning:

  
filename = "asset_returns.txt"

with open(filename) as f:
    my_string = f.read()

my_list = my_string.split("\n")

for i in range(len(my_list)):
    my_list[i] = my_list[i].replace("\t",",")
    my_list[i] = my_list[i].replace("%","")
    my_list


filename = "asset_returns.csv"

with open(filename,"w") as f:
    for i in range(len(my_list)):
        f.write(my_list[i]+"\n")
    


df = pd.read_csv("asset_returns.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Create histograms of all assets returns:
# if you have them or don't want them just comment out the next lines.

if not os.path.exists("./Assets_Returns_histograms"):
    os.mkdir("Assets_Returns_histograms")

for column in list(df.columns)[2:]:
    prov_df = pd.DataFrame({"Year":df.Year,"Returns":df[column]-df["Inflation"]})
    prov_df.dropna(inplace=True)
    plt.hist(prov_df.Returns,bins=30,edgecolor="black")
    plt.title(f"Frequency of {column}'s yearly real returns")
    plt.xlabel("Yearly return")
    plt.ylabel("Frequency")
    plt.savefig(f"./Assets_Returns_histograms/{column}.png")
    plt.clf()



# Create random portolios with specific assets:


del df["Year"]

assets_considered_data = {"US_stock_market":df["US Stock Market"]-df["Inflation"],
                          "US Small Cap":df["US Small Cap"]-df["Inflation"],
                          "Int stocks": df["Intl Developed ex-US Market"]-df["Inflation"],
                          "Emerging Markets":df["Emerging Markets"]-df["Inflation"],
                          "Lonh Term Corporate Bonds":df["Long-Term Corporate Bonds"]-df["Inflation"],
                          "Long Term Treasury":df["Long Term Treasury"]-df["Inflation"],
                          "Gold":df["Gold"]-df["Inflation"]}
assets = pd.DataFrame(assets_considered_data)
assets = assets.iloc[23:]
cov_yearly = assets.cov()
expected_returns = assets.mean()
random_portfolios = return_portfolios(expected_returns,cov_yearly)
# print(random_portfolios.head())

plt.scatter(random_portfolios.Volatility,random_portfolios.Returns)
plt.xlabel("Volatility (std)")
plt.ylabel("Yearly returns")
plt.title("Efficient Frontier")
try:
  single_asset_std=np.sqrt(np.diagonal(cov_yearly))
  plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)
  plt.axvline(x=single_asset_std,color="red")
except:
  pass
summary_df = pd.DataFrame({"Yearly_average":expected_returns,
                           "Volatility":single_asset_std})
print(summary_df)
plt.show()




#NB. gli anni considerati influenzano notevolmente i ritorni previsti con questo genere
# di calcolo. Per esempio il ritorno storico dell'oro è notevolmente superiore
# se si considerano periodi più lunghi.
# Calcolare il ritorno atteso come semplicemente la media dei ritorni degli ultimi 25 anni è
# estremamente semplicistico. Altri modelli di calcolo, che tengono conto di valutazioni attuali e passate
# potrebbero essere decisamente più adeguati (possibilmente TODO in futuro)

# TODO aggiungere metodo di calcolo della linea di frontiera, con la possibilità di ottenere il portfolio migliore
# contenente gli asset suggeriti, per un determinato livello di volatilità