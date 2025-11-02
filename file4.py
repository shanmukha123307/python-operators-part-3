ch = input("Enter any alphabet: ")
if len(ch) == 1 and ch.isalpha():
    print(f"The ASCII value of '{ch}' is {ord(ch)}")
else:
    print("Please enter a single alphabet only.")
