def encrypt(text, shift):
    encrypted_text = ""  
    for char in text:
        if char.isalpha():
            encrypted_char = chr(ord(char) + (shift%26))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""  
    for char in text:
        if char.isalpha():
            decrypted_char = chr(ord(char) - (shift%26))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


while True:
        choice = input("select e for encrypt and d for decrypt (q for quit): ").lower()

        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("enter valid choice")
            continue

        message = input("enter your message: ")
        try:
            shift = int(input("enter shift value: "))
        except: 
            print("invalid shift value... please enter valid integer")
            continue  

        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
