# A set is an unordered collection of unique elements
basket = {"orange", "apples", "mango", "apple", "orange"}

print(type(basket))
print(basket)

a = set()
a.add(1)
a.add(2)
print(a)

#Frozen set(cant change the content of the set e.g cant add new element)

fs = frozenset([1, 2, 3, 4, 5, 6, 2, 3, 4])
print(fs)

#union,intersection,
x = {'a','b','c','d'}
y = {'x','b','z'}
print(x|y)#for union use OR
print(x&y)#for intersection use AND
print(x-y)#for different use '-'
print(x<y)#for subset