ticket_status="confirmed"
luggage_weight=32
weight_limit=30  #weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="confirmed"):
    if(luggage_weight>0) and (luggage_weight<=weight_limit):
        print("check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_lagged_charge>0):
        print("extra luggage charge Rs.",extra_luggage_charge)
        print("please make the payment to clear chek in")
else:
    print("sorry!,ticket is not confirmed")


def display(num):
    if num%3==0 and num%5==0:
        print("Zoom")
    elif num%3==0:
        print("Zip")
    elif num%5==0:
        print("Zap")
    else:
        print("Invallid")
    return display

message=display(15)

baggage_count=100
no_of_baggage_pick=10
while(baggage_count>0):
    no_of_baggage_pick=int(input("number of baggage:"))
    baggage_count=baggage_count-no_of_baggage_pick
    print("no of baggage remaining:",baggage_count)

print("Flight had landed")
print("processed for immigration check ")
for passenger_count in 1,2,3,4,5:
    print("immageratio check done for passengers",passenger_count)

for number in range(1,7,2):
    print("the current number is:",number)

number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1,number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if (security_check==True):
            print("security check of passenger:",passenger_count,"--baggage",baggage_count,"baggage cleared")
        else:
            print("security check of passenger:",passenger_count,"--baggage",baggage_count,"baggage not cleared ")


number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1,number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if (security_check==True):
            print("security check of passenger:",passenger_count,"--baggage",baggage_count,"baggage cleared")
        else:
            print("security check of passenger:",passenger_count,"--baggage",baggage_count,"baggage not cleared ")


for passenger in 



    