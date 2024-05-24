import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'forward.kv')
Builder.load_file(kv_file_path)

# Load user profile data
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')


def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}


class ForwardScreen(Screen):
    user_name = StringProperty("")

    def on_pre_enter(self):
        user_profile = load_user_profile()
        self.user_name = user_profile.get('user_name', "")

    def save_forward(self, play_forward):
        """
        Save the user's answer about playing forward to the profile and navigate to the next screen.
        """
        user_profile = load_user_profile()
        user_profile['forward'] = (play_forward == 'Yes')

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(f"Do you play forward: {user_profile['forward']}")
        # Navigate to the next screen, e.g., 'defense'
        # self.manager.current = 'defense'
