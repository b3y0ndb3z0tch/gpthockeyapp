from kivy.uix.screenmanager import Screen  # Import Screen from Kivy
from kivy.properties import StringProperty  # Import StringProperty for managing string properties
import json  # Import JSON module for reading and writing JSON files
import os  # Import OS module to handle file paths

class VerificationScreen(Screen):  # Define the VerificationScreen class inheriting from Screen
    verification_code = StringProperty('')  # Define a StringProperty to hold the verification code

    def submit_verification(self):
        """
        Handle the verification code submission.
        """
        if self.verification_code == '123':  # Hardcoded for now
            self.save_verification_status()
            self.manager.current = 'profile'  # Navigate to the profile screen
        else:
            # Display an error message or handle incorrect code
            pass

    def save_verification_status(self):
        """
        Save the verification status to the JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_data.json')

        # Load existing data
        with open(file_path, 'r') as f:
            user_data = json.load(f)

        # Update verification status
        user_data['verified'] = True

        # Write data back to file
        with open(file_path, 'w') as f:
            json.dump(user_data, f)
