baggage_count=100
no_of_baggage_pick=0
while(baggage_count>0):
    no_of_baggage_pick=int(input("number of baggage:"))
    baggage_count=baggage_count-no_of_baggage_pick
    print("no of baggage remaining:",baggage_count)