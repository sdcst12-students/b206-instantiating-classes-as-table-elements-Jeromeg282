#!python3

# class objects with multiple instances in a table

class powers:
    val = 0
    def square(self):
        return self.val**2         

    def __init__(self,v): 
        #Constructor         
        self.val = v               


# Create a dictionary that we can store instances in
numbers = {}

# Instantiate 10 instances
namedIndexes = [5,10,15,20]
for i in namedIndexes:
    numbers[i] = powers(i)

print(f"We now have {len(numbers)} instances stored in our dictionary.\n")

print("Instance Data:")
print("**************")
for i in numbers:
    print(f"instance with index:{i} > number:{numbers[i].val} and square:{numbers[i].square()}")
