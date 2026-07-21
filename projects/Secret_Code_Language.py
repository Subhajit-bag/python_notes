import string

# Define the shift key for the secret code (Caesar Cipher logic)
SHIFT = 4

def encode_message(message: str) -> str:
    """Translates regular English text into a secret code."""
    encoded_chars = []
    for char in message:
        if char.isalpha():
            # Handle uppercase letters
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            new_char = chr(start + (ord(char) - start + SHIFT) % 26)
            encoded_chars.append(new_char)
        else:
            # Leave spaces and punctuation exactly as they are
            encoded_chars.append(char)
    return "".join(encoded_chars)

def decode_message(message: str) -> str:
    """Translates the secret code back into regular English."""
    decoded_chars = []
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Shift backward to decrypt and wrap around
            new_char = chr(start + (ord(char) - start - SHIFT) % 26)
            decoded_chars.append(new_char)
        else:
            decoded_chars.append(char)
    return "".join(decoded_chars)

# --- Interactive CLI Interface ---
def main():
    print("--- Secret Communication Tool ---")
    print("1. Encode a message into secret code")
    print("2. Decode a secret code back to English")
    
    choice = input("\nChoose an option (1 or 2): ").strip()
    
    if choice == '1':
        text = input("Enter your secret message: ")
        secret = encode_message(text)
        print(f"\n[Encoded Message]: {secret}")
    elif choice == '2':
        text = input("Enter the secret code to decrypt: ")
        original = decode_message(text)
        print(f"\n[Decrypted Message]: {original}")
    else:
        print("Invalid choice! Program exiting.")

if __name__ == "__main__":
    main()
