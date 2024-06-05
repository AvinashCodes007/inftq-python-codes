def calculate_loans(account_number,account_balance,salary,loan_type,loan_amount_expected,customber_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    if (account_number>999 and account_number<2000):
        if (account_balance>100000):
            if (salary>25000 and loan_type=="Car"):
                eligible_loan_amount=500000
                bank_emi_expected=36
                if (customber_emi_expected<=bank_emi_expected and loan_amount_expected<=eligible_loan_amount):
                    print("Account number:",account_number)
                    print("the customber can avail for the  amount of Rs.",eligible_loan_amount)
                    print("Eligible emi:",bank_emi_expected)
                    print("Requested loan amount:",loan_amount_expected)
                    print("Requested EMI's:",customber_emi_expected)
                else:
                    print("the customber  is not eligible for the loan")
            
            elif(salary>50000 and (loan_type=="Car" or loan_type=="House")):
                eligible_loan_amount=6000000
                bank_emi_expected=60
                if (customber_emi_expected<=bank_emi_expected and loan_amount_expected<=eligible_loan_amount):
                    print("Account numbar:",account_number)
                    print("the customber can avail for the amount of  Rs.",eligible_loan_amount)
                    print("Eligible emi:",bank_emi_expected)
                    print("Requested loan amount:",loan_amount_expected)
                    print("Requested EMI's:",customber_emi_expected)
                else:
                    print("the customber is  not eligible for the loan")

            elif (salary>75000 and (loan_type=="Car" or loan_type=="House" or loan_type=="Business")):
                eligible_loan_amount=7500000
                bank_emi_expected=84
                if (customber_emi_expected<=bank_emi_expected and loan_amount_expected<=eligible_loan_amount):

                    print("Account number:",account_number)	
                    print("the customber can available for the amount of Rs. ",eligible_loan_amount)
                    print("Eligible emi:",bank_emi_expected)
                    print("Requested loan amount:",loan_amount_expected)
                    print("Requested EMI's:",customber_emi_expected)
                else:
                    print("the customber is  not eligible for the loan")

            else:
                print("Invallid loan type or salary ")
        else: 
            print("Insufficient account balance ")
    else:
        print("Invalid account number")

calculate_loans(1002,100200,76000,"Car",5500000,30)