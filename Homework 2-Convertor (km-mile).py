print("**********Convertor from km to mile or reverse**********\n\n\n")
print("""This is a conversion program from km to mile or reverse.
Please choose a operation you would like to do;

For conversion from km to mile press "1"
For conversion from mile to km press "2"
""")
while True:
 operation=input("Please enter a operation code\n")
 if operation=="1":
    km=input("Please enter km you would like to convert\n")
    mile = float(km)*0.62131
    print(km,"km =",mile,"mile")
    q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
    if q=="q" or q=="Q":
        print("Program is ending")
        break
    elif q=="n" or q=="N":
        continue
 elif operation=="2":
    mile1=input("Please enter mile you would like to convert\n")
    km1=float(mile1)*1.609
    print(mile1,"mile =",km1,"km")
    q1=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
    if q1=="q" or q1=="Q":
        print("Program is ending")
        break
    elif q1=="n" or q1=="N":
        continue
 else:
    print("You made a mistake. Please check your operation and follow the instructions.\n")
