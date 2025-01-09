# Hashing Wizard Documentation

## Overview
The **Hashing Wizard** is a Python script designed to compute and format hash values for a given password using various hashing algorithms. The script supports both hashed outputs with and without salt, and provides the results in CSV or JSON formats. It also includes custom error handling and a simple text-based user interface.

## Features
- **Hash Calculation**: Computes hash values for a given password using a variety of hashing algorithms.
- **Salted Hashes**: Optionally adds a random salt to the password before hashing.
- **Output Formats**: Provides hash values in both CSV and JSON formats.
- **Custom Error Handling**: Includes a custom exception class for improved error management.
- **User Interface**: A text-based interface to interact with the user for password input and format selection.
- **Screen Management**: Clears the screen between operations to enhance user experience.

## Dependencies
- **Python 3.x**: The script is written for Python 3.x.
- **`hashlib`**: Provides hashing algorithms such as `md5`, `sha1`, `sha256`, etc., used for computing hash values.
- **`json`**: Used for encoding hash values into JSON format.
- **`os`**: Provides system-specific functionalities such as clearing the screen (`os.system()`) and generating a random salt (`os.urandom()`).
- **`sys`**: Handles system-specific parameters and functions, including exiting the script (`sys.exit()`).
- **`time`**: Provides time-related functions, used here for delays (`time.sleep()`).

## Usage
1. **Run the Script**
   Execute the script from the command line:

   ```
   python hashing_wizard.py
   ```

- **Interactive Commands**
   - **Enter Your Password**: When prompted, input the password you wish to hash.
   - **Use Salt**: Indicate whether you want to use a random salt (`yes` or `no`).
   - **Select Output Format**: Choose the desired output format (`csv` or `json`).

- **Special Commands**
   - **Clear Screen**: Type `clear` to clear the screen.
   - **Exit**: Type `exit` to terminate the script.

## Conclusion
The **Hashing Wizard** script is a versatile tool for computing and formatting password hash values using various algorithms, with optional salting and output in CSV or JSON formats. Designed for educational purposes, it provides a user-friendly interface and robust error handling. While it is a valuable resource for learning about hashing and password security, please use it within the scope of its intended educational use and avoid applying it in industrial or commercial contexts.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.