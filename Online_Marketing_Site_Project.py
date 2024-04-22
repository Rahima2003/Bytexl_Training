# Parent class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price:.2f}")

# Electronics subclass
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        self.brand = brand
        self.warranty = warranty
        super().__init__(product_id, name, price)
    
    def display_product(self):
        super().display_product()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty} months")

# Clothing subclass
class Clothing(Product):
    def __init__(self, product_id, name, price, size, color):
        self.size = size
        self.color = color
        super().__init__(product_id, name, price)
    
    def display_product(self):
        super().display_product()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")

# Example usage
if __name__ == "__main__":
    # Creating instances of Electronics and Clothing
    laptop = Electronics(1, "Laptop", 100000, "Dell", 12)
    t_shirt = Clothing(2, "T-Shirt", 5000, "M", "Blue")

    # Displaying product details
    print("Electronics Details:")
    laptop.display_product()
    print("\nClothing Details:")
    t_shirt.display_product()
