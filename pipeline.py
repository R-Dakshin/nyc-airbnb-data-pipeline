from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, length, datediff, current_date
import pandas as pd

def start_spark():
    return SparkSession.builder.appName("NYC Airbnb Pipeline").getOrCreate()

def ingest_data(spark, input_path):
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    return df

def clean_and_engineer(df):
    # Remove duplicates
    df = df.dropDuplicates()
    
    #These rows are key fields so dropping them is the only way
    df = df.dropna(subset=["id", "name", "latitude", "longitude"])

    #Filling "unknown" for non numerical data
    df = df.fillna({'host_name': 'Unknown', 'neighbourhood_group': 'Unknown'})

    #For last_review, we fill 'N/A'
    df = df.fillna({'last_review': 'N\A',})

    #Filling numerical values with means and since for reviews_per_month, availability_365, calculated_host_listings_count and number_of_reviews, null means that 0 reviews so we will fill that with 0
    df = df.fillna({'reviews_per_month':0,'number_of_reviews':0,'availability_365':0,'calculated_host_listings_count': 0})
    df = df.fillna({'price': df.selectExpr("avg(price)").first()[0]})

    return df

def save_data(df, output_path):
    df.write.mode("overwrite").parquet(output_path)

def preview_data(parquet_path):
    df = pd.read_parquet(parquet_path)
    print(df.sample(5))

if __name__ == "__main__":
    INPUT_CSV = "AB_NYC_2019.csv"
    OUTPUT_PARQUET = "cleaned_airbnb_data"

    spark = start_spark()
    df = ingest_data(spark, INPUT_CSV)
    df_cleaned = clean_and_engineer(df)
    save_data(df_cleaned, OUTPUT_PARQUET)
    preview_data(OUTPUT_PARQUET)
