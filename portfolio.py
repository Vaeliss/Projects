class Portfolio:

	def __init__(self,asset_allocation):
		self.assets = asset_allocation
		self.year = 0


	def update_portfolio(self,performances):
		for key in self.assets.keys():
			self.assets[key] *= (1+performances[key])
		self.year += 1

	def print_total(self):
		total = sum(self.assets.values())
		print(f"\n\nYear: {self.year}\nTotal: {round(total,2)}k euros.")

	def print_actual_allocation(self):
		print("\n")
		for asset,value in self.assets.items():
			print(f"{asset}: {round(value,2)}.  {round(value/sum(self.assets.values())*100,2)}")

	def rebalance_portfolio(self,rebalance):
		total = sum(self.assets.values())
		for key in self.assets.keys():
			self.assets[key] = (total*(rebalance[key]/100))

#portfolio creation
asset_allocation = {"us shares":25,"em_shares":15,"int shares":10,
		"gov bonds":20,"corp bonds":5,"infl bonds":5,"crypto or other":0,
		"gold":10,"silver":10}
rebalance = {"us shares":25,"em_shares":15,"int shares":10,
		"gov bonds":20,"corp bonds":5,"infl bonds":5,"crypto or other":0,
		"gold":10,"silver":10}
my_portfolio = Portfolio(asset_allocation)


#year 0
my_portfolio.print_total()
my_portfolio.print_actual_allocation()

#year 1 2008
my_portfolio.update_portfolio({"us shares":-0.3704,"em_shares":-0.5281,"int shares":-0.4127,
		"gov bonds":0.21,"corp bonds":0.0226,"infl bonds":0.01,"crypto or other":0,
		"gold":0.0492,"silver":-0.2615})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year 2 2009
my_portfolio.update_portfolio({"us shares":0.287,"em_shares":0.7598,"int shares":0.2827,
		"gov bonds":-0.11,"corp bonds":0.0846,"infl bonds":0.03,"crypto or other":0,
		"gold":0.2403,"silver":0.2562})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year 3 2010
my_portfolio.update_portfolio({"us shares":0.1709,"em_shares":0.1886,"int shares":0.0836,
		"gov bonds":0.08,"corp bonds":0.0933,"infl bonds":0.03,"crypto or other":0,
		"gold":0.2927,"silver":0.7117})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)


#year 4 2011
my_portfolio.update_portfolio({"us shares":0.0096,"em_shares":-0.1878,"int shares":-0.1251,
		"gov bonds":0.25,"corp bonds":0.0973,"infl bonds":0.04,"crypto or other":0,
		"gold":0.0957,"silver":0.1477})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year 5 2012
my_portfolio.update_portfolio({"us shares":0.1625,"em_shares":0.1864,"int shares":0.1856,
		"gov bonds":0.03,"corp bonds":0.1058,"infl bonds":0.02,"crypto or other":0,
		"gold":0.0660,"silver":-0.0776})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year 6 2013
my_portfolio.update_portfolio({"us shares":0.3335,"em_shares":-0.0519,"int shares":0.1504,
		"gov bonds":-0.11,"corp bonds":-0.02,"infl bonds":0.02,"crypto or other":1.5256,
		"gold":-0.2833,"silver":-0.3905})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year 7 2014
my_portfolio.update_portfolio({"us shares":0.1243,"em_shares":0.0042,"int shares":-0.0566,
		"gov bonds":0.17,"corp bonds":0.1,"infl bonds":0.01,"crypto or other":56.9096,
		"gold":-0.0219,"silver":-0.0905})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year8 2015
my_portfolio.update_portfolio({"us shares":0.0029,"em_shares":-0.1547,"int shares":-0.0019,
		"gov bonds":0.0,"corp bonds":-0.015,"infl bonds":0.01,"crypto or other":-0.5925,
		"gold":-0.1067,"silver":-0.1835})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year9 2016
my_portfolio.update_portfolio({"us shares":0.1253,"em_shares":0.115,"int shares":0.0245,
		"gov bonds":0.01,"corp bonds":0.07,"infl bonds":0.01,"crypto or other":0.384,
		"gold":0.0803,"silver":0.201})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year10 2017
my_portfolio.update_portfolio({"us shares":0.2105,"em_shares":0.3115,"int shares":0.264,
		"gov bonds":0.05,"corp bonds":0.08,"infl bonds":0.01,"crypto or other":1.2964,
		"gold":0.1281,"silver":-0.0375})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year11 2018
my_portfolio.update_portfolio({"us shares":-0.0526,"em_shares":-0.1471,"int shares":-0.1446,
		"gov bonds":-0.005,"corp bonds":-0.05,"infl bonds":-0.01,"crypto or other":12.4435,
		"gold":-0.0879,"silver":-0.0822})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)

#year12 2019
my_portfolio.update_portfolio({"us shares":0.2703,"em_shares":0.1231,"int shares":0.1793,
		"gov bonds":0.12,"corp bonds":0.17,"infl bonds":0.01,"crypto or other":-0.7115,
		"gold":0.137,"silver":0.0888})
my_portfolio.print_total()
my_portfolio.print_actual_allocation()
my_portfolio.rebalance_portfolio(rebalance)