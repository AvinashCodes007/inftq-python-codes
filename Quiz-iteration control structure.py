for variable_1 in range(1,5,-1):
    print("executed")


grade_list = ["A+","A-","B","B+","A+","A+","A-"]
for grade in grade_list:
    if grade == "A+":
        print("TPF")
    else:
        print("Not TPF")


number=28
for num in range(25,30):
    print(num)
    if(number>num):
        print(num)

    else:
        print(num)
        break




for num in 23, 45, 50, 65, 76, 90:
    if(num%5!=0):
        continue

    if(num%10==0):
        print(num, end=" ")
        
        continue
    if(num%3==0):
        print(num, end=" ")
        

for number in 10,15:
  
    for counter in range(1,3):
        print(number*counter, end=" ")


num1=16
num2=6
while(num1>=2):
    if(num1>num2):
    
        num1=num1/2
        
    else:
        print(num1)
        break


counter=0
while(counter<=9):
    if (counter%2==0): 
        pass
    else:
        print(counter, end=" ")
        
    counter+=1

numbers_list = [98,45,60,71,90]
count = 10
for number in numbers_list:
    if number % 10== 0:
        
        count -= 1
        continue
    counter = 0
    while counter < 2:
        last_digit = number % 10
        
        number = number // 10
        if last_digit > 4:
            count += 1
            break 
        count += 1
        counter += 1
print(count)
















