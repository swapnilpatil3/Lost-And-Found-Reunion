import pandas as pd
import random

products = [
"Apple AirPods Max headphones",
"Sony WH-1000XM5 headphones",
"Dell laptop charger",
"Black Nike backpack",
"Blue steel water bottle",
"Samsung Galaxy Buds earbuds",
"Casio digital watch",
"Brown leather wallet",
"HP laptop",
"Boat wireless earbuds",
"Logitech wireless mouse",
"Red Puma gym bag"
]

locations = [
"lost near library",
"found near canteen",
"lost in classroom",
"found in parking area",
"lost near hostel",
"found near auditorium"
]

rows = []

for i in range(500):

    product = random.choice(products)
    location = random.choice(locations)

    rows.append({
        "id": i,
        "product_name": product,
        "description": f"{product} {location}"
    })

df = pd.DataFrame(rows)

df.to_csv("data/lost_found_dataset.csv", index=False)

print("Dataset created successfully!")
