#py is Dynamic type 
#Standard Data type 

a = 123
b = "conctanate"

# print(a+b)  --> gives error  TypeError: unsupported operand type(s) for +: 'int' and 'str'

c = 1
print(a+c)  # same type data can be add
print("type of a+b: ", type(a+c))

list = ["mutable ", "diffrnt type data "]
tuple = ("ordred colection", "immutable collection")
dict = {"key":"value", "key1":"value1"}

# print(list+tuple+dict)     #TypeError: can only concatenate list (not "tuple") to list
# print(list+dict)           #TypeError: can only concatenate list (not "dict") to list

list1=["ankit","ankita","sona","jana"]

print(list+list1)


#OUTPUT
# 124
# type of a+b:  <class 'int'>   ---> class -mind it ( py is also object type)
# ['mutable ', 'diffrnt type data ', 'ankit', 'ankita', 'sona', 'jana']