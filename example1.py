#!python3

# class objects with multiple instances in a table

class powers:
    val = 0
    def square(self):
        return self.val**2         

    def __init__(self,v): 
        #Constructor         
        self.val = v               


# Create a list that we can store instances in
numbers = []

# Instantiate 10 instances
for i in range(10):
    numbers.append( powers(i) )

print(f"We now have {len(numbers)} instances stored in our table.\n")

print("Instance Data:")
print("**************")
for i in range(10):
    print(f"instance with index:{i} > number:{numbers[i].val} and square:{numbers[i].square()}")
