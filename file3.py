print("enter marks for 6 subject")
maths=int(input("enter maths marks:"))
science=int(input("enter science marks:"))
sst=int(input("enter sst marks:"))
hindi=int(input("enter hindi marks:"))
computer=int(input("enter computer marks:"))
english=int(input("enter english marks:"))
avrage=(maths+hindi+english+science+computer)/6
if avrage>=91 and avrage <=100:
    print("your grade is A1 :)")
elif avrage>=81 and avrage<91:
    print("your grade is A2 :) ")
else:
    print("invalid input :(")