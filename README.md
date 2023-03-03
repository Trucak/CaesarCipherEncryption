# Caesar Cipher Encryption with Random Key

This is a simple Python script that encrypts a message using the Caesar Cipher method with a random key.


## How to Run


Open a terminal and navigate to the directory where the Python script is located.
Run the script by typing python caesar_cipher.py in the terminal.
The encrypted message will be displayed in the terminal, and a text file containing the encryption key will be created in the same directory.
## How it Works

The caesar_cipher function takes a message and a key as input and returns the encrypted message using the Caesar Cipher encryption method.

The key variable is generated using the random module with a random integer between 1 and 25.

The encrypted message is printed to the terminal using the print function.

The key is saved to a text file using the open function in write mode with the with statement. The f-string is used to dynamically create the file name using the value of the key variable. The write method is used to write the key to the file. Finally, a message is printed to the terminal using the print function with an f-string that displays the file name where the key was saved.
## Example output:

```bash
yrtfvnyegz
Key saved to key_12.txt
```


## Note

This script does not include decryption functionality.## CaesarCipherEncryption
