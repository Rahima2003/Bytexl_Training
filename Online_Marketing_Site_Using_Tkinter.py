import tkinter as tk
from tkinter import ttk

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: ${self.price:.2f}"


class Electronics(Product):
    def __init__(self, product_id, name, price, brand, model):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.model = model

    def display_product(self):
        return super().display_product() + f"\nBrand: {self.brand}\nModel: {self.model}\nCategory: Electronics"


class Clothing(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_product(self):
        return super().display_product() + f"\nSize: {self.size}\nColor: {self.color}\nCategory: Clothing"


def display_electronics():
    details_label.config(text=e_product.display_product())


def display_clothing():
    details_label.config(text=c_product.display_product())


# Create instances of Electronics and Clothing classes
e_product = Electronics("E1001", "Laptop", 1200.50, "Dell", "XPS 13")
c_product = Clothing("C2001", "T-shirt", 25.99, "M", "Blue")

# Create Tkinter window
root = tk.Tk()
root.title("Online Marketing Site")

# Create labels and buttons
title_label = ttk.Label(root, text="Online Marketing Site", font=("Arial", 20))
title_label.pack(pady=20)

electronics_button = ttk.Button(root, text="Electronics", command=display_electronics)
electronics_button.pack(pady=10)

clothing_button = ttk.Button(root, text="Clothing", command=display_clothing)
clothing_button.pack(pady=10)

details_label = ttk.Label(root, text="", font=("Arial", 12))
details_label.pack(pady=20)

# Display the Tkinter window
root.mainloop()
