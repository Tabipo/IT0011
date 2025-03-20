class item:
    file_name = "items.txt"
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def create(self):
        file = open(self.file_name, "a")
        self.id = input("Enter Item ID: ")
        self.name = input("Enter Item Name: ")
        self.description = input("Enter Item Description: ")
        self.price = input("Enter Item Price: ")
        item_record = (
            "Item ID: {}\n"
            "Item Name: {}\n"
            "Item Description: {}\n"
            "Item Price: {}\n"
            "---------------------------------\n"
        ).format(self.id, self.name, self.description, self.price)
        file.write(item_record)
        file.close()
        print("Item Created\n")

    def read(self):
        file = open(self.file_name, "r")
        records = file.readlines()
        for record in records:
            print(record)
    
    def update(self):
        find_id = input("Enter Item ID to update: ")
        file = open(self.file_name, "r")
        records = file.read().split("\n---------------------------------\n")
        file.close()

        updated_records = []
        item_found = False
        for record in records:
            if record.strip().startswith("Item ID: " + find_id):
                item_found = True
                print("Item Found:\n")
                print(record)
                print("\nEnter new data")
                self.id = input("Enter Item ID: ")
                self.name = input("Enter Item Name: ")
                self.description = input("Enter Item Description: ")
                self.price = input("Enter Item Price: ")
                new_item_record = (
                    "\nItem ID: {}\n"
                    "Item Name: {}\n"
                    "Item Description: {}\n"
                    "Item Price: {}\n"
                    "---------------------------------"
                ).format(self.id, self.name, self.description, self.price)
                updated_records.append(new_item_record)
            else:
                updated_records.append(record)
        if item_found:
            file = open(self.file_name, "w")
            for record in updated_records:
                file.write(record)
            file.close()
            print("Item Updated\n")

    def delete(self):
        find_id = input("Enter Item ID: ")
        file = open("items.txt", "r")
        records = file.read().split("\n---------------------------------\n")
        file.close()

        print("Searching for Item: " + find_id)

        updated_records = []
        item_found = False
        for record in records:
            if record.strip().startswith("Item ID: " + find_id):
                item_found = True
                print("Item Record Found:\n")
                print(record)
                print("\nDeleting Record...")
            else:
                updated_records.append(record)
        if item_found:
            file = open("items.txt", "w")
            file.writelines("\n---------------------------------\n" .join(updated_records))
            file.close()
            print("Item Record Updated\n")
        else:
            print("Item Record Not Found\n")

choice = ""
while choice != "Q" and choice != "q":
    print("Item Management System")
    print("[C] - Create Item")
    print("[R] - Read Items")
    print("[U] - Update Item")
    print("[D] - Delete Item")
    print("[Q] - Quit")
    choice = input("Enter your choice: ")

    if choice == "C" or choice == "c":
        item1 = item("", "", "", "")
        item1.create()
    elif choice == "R" or choice == "r":
        item1 = item("", "", "", "")
        item1.read()
    elif choice == "U" or choice == "u":
        item1 = item("", "", "", "")
        item1.update()
    elif choice == "D" or choice == "d":
        item1 = item("", "", "", "")
        item1.delete()