# Car data structure
cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2019,
        "mileage": 45000,
        "color": "Silver",
        "price": 15000,
        "is_available": True
    },
    {
        "make": "Honda",
        "model": "Accord",
        "year": 2020,
        "mileage": 30000,
        "color": "Blue",
        "price": 18000,
        "is_available": False
    },
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 2018,
        "mileage": 25000,
        "color": "Red",
        "price": 25000,
        "is_available": True
    },
    {
        "make": "Nissan",
        "model": "Altima",
        "year": 2017,
        "mileage": 60000,
        "color": "Black",
        "price": 12000,
        "is_available": False
    },
    {
         "make": "Chevrolet",
        "model": "Camaro",
        "year": 2021,
        "mileage": 5000,
        "color": "Yellow",
        "price": 30000,
        "is_available": True
    }
]

# Exercise 1: Print the make and model of each car
if True:
    for car in cars:
        print(f"Make: {car['make']},  Model: {car['model']}")
    
# Exercise 2: Calculate the average mileage of the available cars
if False:  # Solution Option - 1
    miles_list = [] # will need this list to collect all the available cars, which will allow you to get the average mileage of only the cars in the list

    for car in cars: # first need to find which cars are available
        if car['is_available']:
            miles_list.append(car['mileage'])

    # Need to define the sum and number of cars in order to calculate the average
    sum_mileage = sum(miles_list)
    number_of_cars = len(miles_list)
    avg_mileage = sum_mileage / number_of_cars

    print(f"Average mileage is: {avg_mileage}")

if False:  # Solution Option - 2
    total_sum = 0 # starting value that initializes the count
    total_number_of_cars = 0

    for car in cars:
        if car['is_available']:
            total_sum = total_sum + car['mileage']  # total_sum += i['mileage'] - shorthand way of doing this line 
            total_number_of_cars = total_number_of_cars + 1  # total_number_of_cars += 1 - shorthand way of doing this line 

        avg_mileage = total_sum / total_number_of_cars

    print(f"Average mileage is: {avg_mileage}")

# Exercise 3: Find the most expensive car
if False:
    max_price = 0 # starting value that initializes the count
    most_expensive_car = None # starting value that initializes the count

    for car in cars:
        price = car['price']
        if price > max_price:
            max_price = price
            most_expensive_car = car

    print(f"The most expensive car is: {most_expensive_car['make']}, {most_expensive_car['model']} ")

# Exercise 4: Check if any car has a mileage greater than 50,000
if False:
    for car in cars:
        if car['mileage'] > 50000:
            print(f"The {car['make']} {car['model']} has mileage more than 50,000.")

# Exercise 5: Calculate the total price of all cars
if False:  # Solution Option 1
    total_price = [] # list that will contain the price of all the cars

    for car in cars:
        car_prices = car['price']
        total_price.append(car_prices)

    print(f'The total price of all the cars is {sum(total_price)} ') 

if False:  # Solution Option 2
    total_price = 0 # this is used when we want to start a count for things

    for car in cars:
        total_price += car['price']

    print(f'The total price of all the cars is {total_price} ')

# Exercise 6: Update the price of all cars by 10% if the year is earlier than 2020 - Ask if the solution should list all car information, or just the updated price for the make and model?
if False: # Solution Option 1
    # The math - 15000 10% of 15000 is 1500 so need a calculation to get 16500 ---> 15000 * 1.1 = 16500 I would have done (x * 0.1) + x
    new_prices = []

    for car in cars:
        if car['year'] < 2020:
            car['price'] = round(car['price'] * 1.1, 1)
            new_prices.append(car['make'])
            new_prices.append(car['model'])
            new_prices.append(car['price'])
    
    print(new_prices)

    # print(updated_prices)

if False:  # Solution Option 2 - List Comprehension version
    new_prices = [(car['make'], car['model'], round(car['price'] * 1.1, 1)) for car in cars if car['year'] < 2020]

    print(new_prices)

# Exercise 7: Print the details of cars with prices greater than $20,000
if False:
    cars_more_than_20k = []

    for car in cars:
        if car['price'] > 20000:
            cars_more_than_20k.append(car)
    print(f"The details of cars more than 20000 are: {cars_more_than_20k}")
