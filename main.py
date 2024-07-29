import json
import matplotlib.pyplot as plt

# Load JSON data from file
with open("countries1.json", "r") as file:
    data = json.load(file)

# Prepare lists for plotting
foods = set()  # Use a set to avoid duplicates
prices = []

# Extract food items and their prices
for country, (currency, items) in data.items():
    for food_item, price in items.items():
        foods.add(food_item)
        prices.append({
            'food': food_item,
            'price': float(price),
            'country': country
        })

# Convert the set to a list for plotting
foods = list(foods)

# For each food item, we will calculate its average price across all countries
average_prices = {food: 0 for food in foods}
food_counts = {food: 0 for food in foods}

# Calculate average prices
for price_entry in prices:
    food = price_entry['food']
    average_prices[food] += price_entry['price']
    food_counts[food] += 1

# Convert averages to actual averages
for food in average_prices:
    if food_counts[food] > 0:
        average_prices[food] /= food_counts[food]

# Plotting
plt.figure(figsize=(12, 8))
food_items = list(average_prices.keys())
avg_prices = list(average_prices.values())

plt.bar(food_items, avg_prices, color='skyblue')
plt.xlabel('Food Items')
plt.ylabel('Average Price')
plt.title('Average Prices of Different Foods Across Countries')
plt.xticks(rotation=45)
plt.show()
