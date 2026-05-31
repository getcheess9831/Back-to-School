library = { 
    "python_entry" : { 
        "author" : "John Doe",
        "year" : 2001,
        "availability" : True,
        "Borrower" : None
    },
    "java_entry" : {
        "author" : "Jane Doe",
        "year" : 2002,
        "availability" : True,
        "Borrower" : None
    },
    "C++_entry" : {
        "author" : "Jim Doe",
        "year" : 2003,
        "availability" : True,
        "Borrower" : None
    },
    "JavaScript_entry" : {
        "author" : "Jill Doe",
        "year" : 2004,
        "availability" : True,
        "Borrower" : None
    },
    "C#_entry" : {
        "author" : "Jack Doe",
        "year" : 2005,
        "availability" : True,
        "Borrower" : None
    }
}

def Librarystatus(library):
    print("Book availability status: ")
    for book, details in library.items():
        if details["availability"]:
            print(f"{book} is available for borrowing.")
        else:
            print(f"{book} is currently borrowed by {details['Borrower']}.")

    print(" ")#Adding space for better readability of the output.

def Borrowbook(library, book, borrower):
    if book in library:
        if library[book]["availability"]:
            library[book]["availability"] = False
            library[book]["Borrower"] = borrower
            print(f"{borrower} has borrowed {book}.")
        else:
            print(f"{book} is currently unavailable. It is borrowed by {library[book]['Borrower']}.")
    else:
        print(f"{book} does not exist in the library.")
    
    print(" ")

def Returnbook(library, book):
    if book in library:
        if  library[book]["availability"]:
            print(f"{book} is already available in the library.")
        else:
            library[book]["Borrower"] = None
            library[book]["availability"] = True
            print(f"{book} has been returned and it is available for borrowing.")
    else:
        print(f"{book} does not exist in the library.")
    
    print(" ")
#Librarystatus(library)

Borrowbook(library, "python_entry", "Alice")
Borrowbook(library, "java_entry", "Bob")
Borrowbook(library, "python_entry", "Charlie")
Borrowbook(library, "react_entry", "David")
Returnbook(library, "python_entry")
Returnbook(library, "java_entry")
Borrowbook(library, "python_entry", "Charlie")

Librarystatus(library)

for book, details in library.items():
    status = "available" if details["availability"] else "not available"
    print(f"{book} by {details['author']} published in {details['year']} is {status}, ", end = "")
    if not details["availability"]:
        print(f"borrowed by {details['Borrower']}.")
    else:
        print(".")

print(" ")
#Printing all the books in the library with their details and availability status.










