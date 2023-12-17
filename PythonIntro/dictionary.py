""""'''#Dictionary allow you to store key,value pairs
d = {"daisy":798778539, "Lopez":732050089}
print(d)
d["Adhiambo"]=758754949
print(d)
del d["Lopez"]
print(d)
for key in d:
    print("key:",key,"value",d[key])

 #OR  
for k,v in d.items():
    print("key:",k,"value",v)

dict = {'dog':'has a tail and goes woof',
        'cat':'says meow',
        'mouse':'chased by cats'}
word = input('Enter a word:')
print('The defination is:',dict[word])
'''
'''Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a product
name and print the corresponding price or a message if the product is not in the dictionary'''
"""
product_dict = {}
while True:
    product_name = input("Enter a product name (or 'done' to finish):")
    if product_name.lower() == 'done':
        break
    try:
        product_price = float(input("Enter the price for {}: $".format(product_name)))
    except:
        print("Invalid number for price. Please enter a valid number.")
        continue
    product_dict[product_name] = product_price

while True:
    print("\nOptions:")
    print("1. Get price by product name")
    print("2. Get products with price less than a specific amount")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    # Check user's choice
    if choice == '1':
        inquiry = input("Enter product name to get the price: ")
        if inquiry in product_dict:
            print("The price for {} is ${:.2f}".format(inquiry, product_dict[inquiry]))
        else:
            print("Product not found in the dictionary.")
    elif choice == '2':
        try:
            max_price = float(input("Enter the maximum price: $"))
        except ValueError:
            print("Invalid input for price. Please enter a valid number.")
            continue

        # Filter and print products with a price less than the specified amount
        affordable_products = {name: price for name, price in product_dict.items() if price < max_price}

        if affordable_products:
            print("Products with price less than ${:.2f}:".format(max_price))
            for name, price in affordable_products.items():
                print("{}: ${:.2f}".format(name, price))
        else:
            print("No products found within the specified price range.")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 'December':31}

while True:
    month_name = input("Enter a month name (or 'exit' to quit):")
    if month_name.lower() == 'exit':
        break
    matched_month = None

    # Convert user input to lowercase for case-insensitive matching
    month_name_lower = month_name.lower()

    for month in days.keys():
        if month.lower().startswith(month_name_lower[:3]):
            matched_month = month
            break

    if matched_month:
        print(f"{matched_month} has {days[matched_month]} days.")
    else:
        print("Month not found.")

# (b) Print all keys in alphabetical order
print("\nAlphabetical order of months:")
for month in sorted(days.keys()):
    print(month)

# (c) Print months with 31 days
print("\nMonths with 31 days:")
for month, days_count in days.items():
    if days_count == 31:
        print(month)

# (d) Print (key-value) pairs sorted by the number of days
print("\nMonths sorted by days:")
for month, days_count in sorted(days.items(), key=lambda x: x[1]):
    print(f"{month}: {days_count} days")        

# (e) Modify the program for partial matching
user_partial_month = input("\nEnter the first three letters of a month: ")

# Find matching month(s) based on the first three letters
matched_months_partial = [month for month in days.keys() if month.lower().startswith(user_partial_month.lower())]

if matched_months_partial:
    print(f"\nMatching month(s) based on the first three letters: {', '.join(matched_months_partial)}")
else:
    print("No matching month found.")    