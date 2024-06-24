from models.SalesReport import SalesReport
from db.schema import SalesOrderDetail, SalesOrderHeader, Product
from sqlalchemy import func, case
import pandas as pd
class ReportSeasonalTrends(SalesReport):
    def __init__(self):
        super().__init__()
    
    def get_seasonal_trends_by_quarter(self, year, quarter=None, limit=None):
        """
        Obtiene el top de productos por trimestre de la base de datos para un año específico.
        :param year: Año a consultar.
        :param quarter: Trimestre a consultar.
        :param limit: Número de productos a mostrar.
        """
        try:
            year_start_date = str(year) + '-01-01 00:00:00'
            year_end_date = str(year) + '-12-31 23:59:59'
            quarter_case = case(
                (func.extract('quarter', SalesOrderHeader.orderdate) == 1, 'Q1'),
                (func.extract('quarter', SalesOrderHeader.orderdate) == 2, 'Q2'),
                (func.extract('quarter', SalesOrderHeader.orderdate) == 3, 'Q3'),
                (func.extract('quarter', SalesOrderHeader.orderdate) == 4, 'Q4'),
            ).label('quarter')

            query = self.session.query(
                quarter_case,
                Product.name.label('product_name'),
                func.sum(SalesOrderDetail.orderqty).label('total_quantity')
            ).join(
                SalesOrderDetail, SalesOrderHeader.salesorderid == SalesOrderDetail.salesorderid
            ).join(
                Product, SalesOrderDetail.productid == Product.productid
            ).filter(
                SalesOrderHeader.orderdate.between(year_start_date, year_end_date)
            )
            
            if quarter:
                query = query.filter(func.extract('quarter', SalesOrderHeader.orderdate) == quarter)
            
            query = query.group_by(
                quarter_case,
                Product.name
            ).order_by(
                quarter_case,
                func.sum(SalesOrderDetail.orderqty).desc()
            )

            results = query.all()

            df = pd.DataFrame(results, columns=['quarter', 'product_name', 'total_quantity'])
            
            if limit:
                df = df.groupby('quarter').head(limit).reset_index(drop=True)
            
            return df
        except Exception as e:
            raise Exception(f"Error al obtener las tendencias trimestrales: {e}")
    