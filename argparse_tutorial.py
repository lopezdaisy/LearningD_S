import argparse
'''
Write a program that takes 3 numbers as an input
i)first number
ii)second number
ii)operstion("add","substract","multiply")
it should return the result of the operstion based on the input
'''
if __name__ == "__main__":
    #add arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="second number")
    parser.add_argument("operation",help="operation")

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1=int(args.number1)
    n2=int(args.number2)
    results= None  
    if args.operation == "add":
        results = n1 + n2
    elif args.operation == "substract":
        results = n1 - n2
    elif args.operation == "multiply":
        results = n1*n2

    print("Result is:",results)

    #To make argument optional just add  -- in the front of argument name