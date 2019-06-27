print("********** Username and Password Character Check **********\n\n\n")
print("""This is a username and password creation program.
There are some crucial rules while creating username and password.

* Username can be created between 3 and 18 characters.
* Username can not be created with using even one single digit.
* Password can be created between 6 and 12 characters.
""")
while True:
 digit=["0","1","2","3","4","5","6","7","8","9"]
 username=input("Please create a username (between 3 and 18 characters and not include digit)\n")
 if not username or username==" "*len(username):
     print("""Username can not be empty.
Please check username and read the instructions.
""")
     continue
 for i in username:
     pass
 if len(username)<3 or len(username)>18:
      print("""Username can be created between 3 and 18 characters.
Please check username and read the instructions.
""")
      continue
 elif i in digit:
      print("""Username can not be created with using even one single digit.
Please check username and read the instructions.
""")
      continue
 else:
     print("Your username has been successfully created.\n")
     break
while True:
 password=input("Please create a password (between 6 and 12 characters)\n")
 if len(password)<6 or len(password)>12:
     print("""Password can be created between 6 and 12 characters.
Please check password and read the instructions.
""")
     continue
 else:
     print("Your password has been successfully created.\n")
     break
print("Your username is ",username,"\n","Your password is ",password,sep="")
new_file=open("Username and Password Character Check.txt","w")
print("Your username is ",username,"\n","Your password is ",password,sep="",file=new_file)
new_file.close()

     
