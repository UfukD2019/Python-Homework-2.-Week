print("********** Number Guessing Game **********\n\n\n")
for i in range (1,6):
 print(i)
 guess=input("""This is a number guessing program.
Please guess a number from 1 to 10.\n""")
 number="5"
 if guess!=number:
     if i==1:
         print("Unfortunately!!! You could not find in first trial. Please try once more.")
     if i==2:
         print("Unfortunately!!! You could not find in second trial. Please try once more.")
     if i==3:
         print("Unfortunately!!! You could not find in third trial. Please try once more.")
     if i==4:
         print("Unfortunately!!! You could not find in fourth trial. Please try once more but be careful! THIS IS LAST TRIAL.")
     if i==5:
         print("YOU LOST.")
         break
 if guess==number:
     if i==1:
         print("Congratulations!!! You found in first trail. ***")
         break
     if i==2:
         print("Congratulations!!! You found in second trail. **")
         break
     if i==3:
         print("Congratulations!!! You found in third trail. **")
         break
     if i==4:
         print("Congratulations!!! You found in fourth trail. *")
         break
     if i==5:
         print("Congratulations!!! You found in fifth trail. *")
         break


        
    
        
