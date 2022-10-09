#email validation

s=input("email= ")

if "@gmail.com" in s and len(s)>10:
    print("valid")
else:
    print("invalid")