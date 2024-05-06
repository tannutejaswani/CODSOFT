class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")
    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts
    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(keyword)
            if found_contacts:
                print("Found contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                new_name = input("Enter new name: ")
                new_phone_number = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                new_contact = Contact(new_name, new_phone_number, new_email, new_address)
                contact_book.update_contact(name, new_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted successfully.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
