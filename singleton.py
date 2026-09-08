class Printer:
    obj = None

    def __new__(cls):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj

    def print_doc(self, name):
        print(name, "is printing")

# Creating objects
p1 = Printer()
p2 = Printer()

# Using the printer
p1.print_doc("Alice")
p2.print_doc("Bob")

# Verify only one object exists
print(id(p1))
print(id(p2))