"""Spark session utilities for MLApp."""
from pyspark.sql import SparkSession

def get_spark_session(app_name="MLApps"):
<<<<<<< HEAD
    # Optimized for large datasets - Rahul's change
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "400") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.default.parallelism","400")\
        .getOrCreate()
=======
    # Partition tuning for our workload - your change
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "400") \
        .config("spark.default.parallelism", "400") \
        .getOrCreate()
>>>>>>> a1b2c3d (feat: optimize spark partitions for large datasets)
    return spark


