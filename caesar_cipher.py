import random

def caesar_cipher(message, key):
    encrypted_message = ""
    for character in message:
        if character == " ":
            continue
        if character.isalpha():
            code = ord(character) + key
            if character.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            else:
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
            encrypted_message += chr(code)
        else:
            encrypted_message += character
    return encrypted_message

message = "tomasmartim"
key = random.randint(1,25)
encrypted = caesar_cipher(message, key)

print(encrypted)

key_filename = f"key_{key}.txt"
with open(key_filename, "w") as key_file:
    key_file.write(str(key))
    print(f"Key saved to {key_filename}")