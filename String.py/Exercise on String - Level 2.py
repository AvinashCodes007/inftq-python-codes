def generate_number(Airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    
    for i in range(no_of_passengers):
        
        ticket_number=f"{Airline} : {source[:3]} : {destination[:3]} : {i+101}"
        ticket_number_list.append(ticket_number)
    if (no_of_passengers<5):
        return ticket_number_list
    else:
        return ticket_number_list[-5:]
    
print(generate_number("BI","Bangalore","London",10))
