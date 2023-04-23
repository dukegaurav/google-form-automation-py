# README

This README file contains the necessary information to run this script. 

## Prerequisites

- Python 3.x installed on your computer.
- Latest version of Firefox web browser installed on your computer.
- Required packages must be installed (if any). These packages are usually listed in a requirements.txt file or mentioned in the script itself. 
- Any required environment variables must be set up.

## Installation

- Install Python 3.x on your computer if it is not already installed. You can download the latest version from the [official Python website](https://www.python.org/downloads/).
- Install any required packages using pip. You can use the following command to install packages listed in requirements.txt:

```bash
pip install -r requirements.txt
```

## Environment Variables

- Some Python scripts require environment variables to be set up before they can be run. These variables are used to store sensitive data such as passwords or API keys, which should not be hard-coded into the script.
- The environment variables required by the script should be listed in a .env file.

## .env File

- Here's an example of a .env file with sample variables:

```
YOUR_EMAIL=abc@xyz.com
PROFILE_NAME=default
EXCEL_FILE=data.xlsx
SPREAD_SHEET=Sheet1
IMAGE=temp_image.png
FORM_URL=https://docs.google.com/forms/d/e/<form-id>/viewform
```

- Replace the values with your own values for your specific use case.

## Usage

- Open a terminal or command prompt window and navigate to the directory where the Python script is located.
- Run the script using the following command:

```bash
python main.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
