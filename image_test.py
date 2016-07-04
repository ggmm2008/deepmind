import pandas.io.data as web
import pandas as pd 

def returnprice():
    all_data={}
    for ticker in ['AAPL','IBM','MSFT','GOOG']:
        all_data[ticker]=web.get_data_yahoo(ticker,'1/1/2015','1/31/2015')

    price=pd.DataFrame({tic:data['Adj Close'] for tic,data in all_data.iteritems()})
    valume=pd.DataFrame({tic:data['Volume'] for tic,data in all_data.iteritems()})

    return price,valume