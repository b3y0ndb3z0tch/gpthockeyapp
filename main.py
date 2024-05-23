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
from email.email import EmailScreen
from email.verification import VerificationScreen

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

        root = Builder.load_file('main.kv')
        self.check_verification(root)
        return root

    def check_verification(self, root):
        """
        Check if the user is verified when the application starts.
        If verified, navigate directly to the profile screen.
        """
        data_directory = os.path.join(os.path.dirname(__file__), 'data')
        file_path = os.path.join(data_directory, 'user_data.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    user_data = json.load(f)
                    if user_data.get('verified'):
                        root.ids.screen_manager.current = 'profile'
                except json.JSONDecodeError:
                    pass

if __name__ == '__main__':
    MainApp().run()
