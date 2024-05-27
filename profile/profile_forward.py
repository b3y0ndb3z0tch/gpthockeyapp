import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'profile_forward.kv')
Builder.load_file(kv_file_path)

# Load user profile data
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')


def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}


class ProfileForwardScreen(Screen):
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])
    label_fontprimary = ListProperty([1, 1, 1, 1])
    button_fontprimary = ListProperty([0, 0, 0, 1])
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])
    background_primary_opaque = ListProperty([0.2, 0.6, 0.8, 0.5])

    def on_pre_enter(self):
        user_profile = load_user_profile()

        # Set checkbox states based on user profile data
        self.ids.left_wing_checkbox.active = user_profile.get('left_wing', False)
        self.ids.center_checkbox.active = user_profile.get('center', False)
        self.ids.right_wing_checkbox.active = user_profile.get('right_wing', False)

        colors = self.load_colors()
        self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
        self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
        self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
        self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])
        self.background_primary_opaque = colors.get('background_primary_opaque', [0.2, 0.6, 0.8, 0.5])

    def on_checkbox_active(self, checkbox, value, position):
        self.save_forward(position, value)

    def save_forward(self, position, value):
        user_profile = load_user_profile()
        user_profile[position] = value

        # Update the "forward" key based on the state of the checkboxes
        user_profile['forward'] = (
            user_profile.get('left_wing', False) or
            user_profile.get('center', False) or
            user_profile.get('right_wing', False)
        )

        file_path = os.path.join(data_folder, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(f"Forward - {position}: {user_profile[position]}")
        print(f"Forward: {user_profile['forward']}")

    def load_colors(self):
        colors_file = os.path.join(data_folder, 'colors.json')
        if os.path.exists(colors_file):
            with open(colors_file, 'r') as file:
                return json.load(file)
        return {}
