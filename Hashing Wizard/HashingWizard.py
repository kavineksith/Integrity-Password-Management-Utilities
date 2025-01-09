import hashlib
import json
import os
import sys
import time


# Custom Exception class for handling errors specific to HashingWizard
class HashingWizardError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Screen Manager Class to handle screen clearing
class ScreenManager:
    def __init__(self):
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'

    def clear_screen(self):
        try:
            os.system(self.clear_command)
        except OSError as e:
            raise HashingWizardError(f"Error clearing the screen: {e}")
        except KeyboardInterrupt:
            raise HashingWizardError("Process interrupted by the user.")
        except Exception as e:
            raise HashingWizardError(f"An error occurred: {e}")


# Hashing Wizard Class to compute hash values for a given password
class HashingWizard:
    def __init__(self, usr_pwd):
        self.hash_list = [
            'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
            'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512'
        ]
        self.hash_values = []  # List to store hash values
        self.usr_password = usr_pwd  # User-provided password
        self.salt = os.urandom(16)  # Generate a random salt

    # Method to compute hash values without salt using various algorithms
    def compute_hashes_without_salt(self):
        try:
            self.hash_values.clear()  # Clear hash_values list
            for hash_method in self.hash_list:
                hash_value = hashlib.new(hash_method, self.usr_password.encode()).hexdigest()
                self.hash_values.append(hash_value)  # Append each hash value to the list
        except Exception as e:
            raise HashingWizardError(f"Error in compute_hashes_without_salt: {e}")

    # Method to compute hash values with salt using various algorithms
    def compute_hashes_with_salt(self):
        try:
            self.hash_values.clear()  # Clear hash_values list
            for hash_method in self.hash_list:
                hasher = hashlib.new(hash_method)
                # Add salt to the password before hashing
                hasher.update(self.usr_password.encode() + self.salt)
                hash_value = hasher.hexdigest()
                self.hash_values.append(hash_value)  # Append each hash value to the list
        except Exception as e:
            raise HashingWizardError(f"Error in compute_hashes_with_salt: {e}")

    # Method to format hash values as CSV and return as a string
    def format_hashes_csv(self):
        try:
            csv_output = "Password, " + ", ".join(key_formatter(self.hash_list)) + "\n"
            csv_output += f"{self.usr_password}, " + ", ".join(self.hash_values)
            return csv_output
        except Exception as e:
            raise HashingWizardError(f"Error in format_hashes_csv: {e}")
        
    # Method to format hash values as JSON and return as a string
    def format_hashes_json(self):
        try:
            json_data = {
                'Password': self.usr_password,
                'Hashes': {key_formatter(key): value for key, value in zip(self.hash_list, self.hash_values)}
            }
            json_output = json.dumps(json_data, indent=4)
            return json_output
        except Exception as e:
            raise HashingWizardError(f"Error in format_hashes_json: {e}")

def key_formatter(value):
    return value.replace('_',' ').upper()

def hashing_wizard_controller(user_password):
    try:
        # Create an instance of HashingWizard with user-provided password
        hashing_wizard = HashingWizard(user_password)

        # Prompt user whether to use salt or not
        use_salt = input('Do you want to use salt? (yes/no): ').strip()
        if use_salt.lower() == 'yes':
            # Compute hash values with salts for the password using defined methods
            hashing_wizard.compute_hashes_with_salt()
            output_format = input('Which format do you want? (csv/json): ').strip()
            if output_format.lower() == 'csv':
                # Display hash values in CSV format
                csv_output = hashing_wizard.format_hashes_csv()
                print(csv_output)
            elif output_format.lower() == 'json':
                # Display hash values in JSON format
                json_output = hashing_wizard.format_hashes_json()
                print(json_output)
            else:
                raise HashingWizardError('Invalid output format specified.')
        elif use_salt.lower() == 'no':
            # Compute hash values without salt for the password using defined methods
            hashing_wizard.compute_hashes_without_salt()
            output_format = input('Which format do you want? (csv/json): ').strip()
            if output_format.lower() == 'csv':
                # Display hash values in CSV format
                csv_output = hashing_wizard.format_hashes_csv()
                print(csv_output)
            elif output_format.lower() == 'json':
                # Display hash values in JSON format
                json_output = hashing_wizard.format_hashes_json()
                print(json_output)
            else:
                raise HashingWizardError('Invalid output format specified.')
        else:
            raise HashingWizardError('Invalid input for using salt.')
    except Exception as e:
        raise HashingWizardError(f'Error in hashing_wizard_controller: {e}')


# Function to interact with the user, compute hashes, and display results
def user_interactive_phrase():
    try:
        while True:
            user_password = input('Your Password: ').strip()

            if user_password.lower() == "clear":
                ScreenManager().clear_screen()
                continue  # Restart the loop after screen clear

            if user_password.lower() == "exit":
                print("Script Terminated...!!")
                time.sleep(2)
                ScreenManager().clear_screen()
                sys.exit(0)

            if not user_password:
                raise HashingWizardError('Please enter your password.')

            # Call hashing wizard controller function to compute hashes and display results
            hashing_wizard_controller(user_password)

    except KeyboardInterrupt:
        raise HashingWizardError("Process interrupted by the user.")
    except HashingWizardError as hwe:
        print(f'Error processing password: {hwe.message}')
        sys.exit(1)  # Exit the script with an error status code
    except Exception as e:
        print(f'Unexpected error occurred: {e}')
        sys.exit(1)  # Exit the script with an error status code


# Entry point of the script
if __name__ == "__main__":
    user_interactive_phrase()  # Call the function to start interactive hashing
    sys.exit(0)  # Exit the script with a success status code
