df1 = spark.read.table("samples.bakehouse.sales_transactions")
df2 = spark.read.table("samples.bakehouse.sales_customers")
df = df1.join(df2, "customerID").select("first_name", "last_name", "product", "quantity", "unitPrice","totalPrice")
display(df)
