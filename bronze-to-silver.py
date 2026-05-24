#This is notebook to read sales and customer from sample databricks table
df1 = spark.read.table("samples.bakehouse.sales_transactions")
df2 = spark.read.table("samples.bakehouse.sales_customers")
from pyspark.sql.functions import sum, desc, col
df = df1.join(df2, "customerID").select("first_name", "last_name", "product", "quantity", "unitPrice", col("totalPrice").cast("float"))\
    .groupBy("product")\
    .agg(sum("totalPrice").alias("totalSales"))\
    .orderBy(desc("totalSales"))

display(df)

