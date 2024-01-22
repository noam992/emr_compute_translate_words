import yfinance as yf
import boto3
from datetime import datetime
# from datetime import datetime, timedelta

# data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
# print(data.head())

### AWS credentials ###
# REMOVE #
aws_access_key_id = 'AKIAURE44WF7IG3WAWVU'
aws_secret_access_key = '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'
region_name = 'us-east-1'




class stock_data:
    def __init__(self):
        self.stock
        self.open
        self.high
        self.low
        self.close
        self.adj_close
        self.volume


def upload_to_s3(bucket, stock, file):

    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    
    year, month, day = get_current_year_month_day()
    file = 'data.csv'
    path = f'{stock}/year={year}/month={month}/day={day}/{file}'

    s3_client.meta.client.upload_file(Filename=path, Bucket=bucket, Key=file)
    return True


def get_stock_data(sign, days_ago):

    recent_data = yf.download(sign, period=days_ago)
    return recent_data

def get_current_year_month_day():

    current_datetime = datetime.now()

    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day

    return year, month, day

if __name__ == "__main__":

    sign = 'AAPL'
    period_days = '5d'
    stock_df = get_stock_data(sign, period_days)

    upload_to_s3('datalake-stock', sign, stock_df)



# msft = yf.Ticker("TSLA")

# msft.info

# # get historical market data
# hist = msft.history(period="1mo")

# # show meta information about the history (requires history() to be called first)
# msft.history_metadata

# # show actions (dividends, splits, capital gains)
# msft.actions
# msft.dividends
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs

# # show share count
# print(msft.get_shares_full(start="2022-01-01", end=None))
    

    # import requests

    # url = "https://currency-exchange.p.rapidapi.com/exchange"

    # querystring = {"to":"ILS","from":"USD","q":"1.0"}

    # headers = {
    # 	"X-RapidAPI-Key": "fc30ecd86cmsh7f3cf76dfa6a129p133c0ejsn8f267f9f96b0",
    # 	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    # }

    # response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())