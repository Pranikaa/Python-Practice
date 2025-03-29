# even_num = int(input("Input an even number:"))
# odd_num = int(input("Input a odd number:"))

#A program to check if a given number is ever or odd

num = int(input("Enter a number:"))  #a number is input in string then changed to int

#ifelse is used to check whether the number is odd or even to print
# if the remainder is 1, it is an odd num if not then even
# if (num % 2) == 0:
#     print("{0} is an even number".format(num))
# else:
#     print("{0} is an odd number".format(num))

if (num%2) == 0:
    print("The num is even")
else:
    print("The num is odd.")