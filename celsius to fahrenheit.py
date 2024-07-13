def fahrenheit_to_celsius(fahrenheit):
    celsius=0
    celsius=(fahrenheit-32)*5/9
    return celsius
 
result=fahrenheit_to_celsius(50)
print(result)

def celsius_to_fahrenheit(celsius):
    fahrenheit=0
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

result=celsius_to_fahrenheit(25)
print(result)


   