#temp = 15 
temp = int(input("Enter the temperature: "))
if temp >= 25:
    print("It is so hot.")
elif temp <= 15 and temp <25:
    print("The temp is okay.")
else:
    print("It is cold.")