import tkinter as tk
from tkinter import messagebox


# Alphabet with PL letters
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZĄĆĘŁŃÓŚŹŻ"


def vigenere_encrypt(text, key):
    """
    Text encryption using Vigenère's method.
    """
    key = key.upper()  # Bring the key to uppercase
    result = []
    key_index = 0

    for char in text:
        if char in ALPHABET:
            text_index = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_index_value = ALPHABET.index(key_char)
            new_index = (text_index + key_index_value) % len(ALPHABET)
            result.append(ALPHABET[new_index])
            key_index += 1
        else:
            continue  # Ignore characters that are not in the alphabet
    return ''.join(result)


def vigenere_decrypt(text, key):
    """
    Text decryption using Vigenère's method.
    """
    key = key.upper()  # Bring the key to uppercase
    result = []
    key_index = 0

    for char in text:
        if char in ALPHABET:
            text_index = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_index_value = ALPHABET.index(key_char)
            new_index = (text_index - key_index_value) % len(ALPHABET)
            result.append(ALPHABET[new_index])
            key_index += 1
        else:
            continue  # Ignore characters that are not in the alphabet
    return ''.join(result)


def encrypt_text():
    """
    A function for encrypting text.
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    key = key_entry.get().strip().upper()

    if not key.isalpha():
        messagebox.showerror("Error", "The key must contain only letters!")
        return

    encrypted_text = vigenere_encrypt(input_text, key)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)


def decrypt_text():
    """
    A function for decrypting text.
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    key = key_entry.get().strip().upper()

    if not key.isalpha():
        messagebox.showerror("Error", "The key must contain only letters!")
        return

    decrypted_text = vigenere_decrypt(input_text, key)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)


# Main window
root = tk.Tk()
root.title("Vigenère cipher")

# Input box
tk.Label(root, text="Enter text:").grid(row=0, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Input box key
tk.Label(root, text="Key:").grid(row=2, column=0, sticky="w")
key_entry = tk.Entry(root)
key_entry.grid(row=2, column=1, pady=5)

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, pady=10)

# Output box
tk.Label(root, text="Result:").grid(row=4, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()
