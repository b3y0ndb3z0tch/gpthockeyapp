# profile/profile.py

from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
import json
import os


class ProfileScreen(MDScreen):
    forward_left_wing_chk = ObjectProperty(None)
    forward_center_chk = ObjectProperty(None)
    forward_right_wing_chk = ObjectProperty(None)
    defense_left_chk = ObjectProperty(None)
    defense_right_chk = ObjectProperty(None)
    goalie_chk = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.load_profile()

    def update_forward(self, checkbox, position):
        if checkbox.active:
            self.ids.forward_left_wing_chk.active = position == 'left_wing'
            self.ids.forward_center_chk.active = position == 'center'
            self.ids.forward_right_wing_chk.active = position == 'right_wing'

    def update_defense(self, checkbox, position):
        if checkbox.active:
            self.ids.defense_left_chk.active = position == 'left'
            self.ids.defense_right_chk.active = position == 'right'

    def update_goalie(self, checkbox, position):
        if checkbox.active:
            self.ids.goalie_chk.active = position == 'goalie'

    def save_profile(self):
        profile_data = {
            "forward": {
                "left_wing": self.ids.forward_left_wing_chk.active,
                "center": self.ids.forward_center_chk.active,
                "right_wing": self.ids.forward_right_wing_chk.active,
            },
            "defense": {
                "left": self.ids.defense_left_chk.active,
                "right": self.ids.defense_right_chk.active,
            },
            "goalie": self.ids.goalie_chk.active,
        }

        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        os.makedirs(data_directory, exist_ok=True)
        file_path = os.path.join(data_directory, 'user_profile.json')

        with open(file_path, 'w') as f:
            json.dump(profile_data, f)

    def load_profile(self):
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_profile.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                profile_data = json.load(f)
                self.ids.forward_left_wing_chk.active = profile_data['forward'].get('left_wing', False)
                self.ids.forward_center_chk.active = profile_data['forward'].get('center', False)
                self.ids.forward_right_wing_chk.active = profile_data['forward'].get('right_wing', False)
                self.ids.defense_left_chk.active = profile_data['defense'].get('left', False)
                self.ids.defense_right_chk.active = profile_data['defense'].get('right', False)
                self.ids.goalie_chk.active = profile_data.get('goalie', False)
