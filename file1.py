x=5
if type(x) is int:
    print("true")
else:
    print("false")

y=5.0
if type(y) is not float:
    print("true")
else:
    print("false")

x=20
y=20
if (x is y):
    print("x & y are same")
z=30
if x is not z:
    print("x & y are not same")
