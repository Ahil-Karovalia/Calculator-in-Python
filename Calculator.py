import tkinter as tk
import math

class Calculator:
    def __init__(self):
        # Initialize the main application window
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("500x600")  # Size to fit all buttons adjested for the buttons size

        # Display entry that spans across all button columns
        self.display = tk.Entry(self.root, font=('Arial', 24), bd=10, insertwidth=2, borderwidth=4, width=22)
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew")  # Span across 5 columns

        # List of button labels for the calculator
        buttons = [
            '1', '2', '3', '+', '-', 
            '4', '5', '6', '*', '/',
            '7', '8', '9', '^', 'e',
            '0', 'log', 'pi', 'exp', '=',
            'sin', 'cos', 'tan', 'ln', 'C'
        ]

        row = 1  # Starting row for buttons
        col = 0  # Starting column for buttons

        # Loop to create each button
        for button in buttons:
            # Create standard buttons (e.g., numbers, operators)
            if button not in {'=', 'C'}:
                b = tk.Button(self.root, text=button, width=8, height=3, font=('Arial', 18),
                              command=lambda b=button: self.on_button_click(b))
            else:
                # Special handling for '=' and 'C' buttons
                if button == '=':
                    b = tk.Button(self.root, text=button, width=8, height=3, font=('Arial', 18), bg='green',
                                  command=self.evaluate)
                else:
                    b = tk.Button(self.root, text=button, width=8, height=3, font=('Arial', 18), bg='red',
                                  command=self.clear)

            # Place the button on the grid
            b.grid(row=row, column=col, sticky="nsew")  # Ensures buttons are next to each other
            col += 1
            if col == 5:  # Move to the next row after 5 buttons
                col = 0
                row += 1

        # Configure grid layout to make rows and columns expand proportionally
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):  # Adjusted for number of button rows
            self.root.grid_rowconfigure(i, weight=1)

        # Start the main loop for the Tkinter GUI
        self.root.mainloop()

    def on_button_click(self, char):
        """Handle button clicks for numbers, constants, and operations."""
        if char == 'pi':
            self.display.insert(tk.END, str(math.pi))
        elif char == 'e':
            self.display.insert(tk.END, str(math.e))
        else:
            self.display.insert(tk.END, char)

    def evaluate(self):
        """Evaluate the expression in the display entry."""
        try:
            expression = self.display.get()
            expression = expression.replace('^', '**')  # Convert power symbol
            # Replace functions with their math module equivalents
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('exp', 'math.exp')
            # Evaluate and display the result
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            # Display an error if evaluation fails
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def clear(self):
        """Clear the display entry."""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    Calculator()
