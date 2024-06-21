count=1
i=1
for baggage_weight in 29,30,31,32,28:
    if (baggage_weight)>=1 and  baggage_weight <=30:
        print("passenger",i,":proceed for baggage check")
    else:
        print("passenger",i,"maximum baggage weight allowd is 30kg.")
        count+=1
    i+=1

print("no of passengers who cleared baggage check:",count)


i=1
n=10
while(i<=n):
    if(i%2==0):
        print(i)
    i+=1
    






