# Booleans represent one of two values: True or False
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False
a = 300
b = 100
if b > a:
    print("b is graeter than a")
else:
    print("b is not greater than a")
    
# Evaluate a string and a number
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# To print fales in python
print(bool(""))
print(bool())

# Most Values are True
#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.

# The  following code will return
bool("123")
bool(123)
bool(["apple","banana","guava"])


#The following will return False:


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool({})
bool([])

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

def is_old_enough(age):
    if age >= 18:
        return True
    else:
        return False

print(is_old_enough(20)) # This would print True

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))