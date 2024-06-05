def product(num1,num2,num3):
    if num3==7:
        return -1
    elif num2==7:
        return num3
    elif num1==7:
        return num2*num3

    else:   
        product=num1*num2*num3
    return product

result=product(7,4,6)
print(result)



# it's same but name change

def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if num3 == 7:
        product=-1
    elif num2 == 7:
        product=num3
    elif num1 == 7:
        product=num2*num3
    else:
        product=num1*num2*num3
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(4,5,7)
print(product)



























        













    



        




            


    
    







