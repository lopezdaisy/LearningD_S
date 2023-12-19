items = ["Bread","Pasta","Fruits","Vegetables"]
print(items)
print(items[2])
items[2] = "Chips"
print(items)
print(items[-1])
items.append("butter")
print(items)
items.insert(1,"samosa")
print(items)
food = ['Bread', 'samosa', 'Pasta', 'Chips', 'Vegetables', 'butter']
bathroom = ['shampoo','soap']
Items = food + bathroom
print(Items)
print(len(Items))

#list omprehension provides a way to transform one list into another

numbers =[1,2,3,4,5,6,7,8]
'''even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)

print(even)    '''

       #OR(using LIST COMPREHENSION)
even = [i for i in  numbers if i % 2 == 0]
print(even)
sqr_numbers =  [i * i for i in numbers]
print(sqr_numbers)
s = set([1, 2, 3, 4, 5, 6, 2, 3, 4])
print(s)
