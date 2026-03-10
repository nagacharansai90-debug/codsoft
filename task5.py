contacts={}

def add_contacts():
    name=input("Enter the contact name:")
    num=input("Enter the contact number:")
    email=input("Enter the contact email:")
    address=input("Enter the contact address:")
    contacts[name]={
        "number":num,
        "email":email,
        "address":address
    }
    print(f"contact '{name}' added successfully!")

def view_saved_contacts():
    print("Saved contacts:....")
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Number: {details['number']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("-------------")

def search_contacts():
    search=input("Enter the contact name or number to search:")
    found = [name for name, details in contacts.items() if search.lower() in name.lower() or search.lower() in details['number'].lower()]
    if found:
        print("Search results:")
        for name in found:
            details = contacts[name]
            print(f"Name: {name}")
            print(f"Number: {details['number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-------------")
    else:
        print("No contacts found matching the search criteria.")


def update_contacts():
    name=input("Enter the contact name to update:")
    if name in contacts:
        num=input("Enter the new contact number:")
        email=input("Enter the new contact email:")
        address=input("Enter the new contact address:")
        contacts[name]={
            "number":num,
            "email":email,
            "address":address
        }
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contacts():
    name=input("Enter the contact name to delete:")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")


print("Welcome to the Contact Manager!")
pw=input("Enter the password to access your contacts:")
if pw=="1234":
    print("Correct password! Access granted.")
    while True:
        print("-- Contact Manager --")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contacts")
        print("5. Delete Contact")
        print("6. Exit")

        choice=input("Enter your choice (1-6):")

        if choice=='1':
            add_contacts()
        elif choice=='2':
            view_saved_contacts()
        elif choice=='3':
            search_contacts()
        elif choice=='4':
            update_contacts()
        elif choice=='5':
            delete_contacts()
        elif choice=='6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
else:
    print("Access denied! Incorrect password.")
