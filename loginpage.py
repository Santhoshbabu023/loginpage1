import re

user_name = re.compile("^[a-z]+[a-z1-9]+@[a-z0-9]+\.[a-z]{1,3}$")

def register():
    if isValid():
        if(passcode()):
            return login()


def isValid():
    email=input("Enter Email ID")
    if re.fullmatch(user_name, email):
        file = open("Credentials.txt","a+")
        file.write(email)
        file.write(" ")
        file.close()
        return True
        
    else:   
        print("Invalid email")
        isValid()
        
def passcode():
    
    password = input('Enter the password : ')
    Specialchar=['$','@','#','*']
    return_A=True
    if len(password) < 5:
        print('the length of password should be at least 5 char long')
        return_A=False
    if len(password) > 16:
        print('the length of password should be not be greater than 16')
        return_A=False
    if not any(B in Specialchar for B in password):
        print('the password should have at least one of the symbols $@#*')
        return_A=False        
    if not any(B.isdigit() for B in password):
        print('the password should have at least one digit')
        return_A=False
    if not any(B.isupper() for B in password):
        print('the password should have at least one uppercase letter')
        return_A=False
    if not any(B.islower() for B in password):
        print('the password should have at least one lowercase letter')
        return_A=False
    if return_A:
        print('Password Created\n')
        file = open("Credentials.txt","a+")
        file.write(password)
        file.write('\n')
        return True
    
    else:
        passcode()
    return  True

   
def login():
    print("YOU ARE IN LOGIN PAGE\n\n")
    Email = input("Please enter your Email")
    Password = input("Please enter your password")  
    for line in open("Credentials.txt","r+").readlines(): 
        login_info = line.split() 
        if Email== login_info[0]:
          if Password == login_info[1]:
            print("Correct credentials!")
            print("YOU ARE LOGGED IN TO THIS PAGE")
            return True
          else:
            print("wrong Password")
            forget=int(input("Press 1 change Password"))
            if(forget==1):
                new_password=input("Enter new password")
                file = open("Credentials.txt","a+")
                file.write( line.replace( Password, new_password) ) 
                file.close()
                login()
                
            
        else:
            register()
            
    print("Incorrect credentials.")
    return False



print("Please Enter 1 for Register\t2 for Login ")
a=int(input())
if(a==1):
  register()

else:
    login()
  
