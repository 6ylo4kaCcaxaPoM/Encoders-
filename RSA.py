import random
import math
import tkinter as tk
from tkinter import messagebox

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime():
    while True:
        num = random.randint(100, 500)
        if is_prime(num):
            return num

# Function to compute gcd (greatest common divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse of a modulo m
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate RSA keys
def generate_rsa_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    d = mod_inverse(e, phi_n)
    
    return (e, n), (d, n)

# Function to encrypt a message
def encrypt_message(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Function to generate keys or use custom keys
def generate_keys():
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()
    public_key_entry.delete(0, tk.END)
    private_key_entry.delete(0, tk.END)
    public_key_entry.insert(0, str(public_key))
    private_key_entry.insert(0, str(private_key))

def encrypt_text():
    # Get public key from the entry field
    try:
        public_key = eval(public_key_entry.get())
        message = input_text.get("1.0", tk.END).strip()
        encrypted_message = encrypt_message(message, public_key)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, str(encrypted_message))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {e}")

def decrypt_text():
    # Get private key from the entry field
    try:
        private_key = eval(private_key_entry.get())
        encrypted_message = eval(output_text.get("1.0", tk.END).strip())
        decrypted_message = decrypt_message(encrypted_message, private_key)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {e}")

# UI
root = tk.Tk()
root.title("RSA Encryption")

# Input text
tk.Label(root, text="Enter Message:").grid(row=0, column=0, sticky="w")
input_text = tk.Text(root, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Public and Private Key input fields
tk.Label(root, text="Public Key (e, n):").grid(row=2, column=0, sticky="w")
public_key_entry = tk.Entry(root, width=50)
public_key_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Private Key (d, n):").grid(row=3, column=0, sticky="w")
private_key_entry = tk.Entry(root, width=50)
private_key_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons 
generate_button = tk.Button(root, text="Generate RSA Keys", command=generate_keys)
generate_button.grid(row=4, column=0, pady=10)

encrypt_button = tk.Button(root, text="Encrypt Message", command=encrypt_text)
encrypt_button.grid(row=5, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt Message", command=decrypt_text)
decrypt_button.grid(row=5, column=1, pady=10)

# Output field
tk.Label(root, text="Output (Encrypted/Decrypted Message):").grid(row=6, column=0, sticky="w")
output_text = tk.Text(root, height=5, width=40)
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
