import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'profile.kv')
Builder.load_file(kv_file_path)

# Load user profile data
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')

def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}

class ProfileScreen(Screen):
    user_name = StringProperty("")
    left_wing_checked = BooleanProperty(False)
    center_checked = BooleanProperty(False)
    right_wing_checked = BooleanProperty(False)
    left_defense_checked = BooleanProperty(False)
    right_defense_checked = BooleanProperty(False)
    shoot_left_checked = BooleanProperty(False)
    shoot_right_checked = BooleanProperty(False)
    goalie_checked = BooleanProperty(False)

    def on_pre_enter(self):
        user_profile = load_user_profile()
        self.user_name = user_profile.get('user_name', "")
        self.left_wing_checked = user_profile.get('left_wing', False)
        self.center_checked = user_profile.get('center', False)
        self.right_wing_checked = user_profile.get('right_wing', False)
        self.left_defense_checked = user_profile.get('left_defense', False)
        self.right_defense_checked = user_profile.get('right_defense', False)
        self.shoot_left_checked = user_profile.get('shoot_left', False)
        self.shoot_right_checked = user_profile.get('shoot_right', False)
        self.goalie_checked = user_profile.get('goalie', False)
        self.update_checkboxes()

    def update_checkboxes(self):
        """
        Update the checkboxes based on the loaded profile data.
        """
        self.ids.left_wing_checkbox.active = self.left_wing_checked
        self.ids.center_checkbox.active = self.center_checked
        self.ids.right_wing_checkbox.active = self.right_wing_checked
        self.ids.left_defense_checkbox.active = self.left_defense_checked
        self.ids.right_defense_checkbox.active = self.right_defense_checked
        self.ids.left_hand_checkbox.active = self.shoot_left_checked
        self.ids.right_hand_checkbox.active = self.shoot_right_checked
        self.ids.goalie_checkbox.active = self.goalie_checked

    def save_user_profile(self):
        """
        Save the user profile information to a JSON file and print status to console.
        """
        profile_data = load_user_profile()  # Load the existing profile data

        # Update the profile data with current screen's data
        profile_data.update({
            'user_name': self.user_name,
            'left_wing': self.ids.left_wing_checkbox.active,
            'center': self.ids.center_checkbox.active,
            'right_wing': self.ids.right_wing_checkbox.active,
            'left_defense': self.ids.left_defense_checkbox.active,
            'right_defense': self.ids.right_defense_checkbox.active,
            'shoot_left': self.ids.left_hand_checkbox.active,
            'shoot_right': self.ids.right_hand_checkbox.active,
            'goalie': self.ids.goalie_checkbox.active
        })

        self.print_profile_data(profile_data)
        self.save_profile_data(profile_data)

    def print_profile_data(self, profile_data):
        """
        Print the profile data to the console.
        """
        print(f"Profile Data: {profile_data}")

    def save_profile_data(self, profile_data):
        """
        Save the profile data to a JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

        with open(file_path, 'w') as f:
            json.dump(profile_data, f, indent=4)

        print(f"Profile saved to {file_path}")

    def go_to_next_screen(self):
        """
        Navigate to the next screen without saving the entire profile.
        """
        self.manager.current = 'profile2'
