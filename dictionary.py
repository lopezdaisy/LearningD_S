#Dictionary allow you to store key,value pairs
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
