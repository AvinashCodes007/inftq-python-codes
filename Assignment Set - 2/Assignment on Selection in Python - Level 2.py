def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    total_amount=5*(no_of_five) + no_of_one
    
    amount_to_make=rupees_to_make
    
    if total_amount<rupees_to_make:
        print(-1)
      
    
    five_needed=rupees_to_make // 5

    if five_needed>no_of_five:
        five_needed=no_of_five
        
    one_needed=rupees_to_make-five_needed*5
    
    if one_needed>no_of_one:
        one_needed=no_of_one
        
     
    if (five_needed*5+one_needed) == rupees_to_make:
        print("no. of Five needed:",five_needed)
        print("no.of One needed:",one_needed)
    else:
        print(-1)
make_amount(26,7,3)






