# Import necessary modules
import string # For accessing character constants
import secrets # For generating a cryptographically secure random password
import pyperclip # For copying the password to the clipboard
import tkinter as tk # For creating the GUI

# Define a class for the password generator GUI
class PasswordGeneratorGUI(tk.Frame):
    # Constructor
    def __init__(self, master=None):
        # Call the constructor of the parent class
        super().__init__(master)
        # Set the master (parent) window and title
        self.master = master
        self.master.title("Password Generator")
        # Set the layout grid
        self.grid()
        # Create the UI elements
        self.createWidgets()
    
    # Method to create the UI elements
    def createWidgets(self):
        ## Password length label and entry
        self.length_label = tk.Label(self, text="Password length:")
        self.length_label.grid(row=0, column=0) # Place the label in row 0, column 0
        self.length_entry = tk.Entry(self)
        self.length_entry.insert(0, "12") # Default length is 12
        self.length_entry.grid(row=0, column=1) # Place the entry in row 0, column 1

        # Checkbuttons for character types
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(self, text="Uppercase letters", variable=self.uppercase_var)
        self.uppercase_checkbutton.select() # Default is checked
        self.uppercase_checkbutton.grid(row=1, column=0, sticky="W") # Place the checkbutton in row 1, column 0, with left alignment

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_checkbutton = tk.Checkbutton(self, text="Lowercase letters", variable=self.lowercase_var)
        self.lowercase_checkbutton.select() # Default is checked
        self.lowercase_checkbutton.grid(row=2, column=0, sticky="W") # Place the checkbutton in row 2, column 0, with left alignment

        self.digits_var = tk.BooleanVar()
        self.digits_checkbutton = tk.Checkbutton(self, text="Digits", variable=self.digits_var)
        self.digits_checkbutton.select() # Default is checked
        self.digits_checkbutton.grid(row=3, column=0, sticky="W") # Place the checkbutton in row 3, column 0, with left alignment

        self.symbols_var = tk.BooleanVar()
        self.symbols_checkbutton = tk.Checkbutton(self, text="Symbols", variable=self.symbols_var)
        self.symbols_checkbutton.select() # Default is checked
        self.symbols_checkbutton.grid(row=4, column=0, sticky="W") # Place the checkbutton in row 4, column 0, with left alignment

        # Generate password button
        self.generate_button = tk.Button(self, text="Generate Password", command=self.generatePassword)
        self.generate_button.grid(row=5, column=0) # Place the button in row 5, column 0

        # Password output label
        self.password_label = tk.Label(self, text="Generated Password: ")
        self.password_label.grid(row=6, column=0) # Place the label in row 6, column 0
        self.password_result = tk.Label(self, text="")
        self.password_result.grid(row=6, column=1) # Place the label in row 6, column 1

        # Copy password to clipboard button
        self.copy_button = tk.Button(self, text="Copy", command=self.copyPassword)
        self.copy_button.grid(row=6, column=3) # Place the button in row 6, column 3

    def generatePassword(self):
        length = int(self.length_entry.get())
        uppercase = self.uppercase_var.get()
        lowercase = self.lowercase_var.get()
        digits = self.digits_var.get()
        symbols = self.symbols_var.get()

        # Define the characters to be used in the password
        characters = ""
        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if digits:
            characters += string.digits
        if symbols:
            characters += string.punctuation

        # Generate a random password
        password = "".join(secrets.choice(characters) for i in range(length))

        self.password_result.config(text=password)

    def copyPassword(self):
        password = self.password_result.cget("text") # Get the generated password from the label
        if password:
            pyperclip.copy(password) # Copy the password to the clipboard using pyperclip


if __name__ == "__main__":
    root = tk.Tk()

    window_width = 500
    window_height = 300

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # root.iconbitmap("img/clock.ico")

    app = PasswordGeneratorGUI(master=root)
    app.mainloop()