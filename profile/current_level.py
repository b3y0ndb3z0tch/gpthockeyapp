# profile/current_level.py
import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.menu import MDDropdownMenu

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'current_level.kv')
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


class CurrentLevelScreen(Screen):
    user_name = StringProperty("")
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])
    label_fontprimary = ListProperty([1, 1, 1, 1])
    button_fontprimary = ListProperty([0, 0, 0, 1])
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])
    dropdown_bg = ListProperty([0.9, 0.9, 0.9, 1])

    def on_pre_enter(self):
        user_profile = load_user_profile()
        colors = load_colors()
        self.user_name = user_profile.get('user_name', "")
        self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
        self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
        self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
        self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])
        self.dropdown_bg = colors.get('dropdown_bg', [0.9, 0.9, 0.9, 1])

        # Create menu items for Tier
        self.tier_menu_items = [
            {"viewclass": "OneLineListItem", "text": "Bronze",
             "on_release": lambda x="Bronze": self.set_item(self.ids.tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Silver (Default)",
             "on_release": lambda x="Silver (Default)": self.set_item(self.ids.tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Gold",
             "on_release": lambda x="Gold": self.set_item(self.ids.tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Platinum",
             "on_release": lambda x="Platinum": self.set_item(self.ids.tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "College",
             "on_release": lambda x="College": self.set_item(self.ids.tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Amateur",
             "on_release": lambda x="Amateur": self.set_item(self.ids.tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Professional",
             "on_release": lambda x="Professional": self.set_item(self.ids.tier_dropdown, x)},
        ]

        # Create menu items for Level
        self.level_menu_items = [
            {"viewclass": "OneLineListItem", "text": "5 (Lowest)",
             "on_release": lambda x="5 (Lowest)": self.set_item(self.ids.level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "4",
             "on_release": lambda x="4": self.set_item(self.ids.level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "3 (Default)",
             "on_release": lambda x="3 (Default)": self.set_item(self.ids.level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "2",
             "on_release": lambda x="2": self.set_item(self.ids.level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "1 (Highest)",
             "on_release": lambda x="1 (Highest)": self.set_item(self.ids.level_dropdown, x)},
        ]

        # Set default values for tier_dropdown and level_dropdown
        self.ids.tier_dropdown.text = "Silver (Default)"
        self.ids.level_dropdown.text = "3 (Default)"

        # Create dropdown menus
        self.tier_menu = MDDropdownMenu(
            caller=self.ids.tier_dropdown,
            items=self.tier_menu_items,
            width_mult=4,
        )
        self.level_menu = MDDropdownMenu(
            caller=self.ids.level_dropdown,
            items=self.level_menu_items,
            width_mult=4,
        )

    def set_item(self, dropdown, text_item):
        dropdown.text = text_item
        dropdown.halign = 'center'
        self.tier_menu.dismiss()
        self.level_menu.dismiss()

    def save_current_level(self, tier, level):
        """
        Save the user's current level to the profile.
        """
        user_profile = load_user_profile()
        user_profile['current_level'] = {'tier': tier, 'level': level}

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(f"Current Level Playing - Tier: {tier}, Level: {level}")
        # Navigate to the next screen, e.g., 'profile'
        self.manager.current = 'profile'
