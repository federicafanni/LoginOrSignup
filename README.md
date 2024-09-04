# User Login and Sign-up system

## Description

This Python script provides a simple user authentication system that allows users to sign up and log in. It uses file handling to store user credentials in a text file and JSON to serialize and deserialize user data. This script is intended for educational purposes and demonstrates basic concepts in Python programming, including file I/O, error handling, and user input validation.

## Features

- **Signup functionality**: Allows new users to register by entering their name, username, and password. Ensures that usernames are unique.
- **Login functionality**: Allows existing users to log in by verifying their username and password against stored data.
- **Username validation**: Checks for unique usernames during the signup process to prevent duplicate accounts.
- **Persistent data storage**: Stores user information in a `users.txt` file, making it available across multiple sessions.
- **Error handling**: Provides feedback and prompts users to re-enter data if an error occurs, such as entering an existing username or incorrect password.

## Installation and Usage

To run this project locally, you will need Python 3.x

After installing Python, proceed as follows:
1. Clone the repository or download the script directly to your local machine.
2. Run `loginSignup.py` in the terminal or using an interpreter.

## Usage
#### To sign up as a new user:

1. When prompted with `"Welcome! Press L to login or S to sign-up:"`, type `S` or `s` and press Enter.
2. Enter your name when prompted. This will be stored as your profile name.
3. Enter a unique username. The system will check if the username already exists; if it does, you will be asked to enter a different one.
4. Enter a password. Choose a secure password that you can remember.
5. After entering all details, you will see a confirmation message: `"You have successfully signed up"`.

#### To log in as an existing user:

1. When prompted with `"Welcome! Press L to login or S to sign-up:"`, type `L` or `l` and press Enter.
2. Enter your username when prompted.
3. Enter your password when prompted. The system will check if the password matches the one stored for the username.
4. If the credentials are correct, a welcome message is displayed: `"Welcome back [Your Name]!"`.
5. If the password is incorrect, you will be prompted to try again.
6. If the username does not exist, you will be informed and asked to enter the username again.


## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
[MIT License](LICENSE.md) - feel free to use and modify this code for your own projects.
