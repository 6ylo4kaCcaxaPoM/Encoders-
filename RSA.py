import tkinter as tk
from tkinter import messagebox
import random


def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers.
    """
    while b:
        a, b = b, a % b
    return a


def modular_inverse(a, m):
    """
    Calculate the modular multiplicative inverse (mod m).
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keys():
    """
    Generate a pair of RSA public and private keys.
    """
    primes = [i for i in range(100, 500) if all(i % d != 0 for d in range(2, int(i ** 0.5) + 1))]
    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])
    d = modular_inverse(e, phi)

    return (e, n), (d, n)


def encrypt_message(message, key):
    """
    Encrypt a message using the public key.
    """
    e, n = key
    return [pow(ord(char), e, n) for char in message]


def decrypt_message(encrypted_message, key):
    """
    Decrypt a message using the private key.
    """
    d, n = key
    return ''.join(chr(pow(char, d, n)) for char in encrypted_message)


# Global variables to store the keys
public_key = None
private_key = None


def generate_key_pair():
    """
    Generate RSA keys and display them in the interface.
    """
    global public_key, private_key
    public_key, private_key = generate_keys()
    public_key_label.config(text=f"Public Key: {public_key}")
    private_key_label.config(text=f"Private Key: {private_key}")
    messagebox.showinfo("RSA Keys", "Keys successfully generated!")


def encrypt_text():
    """
    Encrypt text from the input field.
    """
    if not public_key:
        messagebox.showerror("Error", "Generate RSA keys first!")
        return

    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Enter text to encrypt!")
        return

    encrypted = encrypt_message(input_text, public_key)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, ' '.join(map(str, encrypted)))


def decrypt_text():
    """
    Decrypt text from the input field.
    """
    if not private_key:
        messagebox.showerror("Error", "Generate RSA keys first!")
        return

    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Enter encrypted text to decrypt!")
        return

    try:
        encrypted = list(map(int, input_text.split()))
        decrypted = decrypt_message(encrypted, private_key)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Error", "Enter valid encrypted text!")


# Main window
root = tk.Tk()
root.title("RSA Encryptor")

# Field for generating keys
key_frame = tk.Frame(root)
key_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
tk.Button(key_frame, text="Generate Keys", command=generate_key_pair).grid(row=0, column=0, columnspan=2)

# Labels to display keys
public_key_label = tk.Label(root, text="Public Key: Not generated")
public_key_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

private_key_label = tk.Label(root, text="Private Key: Not generated")
private_key_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Field for text
tk.Label(root, text="Enter text:").grid(row=3, column=0, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Buttons 
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=5, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=5, column=1, pady=10)

# Field for result
tk.Label(root, text="Result:").grid(row=6, column=0, sticky="w")
output_text_box = tk.Text(root, height=5, width=40)
output_text_box.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
