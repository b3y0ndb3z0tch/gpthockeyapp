import os
import json
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from navigationdrawer import ContentNavigationDrawer
from settings.right_navigationdrawer import SettingsRightNavigationDrawer
from home.home import HomeScreen
from settings.settings import SettingsScreen, Screen1, Screen2
from profile.profile import ProfileScreen
from email.email import EmailScreen
from email.verification import VerificationScreen
from events.events import EventScreen
from profile.stickhand import StickHandScreen
from profile.forward import ForwardScreen
from profile.defense import DefenseScreen
from profile.goalie import GoalieScreen
from profile.competitive import CompetitiveScreen
from profile.highest_level import HighestLevelScreen
from profile.current_level import CurrentLevelScreen
from profile.profile2 import Profile2Screen

class MainApp(MDApp):
    def build(self):
        Window.size = (350, 600)
        # Load the KV files
        Builder.load_file('navigationdrawer.kv')
        Builder.load_file('settings/right_navigationdrawer.kv')
        Builder.load_file('home/home.kv')
        Builder.load_file('settings/settings.kv')
        Builder.load_file('settings/screen1.kv')
        Builder.load_file('settings/screen2.kv')
        Builder.load_file('profile/profile.kv')
        Builder.load_file('email/email.kv')
        Builder.load_file('email/verification.kv')
        Builder.load_file('events/events.kv')
        Builder.load_file('profile/stickhand.kv')
        Builder.load_file('profile/forward.kv')
        Builder.load_file('profile/defense.kv')
        Builder.load_file('profile/goalie.kv')
        Builder.load_file('profile/competitive.kv')
        Builder.load_file('profile/highest_level.kv')
        Builder.load_file('profile/current_level.kv')
        Builder.load_file('profile/profile2.kv')

        root = Builder.load_file('main.kv')
        self.check_user_data(root)
        return root

    def check_user_data(self, root):
        """
        Check the user_data.json file to determine which screen to navigate to.
        """
        data_directory = os.path.join(os.path.dirname(__file__), 'data')
        user_data_path = os.path.join(data_directory, 'user_data.json')
        user_profile_path = os.path.join(data_directory, 'user_profile.json')

        if os.path.exists(user_profile_path):
            root.ids.screen_manager.current = 'profile'
        elif os.path.exists(user_data_path):
            with open(user_data_path, 'r') as f:
                try:
                    user_data = json.load(f)
                    email = user_data.get('email')
                    password = user_data.get('password')
                    verified = user_data.get('verified', False)

                    if not email or not password:
                        root.ids.screen_manager.current = 'email'
                    elif not verified:
                        root.ids.screen_manager.current = 'verification'
                    else:
                        root.ids.screen_manager.current = 'stickhand'
                except json.JSONDecodeError:
                    root.ids.screen_manager.current = 'email'
        else:
            root.ids.screen_manager.current = 'email'

if __name__ == '__main__':
    MainApp().run()
