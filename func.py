
import os
import json

class JsonAPI:
    """
    JsonAPI class for handling CRUD operations on a JSON file
    in an object-oriented and reusable way.
    """

    def __init__(self, file_path='data.json'):
        """
        Constructor: Initializes the class with a file path and loads existing data.
        """
        self.file_path = file_path
        self.data = []
        self.load_data()

    def load_data(self):
        """
        Loads data from the JSON file if it exists, else initializes with an empty list.
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.data = json.load(file)
            except json.JSONDecodeError:
                print("Warning: JSON file is corrupted or empty. Initializing as empty list.")
                self.data = []
        else:
            self.data = []

    def save_data(self):
        """
        Saves the in-memory data to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_all(self):
        """
        Returns all records.
        """
        return self.data

    def get_by_id(self, item_id):
        """
        Finds an item by its unique 'id'.
        """
        for item in self.data:
            if item.get('id') == item_id:
                return item
        return None

    def add_entry(self, entry):
        """
        Adds a new dictionary entry if 'id' is unique and entry is valid.
        """
        if not isinstance(entry, dict):
            print("Entry must be a dictionary.")
            return False

        if 'id' not in entry:
            print("Entry must contain an 'id' field.")
            return False

        if self.get_by_id(entry['id']):
            print(f"Item with ID {entry['id']} already exists.")
            return False

        self.data.append(entry)
        self.save_data()
        return True

    def update_entry(self, item_id, updates):
        """
        Updates fields of an existing item by ID.
        """
        for idx, item in enumerate(self.data):
            if item['id'] == item_id:
                self.data[idx].update(updates)
                self.save_data()
                return True
        return False

    def delete_entry(self, item_id):
        """
        Deletes an item from the list by ID.
        """
        for item in self.data:
            if item['id'] == item_id:
                self.data.remove(item)
                self.save_data()
                return True
        return False

    def find_by_key(self, key, value):
        """
        Searches for an item where the given key matches the specified value.
        """
        for item in self.data:
            if item.get(key) == value:
                return item
        return None

def main():
    api = JsonAPI()

    while True:
        print("\n--- JSON API MENU ---")
        print("1. Add Entry")
        print("2. View All")
        print("3. Get by ID")
        print("4. Update Entry")
        print("5. Delete Entry")
        print("6. Search by Key")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                blood_type = input("Enter Blood Type: ")
                api.add_entry({"id": id, "name": name, "age": age, "blood group": blood_type})
                print("✅ Entry added successfully.")
            except ValueError:
                print("❌ Invalid input.")
        elif choice == '2':
            print(json.dumps(api.get_all(), indent=4))
        elif choice == '3':
            id = int(input("Enter ID to fetch: "))
            print(api.get_by_id(id))
        elif choice == '4':
            id = int(input("Enter ID to update: "))
            key = input("Enter field to update (e.g., name): ")
            value = input("Enter new value: ")
            success = api.update_entry(id, {key: value})
            print("✅ Updated." if success else "❌ Not found.")
        elif choice == '5':
            id = int(input("Enter ID to delete: "))
            success = api.delete_entry(id)
            print("✅ Deleted." if success else "❌ Not found.")
        elif choice == '6':
            key = input("Enter key to search (e.g., name): ")
            value = input("Enter value to search: ")
            print(api.find_by_key(key, value))
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
    