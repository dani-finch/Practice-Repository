# Food data structure
food_menu = [
    {
        "category": "Appetizers",
        "items": [
            {"name": "Caesar Salad", "price": 8.99},
            {"name": "Garlic Bread", "price": 4.99},
            {"name": "Bruschetta", "price": 6.99}
        ]
    },
    {
        "category": "Main Course",
        "items": [
            {"name": "Steak", "price": 19.99},
            {"name": "Grilled Salmon", "price": 16.99},
            {"name": "Chicken Parmesan", "price": 14.99},
            {"name": "Vegetable Stir-Fry", "price": 12.99}
        ]
    },
    {
        "category": "Desserts",
        "items": [
            {"name": "Cheesecake", "price": 7.99},
            {"name": "Chocolate Brownie", "price": 5.99},
            {"name": "Ice Cream Sundae", "price": 6.99}
        ]
    }
]

# Exercise 1: Print the names of all food categories
if False:
    for food in food_menu:
        print(food['category'])

# Exercise 2: Calculate the total price of all items in the menu
if False:
    total_price = 0

    for food in food_menu:
        for item in food["items"]:
            total_price += item["price"]
    print("Total Price of all items:", total_price)

# Exercise 3: Find the most expensive item in each category
if False:
    for food in food_menu: # outer loop
        most_expensive_item = None # initializer to start the count
        for item in food["items"]: # inner loop that will go through each item in each menu section
            if most_expensive_item is None or item["price"] > most_expensive_item["price"]: # inner loop of the above inner loop, that goes thru to find the most expensive price
                most_expensive_item = item 
        print(f"Most Expensive {food['category']}: {most_expensive_item['name']}")

# Exercise 4: Check if any category has items with a price greater than $20
if False:
    has_expensive_items = False
    for food in food_menu:
        for item in food["items"]:
            if item["price"] > 20:
                has_expensive_items = True
                break
    print("Any category with items priced above $20?", has_expensive_items)

# Exercise 5: Print the names of the vegetarian items (category: Main Course, item: Vegetable Stir-Fry)
if False:
    vegetarian_items = [item["name"] for food in food_menu for item in food["items"] if food["category"] == "Main Course" and item["name"] == "Vegetable Stir-Fry"]
    print("Vegetarian Items:", vegetarian_items)

# Exercise 6: Calculate the average price of items in the Desserts category
if False:
    desserts_items_total_price = 0
    desserts_items_count = 0
    for food in food_menu:
        if food["category"] == "Desserts":
            for item in food["items"]:
                desserts_items_total_price += item["price"]
                desserts_items_count += 1
    average_price = desserts_items_total_price / desserts_items_count
    print("Average Price of Desserts:", average_price)

# Exercise 7: Update the price of the Grilled Salmon item to $18.99
if False:
    for food in food_menu:
        for item in food["items"]:
            if item["name"] == "Grilled Salmon":
                item["price"] = 18.99

# Exercise 8: Print the names of the items with prices greater than $15
if False:
    expensive_items = []
    for food in food_menu:
        for item in food["items"]:
            if item["price"] > 15:
                expensive_items.append(item["name"])
    print("Expensive Items:", expensive_items)

# Exercise 9: Find the cheapest item in the menu
if False:
    cheapest_item = None
    for food in food_menu:
        for item in food["items"]:
            if cheapest_item is None or item["price"] < cheapest_item["price"]:
                cheapest_item = item
    print("Cheapest Item:", cheapest_item["name"])

# Exercise 10: Count the total number of items in the menu
if False:
    total_items = 0
    for food in food_menu:
        total_items += len(food["items"])
    print("Total Number of Items:", total_items)
