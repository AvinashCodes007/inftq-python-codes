
def find_sum_of_digits(number):
    sum_of_digits=0
    for digit in str(number):

        sum_of_digits+=int(digit)
    
    #Write your logic here
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(196)
print("Sum of digits:",sum_of_digits)