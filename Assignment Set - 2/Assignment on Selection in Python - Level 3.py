def calculate_bill_amount(food_type,quantity_order,distance_in_kms):
    bill_amount=0
    
    if(food_type=='V'or food_type=='N') and quantity_order>=1:
        if food_type=='V':
            bill_amount = 120 * quantity_order
        else:
            bill_amount = 150 * quantity_order
    delivery_amount=0
    if distance_in_kms in [0,3]:
        delivery_amount=0
    elif distance_in_kms>3 and  distance_in_kms<=6:
        delivery_amount=(distance_in_kms-3)*3
    else:
        delivery_amount=9+(distance_in_kms-6)*6

    final_amount=bill_amount+delivery_amount
    return final_amount

print(calculate_bill_amount('N',2,8))
