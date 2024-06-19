import pandas as pd
from sqlalchemy import create_engine
from db.connection import session
from sqlalchemy import func
from db.schema import SalesOrderDetail
from db.schema import SalesOrderHeader
from db.schema import Product

class SalesReport:
    
    def get_best_selling_products(self, year):

        year_start_date = str(year) + '-01-01 00:00:00'
        year_end_date = str(year) + '-12-31 23:59:59'

        query = session.query(
            SalesOrderDetail.productid,
            Product.name,
            func.sum(SalesOrderDetail.orderqty)
        ).join(SalesOrderHeader, SalesOrderDetail.salesorderid == SalesOrderHeader.salesorderid
        ).join(Product, SalesOrderDetail.productid == Product.productid
        ).filter(
            SalesOrderHeader.orderdate.between(year_start_date, year_end_date)
        ).group_by(
            SalesOrderDetail.productid,
            Product.name
        ).order_by(
            func.sum(SalesOrderDetail.orderqty).desc()
        ).all()


        df = pd.DataFrame(query, columns=['productid', 'name', 'total'])
        return df
