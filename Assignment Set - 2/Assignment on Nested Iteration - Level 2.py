def find_max(num1,num2):
    if(num1>num2):
        return -1
    valid_number=[]
    
    for num in range(num1,num2+1):
        
        if (10<=num<100):
            digit_sum=0
            for digit in str(num):
                
                digit_sum+=int(digit) 
            
            if digit_sum%3==0 and num%5==0 :
                valid_number.append(num)
                
    return valid_number

valid_number=find_max(10,99)
print(valid_number)

    
def digit_sum(num):
    sum=0
    num=str(num)
    for digit in num:
        sum += int(digit)
    return sum

sum=digit_sum(123)
print(sum)
