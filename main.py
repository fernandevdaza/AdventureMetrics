from db.schema import SalesOrderDetail
from db.schema import SalesOrderHeader
from db.schema import Product
from db.connection import session
from sqlalchemy import func
import pandas as pd
from matplotlib import pyplot as plt


query = session.query(
    SalesOrderDetail.productid,
    Product.name,
    func.sum(SalesOrderDetail.orderqty)
).join(SalesOrderHeader, SalesOrderDetail.salesorderid == SalesOrderHeader.salesorderid
).join(Product, SalesOrderDetail.productid == Product.productid
).filter(
    SalesOrderHeader.orderdate.between('2012-01-01 00:00:00', '2012-12-31 23:59:59')
).group_by(
    SalesOrderDetail.productid,
    Product.name
).order_by(
    func.sum(SalesOrderDetail.orderqty).desc()
).all()

df = pd.DataFrame(query, columns=['productid', 'name', 'total'])

print(df.head())