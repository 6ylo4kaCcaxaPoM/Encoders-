import tkinter as tk
from tkinter import messagebox

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZĄĆĘŁŃÓŚŹŻ"


def caesar_cipher(text, shift):
    """
    cipher
    """
    result = []
    for char in text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            new_index = (index + shift) % len(ALPHABET)
            result.append(ALPHABET[new_index])
        else:
            continue  # Ignore other symbols
    return ''.join(result)

def encrypt_text():
    """
    A function for encrypting text
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    invalid_chars = [char for char in input_text if char not in ALPHABET and char != ' ']
    if invalid_chars:
        messagebox.showerror("Error", f"Invalid characters found: {''.join(invalid_chars)}")
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter the correct number for the offset!")
        return

    encrypted_text = caesar_cipher(input_text.replace(" ", ""), shift)  # Removing spaces
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)


def decrypt_text():
    """
    A function for decrypting text.
    """
    input_text = input_text_box.get("1.0", tk.END).strip().upper()
    invalid_chars = [char for char in input_text if char not in ALPHABET and char != ' ']
    if invalid_chars:
        messagebox.showerror("Error", f"Invalid characters found: {''.join(invalid_chars)}")
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter the correct number for the offset!")
        return

    decrypted_text = caesar_cipher(input_text.replace(" ", ""), -shift)  # Removing spaces
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)



# Main window
root = tk.Tk()
root.title("Caesar's cipher")

# InputText block 
tk.Label(root, text="Enter text:").grid(row=0, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Field for entering an offset
tk.Label(root, text="Displacement:").grid(row=2, column=0, sticky="w")
shift_entry = tk.Entry(root)
shift_entry.grid(row=2, column=1, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, pady=10)

# Output text
tk.Label(root, text="Outcome:").grid(row=4, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
