import tkinter as tk
from tkinter import messagebox

# PL Alphabet 
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZĄĆĘŁŃÓŚŹŻ"


def create_polybius_square():
    """
    Create a Polybius square of size 6x6 
    """
    return [ALPHABET[i:i + 6] for i in range(0, len(ALPHABET), 6)]


def find_coordinates(matrix, char):
    """
    Find the coordinates of a character in the Polybius square
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == char:
                return row + 1, col + 1  # Use 1-based indexing for the cipher
    return None


def find_char_by_coordinates(matrix, row, col):
    """
    Find the character based on its coordinates in the Polybius square
    """
    return matrix[row - 1][col - 1]  # Convert back to 0-based indexing


def polybius_encrypt(text):
    """
    Encrypt text using the Polybius square
    """
    matrix = create_polybius_square()
    text = text.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    result = []

    for char in text:
        if char in ALPHABET:
            row, col = find_coordinates(matrix, char)
            result.append(str(row) + str(col))
        else:
            continue  # Skip characters not in the alphabet

    return ' '.join(result)


def polybius_decrypt(code):
    """
    Decrypt text using the Polybius square.
    """
    matrix = create_polybius_square()
    codes = code.split()  # Split the code into pairs of digits
    result = []

    for pair in codes:
        if len(pair) == 2 and pair.isdigit():
            row, col = int(pair[0]), int(pair[1])
            if 1 <= row <= 6 and 1 <= col <= 6:
                result.append(find_char_by_coordinates(matrix, row, col))
        else:
            continue  # Skip invalid pairs

    return ''.join(result)


def encrypt_text():
    """
    Function for encrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    encrypted_text = polybius_encrypt(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)


def decrypt_text():
    """
    Function for decrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip()
    decrypted_text = polybius_decrypt(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)


# main window
root = tk.Tk()
root.title("Polybius Square")

# Input text 
tk.Label(root, text="Enter text:").grid(row=0, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Buttons 
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, pady=10)

# result field
tk.Label(root, text="Result:").grid(row=3, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
