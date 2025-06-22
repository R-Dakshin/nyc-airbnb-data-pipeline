# 🏙️ NYC Airbnb Data Cleaning Pipeline

This repository contains a PySpark-based data pipeline to clean and process the **New York City Airbnb 2019 dataset**. The pipeline handles missing values, deduplicates data, and saves the output in an efficient Parquet format.

---

## 📊 Dataset Overview

- **Dataset Source:** [Inside Airbnb - NYC 2019](http://insideairbnb.com/get-the-data.html)
- **File:** `AB_NYC_2019.csv`
- **Records:** ~49,000 rows
- **Columns:** 16 features describing listing, location, host, price, reviews, and availability.

---

## 🧾 Key Columns

| Column Name                     | Description |
|--------------------------------|-------------|
| `id`                           | Unique listing ID |
| `name`                         | Title of the Airbnb listing |
| `host_name`                    | Host's name |
| `neighbourhood_group`         | Borough (e.g. Manhattan) |
| `neighbourhood`               | Specific area |
| `latitude`, `longitude`       | Geolocation |
| `room_type`                   | Type of room (entire, shared, etc.) |
| `price`                       | Price per night (USD) |
| `minimum_nights`              | Minimum booking duration |
| `number_of_reviews`           | Count of all reviews |
| `last_review`                 | Date of most recent review |
| `reviews_per_month`           | Avg monthly reviews |
| `calculated_host_listings_count` | Total listings per host |
| `availability_365`            | Days available per year |

---

## 🧹 Cleaning & Feature Engineering Steps

✔️ Drop duplicate rows  
✔️ Drop records missing key fields: `id`, `name`, `latitude`, `longitude`  
✔️ Fill missing values:
- `host_name` and `neighbourhood_group`: `"Unknown"`
- `last_review`: `"N/A"`
- `reviews_per_month`, `number_of_reviews`, `availability_365`, `calculated_host_listings_count`: `0`
- `price`: filled with dataset **average**

---

## 🛠 Technologies Used

- [PySpark](https://spark.apache.org/docs/latest/api/python/)
- pandas
- Parquet (efficient columnar file format)
- Python 3.7+

---

## 🧪 How to Run

### 🔧 Local Setup

1. **Install dependencies**
```bash
pip install -r requirements.txt
