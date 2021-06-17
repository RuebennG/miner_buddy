import requests
import datetime as dt
import pandas as pd

# wallet = '0x56d890f48b0ce7860d5511432a970c47e7bcdf53'

class eth_nanopool:
    def __init__(self, wallet_addr):
        self.wallet_addr = wallet_addr
        self.current_balance = self.get_general()['balance']
        self.payout = self.get_payout()
        self.report_hashrate = self.get_reported_hashrate()
        self.avg_hashrate = self.get_general()['avgHashrate']['h12']
        self.current_price = self.get_current_price()

    def get_general(self):
        api1 = requests.get("https://api.nanopool.org/v1/eth/user/" + self.wallet_addr).json()
        general_data = api1['data']
        return general_data

    def get_reported_hashrate(self):
        api2 = requests.get("https://api.nanopool.org/v1/eth/reportedhashrates/" + self.wallet_addr).json()
        report_hashrate_data = api2['data']
        return report_hashrate_data[0]['hashrate']
    
    def get_payout(self):
        api3 = requests.get("https://api.nanopool.org/v1/eth/usersettings/" + self.wallet_addr).json()
        payout_data = api3['data']
        return payout_data['payout']

    def get_current_price(self):
        api4 = requests.get("https://api.nanopool.org/v1/eth/prices").json()
        price = api4['data']['price_usd']
        return price
 
    def details(self):
        df = []
        data = []
        data.insert(0, dt.datetime.now().strftime('%Y%m%d'))
        data.insert(1, dt.datetime.now().strftime('%H:%M'))
        data.insert(2, self.report_hashrate)
        data.insert(3, self.avg_hashrate)
        data.insert(4, self.current_balance)
        data.insert(5, self.current_price)
        df.append(data)

        return pd.DataFrame(df, 
        columns = ['Date', 'Time', 'Reported Hashrate', 'Average Hashrate 12h', 'Balance_ETH', 'ETH_price'])

