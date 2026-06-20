from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import col

sc = SparkContext()
glueContext = GlueContext(sc)

# Read from Glue Catalog
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="sales_db",
    table_name="orders"
)

# Convert to DataFrame
df = dynamic_frame.toDF()

# Transform
clean_df = (
    df
    .dropDuplicates()
    .dropna()
    .filter(col("amount") > 0)
)

# Write partitioned parquet
clean_df.write \
.mode("overwrite") \
.partitionBy("year", "month") \
.parquet(
"s3://company/processed/orders/"
)