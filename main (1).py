

class Donor:
    def _init_(self, name, age, blood_group, contact_number):
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.contact_number = contact_number

    def _str_(self):
        return f"Name: {self.name}, Age: {self.age}, Blood Group: {self.blood_group}, Contact Number: {self.contact_number}"

donors = []

def add_donor():
    name = input("Enter Donor Name: ")
    age = int(input("Enter Donor Age: "))
    blood_group = input("Enter Blood Group: ")
    contact_number = input("Enter Contact Number: ")

    donor = Donor(name, age, blood_group, contact_number)
    donors.append(donor)

    print("Donor added successfully!")

def view_donors():
    if not donors:
        print("No donors available.")
    else:
        print("List of Donors:")
        for donor in donors:
            print(donor)

while True:
    print("Blood Donation System Menu:")
    print("1. Add Donor")
    print("2. View Donors")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_donor()
    elif choice == 2:
        view_donors()
    elif choice == 3:
        print("Exiting Blood Donation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")