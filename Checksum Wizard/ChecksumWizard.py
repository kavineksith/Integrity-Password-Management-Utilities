import hashlib
import sys

# Custom Exception class for handling errors specific to ChecksumWizard
class ChecksumWizardError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Checksum Wizard Class to compute hash values for a given file
class ChecksumWizard:
    def __init__(self, file_path, checksum=None):
        """
        Initialize ChecksumWizard with file path and optional checksum for validation.

        :param file_path: Path to the file whose checksum is to be computed or validated.
        :param checksum: Optional checksum value for verification (used only in 'validate' mode).
        """
        self.hash_list = [
            'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
            'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512'
        ]
        self.checksum_values = []  # List to store computed checksum values
        self.file_path = file_path
        self.checksum = checksum  # Checksum value for comparison (for 'validate' mode)
        self.bytes_content = None  # Content of the file to be read

    def source_file_analyzer(self):
        """
        Read the content of the file into memory. This method must be called before computing checksums.
        """
        try:
            with open(self.file_path, 'rb') as binary_form_data:
                self.bytes_content = binary_form_data.read()
                print(f"File '{self.file_path}' successfully read.")
        except FileNotFoundError:
            raise ChecksumWizardError(f"File '{self.file_path}' not found.")
        except PermissionError:
            raise ChecksumWizardError(f"Permission denied while accessing '{self.file_path}'.")
        except Exception as e:
            raise ChecksumWizardError(f"Error in source_file_analyzer: {e}")

    def compute_checksum_for_binary_form_data(self):
        """
        Compute checksums for the file content using the predefined hash methods and store them in `self.checksum_values`.
        """
        if self.bytes_content is None:
            raise ChecksumWizardError("No file content available. Please run source_file_analyzer() first.")
        
        print(f"Computing checksums for file content using methods: {', '.join(self.hash_list)}")
        self.checksum_values.clear()  # Clear checksum_values list
        for hash_method in self.hash_list:
            hash_function = getattr(hashlib, hash_method, None)
            if hash_function is None:
                raise ChecksumWizardError(f"Hash method '{hash_method}' is not available.")
            
            hash_obj = hash_function()
            hash_obj.update(self.bytes_content)
            checksum = hash_obj.hexdigest()
            self.checksum_values.append((hash_method, checksum))
            print(f"{hash_method}: {checksum}")

    def verify_checksum(self):
        """
        Verify the provided checksum against the computed checksums.
        """
        if not self.checksum_values:
            raise ChecksumWizardError("No checksums computed. Please run compute_checksum_for_binary_form_data() first.")
        
        if not self.checksum:
            raise ChecksumWizardError("No checksum provided for validation.")
        
        print(f"Verifying checksum: {self.checksum}")
        matched = False
        for method, computed_checksum in self.checksum_values:
            if self.checksum == computed_checksum:
                print(f"Checksum matched using {method}: {computed_checksum}")
                matched = True
                break

        if not matched:
            print(f"No matching checksum found. Computed checksums were: {self.checksum_values}")

def main():
    """
    Main function to handle command-line arguments and execute the appropriate actions based on the provided purpose.
    """
    if len(sys.argv) < 3:
        # Ensure that enough arguments are provided
        print("Usage: python sample.py <generate|validate> <file_path> [<checksum>]")
        sys.exit(1)  # Exit the script with an error status code
    
    try:
        purpose = sys.argv[1].lower().strip()
        file_path = sys.argv[2].strip()
        checksum = sys.argv[3].strip() if len(sys.argv) == 4 else None  # Optional checksum for 'validate' mode

        # Ensure that the purpose argument is either 'generate' or 'validate'
        if purpose not in ['generate', 'validate']:
            raise ChecksumWizardError("Invalid purpose. Must be 'generate' or 'validate'.")

        # Initialize ChecksumWizard with file path and checksum value
        wizard = ChecksumWizard(file_path, checksum if purpose == 'validate' else None)

        if purpose == "generate":
            wizard.source_file_analyzer()  # Read file content
            wizard.compute_checksum_for_binary_form_data()  # Compute checksums
        elif purpose == "validate":
            if checksum is None:
                raise ChecksumWizardError("Checksum value is required for validation.")
            wizard.source_file_analyzer()  # Read file content
            wizard.compute_checksum_for_binary_form_data()  # Compute checksums
            wizard.verify_checksum()  # Verify the provided checksum
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        sys.exit(1)  # Exit the script with an error status code
    except ChecksumWizardError as cswe:
        print(f'Error processing checksum: {cswe.message}')
        sys.exit(1)  # Exit the script with an error status code
    except Exception as e:
        print(f'Unexpected error occurred: {e}')
        sys.exit(1)  # Exit the script with an error status code

if __name__ == "__main__":
    main()
    sys.exit(0)
