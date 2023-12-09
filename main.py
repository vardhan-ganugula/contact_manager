import json
import os
from tabulate import tabulate

class ContactBook:
    def __init__(self) -> None:
        self.fileName = 'contacts.json'
        if not os.path.exists(self.fileName):
            open(self.fileName, 'x')
    
    def add_contact(self,name : str,phone:int,email:str,address:str) -> bool:
        user_data = {
            name: {
                "phone": phone,
                "email": email,
                "address" : address
            }
        }
        try:
            with open(self.fileName, 'r') as file:
                data = json.loads(file.read())
                if name in (data.keys()):
                    return False
        except json.decoder.JSONDecodeError:
            data = {}
        data.update(user_data)
        update_json = json.dumps(data, indent=2)
        with open(self.fileName, 'w') as file:
            file.write(update_json)
        return True

    def update_contact(self,name : str,phone:int,email:str,address:str) -> bool:
        user_data = {
            name: {
                "phone": phone,
                "email": email,
                "address" : address
            }
        }
        try:
            with open(self.fileName, 'r') as file:
                data = json.loads(file.read())
        except json.decoder.JSONDecodeError:
            data = {}
        data.update(user_data)
        update_json = json.dumps(data, indent=2)
        with open(self.fileName, 'w') as file:
            file.write(update_json)
        return True

    def view_contact(self) -> str:
        try:
            with open(self.fileName, 'r') as file:
                contact_data = json.load(file)
        except json.decoder.JSONDecodeError:
            return "Contact List empty"
        contact_details = []
        for name, details in contact_data.items():
            contact_details.append([name, details['phone'], details['email'], details['address']])
        headers = ['Name', 'Phone', 'Email', 'Address']
        contact_data = (tabulate(contact_details,headers=headers, tablefmt='fancy_grid'))
        return contact_data
    
    def delete_contacts(self, name) -> str:
        try:
            with open(self.fileName, 'r') as file:
                contact_data = json.loads(file.read())
        except:
            return 'Contact Book is empty'
        if name in contact_data:
            del contact_data[name]
        with open(self.fileName, 'w') as file:
            file.write(json.dumps(contact_data, indent=2))
        return "Contact deleted Successfully"
    
    def search_contact(self, info) -> str:
        try:
            with open(self.fileName, 'r') as file:
                contact_data = json.loads(file.read())
        except:
            return 'Contact Book is empty'
        person_info = ''
        if type(info) is str:
            if info in contact_data:
                person_info = [[info, str(contact_data[info]['phone']), contact_data[info]['email'], contact_data[info]['address']]]
        elif type(info) is int:
            for name, details in contact_data.items():
                if details['phone'] == info:
                    person_info = [[name, details['phone'], details['email'], details['address']]]
        person_info = tabulate(person_info, headers=['name', 'phone','email', 'address'], tablefmt='fancy_grid')
        return person_info

def red():
    return ("\033[1;31m ")
def green():
    return ("\033[1;32m ")
def blue():
    return ("\033[1;34m ")
def white():
    return ("\033[1;37m ")
def banner():
    print(f""" \033[1;33m""")

def banner():
    print(f"""{blue()} 
          
  ____            __  __ 
 / ___|          |  \/  |
| |              | |\/| |
| |___           | |  | |
 \____|          |_|  |_|
  contact        Manager 
{red()}          
********** usage **********{green()}
1. Add Contact
2. Update Contact
3. View Contacts
4. Delete Contact
5. Search Contact       
0. Exit
_____________ only integers are allowed ______________  
          {white()}
          """)    
def main():
    cb = ContactBook()
    while True:
        choice = int(input("Enter your Choice : "))
        match(choice):
            case 1: 
                print("\n+++++ Enter the details to add a contact +++++\n")
                name = input('Enter the name of the person : ')
                try:
                    number = int(input("Enter the phone number : "))
                except ValueError:
                    print("only numbers are allowed ")
                email = input("Enter the email : ")
                address = input("Enter the address : ")
                status = cb.add_contact(name=name, phone=number, email=email, address=address)
                if status:
                    print('\n----- Contact saved successfully -----\n')
                else:
                    print("\n----- contact didn't saved. May be a person with same name exists'n")
            case 2:
                print("\n+++++ Enter the details to update a contact +++++\n")
                name = input('Enter the name of the person : ')
                try:
                    number = int(input("Enter the phone number : "))
                except ValueError:
                    print("only numbers are allowed ")
                email = input("Enter the email : ")
                address = input("Enter the address : ")
                status = cb.update_contact(name=name, phone=number, email=email, address=address)
                if status:
                    print('\n----- Contact updated successfully -----\n')
                else:
                    print("\n----- contact didn't update. -----\n")
            case 3:
                print("\n+++++ View Contacts +++++\n")
                contacts = cb.view_contact()
                print(contacts)
            case 4:
                name = input("Enter the Name : ")
                print(cb.delete_contacts(name))
            case 5:
                info = input("Enter the name or phone number : ")
                try:
                    info = int(info)
                    print(cb.search_contact(info))
                except ValueError:
                    print(cb.search_contact(info))
            case 0: break
            case _ : print('\nonly numbers are allowed\n')
if __name__ == "__main__":
    banner()
    main()
    print('program exited successfully')
