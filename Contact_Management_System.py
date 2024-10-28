import re
#^importing regex
#main set for all contacts
contacts = {}

#UI menu
def display_menu():
    print("Welcome to the Contact Management System!")
    print("1. Add a new contact")
    print("2. Edit a contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a file")
    print("7. Import contacts from a file")
    print("8. Quit")
#phone number validation
def is_valid_phone(phone):
    return re.match(r'^\d{10}$', phone)
#email validation
def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

#function to add contacts
def add_contact():
    phone = input("Enter phone number (10 digits): ")
    if not is_valid_phone(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        return
    if phone in contacts:
        print("Contact already exists.")
        return

    name = input("Enter name: ")
    email = input("Enter email: ")
    if email and not is_valid_email(email):
        print("Invalid email format. Please try again.")
        return

    contacts[phone] = {'Name': name, 'Email': email}
    print("Contact added.")
    
#function to edit contacts
def edit_contact():
    phone = input("Enter phone number of the contact to edit: ")
    if phone not in contacts:
        print("Contact not found.")
        return

    name = input("Enter new name: ")
    email = input("Enter new email: ")
    if email and not is_valid_email(email):
        print("Invalid email format. Please try again.")
        return

    if name:
        contacts[phone]['Name'] = name
    if email:
        contacts[phone]['Email'] = email
    print("Contact updated.")
    
#function to delete contacts
def delete_contact():
    phone = input("Enter phone number to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted.")
    else:
        print("Contact not found.")
        
#function to search for contacts
def search_contact():
    phone = input("Enter phone number to search: ")
    if phone in contacts:
        print(contacts[phone])
    else:
        print("Contact not found.")
        
#function to display contacts
def display_all_contacts():
    if not contacts:
        print("No contacts available.")
    for phone, info in contacts.items():
        print(f"{phone}: {info}")
        
#function to export contacts
def export_contacts():
    with open("contacts.txt", "w") as file:
        for phone, info in contacts.items():
            file.write(f"{phone},{info['Name']},{info['Email']}\n")
    print("Contacts exported.")
    
#function to import contacts
def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                phone, name, email = line.strip().split(',')
                if is_valid_phone(phone) and is_valid_email(email):
                    contacts[phone] = {'Name': name, 'Email': email}
        print("Contacts imported.")
    except FileNotFoundError:
        print("No file found.")
        
#main app function
def main():
    while True:
        display_menu()
        choice = input("Choose an option 1-8: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            
main()
