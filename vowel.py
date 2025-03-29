userinput = input("Enter a word:")
first_char = (userinput.lower()[0]) #.lower() is used so the imput word wouuld be kept in lower char

if first_char == "e" or first_char == "i" or first_char == "a" or first_char == "o" or first_char == "u":
    print("Word is vowel")
else:
    print("Word not vowel")