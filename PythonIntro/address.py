# JSON = Java Script Object Notation
# its similar to XML

"""
i)Write a program to create an address book and write some record in it
ii) Read this address book
"""

import json
book = {
    'daisy': {
        'name': 'daisy',
        'address': '1 Red Street, KS',
        'phone': 798778539
    },
    'lopez': {
        'name': 'lopez',
        'address': '1 Green Street, KS',
        'phone': 758754949
    },
    'adhiambo': {
        'name': 'adhiambo',
        'address': '1 Blue Street, KS',
        'phone': 732050089
    }
}

# Write the address book to a text file (book.txt)
with open('book.txt', 'w') as txt_file:
    for person, details in book.items():
        txt_file.write(f"{person}:\n")
        for key, value in details.items():
            txt_file.write(f"    {key}: {value}\n")
        txt_file.write("\n")

print("Data written to book.txt")

# Read the content of the book.txt file
with open('book.txt', 'r') as txt_file:
    content = txt_file.read()


print("Content of book.txt:")
print(content)

    
