## **AES Encryption and Decryption Utility Documentation**

## Overview

The AESCipher script provides a secure implementation of AES (Advanced Encryption Standard) encryption and decryption, utilizing the PBKDF2 (Password-Based Key Derivation Function 2) algorithm to derive encryption keys from user-provided passwords. This script allows users to encrypt and decrypt text with a password while handling essential aspects of cryptography, including padding and initialization vectors (IVs). It ensures that data remains confidential and integrates robust password validation to enhance security.

## Features

- **AES Encryption/Decryption**: Utilizes AES with CFB (Cipher Feedback) mode for encryption and decryption.
- **Password-Based Key Derivation**: Uses PBKDF2 with SHA-256 to generate a strong encryption key from the user’s password.
- **Secure Padding**: Applies PKCS7 padding to ensure plaintext is a multiple of the AES block size.
- **Random Salt and IV**: Generates random salt and IV for each encryption operation to ensure security and uniqueness.
- **Password Validation**: Ensures that the password meets complexity requirements before proceeding with encryption or decryption.

## Dependencies

This script requires the `cryptography` library, which includes:

- **`cryptography.hazmat.primitives.ciphers`**: For encryption and decryption operations.
- **`cryptography.hazmat.primitives.kdf.pbkdf2`**: For key derivation using PBKDF2.
- **`cryptography.hazmat.primitives`**: For cryptographic primitives such as padding and hashing.
- **`cryptography.hazmat.backends`**: Provides cryptographic backend support.
- **`os`**: For generating random salt and IV.
- **`binascii`**: For encoding and decoding hexadecimal representations.
- **`re`**: For regular expression operations.
- **`sys`**: For system-specific functions and exit handling.

To install the necessary library, use:

```sh
pip install cryptography
```

## Usage

To use the AESCipher script, follow these steps:

1. **Run the Script**: Save the script as `aes_cryptography_utility.py` and execute it using Python:

   ```
   python aes_cryptography_utility.py
   ```

2. **Provide Password**: Enter a password that adheres to the complexity requirements (at least 8 characters long, with a mix of uppercase letters, lowercase letters, digits, and special characters).

3. **Enter Text**: Input the text you wish to encrypt or decrypt.

4. **Select Operation**: Choose between encryption and decryption by entering:
   - `1` for encryption
   - `2` for decryption

5. **View Results**: The script will display the encrypted or decrypted text based on your selection.

## Interactive Commands

- **Encryption**: Enter `1` to encrypt the provided text. The script will return the encrypted text as a hexadecimal string combining the salt, IV, and ciphertext.
- **Decryption**: Enter `2` to decrypt the provided encrypted text. The script will return the original plaintext if the correct password is provided.

## Special Commands

- **Password Validation**: The script validates the password against specific criteria to ensure its strength. If the password does not meet these criteria, an error is raised.
- **Error Handling**: The script handles various exceptions, including invalid input, encryption/decryption failures, and unexpected errors, to ensure a smooth user experience.

## Conclusion

The AESCipher script provides a robust and secure solution for text encryption and decryption using AES and PBKDF2. By incorporating strong cryptographic practices such as random salt and IV generation, as well as thorough password validation, the script ensures that sensitive data can be encrypted and decrypted reliably. Its design and functionality make it a valuable tool for both educational purposes and practical applications in data security.

### **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
