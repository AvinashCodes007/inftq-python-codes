def find_leap_years(given_year):
    
    # find next leap yr from the given leap yr, it may be the same or anything else

    list_of_leap_years=[]
   
    while len(list_of_leap_years)<15:
        if (given_year%4==0 and  given_year%100!=0)or(given_year%400==0) :
           list_of_leap_years.append(given_year)
    
        given_year+=1
            
    return list_of_leap_years

list_of_leap_years=find_leap_years(1684)
print(list_of_leap_years)

     


