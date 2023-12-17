#A block of code that perform a specific tasks
tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

#Using a for loop
total = 0
for i in tom_exp_list:
    total += i
    print("Tom's expenses  is:",total)

total = 0
for _ in joe_exp_list:
    total += _
    print("Joe's expenses  is:",total) 

#Using a Function
def calculate_total(exp):
    total = 0
    for item in exp:
        total += item
    return total    

tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]  

toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)

print("Tom's total expenses:",  toms_total)
print("Joe's total expenses:", joes_total)

def sum(a,b):
    print("a:",a)
    print("b:",b)
    total = a+b
    print("total inside function:",total)
    return total
n = sum(5,6)
print("Total=",n)

#Default Arguments
def add(a,b=0):
    '''
    This function takes two arguments which are integers numbers and it will retuen sum of them as an output. 
    '''
    total =a+b
    return total
x = sum(7,5)
print("Total = ",x)