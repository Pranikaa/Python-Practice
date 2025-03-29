#a program to initialize list of books available in the library

book_names = input("Enter the name of the book:")
available_books = ["Ikigai", "White Nights", "Ijoria", "The seven husbands of evelyn hugo", "Cruel prince"]

print(f"{book_names in available_books}")

if book_names in available_books:
    print(f"The book: {book_names} is available in the libary.")
else:
    print(f"The book: {book_names} is not available in the libary.")