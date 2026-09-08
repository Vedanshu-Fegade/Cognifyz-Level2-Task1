# COGNIFYZ TECHNOLOGIES
# DATA SCIENCE INTERNSHIP - LEVEL 2 TASK 1
# TABLE BOOKING AND ONLINE DELIVERY

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# 1. PATHS

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "Data" / "Dataset (2).csv"
OUTPUT_DIR = BASE_DIR / "Visualizations"

OUTPUT_DIR.mkdir(exist_ok=True)


# 2. LOAD DATASET

df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("COGNIFYZ TECHNOLOGIES - LEVEL 2 TASK 1")
print("TABLE BOOKING AND ONLINE DELIVERY")
print("=" * 70)

print("\nDATASET INFORMATION")
print("-" * 70)
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


# 3. TABLE BOOKING ANALYSIS

table_booking_counts = df["Has Table booking"].value_counts()

table_booking_percentages = (
    df["Has Table booking"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\n" + "=" * 70)
print("1. TABLE BOOKING")
print("=" * 70)

print("\nNumber of restaurants:")
print(table_booking_counts)

print("\nPercentage of restaurants:")
print(table_booking_percentages)


# 4. ONLINE DELIVERY ANALYSIS

online_delivery_counts = df["Has Online delivery"].value_counts()

online_delivery_percentages = (
    df["Has Online delivery"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\n" + "=" * 70)
print("2. ONLINE DELIVERY")
print("=" * 70)

print("\nNumber of restaurants:")
print(online_delivery_counts)

print("\nPercentage of restaurants:")
print(online_delivery_percentages)


# 5. AVERAGE RATING BY TABLE BOOKING

average_rating = (
    df.groupby("Has Table booking")["Aggregate rating"]
    .mean()
    .round(2)
)

rating_difference = (
    average_rating["Yes"] - average_rating["No"]
)

print("\n" + "=" * 70)
print("3. AVERAGE RATING BY TABLE BOOKING")
print("=" * 70)

print("\nAverage rating:")
print(average_rating)

print(f"\nDifference in average rating: {rating_difference:.2f}")


# 6. ONLINE DELIVERY BY PRICE RANGE

delivery_by_price = pd.crosstab(
    df["Price range"],
    df["Has Online delivery"]
)

delivery_percentage_by_price = (
    pd.crosstab(
        df["Price range"],
        df["Has Online delivery"],
        normalize="index"
    )
    .mul(100)
    .round(2)
)

print("\n" + "=" * 70)
print("4. ONLINE DELIVERY BY PRICE RANGE")
print("=" * 70)

print("\nCounts:")
print(delivery_by_price)

print("\nPercentages:")
print(delivery_percentage_by_price)


# 7. VISUALIZATION

sns.set_theme(style="whitegrid")


# Chart 1: Table Booking Availability

plt.figure(figsize=(8, 6))

ax = sns.countplot(
    data=df,
    x="Has Table booking"
)

plt.title(
    "Table Booking Availability",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Has Table Booking")
plt.ylabel("Number of Restaurants")

for container in ax.containers:
    ax.bar_label(container, fmt="%d")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "01_table_booking_availability.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# Chart 2: Online Delivery Availability

plt.figure(figsize=(8, 6))

ax = sns.countplot(
    data=df,
    x="Has Online delivery"
)

plt.title(
    "Online Delivery Availability",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Has Online Delivery")
plt.ylabel("Number of Restaurants")

for container in ax.containers:
    ax.bar_label(container, fmt="%d")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "02_online_delivery_availability.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# Chart 3: Average Rating

plt.figure(figsize=(8, 6))

ax = sns.barplot(
    x=average_rating.index,
    y=average_rating.values
)

plt.title(
    "Average Rating: Table Booking vs No Table Booking",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Has Table Booking")
plt.ylabel("Average Aggregate Rating")
plt.ylim(0, 5)

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "03_average_rating_table_booking.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# Chart 4: Online Delivery by Price Range

delivery_plot = delivery_percentage_by_price.reset_index()

plt.figure(figsize=(9, 6))

ax = sns.barplot(
    data=delivery_plot,
    x="Price range",
    y="Yes"
)

plt.title(
    "Online Delivery Availability by Price Range",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Price Range")
plt.ylabel("Restaurants with Online Delivery (%)")
plt.ylim(0, 50)

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "04_online_delivery_by_price_range.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# 8. COMPLETION

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nCharts saved in:")
print(OUTPUT_DIR)

print("\nGenerated files:")

for file in sorted(OUTPUT_DIR.glob("*.png")):
    print("-", file.name)