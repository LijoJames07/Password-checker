def check_password(password):
    score=0
    if len(password)>=8:
        score+=1
    else:
        print("Password must consist of atleast 8 characters")
    if any(c.isdigit() for c in password):
        score+=1
    else:
        print("Include numbers")
    if any(c.islower() for c in password):
        score+=1
    else:
        print("Include lower case letters")
    if any(c.isupper() for c in password):
        score+=1
    else:
        print("Include upper case letters")
    if any(c in "!@#$^%&*?" for c in password):
        score+=1
    else:
        print("Include special characters")
    if score<=2:
        strength="Weak"
    elif score<=4:
        strength="Medium"
    else:
        strength="Strong"
    return strength
    
password=input("Enter your Password: ")
strength=check_password(password)
print("\n Password Strength is :",strength)
