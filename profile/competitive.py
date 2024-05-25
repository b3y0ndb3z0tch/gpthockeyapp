import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'competitive.kv')
Builder.load_file(kv_file_path)

# Load user profile data and colors
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')
colors_file = os.path.join(data_folder, 'colors.json')

def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}

def load_colors():
    if os.path.exists(colors_file):
        with open(colors_file, 'r') as file:
            return json.load(file)
    return {}

class CompetitiveScreen(Screen):
    user_name = StringProperty("")
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])
    label_fontprimary = ListProperty([1, 1, 1, 1])
    button_fontprimary = ListProperty([0, 0, 0, 1])
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])
    slider_active = ListProperty([0.4, 0.8, 0.4, 1])
    slider_inactive = ListProperty([0.7, 0.7, 0.7, 1])
    slider_thumb = ListProperty([0.2, 0.6, 0.2, 1])
    slider_value_bg = ListProperty([0.4, 0.8, 0.4, 1])
    slider_value_text = ListProperty([1, 1, 1, 1])
    slider_thumb_inactive = ListProperty([0.2, 0.6, 0.8, 1])

    def on_pre_enter(self):
        user_profile = load_user_profile()
        colors = load_colors()
        self.user_name = user_profile.get('user_name', "")
        self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
        self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
        self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
        self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])
        self.slider_active = colors.get('slider_active', [0.4, 0.8, 0.4, 1])
        self.slider_inactive = colors.get('slider_inactive', [0.7, 0.7, 0.7, 1])
        self.slider_thumb = colors.get('slider_thumb', [0.2, 0.6, 0.2, 1])
        self.slider_value_bg = colors.get('slider_value_bg', [0.4, 0.8, 0.4, 1])
        self.slider_value_text = colors.get('slider_value_text', [1, 1, 1, 1])
        self.slider_thumb_inactive = colors.get('slider_thumb_inactive', [0.2, 0.6, 0.8, 1])

    def save_competitive(self, social, competitive, skill):
        """
        Save the user's competitive levels to the profile and navigate to the next screen.
        """
        user_profile = load_user_profile()
        user_profile['social'] = social
        user_profile['competitive'] = competitive
        user_profile['skill'] = skill

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(f"Social: {social}, Competitive: {competitive}, Skill: {skill}")
        # Navigate to the next screen, e.g., 'next_screen'
        self.manager.current = 'highest_level'
