#clculator mvp

# user input to perform operation
# lgoic for operation
# output 


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mull(x,y):
    return x*y

def div(x,y):
    return x/y

def power(x,y):
    return x**y

def calculator():
    print("Simple calculator")

    while True:

        try:
            num1=float(input("Enter a number"))
            num2=float(input("Enter second number"))
        except:
            print("Enter a valid number")
            continue

        print("\n Select operation")
        print("1: add(+)")
        print("2: Sub(-)")
        print("3: mull(*)")
        print("4: div(/)")
        print("5: Power(**)")

        choice=input("Enter choices (1,2,3,4,5): ")

        if choice =="1":
            print(f"{num1}+{num2} = {add(num1,num2)}")
        elif choice == "2":
            print(f"{num1}-{num2} ={sub(num1,num2)}")
        elif choice =="3":
            print(f"{num1}*{num2} = {mull(num1,num2)}")
        elif choice =="4":
            print(f"{num1}/{num2}={div(num1,num2)}")
        elif choice =="5":
            print(f"{num1}**{num2}={power(num1,num2)}")

            # break

        else:
            print("Enter a valid number")

if __name__=="__main__":
    calculator()
        


    