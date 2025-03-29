#a program that takes ages of two people as inpure fromt the user and compare 

person1 = int(input("Enter the age of a user:"))
person2 = int(input("Enter the age of another user:"))

print(f"{person1 == person2}, They are of same age.")
print(f"{person1 != person2}, They are not of same age.")
print(f"{person1 > person2}, Person 1 is older than Person 2.")
print(f"{person1 < person2}, Person 2 is smaller than Person 1.")
print(f"{person1 >= person2} Person 1 older or equal to Person 2.")
print(f"{person1 <= person2}, Person 2 is smaller or equal to Person 1.")

#print(f"The names are {names}")
# if person1 == person2:
#     print("They both are of same age")
# else:
#     print("They both are diff age")

