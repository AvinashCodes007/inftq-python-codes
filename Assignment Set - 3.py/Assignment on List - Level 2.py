def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for i in reqd_gems:
        if i not in gems_list:
            bill_amount = -1
            return bill_amount
  
    for i in range(len(reqd_gems)):
       
        bill_amount+=price_list[i]*reqd_quantity[i]

    if bill_amount > 30000:
        
        bill_amount=bill_amount-(bill_amount)*5/100
    return bill_amount


gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

price_list=[1760,2119,1599,3920,3999]

reqd_gems=["Ivory","Emerald","Garnet"]

reqd_quantity=[3,10,12]


# gems_list=['Moonstone', 'Sapphire', 'Quartz']
# price_list=[3498, 1257, 5467]
# reqd_gems=['Ivory']
# reqd_quantity=[10]


bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)



