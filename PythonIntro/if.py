num = input("Enter a number: ")
num = int(num)
if num%2 == 0:
    print("Number is even")
else:
    print("Number is odd")


indian = ["Samosa","daal","naan"]
chinese = ["Egg role","Pot sticker","Fried rice"]
italian = ["Pizza","Pasta","Risotto"]

dish = input("Enter a dish  name: ")
if dish in indian:
    print("Indian Dish")
elif dish in chinese:
    print("Chinese Dish")
elif dish in italian:
    print("italian  dish")
else:
    print("Based on the knowledge I have, don't know all the dishes in the world")
