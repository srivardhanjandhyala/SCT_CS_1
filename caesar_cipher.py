def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within the alphabet
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            # Non-alphabet characters remain unchanged
            result += char
    return result

def decrypt(text, shift):
    # Decrypt by shifting in the opposite direction
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    choice = input("Type 'e' for encryption or 'd' for decryption: ").lower()
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
