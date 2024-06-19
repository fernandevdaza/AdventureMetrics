import pandas as pd
from matplotlib import pyplot as plt
from models.SalesReport import SalesReport



print("Generando reporte de ventas...")
reporteProductos = SalesReport()
df = reporteProductos.get_best_selling_products(2011)

print(df.head(20))

## Generar grafico
df.head(20).plot(kind='bar', x='name', y='total')
plt.show()
