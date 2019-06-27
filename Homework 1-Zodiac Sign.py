print("******** The Zodiac Sign Program **********")
while True:
 day=int(input("Please enter your birthday (only day) :\n"))
 month=input("Please enter month of your birthday : \n")
 if (month=="MARCH" or month=="march" and day in range(21,32)) or (month=="APRIL" or month=="april" and day in range(1,21)):
    print("Your Zodiac Sign Name is: Aries")
    break
 elif(month=="APRIL" or month=="april" and day in range(21,31)) or (month=="MAY" or month=="may" and day in range(1,22)):
    print("Your Zodiac Sign Name is: TAURUS")
    break
 elif(month=="MAY" or month=="may" and day in range(22,32)) or (month=="JUNE" or month=="june" and day in range(1,23)):
    print("Your Zodiac Sign Name is: GEMINI")
    break
 elif(month=="JUNE" or month=="june" and day in range(23,31)) or (month=="JULY" or month=="july" and day in range(1,23)):
    print("Your Zodiac Sign Name is: The CRAB")
    break
 elif(month=="JULY" or month=="july" and day in range(23,32)) or (month=="AUGUST" or month=="august" and day in range(1,23)):
    print("Your Zodiac Sign Name is: LEO")
    break
 elif(month=="AUGUST" or month=="august" and day in range(23,32)) or (month=="SEPTEMBER" or month=="september" and day in range(1,23)):
    print("Your Zodiac Sign Name is: VIRGO")
    break
 elif(month=="SEPTEMBER" or month=="september" and day in range(23,31)) or (month=="OCTOBER" or month=="october" and day in range(1,23)):
    print("Your Zodiac Sign Name is: LIBRA")
    break
 elif(month=="OCTOBER" or month=="october" and day in range(23,32)) or (month=="NOVEMBER" or month=="november" and day in range(1,22)):
    print("Your Zodiac Sign Name is: SCORPIO")
    break
 elif(month=="NOVEMBER" or month=="november" and day in range(22,31)) or (month=="DECEMBER" or month=="december" and day in range(1,22)):
    print("Your Zodiac Sign Name is: SAGITTARIUS")
    break
 elif(month=="DECEMBER" or month=="december" and day in range(22,32)) or (month=="JANURARY" or month=="janurary" and day in range(1,22)):
    print("Your Zodiac Sign Name is: CAPRICORN")
    break
 elif(month=="JANURARY" or month=="janurary" and day in range(22,32)) or (month=="FEBRUARY" or month=="february" and day in range(1,20)):
    print("Your Zodiac Sign Name is: AQUARIUS")
    break
 elif(month=="FEBRUARY" or month=="february" and day in range(20,29)) or (month=="MARCH" or month=="march" and day in range(1,21)):
    print("Your Zodiac Sign Name is: PISCES")
    break
 else:
    print("The information you entered is not acceptable.\nPlease check your information and enter your accurate birthday!")
