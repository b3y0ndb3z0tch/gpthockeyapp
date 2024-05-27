import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty, BooleanProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'profile_stickhand.kv')
Builder.load_file(kv_file_path)

# Load user profile data
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')


def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}


class ProfileStickHandScreen(Screen):
    right_hand = BooleanProperty(False)
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])
    label_fontprimary = ListProperty([1, 1, 1, 1])
    button_fontprimary = ListProperty([0, 0, 0, 1])
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])
    background_primary_opaque = ListProperty([0.2, 0.6, 0.8, 0.5])  # Lighter, see-through blue

    def on_pre_enter(self):
        user_profile = load_user_profile()
        self.right_hand = user_profile.get('right_hand', False)
        colors = self.load_colors()
        self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
        self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
        self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
        self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])
        self.background_primary_opaque = colors.get('background_primary_opaque', [0.2, 0.6, 0.8, 0.5])
        self.update_checkboxes()

    def update_checkboxes(self):
        self.ids.left_hand_checkbox.active = not self.right_hand
        self.ids.right_hand_checkbox.active = self.right_hand

    def on_checkbox_active(self, checkbox, value, right_hand):
        if value:
            self.right_hand = right_hand
            self.save_stickhand()

    def save_stickhand(self):
        user_profile = load_user_profile()
        user_profile['right_hand'] = self.right_hand

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(f"Stickhand - Right Hand: {self.right_hand}")

    def load_colors(self):
        colors_file = os.path.join(data_folder, 'colors.json')
        if os.path.exists(colors_file):
            with open(colors_file, 'r') as file:
                return json.load(file)
        return {}
