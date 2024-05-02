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
    if(extra_luggage_charge>0):
        print("extra luggage charge Rs.",extra_luggage_charge)
        print("please make the payment to clear chek in")
else:
    print("sorry!,ticket is not confirmed")