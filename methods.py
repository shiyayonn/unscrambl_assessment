import data.extract as data
import pandas as pd

from datetime import timedelta

today = pd.to_datetime('now').to_pydatetime()
tdf = data.getTransactions()
pdf = data.getProducts()



def TransactionById(id):
    
    result = tdf.loc[tdf['transactionId']== id]
    
    if not result.empty:
        return result.to_json(orient='records')
    else:
        return False

def TransactionSummaryByProductsByDays(_days):
    
    startDate = today - timedelta(days=_days)
    i = pd.date_range(startDate,periods=_days,freq='d')
    tdf['transactionDatetime'] = pd.to_datetime(tdf.transactionDatetime)
    transactions = tdf.loc[(tdf.transactionDatetime >=i[0])&(tdf.transactionDatetime<=i[-1])]
    product_details = pd.merge(transactions, pdf, left_on="productId", right_on="productId")
    product_summary =  product_details[['productName','transactionAmount']]
    result = product_summary.groupby('productName').sum().reset_index().to_json(orient='records')
  
    if not result=='[]':
        return result
    else:
        return False


def TransactionSummaryByManufacturingCityByDays(_days):
    
    startDate = today - timedelta(days=_days)
    i = pd.date_range(startDate,periods=_days,freq='d')
    tdf['transactionDatetime'] = pd.to_datetime(tdf.transactionDatetime)
    transactions = tdf.loc[(tdf.transactionDatetime >=i[0])&(tdf.transactionDatetime<=i[-1])]
    product_details = pd.merge(transactions, pdf, left_on="productId", right_on="productId")
    product_summary =  product_details[['productManufacturingCity','transactionAmount']]
    result = product_summary.groupby('productManufacturingCity').sum().reset_index().to_json(orient='records')
    
    if not result=='[]':
        return result
    else:
        return False