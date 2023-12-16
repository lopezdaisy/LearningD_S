exp = [2340,2500,2100,3100,2980]
total = 0
for _ in exp:
    total += _
    print(total)

for i in range(1,11):
    print(i)

for alphabet in range(ord('A'), ord('Z')+1):
    print(chr(alphabet),end = '' )

exp1 = [2340,2500,2100,3100,2980]
total =0
for i in range (len(exp1)):
    print('Month:', (i+1), 'Expense:',exp1[i])
    total = total + exp1[i]

print('Total expense is:',total)   

key_location ="chair"
locations =['garage','living room','chair','closet']
for i in locations :
    if i ==  key_location:
        print("Key is found in",i)
        break
    else:
        print("Key is not found in",i) 


for i in range(1,6):
    if i%2 ==0:
        continue
    print(i*i)

 #while loop
i = 1
while i<=5:
    print(i)
    i += 1 

