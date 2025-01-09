## Documentation : File and Folder Security Manager

## Overview

The File Encryptor/Decryptor script is a robust tool designed for encrypting and decrypting files and directories using the `cryptography` library. It leverages the `Fernet` symmetric encryption method to ensure that your files are securely encrypted and can be decrypted accurately. This tool is suitable for protecting sensitive data during storage and transmission.

## Features

- **File Encryption**: Securely encrypt individual files.
- **File Decryption**: Restore encrypted files to their original state.
- **Directory Encryption**: Encrypt all files within a specified directory.
- **Directory Decryption**: Decrypt all files within a specified directory.
- **Error Handling**: Gracefully manages common file operation errors and invalid user inputs.
- **Key Management**: Uses symmetric encryption keys to encrypt and decrypt data.

## Dependencies

- **Python 3.x**: The script is compatible with Python 3.x.
- **cryptography**: Provides the `Fernet` encryption algorithm. Ensure that the `cryptography` library is installed:

  ```bash
  pip install cryptography
  ```

- **Standard Libraries**: Utilizes built-in Python libraries:
  - `pathlib` for file and directory path manipulations.
  - `sys` for system-specific parameters and functions.

## Usage

To use the File Encryptor/Decryptor script, follow these steps:

1. **Install Dependencies**: Ensure you have the `cryptography` library installed using pip.
2. **Run the Script**: Execute the script from the command line or terminal:

   ```bash
   python file_and_folder_security_manager.py
   ```

3. **Follow On-Screen Prompts**: Choose an operation from the menu and provide the required paths.

## Interactive Commands

The script provides a menu-driven interface with the following commands:

1. **Encrypt File**:
   - **Command**: `1`
   - **Description**: Encrypts a specified file and saves the encrypted content to a new file.
   - **Prompts**:
     - Enter input file path
     - Enter output file path

2. **Decrypt File**:
   - **Command**: `2`
   - **Description**: Decrypts a specified encrypted file and saves the decrypted content to a new file.
   - **Prompts**:
     - Enter input file path
     - Enter output file path

3. **Encrypt Directory**:
   - **Command**: `3`
   - **Description**: Encrypts all files within a specified directory and saves them to a new directory.
   - **Prompts**:
     - Enter input directory path
     - Enter output directory path

4. **Decrypt Directory**:
   - **Command**: `4`
   - **Description**: Decrypts all files within a specified directory and saves them to a new directory.
   - **Prompts**:
     - Enter input directory path
     - Enter output directory path

5. **Exit**:
   - **Command**: `5`
   - **Description**: Exits the application.

## Special Commands

- **Error Handling**:
  - **ValueError**: Raised if the input and output file paths are identical or if there are invalid inputs.
  - **FileExistsError**: Raised if the output file or directory already exists.
  - **FileNotFoundError**: Raised if the input file is not found.
  
- **Keyboard Interrupt**: Handles interruptions from the user (e.g., pressing Ctrl+C) to exit gracefully.

## Conclusion

The File Encryptor/Decryptor script is an essential tool for managing file security through encryption and decryption. It provides a user-friendly command-line interface for handling individual files and entire directories. With its robust error handling and easy-to-use features, it ensures that your sensitive data remains protected while allowing for straightforward file management.

For further customization or extension of functionality, users may modify the script or integrate it with other systems as required.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.