num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"The given number {num} is an even number.".format(num))
# elif num%2 != 0:
#     print (f"The given {num} is not an even number.")
else:
    print(f"The given numbers: {num} is an odd number.")