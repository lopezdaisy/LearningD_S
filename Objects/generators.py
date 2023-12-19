#generaor is a simple way of creating iterator
def remote_control_next():
    yield "cnn"
    yield "espn"

itr = remote_control_next()
'''print(itr)   
print(next(itr))'''

for _ in remote_control_next():
    print(_)
    print("\n")

#Produce a fibonacci sequence using generators
def fib():
    a,b = 0,1
    while True:
        yield a
        a ,b = b, a+b
for _ in fib():
    if _>100:
        break
    print(_)