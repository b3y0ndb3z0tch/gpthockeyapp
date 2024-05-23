# email/email.py
from kivy.uix.screenmanager import Screen  # Import Screen from Kivy
from kivy.properties import StringProperty  # Import StringProperty for managing string properties
import re  # Import the regular expression module for email validation
import json  # Import JSON module for reading and writing JSON files
import os  # Import OS module to handle file paths

class EmailScreen(Screen):  # Define the EmailScreen class inheriting from Screen
    email = StringProperty('')  # Define a StringProperty to hold the email
    password = StringProperty('')  # Define a StringProperty to hold the password

    def on_enter(self):
        """
        This method is called when the screen is entered.
        It checks if there is already a valid email and user_id in the JSON file,
        and if so, navigates directly to the home screen.
        """
        user_data = self.load_user_data()
        if user_data and user_data.get('email') and user_data.get('user_id'):
            self.manager.current = 'home'

    def validate_email(self):
        """
        Validates the email format and checks for malicious inputs.
        Returns True if the email is valid and safe, False otherwise.
        """
        # Regular expression for basic email format validation
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if email_pattern.match(self.email):
            # Check for SQL injection or other malicious inputs
            if any(keyword in self.email.lower() for keyword in ['select', 'insert', 'delete', 'drop', 'update', '--', ';', '/*', '*/']):
                return False
            return True
        return False

    def validate_password(self):
        """
        Validates the password to ensure it is at least 4 characters long
        and not composed of all repeating characters.
        Returns True if the password is valid, False otherwise.
        """
        if len(self.password) < 4:
            return False
        if len(set(self.password)) == 1:
            return False
        return True

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
        user_data['password'] = '1234'  # Hardcoded for now
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
