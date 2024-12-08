import tkinter as tk
from tkinter import messagebox


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZĄĆĘŁŃÓŚŹŻ"


def create_polybius_square():
    """
    Creating a 6x6 Polybius square (for the alphabet with Polish letters).
    """
    return [ALPHABET[i:i + 6] for i in range(0, len(ALPHABET), 6)]


def find_coordinates(matrix, char):
    """
    Finding the coordinates of the symbol in Polybius' square.
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == char:
                return row + 1, col + 1  # Use 1-indexing for the cipher
    return None


def find_char_by_coordinates(matrix, row, col):
    """
    Finding a symbol by its coordinates in Polybius' square.
    """
    return matrix[row - 1][col - 1]  # Convert back to 0-indexing


def polybius_encrypt(text):
    """
    Text encryption using the Polybius square method.
    """
    matrix = create_polybius_square()
    text = text.upper().replace(" ", "")  
    result = []

    for char in text:
        if char in ALPHABET:
            row, col = find_coordinates(matrix, char)
            result.append(str(row) + str(col))
        else:
            continue  

    return ' '.join(result)


def polybius_decrypt(code):
    """
    Text decryption by the Polybius square method.
    """
    matrix = create_polybius_square()
    codes = code.split()  # Split the code into pairs of numbers
    result = []

    for pair in codes:
        if len(pair) == 2 and pair.isdigit():
            row, col = int(pair[0]), int(pair[1])
            if 1 <= row <= 6 and 1 <= col <= 6:
                result.append(find_char_by_coordinates(matrix, row, col))
        else:
            continue 

    return ''.join(result)


def encrypt_text():
    """
    A function for encrypting text.
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    encrypted_text = polybius_encrypt(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)


def decrypt_text():
    """
    A function for decrypting text.
    """
    input_text = input_text_box.get("1.0", tk.END).strip()
    decrypted_text = polybius_decrypt(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)



root = tk.Tk()
root.title("Polybius' square")

# Text entry field
tk.Label(root, text="Enter text:").grid(row=0, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, pady=10)

# Field for outputting the result
tk.Label(root, text="Result:").grid(row=3, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()
