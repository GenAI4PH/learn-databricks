#This is notebook to read sales and customer from sample databricks table
df1 = spark.read.table("samples.bakehouse.sales_transactions")
df2 = spark.read.table("samples.bakehouse.sales_customers")
from pyspark.sql.functions import sum, desc, col
# Aggregate at product level
print("Aggregating at product level")
df_product = df1.join(df2, "customerID").select("first_name", "last_name", "product", "quantity", "unitPrice", col("totalPrice").cast("float"))\
    .groupBy("product")\
    .agg(sum("totalPrice").alias("totalSales"))\
    .orderBy(desc("totalSales"))

display(df_product)

#  Aggregate at customer level
# print("Aggregating at customer level")
# df_customer = df1.join(df2, "customerID").select("first_name", "last_name", "product", "quantity", "unitPrice", col("totalPrice").cast("float"))\
#     .groupBy("first_name", "last_name")\
#     .agg(sum("totalPrice").alias("totalSales"))\
#     .orderBy(desc("totalSales"))

# display(df_customer)

#  Aggregate at City level
print("Aggregating at City level")
df_city = df1.join(df2, "customerID").select("city", "product", "quantity", "unitPrice", col("totalPrice").cast("float"))\
    .groupBy("city")\
    .agg(sum("totalPrice").alias("totalSales"))\
    .orderBy(desc("totalSales"))

display(df_city)



