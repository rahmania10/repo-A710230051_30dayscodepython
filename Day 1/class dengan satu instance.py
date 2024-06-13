class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

# Membuat instance dari kelas MyClass
obj = MyClass("World")

# Memanggil metode greet dari instance
obj.greet()  # Output: Hello, World