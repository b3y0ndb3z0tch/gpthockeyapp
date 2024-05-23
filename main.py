from kivy.lang import Builder  # Import the Builder module from Kivy to load .kv files
from kivy.core.window import Window  # Import the Window module to set window size
from kivymd.app import MDApp  # Import the MDApp class from KivyMD to create the app
from kivymd.uix.screenmanager import MDScreenManager  # Import MDScreenManager for managing screens
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer  # Import navigation drawer components
from navigationdrawer import ContentNavigationDrawer  # Import custom content for the left navigation drawer
from settings.right_navigationdrawer import \
    SettingsRightNavigationDrawer  # Import custom content for the right navigation drawer
from home.home import HomeScreen  # Import HomeScreen from the home directory
from settings.settings import SettingsScreen, Screen1, Screen2  # Import SettingsScreen and its sub-screens
from profile.profile import ProfileScreen  # Import ProfileScreen from the profile directory
from email.email import EmailScreen  # Import EmailScreen from the email directory
from email.verification import VerificationScreen  # Import VerificationScreen from the email directory
import json  # Import JSON module for reading and writing JSON files
import os  # Import OS module to handle file paths


class MainApp(MDApp):  # Define the main application class inheriting from MDApp
    def build(self):
        Window.size = (350, 600)  # Set the size of the window
        # Load the KV files
        Builder.load_file('navigationdrawer.kv')  # Load the left navigation drawer .kv file
        Builder.load_file(
            'settings/right_navigationdrawer.kv')  # Load the new KV file for the settings right navigation drawer
        Builder.load_file('home/home.kv')  # Load the home screen .kv file
        Builder.load_file('settings/settings.kv')  # Load the settings screen .kv file
        Builder.load_file('settings/screen1.kv')  # Load the settings sub-screen1 .kv file
        Builder.load_file('settings/screen2.kv')  # Load the settings sub-screen2 .kv file
        Builder.load_file('profile/profile.kv')  # Load the profile screen .kv file
        Builder.load_file('email/email.kv')  # Load the email screen .kv file
        Builder.load_file('email/verification.kv')  # Load the verification screen .kv file

        root = Builder.load_file('main.kv')  # Return the main .kv file to start the app
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
    MainApp().run()  # Run the application
