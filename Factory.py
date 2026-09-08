class Mango:
    def display(self):
        print("Fruit: Mango")

class Apple:    
    def display(self):
        print("Friut: Apple")

class Orange:
    def display(self):
        print("Fruit: Orange")

class FruitFactory:
    def get_fruit(self, fruit_name):
        if fruit_name.lower() == "apple":
            return Apple()
        elif fruit_name.lower() == "mango":
            return Mango()
        elif fruit_name.lower() == "orange":
            return Orange()
        else:
            return None

factory = FruitFactory()

fruit_name = input("Enter fruit (Apple/Mango/Orange): ")

fruit = factory.get_fruit(fruit_name)

if fruit:
    fruit.display()
else:
    print("Invalid fruit!")