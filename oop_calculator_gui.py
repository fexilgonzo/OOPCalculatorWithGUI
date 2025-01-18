import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self):
        # Initialize the Tkinter window
        self.window = tk.Tk()
        self.window.title("Simple Calculator")

        # Entry widget for user input/output
        self.input_field = tk.Entry(self.window, width=20, font=("Arial", 16), justify='right')
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create calculator buttons
        self.create_buttons()

        # Start the Tkinter event loop
        self.window.mainloop()

    def create_buttons(self):
        # Define the button labels and positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons dynamically
        for (text, row, col) in buttons:
            tk.Button(self.window, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

    def on_button_click(self, button_text):
        # Handle button clicks
        if button_text == "C":
            self.input_field.delete(0, tk.END) # Clear the input field
        elif button_text == "=":
            try:
                expression = self.input_field.get()
                result = self.evaluate_expression(expression) # A simple evaluation of the expression
                self.input_field.delete(0, tk.END)
                self.input_field.insert(tk.END, str(result))
            except Exception:
                messagebox.showerror("Error", "Invalid input") # Show error for invalid expressions/input
        else:
            self.input_field.insert(tk.END, button_text) # Add button text to input field

    def evaluate_expression(self, expression):
        # Evaluate arithmetic expressions manually
        if "+" in expression:
            a, b = map(float, expression.split("+"))
            return self.add(a, b)
        
        elif "-" in expression:
            a, b = map(float, expression.split("-"))
            return self.subtract(a, b)
        
        elif "*" in expression:
            a, b = map(float, expression.split("*"))
            return self.multiply(a, b)
        elif "/" in expression:
            a, b = map(float, expression.split("/"))
            return self.divide(a, b)
        else:
            raise ValueError("Unsupported operation")
        
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return a / b

if __name__=="__main__":
    SimpleCalculator()