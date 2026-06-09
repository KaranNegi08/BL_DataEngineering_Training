from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local")\
        .appName("test")\
        .getOrCreate()

data=[
    ("James",'','Smith','1991-04-01','M',3000),
    ("Michael",'','Rose','2000-06-02','M',4000),
    ("Robert",'','Williams','2002-08-10','M',4000),
    ("Jen",'Anne','Jones','2004-01-15','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]

df = spark.createDataFrame(data=data, schema=columns)
print(df.printSchema())  #  GIVE SCHEMA IN OUTPUT