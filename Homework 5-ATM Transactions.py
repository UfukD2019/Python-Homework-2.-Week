print("********** ATM Transactions **********\n\n\n")
balance=1000
print(""" Welcome to the X Bank
Dear Costumer,
How can I help you? What would you like to do?
For Balance Check "Please press 1"
For Deposit       "Please press 2"
For Withdrawal    "Please press 3"
""")
while True:
 transaction=input("Please enter the transaction code.\n")
 if transaction=="1":
    print("Your balance is: ",balance,"Euro.\n")
    other=input("""Would you like to do another transaction?
Please press "Y" for YES, "N" for NO.
""")
    if other=="y" or other=="Y":
        continue
    elif other=="n" or other=="N":
        print("Your transaction has ended. Thank you. Have a good day.")
        break
 elif transaction=="2":
    deposit=float(input("Please enter the amount you would like to deposit.\n"))
    balance+=deposit
    print("Your transaction is succesfully completed. Your current balance is:",balance,"Euro.\n")
    other1=input("""Would you like to do another transaction?
Please press "Y" for YES, "N" for NO.
""")
    if other1=="y" or other1=="Y":
        continue
    elif other1=="n" or other1=="N":
        print("Your transaction has ended. Thank you. Have a good day.")
        break
 elif transaction=="3":
     withdrawal=float(input("Please enter the amount you would like to withdraw.\n"))
     if balance>=withdrawal:
         balance-=withdrawal
         print("Your transaction is succesfully completed. Your current balance is:",balance,"Euro.\n")
         other2=input("""Would you like to do another transaction?
Please press "Y" for YES, "N" for NO.
""")
         if other2=="y" or other2=="Y":
            continue
         elif other2=="n" or other2=="N":
            print("Your transaction has ended. Thank you. Have a good day.")
            break
     else:
         print("Your balance is not sufficient. You can not withdraw more than balance.\nPlease check the amount.\n")
         other3=input("""Would you like to do another transaction?
Please press "Y" for YES, "N" for NO.
""")
         if other3=="y" or other3=="Y":
            continue
         elif other3=="n" or other3=="N":
            print("Your transaction has ended. Thank you. Have a good day.")
            break
            
        
     
