import tkinter as tk
from tkinter import messagebox

# Alphabet (Latin and Polish letters)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZĄĆĘŁŃÓŚŹŻ"


def create_polybius_square():
    """
    Creating a 6x6 Polybius square (for the alphabet with Polish letters)
    """
    return [ALPHABET[i:i + 6] for i in range(0, len(ALPHABET), 6)]


def find_coordinates(matrix, char):
    """
    Finding the coordinates of the symbol in the Polybius square
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == char:
                return row + 1, col + 1  # We use 1-indexing for the cipher
    return None


def find_char_by_coordinates(matrix, row, col):
    """
    Finding a symbol by its coordinates in the Polybius square
    """
    return matrix[row - 1][col - 1]  # Convert back to 0-indexing


def apply_encryption_formula(x, a, b):
    """
    Application of the equation y = ax^2 + b
    """
    return (a * x ** 2 + b) % 6 + 1  # The result is always within [1, 6]


def polybius_encrypt(text, a, b):
    """
    Text encryption
    """
    matrix = create_polybius_square()
    text = text.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    result = []

    for char in text:
        if char in ALPHABET:
            row, col = find_coordinates(matrix, char)           
            encrypted_row = apply_encryption_formula(row, a, b)
            encrypted_col = apply_encryption_formula(col, a, b)
            result.append(f"{encrypted_row}{encrypted_col}")
        else:
            continue  # Skip characters that are not in the alphabet

    return ' '.join(result)


def polybius_decrypt(code, a, b):
    """
    Text decryption
    """
    matrix = create_polybius_square()
    inverse_mapping = {apply_encryption_formula(x, a, b): x for x in range(1, 7)}
    codes = code.split()  
    result = []

    for pair in codes:
        if len(pair) == 2 and pair.isdigit():
            encrypted_row, encrypted_col = int(pair[0]), int(pair[1])
            if encrypted_row in inverse_mapping and encrypted_col in inverse_mapping:
                row = inverse_mapping[encrypted_row]
                col = inverse_mapping[encrypted_col]
                result.append(find_char_by_coordinates(matrix, row, col))
        else:
            continue

    return ''.join(result)


def encrypt_text():
    """
    A function for encrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
    except ValueError:
        messagebox.showerror("Error", "The coefficients a and b must be integers!")
        return

    encrypted_text = polybius_encrypt(input_text, a, b)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)


def decrypt_text():
    """
    Function for decrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip()
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
    except ValueError:
        messagebox.showerror("Error", "The coefficients a and b must be integers!")
        return

    decrypted_text = polybius_decrypt(input_text, a, b)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)


# Main window
root = tk.Tk()
root.title("Polybius square with encryption measure")

# Text field
tk.Label(root, text="Input text").grid(row=0, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# a & b
tk.Label(root, text="Coefficients a:").grid(row=2, column=0, sticky="w")
a_entry = tk.Entry(root)
a_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Coefficients b:").grid(row=3, column=0, sticky="w")
b_entry = tk.Entry(root)
b_entry.grid(row=3, column=1, pady=5)

# buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=4, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=4, column=1, pady=10)

# Answer field
tk.Label(root, text="Outcome:").grid(row=5, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()