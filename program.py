librarian_name = "Pranika" #str
isOpen = True #bool
book_names = ["Ikigai", "The Vegetarian", "Lies"] #list
location_coordinates = (40.098, -23.095) #tuple
contact_details = {
    "phone" : "981909876", 
    "email" : "libarry@gmail.com",
    "address": "123 east red st, Lib St"
} #dict 
genres = {"Fiction", "Non-Fiction", "Thrill"} #set
#print out library information 
print("Library Information")
print(f"The name of the librarian is {librarian_name}")
#print(f"The total number of books are {total_books}")
print(f"IS Library open?:{'Yes' if isOpen else 'No'}")
print(f"List of book names available: {book_names}")
print(f"Locations Coordinates: {location_coordinates}")
print(f"The contact details are {contact_details}")
print(f"The genres availabke in the library are {genres}")