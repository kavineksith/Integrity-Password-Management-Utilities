import string
import secrets
import random
import os
import time
import sys

# Custom Exception Classes
class PasswordGeneratorError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(PasswordGeneratorError):
    """Exception raised for invalid user inputs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PasswordLengthError(PasswordGeneratorError):
    """Exception raised for invalid password length."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PasswordCategoryError(PasswordGeneratorError):
    """Exception raised for invalid password category."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ScreenManager:
    def __init__(self):
        """Initialize ScreenManager with the command to clear the screen."""
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'

    def clear_screen(self):
        """Clear the terminal screen."""
        try:
            os.system(self.clear_command)
        except OSError as e:
            print(f"Error clearing the screen: {e}")
        except KeyboardInterrupt:
            print("\nProcess interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

class CharacterLake:
    def __init__(self):
        """Initialize CharacterLake with character sets for password generation."""
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_chars = string.punctuation

    def get_characters(self):
        """Return a string of all characters for password generation."""
        return self.letters + self.digits + self.special_chars

class PasswordGenerator:
    def __init__(self):
        """Initialize PasswordGenerator with CharacterLake for password creation."""
        self.character_lake = CharacterLake()

    def generate_password(self, length, secure=False):
        """
        Generate a password of the given length.
        
        :param length: Length of the password to be generated.
        :param secure: If True, use secrets.choice for a more secure password.
        :return: The generated password as a string.
        """
        characters = self.character_lake.get_characters()
        if secure:
            password = ''.join(secrets.choice(characters) for _ in range(length))
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_secure_password(self, length):
        """
        Generate a secure password of the given length.
        
        A secure password must include at least one special character and at least five digits.
        
        :param length: Length of the password to be generated.
        :return: The generated secure password as a string.
        """
        digits = self.character_lake.digits
        special_chars = self.character_lake.special_chars

        while True:
            password = self.generate_password(length, secure=True)
            if (any(char in special_chars for char in password) and sum(char in digits for char in password) >= 5):
                return password

    @staticmethod
    def get_pwd_length():
        """
        Prompt the user to enter the desired password length.
        
        :return: Password length as an integer.
        :raises PasswordLengthError: If the input is not a positive integer.
        """
        try:
            length = input('Password Length (positive integer): ')
            if length.lower() == "clear":
                ScreenManager().clear_screen()
                main()
            
            if length.lower() == "exit":
                print("Script Terminated...!!")
                time.sleep(2)
                ScreenManager().clear_screen()
                sys.exit(0)
            
            length = int(length)
            if length <= 0:
                raise PasswordLengthError("Password length must be a positive integer.")
        except ValueError:
            raise PasswordLengthError("Invalid input: Please enter a positive integer for the password length.")
        except KeyboardInterrupt:
            print("\nProcess interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            raise PasswordGeneratorError(f"An error occurred: {e}")

        return length

    @staticmethod
    def get_pwd_category():
        """
        Prompt the user to select the password category.
        
        :return: Password category as an integer (1 for Normal, 2 for Secure).
        :raises PasswordCategoryError: If the input is not 1 or 2.
        """
        try:
            value = input('Password Category (1 for Normal, 2 for Secure): ')
            if value.lower() == "clear":
                ScreenManager().clear_screen()
                main()

            if value.lower() == "exit":
                print("Script Terminated...!!")
                time.sleep(2)
                ScreenManager().clear_screen()
                sys.exit(0)
            
            value = int(value)
            if value not in [1, 2]:
                raise PasswordCategoryError("Password category must be either 1 or 2.")
        except ValueError:
            raise PasswordCategoryError("Invalid input: Please enter 1 for Normal or 2 for Secure.")
        except KeyboardInterrupt:
            print("\nProcess interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            raise PasswordGeneratorError(f"An error occurred: {e}")

        return value

    @staticmethod
    def pwd_wizard():
        """
        Main wizard function to generate or validate passwords based on user input.
        
        :return: The generated password as a string.
        """
        password_generator = PasswordGenerator()
        pwd_category = password_generator.get_pwd_category()

        try:
            if pwd_category == 1:
                password = password_generator.generate_password(password_generator.get_pwd_length())
            elif pwd_category == 2:
                password = password_generator.generate_secure_password(password_generator.get_pwd_length())
            else:
                raise PasswordCategoryError("Invalid password category.")
        except PasswordCategoryError as pce:
            print(f"Error generating password: {pce.message}")
            sys.exit(1)
        except PasswordLengthError as ple:
            print(f"Error with password length: {ple.message}")
            sys.exit(1)
        except InvalidInputError as iie:
            print(f"Invalid input: {iie.message}")
            sys.exit(1)
        except PasswordGeneratorError as pge:
            print(f'Error processing password: {pge.message}')
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

        return password

def main():
    """
    Main function to run the password generation wizard and display the generated password.
    """
    while True:
        try:
            generated_password = PasswordGenerator().pwd_wizard()
            print(f"Generated Password: {generated_password}")
        except KeyboardInterrupt:
            print("\nProcess interrupted by the user.")
            sys.exit(1)
        except InvalidInputError as iie:
            print(f"Invalid input: {iie.message}")
            sys.exit(1)
        except PasswordLengthError as ple:
            print(f"Error with password length: {ple.message}")
            sys.exit(1)
        except PasswordCategoryError as pce:
            print(f"Error with password category: {pce.message}")
            sys.exit(1)
        except PasswordGeneratorError as pge:
            print(f'Error processing password: {pge.message}')
            sys.exit(1)
        except Exception as e:
            print(f'Unexpected error occurred: {e}')
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)