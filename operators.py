#arthimetic operators
# num1 = 10
# num2 = 20

# print(num1 + num2) #add
# print(num1 - num2) #sub
# print(num1 * num2) #multiplication
# print(num1 / num2) #division
# print(num1 // num2) #nodulues
# print(num1 ** num2) #exponentation as in num1 is 10 ra num2 is 3 so 10*10*10 hunxa

# print(num1 == num2) #to check whether both value are equak or not
# print (num1 != num2) #not equal
# print(num1>num2) #greater
# print(num1<num2) #less
# print(num1>=num2) #greateroreuqual
# print(num1<=num2) #lessthatorequal

##logical operators 
atm_user_id = 10
atm_user_pin = 1217

inputid = int(input("Enter user id"))
inputpin = int(input("Enter pin:"))


#check if the id and pin used is true or not 
#and used to check every is true 
#or used to check even 1 is true
if atm_user_id == inputid and atm_user_pin==inputpin:
    print("login successful")
else:
    print("login failed")
