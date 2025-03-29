#a program that takes age and citizenship stat of person and use to check if they are eligible to vote 

person_age = int(input("Enter your age:"))
citizen_stat = str(input("Are you a citizen? (yes/no):").strip().lower())
isCitizen = citizen_stat == "yes" #checking eligibility


if person_age >= 18 and isCitizen:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")