# OneClickStars

This Python script automates the login process to Bilkent University's STARS system. It handles the verification code sent via email, allowing for a streamlined and hassle-free login.

## Features

- **Automated Login**: Log in without entering credentials and verification code manually.
- **Security**: Your credentials are only used during the execution of the script and are not stored anywhere.

## Prerequisites

- Python 3.x installed on your machine.
- Selenium WebDriver package for Python.
- A compatible WebDriver for your browser (I recommend Chrome, this code is built and tested on Chrome Webdriver, but any other webdriver will be fine, although you need to change some stuff in the code).
- Ensure that SRS is set to send you the verification code via email, not SMS.

## Installation

1. Clone or download this repository to your local machine.
2. Install Selenium by running `pip install selenium` or `pip3 install selenium` (depending on your pip version) in your terminal or command prompt.

## Setup

1. Open the `stars_login.py` script with your desired text editor or IDE, if you have one installed. 
2. Locate the placeholders for your credentials (`yourID`, `yourPassword`, `your.mail@ug.bilkent.edu.tr`, `yourMailPassword`).
3. Replace these with your actual STARS username, password, Bilkent email, and email password.

**Note**: Keep your modified script private and do not share it.

## Building an Executable File

If you prefer to run this script as an executable file, you can build one using PyInstaller. Here's how:

1. Install PyInstaller via pip with the command `pip3 install pyinstaller`.
2. Navigate to the script's directory in your command prompt or terminal.
3. Run the command `pyinstaller --onefile stars_login.py`.

This will create a `dist` directory containing your executable file. You can run this file on any Windows or MacOS. (Probably it will work on any Linux too but I don't have any Linux machine to test, feel free to try)
## Usage

To use the script:

1. Run the generated executable file from the `dist` directory.
2. The script will open a browser window and navigate to the STARS login page to perform the login process.

## Troubleshooting

- Ensure that the Python and Selenium installations are correct.
- Make sure that the WebDriver corresponds to the version of the browser installed on your machine.
- If the login process fails, double-check your credentials and their correct input in the script.

## Contribution

Contributions are welcome! If you are a Bilkent student familiar with the SRS system, please fork this repository, make your changes, and submit a pull request.

## Disclaimer

This script is for educational purposes and should be used ethically and responsibly. The author bears no responsibility for any misuse or damage. 

Also I don't think I will maintain this repository, therefore if BCC changes the SRS Login System in the future, you may need to adjust the code accordingly. This code is written in 2023 and works fine with this system.

## License

This project is open-source and available under the [MIT License](LICENSE).
