# Password Generator Script Documentation

## Overview
This Python script generates passwords of specified length and complexity levels. It allows users to choose between generating normal passwords or secure passwords with specific criteria for complexity. The script utilizes both built-in Python libraries and custom classes for functionality.

## Features
- **Password Generation**: Generate passwords of varying lengths and categories.
- **Normal Passwords**: Generates passwords with random characters.
- **Secure Passwords**: Generates passwords with specific criteria for enhanced security.
- **Interactive Interface**: Prompts users for input regarding password length and category.
- **Error Handling**: Provides robust error handling for various user inputs and unexpected errors.

## Dependencies
- Python 3.x
- `string` library for character pool retrieval
- `secrets` and `random` modules for secure and normal password generation, respectively
- `os` library for system-specific functions
- `time` library for time-related operations
- `sys` library for system-specific parameters and functions

## Usage
1. **Password Length**: Specify the desired length for the generated password.
2. **Password Category**: Choose between generating a normal password (Category 1) or a secure password (Category 2) with specific complexity criteria.
3. **Generated Password**: Upon successful generation, the script displays the generated password.

- **Interactive Commands**
   - **Password Length**: Enter the desired length for the password when prompted.
   - **Password Category**: Choose between a normal password (1) or a secure password (2).

- **Special Commands**:
    - **Clear Screen**: Type `clear` to clear the terminal screen.
    - **Exit**: Type `exit` to terminate the script.

## Conclusion
The Password Generator script offers a flexible solution for generating passwords tailored to specific requirements. Whether users need a simple, randomly generated password or a secure password meeting specific complexity criteria, this script provides a reliable and user-friendly interface for password generation.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.