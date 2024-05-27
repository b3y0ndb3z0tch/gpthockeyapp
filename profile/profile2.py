import os
import json
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty, ListProperty

# Define the path for the .kv file
kv_file_path = os.path.join(os.path.dirname(__file__), 'profile2.kv')
Builder.load_file(kv_file_path)

# Load user profile data
data_folder = os.path.join(os.path.dirname(__file__), '../data')
user_profile_file = os.path.join(data_folder, 'user_profile.json')


def load_user_profile():
    if os.path.exists(user_profile_file):
        with open(user_profile_file, 'r') as file:
            return json.load(file)
    return {}


class Profile2Screen(Screen):
    highest_tier = StringProperty("Silver (Default)")
    highest_level = StringProperty("3 (Default)")
    current_tier = StringProperty("Silver (Default)")
    current_level = StringProperty("3 (Default)")
    background_primary = ListProperty([0.2, 0.6, 0.8, 1])
    label_fontprimary = ListProperty([1, 1, 1, 1])
    button_fontprimary = ListProperty([0, 0, 0, 1])
    button_pressed = ListProperty([0.9, 0.1, 0.1, 1])

    def on_pre_enter(self):
        user_profile = load_user_profile()
        self.highest_tier = user_profile.get('highest_level', {}).get('tier', "Silver (Default)")
        self.highest_level = user_profile.get('highest_level', {}).get('level', "3 (Default)")
        self.current_tier = user_profile.get('current_level', {}).get('tier', "Silver (Default)")
        self.current_level = user_profile.get('current_level', {}).get('level', "3 (Default)")

        colors = self.load_colors()
        self.background_primary = colors.get('background_primary', [0.2, 0.6, 0.8, 1])
        self.label_fontprimary = colors.get('label_fontprimary', [1, 1, 1, 1])
        self.button_fontprimary = colors.get('button_fontprimary', [0, 0, 0, 1])
        self.button_pressed = colors.get('button_pressed', [0.9, 0.1, 0.1, 1])

        # Initialize dropdown menus
        self.init_dropdown_menus()
        self.update_dropdown_menu()
    def update_dropdown_menu(self):
        self.ids.highest_tier_dropdown.text = self.highest_tier
        self.ids.highest_level_dropdown.text = self.highest_level
        self.ids.current_level_dropdown.text = self.current_level
        self.ids.current_tier_dropdown.text = self.current_tier
    def init_dropdown_menus(self):
        self.tier_menu_items = [
            {"viewclass": "OneLineListItem", "text": "Bronze",
             "on_release": lambda x="Bronze": self.set_item(self.ids.highest_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Silver (Default)",
             "on_release": lambda x="Silver (Default)": self.set_item(self.ids.highest_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Gold",
             "on_release": lambda x="Gold": self.set_item(self.ids.highest_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Platinum",
             "on_release": lambda x="Platinum": self.set_item(self.ids.highest_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "College",
             "on_release": lambda x="College": self.set_item(self.ids.highest_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Amateur",
             "on_release": lambda x="Amateur": self.set_item(self.ids.highest_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Professional",
             "on_release": lambda x="Professional": self.set_item(self.ids.highest_tier_dropdown, x)},
        ]

        self.level_menu_items = [
            {"viewclass": "OneLineListItem", "text": "5 (Lowest)",
             "on_release": lambda x="5 (Lowest)": self.set_item(self.ids.highest_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "4",
             "on_release": lambda x="4": self.set_item(self.ids.highest_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "3 (Default)",
             "on_release": lambda x="3 (Default)": self.set_item(self.ids.highest_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "2",
             "on_release": lambda x="2": self.set_item(self.ids.highest_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "1 (Highest)",
             "on_release": lambda x="1 (Highest)": self.set_item(self.ids.highest_level_dropdown, x)},
        ]

        self.current_tier_menu_items = [
            {"viewclass": "OneLineListItem", "text": "Bronze",
             "on_release": lambda x="Bronze": self.set_item(self.ids.current_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Silver (Default)",
             "on_release": lambda x="Silver (Default)": self.set_item(self.ids.current_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Gold",
             "on_release": lambda x="Gold": self.set_item(self.ids.current_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Platinum",
             "on_release": lambda x="Platinum": self.set_item(self.ids.current_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "College",
             "on_release": lambda x="College": self.set_item(self.ids.current_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Amateur",
             "on_release": lambda x="Amateur": self.set_item(self.ids.current_tier_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "Professional",
             "on_release": lambda x="Professional": self.set_item(self.ids.current_tier_dropdown, x)},
        ]

        self.current_level_menu_items = [
            {"viewclass": "OneLineListItem", "text": "5 (Lowest)",
             "on_release": lambda x="5 (Lowest)": self.set_item(self.ids.current_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "4",
             "on_release": lambda x="4": self.set_item(self.ids.current_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "3 (Default)",
             "on_release": lambda x="3 (Default)": self.set_item(self.ids.current_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "2",
             "on_release": lambda x="2": self.set_item(self.ids.current_level_dropdown, x)},
            {"viewclass": "OneLineListItem", "text": "1 (Highest)",
             "on_release": lambda x="1 (Highest)": self.set_item(self.ids.current_level_dropdown, x)},
        ]

        self.tier_menu = MDDropdownMenu(
            caller=self.ids.highest_tier_dropdown,
            items=self.tier_menu_items,
            width_mult=4,
        )
        self.level_menu = MDDropdownMenu(
            caller=self.ids.highest_level_dropdown,
            items=self.level_menu_items,
            width_mult=4,
        )
        self.current_tier_menu = MDDropdownMenu(
            caller=self.ids.current_tier_dropdown,
            items=self.current_tier_menu_items,
            width_mult=4,
        )
        self.current_level_menu = MDDropdownMenu(
            caller=self.ids.current_level_dropdown,
            items=self.current_level_menu_items,
            width_mult=4,
        )

    def set_item(self, dropdown, text_item):
        dropdown.text = text_item
        dropdown.halign = 'center'
        self.tier_menu.dismiss()
        self.level_menu.dismiss()
        self.current_tier_menu.dismiss()
        self.current_level_menu.dismiss()
        self.save_profile2()

    def save_profile2(self):
        user_profile = load_user_profile()
        user_profile['highest_level'] = {'tier': self.ids.highest_tier_dropdown.text,
                                         'level': self.ids.highest_level_dropdown.text}
        user_profile['current_level'] = {'tier': self.ids.current_tier_dropdown.text,
                                         'level': self.ids.current_level_dropdown.text}

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(user_profile, f, indent=4)

        print(
            f"Highest Level - Tier: {self.ids.highest_tier_dropdown.text}, Level: {self.ids.highest_level_dropdown.text}")
        print(
            f"Current Level - Tier: {self.ids.current_tier_dropdown.text}, Level: {self.ids.current_level_dropdown.text}")
        #self.manager.current = 'profile'

    def change_screen(self):
        self.save_profile2()
        self.manager.current = 'profile'
    def load_colors(self):
        colors_file = os.path.join(data_folder, 'colors.json')
        if os.path.exists(colors_file):
            with open(colors_file, 'r') as file:
                return json.load(file)
        return {}
