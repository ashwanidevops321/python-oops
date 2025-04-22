from abc import ABC, abstractmethod
import json

class Animal(ABC):
    def __init__(self, name, animal_type, eat, sleep, move):
        self.name = name
        self.animal_type = animal_type
        self.eat = eat
        self.sleep = sleep
        self.move = move

    @abstractmethod                       
    def make_sound(self):
        pass

    def describe(self):
        print(f"\n{self.name} is a {self.animal_type} animal that makes a sound: {self.make_sound()}.")
        print(f"It eats: {self.eat}, sleeps: {self.sleep}, and moves: {self.move}.")

    def feed(self):
        print(f"You fed the {self.name}. It enjoys eating {self.eat}.")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "Domestic", "Meat", "8 hours", "Walks")
        
    def make_sound(self):
        return "woof"

class Lion(Animal):
    def __init__(self):
        super().__init__("Lion", "Wild", "Meat", "10 hours", "Runs")
        
    def make_sound(self):
        return "roar"
    
class Cat(Animal):
    def __init__(self):
        super().__init__("Cat", "Domestic", "Meat", "8 hours", "Walks")
        
    def make_sound(self):
        return "meow"
    
class Elephant(Animal):
    def __init__(self):
        super().__init__("Elephant", "Wild", "Grass", "12 hours", "Walks")
        
    def make_sound(self):
        return "trumpet"
    
    def feed(self):
        print(f"You fed the {self.name}. It enjoys eating {self.eat}.")
        
class Tiger(Animal):
    def __init__(self):
        super().__init__("Tiger", "Wild", "Meat", "10 hours", "Runs")
        
    def make_sound(self):
        return "roar"
    
    def feed(self):
        print(f"You fed the {self.name}. It enjoys eating {self.eat}.")
        
class Snake(Animal):
    def __init__(self):
        super().__init__("Snake", "Wild", "Insects", "8 hours", "Crawls")
        
    def make_sound(self):
        return "hiss"
    
    def feed(self):
        print(f"You fed the {self.name}. It enjoys eating {self.eat}.")
        
class Parrot(Animal):
    def __init__(self):
        super().__init__("Parrot", "Domestic", "Seeds", "8 hours", "Flies")
        
    def make_sound(self):
        return "squawk"
    
class Rabit(Animal):
    def __init__(self):
        super().__init__("Rabit", "Domestic", "Carrot", "8 hours", "Hops")
        
    def make_sound(self):
        return "squeak"
    
class Zoo:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("Only animals can be added to the zoo.")
            
    def show_all_animal(self):
        if not self.animals:
            print("No animals in the zoo.")
        for animal in self.animals:
            animal.describe()
            
    def show_by_type(self, animal_type):
        found = False
        print(f"\n--- {animal_type.capitalize()} Animals ---")
        for animal in self.animals:
            if animal.animal_type.lower() == animal_type.lower():
                animal.describe()
                found = True
        if not found:
            print(f"No {animal_type} animals found in the zoo.")
            
    def feed_animals(self):
        if not self.animals:
            print("No animals to feed.")
            for animal in self.animals:
                animal.feed()
        print("All animals have been fed.")
        
    def save_zoo(self, filename="zoo.json"):
        import json
        data = []
        for animal in self.animals:
            animal_data = animal.__dict__.copy()
            animal_data["class_name"] = type(animal).__name__ 
            data.append(animal_data)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    def load_zoo(self, filename="zoo.json"):
        import json
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.animals.clear()
                for animal_data in data:
                    class_name = animal_data.pop("class_name", None)
                    animal = None

                    if class_name == "Dog":
                        animal = Dog()
                    elif class_name == "Lion":
                        animal = Lion()
                    elif class_name == "Cat":
                        animal = Cat()
                    elif class_name == "Elephant":
                        animal = Elephant()
                    elif class_name == "Tiger":
                        animal = Tiger()
                    elif class_name == "Snake":
                        animal = Snake()
                    elif class_name == "Parrot":
                        animal = Parrot()
                    elif class_name == "Rabit":
                        animal = Rabit()

                    if animal:
                        for key, value in animal_data.items():
                            setattr(animal, key, value)
                        self.animals.append(animal)
                    else:
                        print(f"⚠ Unknown or missing class_name: {class_name} — skipping.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error decoding JSON or file not found. Starting with an empty zoo.")


def main():
    zoo = Zoo()
    animal_classes = {
        "Dog": Dog,
        "Lion": Lion,
        "Cat": Cat,
        "Elephant": Elephant,
        "Tiger": Tiger,
        "Snake": Snake,
        "Parrot": Parrot,
        "Rabit": Rabit
    }
    
    try:
        zoo.load_zoo()
    except FileNotFoundError:
        print("No existing zoo data found. Starting with an empty zoo.")
        
    
    while True:
        print("\n--- Zoo Management ---")
        print("1. Add Animal")
        print("2. Show All Animals")
        print("3. Show Animals by Type")
        print("4. Feed Animals")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            animal_type = input("Enter the type of animal (Dog, Lion, Cat, Elephant, Tiger, Snake, Parrot, Rabit): ")
            if animal_type in animal_classes:
                animal = animal_classes[animal_type]()
            else:
                print("Invalid animal type.")
        elif choice == "2":
            zoo.show_all_animal()
        elif choice == "3":
            animal_type = input("Enter the type of animal (Domestic, Wild): ")
            zoo.show_by_type(animal_type)
        elif choice == "4":
            zoo.feed_animals()
        elif choice == "5":
            print("Exiting the zoo management system.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        zoo.save_zoo()
            
if __name__ == "__main__":
    main()