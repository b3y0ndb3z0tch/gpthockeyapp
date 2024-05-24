import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'stickhand.kv')
Builder.load_file(kv_file_path)

# Load user profile data
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')


def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}


class StickHandScreen(Screen):
    user_name = StringProperty("")

    def on_pre_enter(self):
        user_profile = load_user_profile()
        self.user_name = user_profile.get('user_name', "")

    def save_stick_hand(self, hand):
        """
        Save the stick hand option to the profile and navigate to the next screen.
        """
        user_profile = load_user_profile()
        user_profile['right_handed'] = (hand == 'Right')

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(f"Stick Hand saved: {user_profile['right_handed']}")
        self.manager.current = 'forward'
