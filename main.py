from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
import os
import json

from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from navigationdrawer import ContentNavigationDrawer
from settings.right_navigationdrawer import SettingsRightNavigationDrawer
from home.home import HomeScreen
from settings.settings import SettingsScreen, Screen1, Screen2
from profile.profile import ProfileScreen
from profile.stickhand import StickHandScreen  # Import the StickHandScreen
from profile.forward import ForwardScreen  # Import the ForwardScreen
from profile.defense import DefenseScreen  # Import the DefenseScreen
from profile.goalie import GoalieScreen  # Import the GoalieScreen
from profile.competitive import CompetitiveScreen  # Import the CompetitiveScreen
from email.email import EmailScreen
from email.verification import VerificationScreen
from events.events import EventScreen  # Import the EventScreen
from profile.highest_level import HighestLevelScreen  # Import the HighestLevelScreen
from profile.current_level import CurrentLevelScreen  # Import the CurrentLevelScreen

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
        Builder.load_file('profile/current_level.kv')  # Load the current_level.kv file

        root = Builder.load_file('main.kv')
        self.check_verification(root)
        return root

    def check_verification(self, root):
        """
        Check if the user is verified when the application starts.
        If verified, navigate directly to the stickhand screen.
        """
        data_directory = os.path.join(os.path.dirname(__file__), 'data')
        file_path = os.path.join(data_directory, 'user_data.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    user_data = json.load(f)
                    if user_data.get('verified'):
                        root.ids.screen_manager.current = 'stickhand'
                except json.JSONDecodeError:
                    pass

if __name__ == '__main__':
    MainApp().run()
