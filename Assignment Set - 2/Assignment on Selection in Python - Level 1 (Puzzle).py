# 1st method
def form_triangle(num1,num2,num3):
    success="triangle can be formed"
    failure="triangle can't be formed"
    if (num1<num2+num3) and (num2<num1+num3) and (num3<num1+num2):
        return success
    else:
        return failure
   
num1=4
num2=6
num3=3
print(form_triangle(num1,num2,num3))

# 2nd method 

def form_triangle(num1,num2,num3):
    # Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    # Write your logic here
    if (num1 + num2 < num3) or (num1 + num3 < num2) or (num2 + num3 < num1):
    # Use the following messages to return the result wherever necessary
        return failure
    else:
        return success
print(form_triangle(1,4,5))

# 3rd method

def form_triangle(num1, num2, num3):
    # Check for each side being smaller than sum of other two
    if (num1+ num2 > num3) and (num2 + num3 > num1) and (num3 + num1 > num2):
        return True
    else:
        return False

# Provide different values for the variables, num1, num2, num3 and test your program
num1=10
num2=40
num3=45
print(form_triangle(num1, num2, num3))