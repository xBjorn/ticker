import json,requests,sys
from time import sleep

class Currency:

	def __init__(self, setCurrency):
		self.setCurrency = setCurrency


	def calculateCurrency(self):
		print "===========BLOCKCHAIN==========="
		print "Currency: {} || Worth: {}{}".format(self.setCurrency, showCurrency[self.setCurrency]['symbol'], showCurrency[self.setCurrency]['sell'])
		print "================================"

def usage():

		print "===Options==="

		for currency in showCurrency:
			print currency

		print "============="
		print "Usage like so:"
		print "ticker.py <currency>"




if __name__ == '__main__':

		r = requests.get('https://blockchain.info/ticker')
		showCurrency = json.loads(r.text)

		if len(sys.argv) == 2 and sys.argv[1] in showCurrency:

			c = Currency(sys.argv[1])
			c.calculateCurrency()

		else:

			print "[!] CHOOSE A CURRENCY FROM THE LIST APPEARING IN 5 SECONDS! [!]"
			sleep(5)
			usage()

	














