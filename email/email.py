# email/email.py
from kivy.uix.screenmanager import Screen  # Import Screen from Kivy
from kivy.properties import StringProperty, ListProperty  # Import StringProperty for managing string properties
import re  # Import the regular expression module for email validation
import json  # Import JSON module for reading and writing JSON files
import os  # Import OS module to handle file paths


class EmailScreen(Screen):  # Define the EmailScreen class inheriting from Screen
    email = StringProperty('')  # Define a StringProperty to hold the email
    password = StringProperty('')  # Define a StringProperty to hold the password
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])  # Define a ListProperty for the background color
    label_fontprimary = ListProperty([1, 1, 1, 1])  # Define a ListProperty for the label font color
    button_fontprimary = ListProperty([0, 0, 0, 1])  # Define a ListProperty for the button font color
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])  # Define a ListProperty for the button pressed color
    textfield_fontprimary = ListProperty([1, 1, 1, 1])  # Define a ListProperty for the textfield font color

    def on_enter(self):
        """
        This method is called when the screen is entered.
        It checks if there is already a valid email and user_id in the JSON file,
        and if so, navigates directly to the verification screen.
        """
        user_data = self.load_user_data()
        if user_data and user_data.get('email') and user_data.get('user_id'):
            self.manager.current = 'verification'

        # Load colors from colors.json
        self.load_colors()

    def load_colors(self):
        """
        Load colors from the colors.json file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        colors_file = os.path.join(data_directory, 'colors.json')

        if os.path.exists(colors_file):
            with open(colors_file, 'r') as f:
                try:
                    colors = json.load(f)
                    self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
                    self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
                    self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
                    self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])
                    self.textfield_fontprimary = colors.get('textfield_fontprimary', [1, 1, 1, 1])
                except json.JSONDecodeError:
                    pass

    def validate_email(self, email):
        """
        Validates the email format and checks for malicious inputs.
        Returns True if the email is valid and safe, False otherwise.
        """
        # Regular expression for basic email format validation
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if email_pattern.match(email):
            # Check for SQL injection or other malicious inputs
            if any(keyword in email.lower() for keyword in
                   ['select', 'insert', 'delete', 'drop', 'update', '--', ';', '/*', '*/']):
                return False
            return True
        return False

    def validate_password(self, password):
        """
        Validates the password to ensure it is at least 4 characters long
        and not composed of all repeating characters.
        Returns True if the password is valid, False otherwise.
        """
        if len(password) < 4:
            return False
        if len(set(password)) == 1:
            return False
        return True

    def validate_fields(self):
        """
        Validate the email and password fields and enable/disable the submit button.
        """
        email_valid = self.validate_email(self.email)
        password_valid = self.validate_password(self.password)

        if email_valid:
            self.ids.email_input.error = False
            self.ids.email_input.text_color_normal = self.textfield_fontprimary
        else:
            self.ids.email_input.error = True
            self.ids.email_input.text_color_normal = [1, 0, 0, 1]

        if password_valid:
            self.ids.password_input.error = False
            self.ids.password_input.text_color_normal = self.textfield_fontprimary
        else:
            self.ids.password_input.error = True
            self.ids.password_input.text_color_normal = [1, 0, 0, 1]

        self.ids.submit_button.disabled = not (email_valid and password_valid)

    def submit_email(self):
        """
        Handle the email submission. Eventually, this will send the email to the backend
        and handle the response (e.g., verification code and user_id).
        For now, it navigates to the verification screen and saves the email to a JSON file.
        """
        # Save email, password, and user_id to JSON file
        self.save_user_data(self.email, self.password)

        # Navigate to the verification screen
        self.manager.current = 'verification'

    def save_user_data(self, email, password):
        """
        Save the user email, password, and user_id to a JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        os.makedirs(data_directory, exist_ok=True)
        file_path = os.path.join(data_directory, 'user_data.json')

        # Load existing data
        user_data = self.load_user_data() or {}

        # Update with new email, password, and user_id
        user_data['email'] = email
        user_data['password'] = password  # Save the actual password entered by the user
        user_data['user_id'] = '1'  # Hardcoded for now

        # Write data back to file
        with open(file_path, 'w') as f:
            json.dump(user_data, f)

    def load_user_data(self):
        """
        Load user data from the JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_data.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return None
        return None
