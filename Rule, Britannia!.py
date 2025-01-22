import tkinter as tk
from tkinter import messagebox


# PL Alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZĄĆĘŁŃÓŚŹŻ"


def prepare_key(key):
    """
    Preparing the key for the matrix: removing repetitive characters.
    """
    seen = set()
    return ''.join([c for c in key.upper() if c in ALPHABET and not (c in seen or seen.add(c))])


def create_playfair_matrix(key):
    """
    cipher matrix
    """
    key = prepare_key(key)
    remaining_letters = ''.join([c for c in ALPHABET if c not in key])
    matrix = key + remaining_letters
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]


def find_position(matrix, char):
    """
    Finding the position of a symbol in a matrix
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_encrypt(text, key):
    """
    Text encryption 
    """
    matrix = create_playfair_matrix(key)
    text = text.upper().replace(' ', '')

    # Split the text into bigrams 
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'  # Fill in X if there is no character
        if a == b:
            b = 'X'
            pairs.append((a, b))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    result = []
    for a, b in pairs:
        if a not in ALPHABET or b not in ALPHABET:
            continue  # Skip the non-alphabetic characters

        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # One line
            result.append(matrix[row_a][(col_a + 1) % 5])
            result.append(matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:  # One column
            result.append(matrix[(row_a + 1) % 5][col_a])
            result.append(matrix[(row_b + 1) % 5][col_b])
        else:  # Different rows and columns
            result.append(matrix[row_a][col_b])
            result.append(matrix[row_b][col_a])

    return ''.join(result)


def playfair_decrypt(text, key):
    """
    Text decryption using the Playfair cipher
    """
    matrix = create_playfair_matrix(key)
    text = text.upper().replace(' ', '')

    pairs = [(text[i], text[i + 1]) for i in range(0, len(text), 2)]
    result = []
    for a, b in pairs:
        if a not in ALPHABET or b not in ALPHABET:
            continue

        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # One line
            result.append(matrix[row_a][(col_a - 1) % 5])
            result.append(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:  # One column
            result.append(matrix[(row_a - 1) % 5][col_a])
            result.append(matrix[(row_b - 1) % 5][col_b])
        else:  # Different rows and columns
            result.append(matrix[row_a][col_b])
            result.append(matrix[row_b][col_a])

    return ''.join(result)


def encrypt_text():
    """
    A function for encrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    key = key_entry.get().strip().upper()

    # Key check
    if not key:
        messagebox.showerror("Error", "The key can't be empty!")
        return
    if any(char not in ALPHABET for char in key):
        messagebox.showerror("Error", "The key contains invalid characters!")
        return

    # text check
    if any(char not in ALPHABET and char != ' ' for char in input_text):
        invalid_chars = ''.join(set(char for char in input_text if char not in ALPHABET and char != ' '))
        messagebox.showerror("Error", f"The text contains invalid characters: {invalid_chars}")
        return

    encrypted_text = playfair_encrypt(input_text, key)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)


def decrypt_text():
    """
    A function for decrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    key = key_entry.get().strip().upper()

    # Key check
    if not key:
        messagebox.showerror("Error", "The key can't be empty!")
        return
    if any(char not in ALPHABET for char in key):
        messagebox.showerror("Error", "The key contains invalid characters!")
        return

    # text check
    if any(char not in ALPHABET and char != ' ' for char in input_text):
        invalid_chars = ''.join(set(char for char in input_text if char not in ALPHABET and char != ' '))
        messagebox.showerror("Error", f"The text contains invalid characters: {invalid_chars}")
        return

    decrypted_text = playfair_decrypt(input_text, key)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)



# Main Window
root = tk.Tk()
root.title("Playfair's cipher")

# Input box
tk.Label(root, text="Enter text:").grid(row=0, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Key box
tk.Label(root, text="Key:").grid(row=2, column=0, sticky="w")
key_entry = tk.Entry(root)
key_entry.grid(row=2, column=1, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, pady=10)

# Output
tk.Label(root, text="Result:").grid(row=4, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
