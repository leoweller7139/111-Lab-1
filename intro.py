# Python Executes linear, from top to bottom

print('Hello World')

name = 'Leonardo'
last_name = 'Weller'
age = 21
found = False
average = 42.32

print(name)
print(last_name)
print("Age:", age)
print(found)
print(average)

print(21 + 21)
print(age - 1)
print(74*64)
print(120 / 20)
print(10 % 3)

# -------------------------------
# Declaring a function
# This is a function and the stuff inside it
def test():
    print("inside the function")
    print("this too")
# --------------------------------
#  Pressing Tab will put this v into the function
print('outside the function')

test() #Executing a function

def example():
    print('Leo is the greatest')

def seperator():
    print('-------------------------')

example()

seperator()

# Can only combine strings together and not a string with an int
print(name + last_name)

seperator()

if(age < 90):
    print('You are Young!')
elif(age == 90):
    print('You got too many wrinkles, oldy!')
else:
    print('Sorry bud, you are getting old!')