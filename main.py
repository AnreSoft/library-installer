import subprocess
import sys

def list_to_format_str(libs_to_install: list) -> str:
    """
    Converts a list of library names into a single space-separated string.

    Args:
        libs_to_install (list): List of library names to install.

    Returns:
        str: A single string containing all library names separated by spaces.
    """
    return ' '.join(map(str, libs_to_install))


def libs_download(libs_to_install: list, suppress_output: bool = True):
    """
    Installs the given list of Python libraries using pip.

    Args:
        libs_to_install (list): List of library names to install.
        suppress_output (bool): If True, suppresses pip's output (stdout and stderr).
                                If False, displays pip's output in the console.

    Raises:
        subprocess.CalledProcessError: If the pip command fails.
    """
    # Convert list of libraries to a space-separated string
    str_libs_to_install = list_to_format_str(libs_to_install)

    # Prepare command for pip installation
    command = [sys.executable, '-m', 'pip', 'install'] + libs_to_install

    # Redirect output based on suppress_output flag
    stdout = subprocess.DEVNULL if suppress_output else None
    stderr = subprocess.DEVNULL if suppress_output else None

    # Execute the pip command
    subprocess.check_call(command, stdout=stdout, stderr=stderr)


if __name__ == "__main__":
    # Example usage
    print("Welcome to the library installer!")

    # Ask the user for a comma-separated list of libraries
    libs = ['pyperclip', 'requests']

    # Ask the user if they want to suppress output
    suppress = True

    try:
        # Download and install libraries
        libs_download(libs, suppress_output=suppress)
        print("Libraries installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing libraries: {e}")
