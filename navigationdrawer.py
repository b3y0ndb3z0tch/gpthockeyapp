from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
