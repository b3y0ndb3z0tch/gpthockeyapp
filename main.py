from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from navigationdrawer import ContentNavigationDrawer
from right_navigationdrawer import RightContentNavigationDrawer  # Import the new class
from home.home import HomeScreen
from settings.settings import SettingsScreen, Screen1, Screen2
from profile.profile import ProfileScreen


class MainApp(MDApp):
    def build(self):
        Window.size = (350, 600)
        # Load the KV files
        Builder.load_file('navigationdrawer.kv')
        Builder.load_file('right_navigationdrawer.kv')  # Load the new KV file
        Builder.load_file('home/home.kv')
        Builder.load_file('settings/settings.kv')
        Builder.load_file('settings/screen1.kv')
        Builder.load_file('settings/screen2.kv')
        Builder.load_file('profile/profile.kv')

        return Builder.load_file('main.kv')


if __name__ == '__main__':
    MainApp().run()
