from kivy.uix.boxlayout import BoxLayout  # Import BoxLayout from Kivy
from kivy.properties import ObjectProperty  # Import ObjectProperty for property management

# Define the content for the left navigation drawer
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()  # Property to reference the screen manager
    nav_drawer = ObjectProperty()  # Property to reference the navigation drawer
