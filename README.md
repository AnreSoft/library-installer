# Library Installer Tool

This Python script provides a simple utility for installing Python libraries using `pip`. It allows you to supply a list of libraries to be installed and includes the option to suppress output for cleaner installations.

## Features

- **Bulk Library Installation**: Install multiple Python libraries at once.
- **Optional Output Suppression**: Choose whether to hide or display installation logs.
- **Error Handling**: Captures and reports errors during the installation process.
- **Customizable**: Easy to integrate into other projects.

---

## How It Works

1. **Input List**: The script takes a list of library names to be installed.
2. **Command Execution**: Uses the `subprocess` module to call `pip` and install the specified libraries.
3. **Output Control**: By default, suppresses `pip`'s output (can be toggled).
4. **Error Reporting**: Raises exceptions if the installation process encounters errors.

---

## Installation

Ensure you have Python 3.6 or newer installed.

Clone or copy the script to your local environment:

```bash
git clone https://github.com/ArneSoft/library-installer.git
cd library-installer
```

# Parameters

- **`libs_to_install` (list)**: A list of library names to install.
- **`suppress_output` (bool)**: Whether to suppress `pip`'s output (default: `True`).

## Requirements

- Python >= 3.6
- `pip` installed and properly configured in your environment.

---

## Customization

You can modify the script to:

- Accept user input dynamically (e.g., via command-line arguments).
- Add additional error handling for specific use cases.
- Include version pinning for libraries (e.g., `requests==2.28.1`).
