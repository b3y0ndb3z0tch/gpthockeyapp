# email/verification.py
import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, StringProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'verification.kv')
Builder.load_file(kv_file_path)

# Load colors from colors.json
data_folder = os.path.join(os.path.dirname(__file__), '../data')
colors_file = os.path.join(data_folder, 'colors.json')

def load_colors():
    if os.path.exists(colors_file):
        with open(colors_file, 'r') as file:
            return json.load(file)
    return {}

class VerificationScreen(Screen):
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])
    label_fontprimary = ListProperty([1, 1, 1, 1])
    button_fontprimary = ListProperty([0, 0, 0, 1])
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])
    textfield_fontprimary = ListProperty([1, 1, 1, 1])  # Added textfield font color

    def on_pre_enter(self):
        colors = load_colors()
        self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
        self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
        self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
        self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])
        self.textfield_fontprimary = colors.get('textfield_fontprimary', [1, 1, 1, 1])

    def submit_verification(self, code):
        """
        Handle the verification code submission.
        """
        if self.validate_code(code):
            self.save_verification_status()
            self.manager.current = 'stickhand'
        else:
            # Handle invalid code case
            print("Invalid verification code")

    def validate_code(self, code):
        """
        Validate the verification code.
        For now, we'll just check if it matches a hardcoded value.
        """
        return code == "1234"  # Example validation

    def save_verification_status(self):
        """
        Save the verification status to a JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_data.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                user_data = json.load(f)
                user_data['verified'] = True

            with open(file_path, 'w') as f:
                json.dump(user_data, f)
